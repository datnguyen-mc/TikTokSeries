import { useState, useEffect, useCallback } from 'react'
import { useNavigate } from 'react-router-dom'
import {
  BarChart3,
  Tv,
  Film,
  Video,
  Lock,
  Cloud,
  Database,
  Sparkles,
  RefreshCw,
  ArrowRight,
  GitFork,
  ChevronDown,
  ChevronUp,
  Activity,
  CheckCircle2,
  Clock,
  ExternalLink,
  Layers,
} from 'lucide-react'
import { fetchAPI } from '../api/client'
import { useWebSocketContext } from '../api/useWebSocketContext'

interface CharacterSpec {
  tag: string
  name: string
  locked_media_id?: string
  description?: string
}

interface ChannelSummary {
  slug: string
  name: string
  project_id: string
  aspect_ratio: string
  runner_script: string
  description: string
  characters: CharacterSpec[]
  stats: {
    total_episodes: number
    completed_episodes?: number
    total_clips: number
    rendered_clips: number
    r2_synced_clips?: number
    merged_episodes: number
    r2_merged_episodes?: number
  }
  active_job: {
    running: boolean
    pid?: number
    start_ep?: number
    end_ep?: number
  } | null
  latest_log: {
    level: string
    category: string
    message: string
    created_at: string
  } | null
}

interface CloudStatusSummary {
  ok: boolean
  d1: { configured: boolean; ok?: boolean }
  r2: { configured: boolean; ok?: boolean; bucket?: string }
  stats: {
    indexed_episodes: number
    r2_merged_episodes: number
    indexed_clips: number
    r2_clips: number
  }
}

interface CmsLogItem {
  id: number
  channel_slug: string
  episode?: number
  clip_num?: number
  level: string
  category: string
  message: string
  created_at: string
}

const CHANNEL_ACCENTS: Record<string, { badge: string; bar: string; dot: string }> = {
  'mit-va-du-1970': {
    badge: 'bg-amber-500/15 text-amber-300 border-amber-500/30',
    bar: 'from-amber-500 to-orange-500',
    dot: 'bg-amber-400',
  },
  '365ngayvietnam': {
    badge: 'bg-emerald-500/15 text-emerald-300 border-emerald-500/30',
    bar: 'from-emerald-500 to-teal-500',
    dot: 'bg-emerald-400',
  },
  'me-va-be': {
    badge: 'bg-rose-500/15 text-rose-300 border-rose-500/30',
    bar: 'from-rose-500 to-pink-500',
    dot: 'bg-rose-400',
  },
  'pheo-va-no-meo': {
    badge: 'bg-purple-500/15 text-purple-300 border-purple-500/30',
    bar: 'from-purple-500 to-indigo-500',
    dot: 'bg-purple-400',
  },
  'tay-du-ky-2026': {
    badge: 'bg-cyan-500/15 text-cyan-300 border-cyan-500/30',
    bar: 'from-cyan-500 to-blue-500',
    dot: 'bg-cyan-400',
  },
  'biet-doi-gara': {
    badge: 'bg-indigo-500/15 text-indigo-300 border-indigo-500/30',
    bar: 'from-indigo-500 to-violet-500',
    dot: 'bg-indigo-400',
  },
  'ke-song-sot': {
    badge: 'bg-rose-500/15 text-rose-300 border-rose-500/30',
    bar: 'from-rose-500 to-red-600',
    dot: 'bg-rose-400',
  },
}

export default function AnalyticsDashboardPage() {
  const navigate = useNavigate()
  const { lastEvent } = useWebSocketContext()

  const [channels, setChannels] = useState<ChannelSummary[]>([])
  const [cloud, setCloud] = useState<CloudStatusSummary | null>(null)
  const [recentLogs, setRecentLogs] = useState<CmsLogItem[]>([])
  const [loading, setLoading] = useState(true)
  const [syncingD1, setSyncingD1] = useState(false)
  const [syncMsg, setSyncMsg] = useState<string | null>(null)

  // Collapsible states for long text & character lists
  const [expandedCharsBySlug, setExpandedCharsBySlug] = useState<Record<string, boolean>>({})
  const [expandedDescBySlug, setExpandedDescBySlug] = useState<Record<string, boolean>>({})
  const [expandedLogIds, setExpandedLogIds] = useState<Record<number, boolean>>({})
  const [showAllLogs, setShowAllLogs] = useState(false)

  const loadAll = useCallback(async () => {
    try {
      const [chRes, cloudRes, logRes] = await Promise.all([
        fetchAPI<{ channels: ChannelSummary[] }>('/api/cms/channels'),
        fetchAPI<CloudStatusSummary>('/api/cms/cloud/status?live=false').catch(() => null),
        fetchAPI<{ logs: CmsLogItem[] }>('/api/cms/logs?limit=20').catch(() => ({ logs: [] })),
      ])
      setChannels(chRes.channels || [])
      if (cloudRes) setCloud(cloudRes)
      setRecentLogs(logRes.logs || [])
    } catch (e) {
      console.error('Failed to load analytics dashboard:', e)
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => {
    loadAll()
  }, [loadAll])

  useEffect(() => {
    if (!lastEvent) return
    if (
      lastEvent.type === 'cms_log' ||
      lastEvent.type === 'cms_episode_merged' ||
      lastEvent.type === 'cms_clip_synced' ||
      lastEvent.type === 'cms_job_status'
    ) {
      loadAll()
    }
  }, [lastEvent, loadAll])

  async function handleQuickSyncD1(direction: 'pull' | 'push') {
    setSyncingD1(true)
    setSyncMsg(null)
    try {
      const res = await fetchAPI<{ ok: boolean; total_rows_synced?: number; total_rows_pulled?: number }>(
        `/api/cms/cloud/sync-d1?direction=${direction}`,
        { method: 'POST' },
      )
      await loadAll()
      if (direction === 'pull') {
        setSyncMsg(`✅ Đã kéo ${res.total_rows_pulled ?? 0} bản ghi từ Cloudflare D1 về Local SQLite!`)
      } else {
        setSyncMsg(`✅ Đã đẩy ${res.total_rows_synced ?? 0} bản ghi từ Local SQLite lên Cloudflare D1!`)
      }
    } catch (e) {
      setSyncMsg(`❌ Lỗi đồng bộ D1: ${e instanceof Error ? e.message : 'Không xác định'}`)
    } finally {
      setSyncingD1(false)
    }
  }

  const totalChannels = channels.length
  const runningChannels = channels.filter(c => c.active_job?.running).length
  const portraitChannels = channels.filter(c => c.aspect_ratio.includes('PORTRAIT')).length
  const landscapeChannels = totalChannels - portraitChannels

  const totalEpisodes = channels.reduce((s, c) => s + c.stats.total_episodes, 0)
  const completedEpisodes = channels.reduce(
    (s, c) => s + (c.stats.completed_episodes ?? c.stats.merged_episodes),
    0,
  )
  const totalMerged = channels.reduce((s, c) => s + c.stats.merged_episodes, 0)
  const totalClips = channels.reduce((s, c) => s + c.stats.total_clips, 0)
  const renderedClips = channels.reduce((s, c) => s + c.stats.rendered_clips, 0)
  const pendingClips = Math.max(0, totalClips - renderedClips)
  const totalCharacters = channels.reduce((s, c) => s + c.characters.length, 0)
  const lockedCharacters = channels.reduce(
    (s, c) => s + c.characters.filter(ch => Boolean(ch.locked_media_id)).length,
    0,
  )

  const clipProgressPct = totalClips > 0 ? Math.round((renderedClips / totalClips) * 100) : 0
  const epProgressPct = totalEpisodes > 0 ? Math.round((completedEpisodes / totalEpisodes) * 100) : 0
  const mergeProgressPct = totalEpisodes > 0 ? Math.round((totalMerged / totalEpisodes) * 100) : 0

  const displayedLogs = showAllLogs ? recentLogs : recentLogs.slice(0, 6)

  return (
    <div className="flex flex-col gap-6 pb-12 max-w-[1600px] mx-auto">
      {/* Top Action & Quick Navigation Hero Bar */}
      <div className="studio-card rounded-3xl p-5 flex flex-wrap items-center justify-between gap-4 border border-slate-800/90">
        <div className="flex items-center gap-3.5">
          <div className="w-12 h-12 rounded-2xl bg-gradient-to-br from-indigo-500/25 to-purple-500/20 border border-indigo-500/40 flex items-center justify-center text-indigo-300 shadow-lg">
            <BarChart3 size={22} />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h2 className="text-base font-extrabold text-white">
                Trung Tâm Thống Kê & Giám Sát Sản Xuất Series AI
              </h2>
              <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-500/15 text-emerald-300 border border-emerald-500/30">
                Realtime Telemetry
              </span>
            </div>
            <p className="text-xs text-slate-400 mt-0.5">
              Tổng hợp tiến độ render 24fps, tỷ lệ ghép tập FULL MP4, nhân vật khóa cố định và đồng bộ Cloudflare D1 / R2
            </p>
          </div>
        </div>

        <div className="flex items-center gap-2.5 flex-wrap">
          <button
            onClick={() => navigate('/channels')}
            className="px-4 py-2 rounded-xl text-xs font-bold studio-glow-btn flex items-center gap-2 cursor-pointer"
          >
            <Tv size={14} />
            Mở Studio Kênh Series (/channels)
            <ArrowRight size={13} />
          </button>

          <button
            onClick={() => navigate('/workflow')}
            className="px-3.5 py-2 rounded-xl bg-indigo-500/15 hover:bg-indigo-500/25 border border-indigo-500/40 text-xs font-bold text-indigo-200 flex items-center gap-1.5 transition-colors cursor-pointer"
          >
            <GitFork size={13} className="text-indigo-400" />
            Workflow Kéo Thả Agent
          </button>

          <button
            disabled={syncingD1}
            onClick={() => handleQuickSyncD1('pull')}
            className="px-3 py-2 rounded-xl bg-cyan-500/15 hover:bg-cyan-500/25 border border-cyan-500/40 text-xs font-semibold text-cyan-200 flex items-center gap-1.5 transition-colors cursor-pointer disabled:opacity-50"
          >
            <Database size={13} className="text-cyan-400" />
            Pull D1 → Local
          </button>

          <button
            onClick={loadAll}
            className="px-3 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-xs font-medium text-slate-200 flex items-center gap-1.5 transition-colors cursor-pointer"
          >
            <RefreshCw size={13} /> Làm mới
          </button>
        </div>
      </div>

      {syncMsg && (
        <div className="px-4 py-2.5 rounded-2xl bg-indigo-500/15 border border-indigo-500/40 text-xs font-medium text-indigo-200 flex items-center justify-between">
          <span>{syncMsg}</span>
          <button onClick={() => setSyncMsg(null)} className="text-slate-400 hover:text-white text-xs cursor-pointer">
            Đóng
          </button>
        </div>
      )}

      {/* 6 Primary KPI Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6 gap-4">
        <div
          onClick={() => navigate('/channels')}
          className="studio-card rounded-2xl p-4 flex flex-col justify-between gap-2 cursor-pointer hover:border-indigo-500/50 transition-all"
        >
          <div className="flex items-center justify-between">
            <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400">Tổng Kênh Series</span>
            <Tv size={16} className="text-indigo-400" />
          </div>
          <div className="flex items-baseline gap-2">
            <span className="text-2xl font-extrabold text-white">{totalChannels}</span>
            <span className="text-[11px] text-slate-400">
              ({portraitChannels} dọc • {landscapeChannels} ngang)
            </span>
          </div>
          <span className="text-[11px] text-indigo-400 font-medium">
            {runningChannels > 0 ? `⚡ ${runningChannels} kênh đang chạy` : '🟢 Tất cả kênh sẵn sàng'}
          </span>
        </div>

        <div className="studio-card rounded-2xl p-4 flex flex-col justify-between gap-2">
          <div className="flex items-center justify-between">
            <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400">Tiến Độ Tập Phim</span>
            <Layers size={16} className="text-emerald-400" />
          </div>
          <div className="flex items-baseline gap-1.5">
            <span className="text-2xl font-extrabold text-emerald-400">{completedEpisodes}</span>
            <span className="text-xs text-slate-400">/ {totalEpisodes} tập</span>
            <span className="ml-auto text-xs font-mono font-bold text-emerald-300">{epProgressPct}%</span>
          </div>
          <div className="w-full h-1.5 rounded-full bg-slate-800 overflow-hidden">
            <div
              className="h-full rounded-full bg-gradient-to-r from-emerald-500 to-teal-400 transition-all duration-500"
              style={{ width: `${epProgressPct}%` }}
            />
          </div>
        </div>

        <div className="studio-card rounded-2xl p-4 flex flex-col justify-between gap-2">
          <div className="flex items-center justify-between">
            <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400">Clips Đã Render</span>
            <Video size={16} className="text-cyan-400" />
          </div>
          <div className="flex items-baseline gap-1.5">
            <span className="text-2xl font-extrabold text-cyan-400">{renderedClips}</span>
            <span className="text-xs text-slate-400">/ {totalClips} clips</span>
            <span className="ml-auto text-xs font-mono font-bold text-cyan-300">{clipProgressPct}%</span>
          </div>
          <div className="w-full h-1.5 rounded-full bg-slate-800 overflow-hidden">
            <div
              className="h-full rounded-full bg-gradient-to-r from-cyan-500 to-blue-400 transition-all duration-500"
              style={{ width: `${clipProgressPct}%` }}
            />
          </div>
        </div>

        <div
          onClick={() => navigate('/gallery')}
          className="studio-card rounded-2xl p-4 flex flex-col justify-between gap-2 cursor-pointer hover:border-amber-500/50 transition-all"
        >
          <div className="flex items-center justify-between">
            <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400">Tập FULL MP4</span>
            <Film size={16} className="text-amber-400" />
          </div>
          <div className="flex items-baseline gap-1.5">
            <span className="text-2xl font-extrabold text-amber-400">{totalMerged}</span>
            <span className="text-xs text-slate-400">tập hoàn chỉnh</span>
            <span className="ml-auto text-xs font-mono font-bold text-amber-300">{mergeProgressPct}%</span>
          </div>
          <span className="text-[11px] text-amber-300/80 font-medium">
            Còn {pendingClips} clips đang chờ kết xuất
          </span>
        </div>

        <div className="studio-card rounded-2xl p-4 flex flex-col justify-between gap-2">
          <div className="flex items-center justify-between">
            <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400">Nhân Vật (@Tag)</span>
            <Lock size={16} className="text-purple-400" />
          </div>
          <div className="flex items-baseline gap-1.5">
            <span className="text-2xl font-extrabold text-purple-300">{lockedCharacters}</span>
            <span className="text-xs text-slate-400">/ {totalCharacters} đã khóa ID</span>
          </div>
          <span className="text-[11px] text-purple-300/80 font-medium">
            Đồng nhất ngoại hình R2V + I2V
          </span>
        </div>

        <div className="studio-card rounded-2xl p-4 flex flex-col justify-between gap-2">
          <div className="flex items-center justify-between">
            <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400">Cloudflare D1 & R2</span>
            <Cloud size={16} className="text-sky-400" />
          </div>
          <div className="flex items-baseline gap-1.5">
            <span className="text-2xl font-extrabold text-sky-300">{cloud?.stats.r2_clips ?? 0}</span>
            <span className="text-xs text-slate-400">clips trên R2</span>
          </div>
          <span className="text-[11px] text-sky-300/80 font-medium">
            {cloud?.stats.r2_merged_episodes ?? 0} tập FULL • {cloud?.stats.indexed_clips ?? totalClips} D1 rows
          </span>
        </div>
      </div>

      {/* Main Analytics Grid: Left 8 Cols = Channel Breakdown Cards & Visual Bars, Right 4 Cols = Cloud & Live Logs */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
        {/* Left 8 Cols: Per-Channel Statistical Breakdown */}
        <div className="lg:col-span-8 studio-card rounded-3xl p-5 flex flex-col gap-4">
          <div className="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800/80 pb-3.5">
            <div className="flex items-center gap-2.5">
              <Sparkles size={16} className="text-indigo-400" />
              <div>
                <h3 className="text-sm font-bold text-white">
                  Biểu Đồ Tiến Độ Sản Xuất & Khóa Nhân Vật Theo Từng Kênh
                </h3>
                <p className="text-[11px] text-slate-400">
                  Mỗi kênh hiển thị thanh tiến độ Clips, Tập FULL, mô tả rút gọn và danh sách @Character đóng/mở tiện lợi
                </p>
              </div>
            </div>

            <button
              onClick={() => navigate('/channels')}
              className="px-3 py-1.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-xs font-semibold text-indigo-300 flex items-center gap-1.5 cursor-pointer"
            >
              Xem Bảng Quản Lý Kênh <ArrowRight size={12} />
            </button>
          </div>

          {loading ? (
            <div className="py-12 text-center text-xs text-slate-400">Đang tải dữ liệu thống kê kênh...</div>
          ) : (
            <div className="flex flex-col gap-3.5">
              {channels.map(ch => {
                const accent = CHANNEL_ACCENTS[ch.slug] || CHANNEL_ACCENTS['mit-va-du-1970']
                const is916 = ch.aspect_ratio.includes('PORTRAIT')
                const clipPct =
                  ch.stats.total_clips > 0 ? Math.round((ch.stats.rendered_clips / ch.stats.total_clips) * 100) : 0
                const doneEps = ch.stats.completed_episodes ?? ch.stats.merged_episodes
                const epPct =
                  ch.stats.total_episodes > 0 ? Math.round((doneEps / ch.stats.total_episodes) * 100) : 0

                const charsExpanded = Boolean(expandedCharsBySlug[ch.slug])
                const visibleChars = charsExpanded ? ch.characters : ch.characters.slice(0, 4)
                const hiddenCharCount = Math.max(0, ch.characters.length - 4)

                const descExpanded = Boolean(expandedDescBySlug[ch.slug])
                const isDescLong = (ch.description || '').length > 110

                return (
                  <div
                    key={ch.slug}
                    className="p-4 rounded-2xl bg-slate-950/75 border border-slate-800/90 hover:border-slate-700 transition-all flex flex-col gap-3"
                  >
                    <div className="flex flex-wrap items-start justify-between gap-3">
                      <div className="flex items-start gap-3 min-w-0 flex-1">
                        <span className={`w-3 h-3 rounded-full mt-1.5 shrink-0 ${accent.dot}`} />
                        <div className="flex flex-col gap-1 min-w-0 flex-1">
                          <div className="flex items-center gap-2 flex-wrap">
                            <span
                              onClick={() => navigate(`/channels/${ch.slug}`)}
                              className="text-sm font-extrabold text-white hover:text-indigo-300 cursor-pointer transition-colors"
                            >
                              {ch.name}
                            </span>
                            <code className="text-[11px] px-2 py-0.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
                              {ch.slug}
                            </code>
                            <span
                              className={`px-2 py-0.5 rounded text-[10px] font-bold border ${
                                is916
                                  ? 'bg-indigo-500/15 text-indigo-300 border-indigo-500/30'
                                  : 'bg-cyan-500/15 text-cyan-300 border-cyan-500/30'
                              }`}
                            >
                              {is916 ? '9:16 DỌC' : '16:9 NGANG'}
                            </span>
                            {ch.active_job?.running && (
                              <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 animate-pulse">
                                ● Đang Render Tập {ch.active_job.start_ep}
                              </span>
                            )}
                          </div>

                          {/* Collapsible Long Description */}
                          {ch.description && (
                            <div className="text-xs text-slate-400 leading-relaxed">
                              <span>
                                {descExpanded || !isDescLong
                                  ? ch.description
                                  : `${ch.description.slice(0, 110).trim()}...`}
                              </span>
                              {isDescLong && (
                                <button
                                  type="button"
                                  onClick={() =>
                                    setExpandedDescBySlug(prev => ({ ...prev, [ch.slug]: !prev[ch.slug] }))
                                  }
                                  className="ml-1.5 text-[11px] font-semibold text-indigo-400 hover:text-indigo-300 inline-flex items-center gap-0.5 cursor-pointer"
                                >
                                  {descExpanded ? (
                                    <>
                                      Thu gọn <ChevronUp size={11} />
                                    </>
                                  ) : (
                                    <>
                                      Xem thêm <ChevronDown size={11} />
                                    </>
                                  )}
                                </button>
                              )}
                            </div>
                          )}
                        </div>
                      </div>

                      <div className="flex items-center gap-2 shrink-0">
                        <a
                          href={`https://labs.google/fx/vi/tools/flow/project/${ch.project_id}`}
                          target="_blank"
                          rel="noreferrer"
                          className="px-2.5 py-1.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-[11px] font-medium text-slate-300 flex items-center gap-1"
                          title="Mở Project trên Google Flow"
                        >
                          <ExternalLink size={11} className="text-indigo-400" /> Flow
                        </a>
                        <button
                          onClick={() => navigate(`/channels/${ch.slug}`)}
                          className="px-3 py-1.5 rounded-xl text-xs font-bold studio-glow-btn flex items-center gap-1.5 cursor-pointer"
                        >
                          Studio Sản Xuất <ArrowRight size={12} />
                        </button>
                      </div>
                    </div>

                    {/* Dual Progress Bars: Episodes & Clips */}
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-3 pt-1">
                      <div className="p-2.5 rounded-xl bg-slate-900/70 border border-slate-800/80 flex flex-col gap-1.5">
                        <div className="flex items-center justify-between text-[11px]">
                          <span className="text-slate-400 font-medium">
                            Tiến độ Clips (.mp4):{' '}
                            <strong className="text-white">
                              {ch.stats.rendered_clips}/{ch.stats.total_clips}
                            </strong>
                          </span>
                          <span className="font-mono font-bold text-emerald-400">{clipPct}%</span>
                        </div>
                        <div className="w-full h-1.5 rounded-full bg-slate-800 overflow-hidden">
                          <div
                            className={`h-full rounded-full bg-gradient-to-r ${accent.bar} transition-all duration-500`}
                            style={{ width: `${clipPct}%` }}
                          />
                        </div>
                      </div>

                      <div className="p-2.5 rounded-xl bg-slate-900/70 border border-slate-800/80 flex flex-col gap-1.5">
                        <div className="flex items-center justify-between text-[11px]">
                          <span className="text-slate-400 font-medium">
                            Tập hoàn thành & FULL MP4:{' '}
                            <strong className="text-amber-300">{doneEps}/{ch.stats.total_episodes}</strong> tập ({ch.stats.merged_episodes} FULL)
                          </span>
                          <span className="font-mono font-bold text-amber-300">{epPct}%</span>
                        </div>
                        <div className="w-full h-1.5 rounded-full bg-slate-800 overflow-hidden">
                          <div
                            className="h-full rounded-full bg-gradient-to-r from-amber-500 to-yellow-400 transition-all duration-500"
                            style={{ width: `${epPct}%` }}
                          />
                        </div>
                      </div>
                    </div>

                    {/* Locked Characters Row with More / Less Button */}
                    <div className="flex items-center justify-between gap-2 flex-wrap pt-1">
                      <div className="flex items-center gap-1.5 flex-wrap">
                        <span className="text-[10px] font-bold uppercase tracking-wider text-slate-500 mr-1">
                          Nhân Vật ({ch.characters.length}):
                        </span>
                        {visibleChars.map(c => (
                          <span
                            key={c.tag}
                            className={`inline-flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-md border font-semibold ${accent.badge}`}
                            title={`${c.name} — ${c.description || ''}`}
                          >
                            <Lock size={9} />
                            {c.tag}
                          </span>
                        ))}
                        {ch.characters.length > 4 && (
                          <button
                            type="button"
                            onClick={() =>
                              setExpandedCharsBySlug(prev => ({ ...prev, [ch.slug]: !prev[ch.slug] }))
                            }
                            className="inline-flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-md bg-slate-800 hover:bg-slate-700 text-indigo-300 border border-slate-700 font-bold transition-colors cursor-pointer"
                          >
                            {charsExpanded ? (
                              <>
                                Thu gọn <ChevronUp size={10} />
                              </>
                            ) : (
                              <>
                                +{hiddenCharCount} xem thêm <ChevronDown size={10} />
                              </>
                            )}
                          </button>
                        )}
                      </div>

                      {ch.latest_log && (
                        <span
                          className="text-[10px] font-mono text-slate-500 truncate max-w-xs"
                          title={ch.latest_log.message}
                        >
                          [{ch.latest_log.created_at.slice(11)}] {ch.latest_log.message}
                        </span>
                      )}
                    </div>
                  </div>
                )
              })}
            </div>
          )}
        </div>

        {/* Right 4 Cols: Cloud Sync Status + Recent SQLite Activity Feed (Collapsible Long Logs) */}
        <div className="lg:col-span-4 flex flex-col gap-6">
          {/* Cloud Sync Summary Card */}
          <div className="studio-card rounded-3xl p-5 flex flex-col gap-3.5">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                <Cloud size={16} className="text-cyan-400" />
                <h3 className="text-sm font-bold text-white">Đồng Bộ Cloudflare D1 & R2</h3>
              </div>
              <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-cyan-500/15 text-cyan-300 border border-cyan-500/30">
                Cloud Storage
              </span>
            </div>

            <div className="grid grid-cols-2 gap-2.5 text-xs">
              <div className="p-3 rounded-2xl bg-slate-950/80 border border-slate-800 flex flex-col gap-1">
                <span className="text-[10px] text-slate-400">Bản ghi D1 SQL</span>
                <span className="text-base font-extrabold text-white">
                  {cloud?.stats.indexed_clips ?? totalClips} clips
                </span>
                <span className="text-[10px] text-emerald-400 flex items-center gap-1">
                  <CheckCircle2 size={10} /> {cloud?.stats.indexed_episodes ?? totalEpisodes} tập đã index
                </span>
              </div>

              <div className="p-3 rounded-2xl bg-slate-950/80 border border-slate-800 flex flex-col gap-1">
                <span className="text-[10px] text-slate-400">Media trên R2 Bucket</span>
                <span className="text-base font-extrabold text-cyan-300">
                  {cloud?.stats.r2_clips ?? 0} clips
                </span>
                <span className="text-[10px] text-amber-300 flex items-center gap-1">
                  <Film size={10} /> {cloud?.stats.r2_merged_episodes ?? 0} tập FULL MP4
                </span>
              </div>
            </div>

            <div className="grid grid-cols-2 gap-2 pt-1">
              <button
                disabled={syncingD1}
                onClick={() => handleQuickSyncD1('pull')}
                className="py-2 px-3 rounded-xl bg-cyan-500/15 hover:bg-cyan-500/25 border border-cyan-500/40 text-xs font-bold text-cyan-200 flex items-center justify-center gap-1.5 cursor-pointer disabled:opacity-50"
              >
                <Database size={12} /> Pull D1 Về Local
              </button>
              <button
                disabled={syncingD1}
                onClick={() => handleQuickSyncD1('push')}
                className="py-2 px-3 rounded-xl bg-indigo-500/15 hover:bg-indigo-500/25 border border-indigo-500/40 text-xs font-bold text-indigo-200 flex items-center justify-center gap-1.5 cursor-pointer disabled:opacity-50"
              >
                <Cloud size={12} /> Push Local Lên D1
              </button>
            </div>
          </div>

          {/* Live SQLite Activity Logs Card with Expandable Long Messages */}
          <div className="studio-card rounded-3xl p-5 flex flex-col gap-3.5">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                <Activity size={16} className="text-indigo-400" />
                <h3 className="text-sm font-bold text-white">Nhật Ký Hoạt Động Gần Đây</h3>
              </div>
              <button
                onClick={() => navigate('/logs')}
                className="text-[11px] font-semibold text-indigo-400 hover:text-indigo-300 cursor-pointer"
              >
                Mở toàn bộ Log →
              </button>
            </div>

            <div className="flex flex-col gap-2">
              {displayedLogs.length === 0 ? (
                <div className="py-8 text-center text-xs text-slate-500">Chưa có bản ghi hoạt động nào.</div>
              ) : (
                displayedLogs.map(log => {
                  const isLong = (log.message || '').length > 90
                  const isExpanded = Boolean(expandedLogIds[log.id])
                  return (
                    <div
                      key={log.id}
                      className="p-3 rounded-2xl bg-slate-950/80 border border-slate-800/90 flex flex-col gap-1.5 text-xs"
                    >
                      <div className="flex items-center justify-between gap-2">
                        <div className="flex items-center gap-1.5">
                          <span
                            className={`px-1.5 py-0.5 rounded text-[9px] font-bold ${
                              log.level === 'ERROR'
                                ? 'bg-rose-500/20 text-rose-300'
                                : log.level === 'SUCCESS'
                                  ? 'bg-emerald-500/20 text-emerald-300'
                                  : 'bg-indigo-500/20 text-indigo-300'
                            }`}
                          >
                            {log.level}
                          </span>
                          <span className="font-bold text-slate-200 text-[11px]">{log.channel_slug}</span>
                          {log.episode ? (
                            <span className="text-[10px] font-mono text-amber-300">
                              Tập {log.episode}
                              {log.clip_num ? `•C${log.clip_num}` : ''}
                            </span>
                          ) : null}
                        </div>
                        <span className="text-[10px] font-mono text-slate-500 flex items-center gap-1">
                          <Clock size={10} />
                          {log.created_at.slice(11)}
                        </span>
                      </div>

                      <div className="text-[11px] text-slate-300 break-words leading-relaxed">
                        <span>
                          {isExpanded || !isLong ? log.message : `${log.message.slice(0, 90).trim()}...`}
                        </span>
                        {isLong && (
                          <button
                            type="button"
                            onClick={() => setExpandedLogIds(prev => ({ ...prev, [log.id]: !prev[log.id] }))}
                            className="ml-1.5 text-[10px] font-bold text-indigo-400 hover:text-indigo-300 inline-flex items-center gap-0.5 cursor-pointer"
                          >
                            {isExpanded ? (
                              <>
                                Thu gọn <ChevronUp size={10} />
                              </>
                            ) : (
                              <>
                                Xem thêm <ChevronDown size={10} />
                              </>
                            )}
                          </button>
                        )}
                      </div>
                    </div>
                  )
                })
              )}
            </div>

            {recentLogs.length > 6 && (
              <button
                type="button"
                onClick={() => setShowAllLogs(v => !v)}
                className="w-full py-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-xs font-semibold text-slate-300 flex items-center justify-center gap-1 cursor-pointer"
              >
                {showAllLogs ? (
                  <>
                    Thu gọn danh sách Log <ChevronUp size={13} />
                  </>
                ) : (
                  <>
                    Xem thêm {recentLogs.length - 6} bản ghi gần đây <ChevronDown size={13} />
                  </>
                )}
              </button>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

