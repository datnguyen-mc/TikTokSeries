import { useState, useEffect, useMemo, useCallback } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import {
  Search,
  RefreshCw,
  ExternalLink,
  Copy,
  Check,
  Lock,
  Film,
  Tv,
  Cloud,
  FolderKanban,
  Users,
  ArrowRight,
  Sparkles,
} from 'lucide-react'
import { fetchAPI } from '../api/client'
import type { Project } from '../types'
import ProjectDetailPage from './ProjectDetailPage'

interface CMSCharacterSpec {
  tag: string
  name: string
  default_media_id?: string
  locked_media_id?: string
  description?: string
}

interface CMSChannelSummary {
  slug: string
  name: string
  project_id: string
  aspect_ratio: string
  runner_script: string
  series_dir: string
  ep_prefix: string
  description: string
  characters: CMSCharacterSpec[]
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
}

interface UnifiedProjectRow {
  id: string
  name: string
  description: string
  status: 'ACTIVE' | 'ARCHIVED' | 'DELETED'
  material: string
  user_paygate_tier: string | null
  created_at: string
  updated_at: string
  channel_slug: string | null
  aspect_ratio: string
  runner_script: string | null
  characters: CMSCharacterSpec[]
  total_episodes: number
  completed_episodes: number
  total_clips: number
  rendered_clips: number
  r2_synced_clips: number
  merged_episodes: number
  r2_merged_episodes: number
  is_running: boolean
}

interface FlattenedCharacterRow {
  key: string
  tag: string
  name: string
  media_id: string
  description: string
  project_id: string
  project_name: string
  channel_slug: string | null
  aspect_ratio: string
}

type ViewMode = 'projects' | 'characters'
type StatusFilter = 'ALL' | 'ACTIVE' | 'ARCHIVED'

function formatDate(iso: string | null | undefined) {
  if (!iso) return '—'
  const d = new Date(iso)
  if (Number.isNaN(d.getTime())) return '—'
  return d.toLocaleDateString('vi-VN', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
  })
}

function normalizeAspectRatio(ar: string | null | undefined): string {
  if (!ar) return '9:16'
  if (ar.includes('PORTRAIT') || ar.includes('9:16')) return '9:16'
  if (ar.includes('LANDSCAPE') || ar.includes('16:9')) return '16:9'
  return ar
}

export default function ProjectsPage() {
  const { id } = useParams<{ id?: string }>()
  const navigate = useNavigate()

  const [projects, setProjects] = useState<Project[]>([])
  const [channels, setChannels] = useState<CMSChannelSummary[]>([])
  const [loading, setLoading] = useState(true)

  // Filters & Table state
  const [viewMode, setViewMode] = useState<ViewMode>('projects')
  const [selectedProjectOrChannel, setSelectedProjectOrChannel] = useState<string>('ALL')
  const [statusFilter, setStatusFilter] = useState<StatusFilter>('ALL')
  const [aspectFilter, setAspectFilter] = useState<string>('ALL')
  const [searchQuery, setSearchQuery] = useState<string>('')
  const [copiedKey, setCopiedKey] = useState<string | null>(null)

  // Pagination state
  const [currentPage, setCurrentPage] = useState<number>(1)
  const [pageSize, setPageSize] = useState<number>(10)

  const loadData = useCallback(async () => {
    setLoading(true)
    try {
      const [projRes, chanRes] = await Promise.all([
        fetchAPI<Project[]>('/api/projects').catch(() => [] as Project[]),
        fetchAPI<{ channels?: CMSChannelSummary[] } | CMSChannelSummary[]>('/api/cms/channels').catch(
          () => ({ channels: [] })
        ),
      ])
      setProjects(Array.isArray(projRes) ? projRes : [])
      const chanList = Array.isArray(chanRes) ? chanRes : chanRes?.channels || []
      setChannels(chanList)
    } catch (err) {
      console.error('Failed to load projects data:', err)
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => {
    loadData()
  }, [loadData])

  const copyText = (text: string, key: string) => {
    navigator.clipboard.writeText(text)
    setCopiedKey(key)
    setTimeout(() => setCopiedKey(null), 1800)
  }

  // Merge `/api/projects` and `/api/cms/channels` into a single unified list
  const unifiedProjects = useMemo<UnifiedProjectRow[]>(() => {
    const channelByPid = new Map<string, CMSChannelSummary>()
    channels.forEach(ch => {
      if (ch.project_id) channelByPid.set(ch.project_id, ch)
    })

    const seenPids = new Set<string>()
    const rows: UnifiedProjectRow[] = []

    for (const p of projects) {
      if (p.status === 'DELETED') continue
      seenPids.add(p.id)
      const ch = channelByPid.get(p.id)
      rows.push({
        id: p.id,
        name: ch?.name || p.name,
        description: ch?.description || p.description || '',
        status: p.status,
        material: p.material || '3d_pixar',
        user_paygate_tier: p.user_paygate_tier || 'PAYGATE_TIER_TWO',
        created_at: p.created_at,
        updated_at: p.updated_at,
        channel_slug: ch?.slug || null,
        aspect_ratio: normalizeAspectRatio(ch?.aspect_ratio),
        runner_script: ch?.runner_script || null,
        characters: ch?.characters || [],
        total_episodes: ch?.stats?.total_episodes ?? 0,
        completed_episodes: ch?.stats?.completed_episodes ?? ch?.stats?.merged_episodes ?? 0,
        total_clips: ch?.stats?.total_clips ?? 0,
        rendered_clips: ch?.stats?.rendered_clips ?? 0,
        r2_synced_clips: ch?.stats?.r2_synced_clips ?? 0,
        merged_episodes: ch?.stats?.merged_episodes ?? 0,
        r2_merged_episodes: ch?.stats?.r2_merged_episodes ?? 0,
        is_running: Boolean(ch?.active_job?.running),
      })
    }

    // Include any CMS channels whose project_id wasn't in `project` table yet
    for (const ch of channels) {
      if (ch.project_id && !seenPids.has(ch.project_id)) {
        seenPids.add(ch.project_id)
        rows.push({
          id: ch.project_id,
          name: ch.name,
          description: ch.description || '',
          status: 'ACTIVE',
          material: '3d_pixar',
          user_paygate_tier: 'PAYGATE_TIER_TWO',
          created_at: new Date().toISOString(),
          updated_at: new Date().toISOString(),
          channel_slug: ch.slug,
          aspect_ratio: normalizeAspectRatio(ch.aspect_ratio),
          runner_script: ch.runner_script || null,
          characters: ch.characters || [],
          total_episodes: ch.stats?.total_episodes ?? 0,
          completed_episodes: ch.stats?.completed_episodes ?? ch.stats?.merged_episodes ?? 0,
          total_clips: ch.stats?.total_clips ?? 0,
          rendered_clips: ch.stats?.rendered_clips ?? 0,
          r2_synced_clips: ch.stats?.r2_synced_clips ?? 0,
          merged_episodes: ch.stats?.merged_episodes ?? 0,
          r2_merged_episodes: ch.stats?.r2_merged_episodes ?? 0,
          is_running: Boolean(ch.active_job?.running),
        })
      }
    }

    return rows
  }, [projects, channels])

  // Filtered projects
  const filteredProjects = useMemo(() => {
    const q = searchQuery.trim().toLowerCase()
    return unifiedProjects.filter(p => {
      if (selectedProjectOrChannel !== 'ALL') {
        if (p.id !== selectedProjectOrChannel && p.channel_slug !== selectedProjectOrChannel) {
          return false
        }
      }
      if (statusFilter !== 'ALL' && p.status !== statusFilter) return false
      if (aspectFilter !== 'ALL' && p.aspect_ratio !== aspectFilter) return false

      if (q) {
        const matchName = p.name.toLowerCase().includes(q)
        const matchId = p.id.toLowerCase().includes(q)
        const matchSlug = (p.channel_slug || '').toLowerCase().includes(q)
        const matchDesc = p.description.toLowerCase().includes(q)
        const matchChar = p.characters.some(
          c =>
            c.tag.toLowerCase().includes(q) ||
            c.name.toLowerCase().includes(q) ||
            (c.locked_media_id || c.default_media_id || '').toLowerCase().includes(q)
        )
        if (!matchName && !matchId && !matchSlug && !matchDesc && !matchChar) return false
      }
      return true
    })
  }, [unifiedProjects, selectedProjectOrChannel, statusFilter, aspectFilter, searchQuery])

  // Flattened characters across filtered projects
  const filteredCharacters = useMemo<FlattenedCharacterRow[]>(() => {
    const q = searchQuery.trim().toLowerCase()
    const list: FlattenedCharacterRow[] = []

    for (const p of unifiedProjects) {
      if (selectedProjectOrChannel !== 'ALL') {
        if (p.id !== selectedProjectOrChannel && p.channel_slug !== selectedProjectOrChannel) {
          continue
        }
      }
      if (statusFilter !== 'ALL' && p.status !== statusFilter) continue
      if (aspectFilter !== 'ALL' && p.aspect_ratio !== aspectFilter) continue

      for (const c of p.characters) {
        const mediaId = c.locked_media_id || c.default_media_id || ''
        if (q) {
          const matchTag = c.tag.toLowerCase().includes(q)
          const matchName = c.name.toLowerCase().includes(q)
          const matchMedia = mediaId.toLowerCase().includes(q)
          const matchDesc = (c.description || '').toLowerCase().includes(q)
          const matchProj = p.name.toLowerCase().includes(q)
          if (!matchTag && !matchName && !matchMedia && !matchDesc && !matchProj) continue
        }
        list.push({
          key: `${p.id}-${c.tag}`,
          tag: c.tag,
          name: c.name,
          media_id: mediaId,
          description: c.description || '',
          project_id: p.id,
          project_name: p.name,
          channel_slug: p.channel_slug,
          aspect_ratio: p.aspect_ratio,
        })
      }
    }
    return list
  }, [unifiedProjects, selectedProjectOrChannel, statusFilter, aspectFilter, searchQuery])

  // Reset pagination when filters change
  useEffect(() => {
    setCurrentPage(1)
  }, [viewMode, selectedProjectOrChannel, statusFilter, aspectFilter, searchQuery, pageSize])

  // If there's an :id param, show detail page
  if (id) {
    return <ProjectDetailPage projectId={id} onBack={() => navigate('/projects')} />
  }

  const totalItems = viewMode === 'projects' ? filteredProjects.length : filteredCharacters.length
  const totalPages = Math.max(1, Math.ceil(totalItems / pageSize))
  const safePage = Math.min(currentPage, totalPages)
  const startIndex = (safePage - 1) * pageSize
  const paginatedProjects = filteredProjects.slice(startIndex, startIndex + pageSize)
  const paginatedCharacters = filteredCharacters.slice(startIndex, startIndex + pageSize)

  const totalLockedChars = unifiedProjects.reduce((acc, p) => acc + p.characters.length, 0)
  const totalR2Clips = unifiedProjects.reduce((acc, p) => acc + p.r2_synced_clips, 0)
  const totalMergedEps = unifiedProjects.reduce((acc, p) => acc + p.merged_episodes, 0)

  return (
    <div className="flex flex-col gap-4 pb-10">
      {/* Top Header & Summary Stats */}
      <div
        className="rounded-xl p-4 flex flex-wrap items-center justify-between gap-4"
        style={{
          background: 'linear-gradient(135deg, rgba(16,185,129,0.08) 0%, rgba(59,130,246,0.06) 100%)',
          border: '1px solid var(--border)',
        }}
      >
        <div className="flex flex-col gap-1">
          <div className="flex items-center gap-2.5">
            <span
              className="w-8 h-8 rounded-lg flex items-center justify-center"
              style={{ background: 'rgba(16,185,129,0.16)', color: '#34d399' }}
            >
              <FolderKanban className="w-4 h-4" />
            </span>
            <div>
              <h1 className="m-0 text-base font-bold tracking-tight" style={{ color: 'var(--text)' }}>
                Quản Lý Dự Án Google Flow & Nhân Vật Khóa Cố Định
              </h1>
              <p className="m-0 text-[11px]" style={{ color: 'var(--muted)' }}>
                Danh sách dự án (List Table) đồng bộ trực tiếp với Kênh Series, Mã nhân vật @Character & Cloudflare R2 CDN
              </p>
            </div>
          </div>
        </div>

        <div className="flex flex-wrap items-center gap-2.5">
          <div
            className="px-3 py-1.5 rounded-lg flex items-center gap-2 text-xs"
            style={{ background: 'var(--surface)', border: '1px solid var(--border)' }}
          >
            <FolderKanban className="w-3.5 h-3.5" style={{ color: '#34d399' }} />
            <span style={{ color: 'var(--muted)' }}>Dự án:</span>
            <strong style={{ color: 'var(--text)' }}>{unifiedProjects.length}</strong>
          </div>

          <div
            className="px-3 py-1.5 rounded-lg flex items-center gap-2 text-xs"
            style={{ background: 'var(--surface)', border: '1px solid var(--border)' }}
          >
            <Lock className="w-3.5 h-3.5" style={{ color: '#f59e0b' }} />
            <span style={{ color: 'var(--muted)' }}>Nhân vật @Tag:</span>
            <strong style={{ color: '#fbbf24' }}>{totalLockedChars}</strong>
          </div>

          <div
            className="px-3 py-1.5 rounded-lg flex items-center gap-2 text-xs"
            style={{ background: 'var(--surface)', border: '1px solid var(--border)' }}
          >
            <Cloud className="w-3.5 h-3.5" style={{ color: '#38bdf8' }} />
            <span style={{ color: 'var(--muted)' }}>R2 Clips / Tập:</span>
            <strong style={{ color: '#38bdf8' }}>
              {totalR2Clips} clips · {totalMergedEps} tập
            </strong>
          </div>

          <button
            onClick={loadData}
            className="px-3 py-1.5 rounded-lg text-xs font-medium flex items-center gap-1.5 cursor-pointer transition-opacity hover:opacity-90"
            style={{
              background: 'var(--surface)',
              border: '1px solid var(--border)',
              color: 'var(--text)',
            }}
            title="Làm mới dữ liệu"
          >
            <RefreshCw className={`w-3.5 h-3.5 ${loading ? 'animate-spin' : ''}`} />
            Làm mới
          </button>
        </div>
      </div>

      {/* Filter & View Switcher Bar */}
      <div
        className="rounded-xl p-3.5 flex flex-wrap items-center gap-3"
        style={{ background: 'var(--surface)', border: '1px solid var(--border)' }}
      >
        {/* View Mode Tabs */}
        <div
          className="flex items-center p-1 rounded-lg gap-1"
          style={{ background: 'rgba(255,255,255,0.03)', border: '1px solid var(--border)' }}
        >
          <button
            onClick={() => setViewMode('projects')}
            className="px-3 py-1.5 rounded-md text-xs font-semibold flex items-center gap-1.5 cursor-pointer transition-all"
            style={{
              background: viewMode === 'projects' ? 'rgba(16,185,129,0.18)' : 'transparent',
              color: viewMode === 'projects' ? '#34d399' : 'var(--muted)',
              border:
                viewMode === 'projects' ? '1px solid rgba(16,185,129,0.35)' : '1px solid transparent',
            }}
          >
            <FolderKanban className="w-3.5 h-3.5" />
            Bảng Dự Án ({filteredProjects.length})
          </button>
          <button
            onClick={() => setViewMode('characters')}
            className="px-3 py-1.5 rounded-md text-xs font-semibold flex items-center gap-1.5 cursor-pointer transition-all"
            style={{
              background: viewMode === 'characters' ? 'rgba(245,158,11,0.18)' : 'transparent',
              color: viewMode === 'characters' ? '#fbbf24' : 'var(--muted)',
              border:
                viewMode === 'characters' ? '1px solid rgba(245,158,11,0.35)' : '1px solid transparent',
            }}
          >
            <Users className="w-3.5 h-3.5" />
            Bảng Nhân Vật @Tag ({filteredCharacters.length})
          </button>
        </div>

        {/* Select Channel / Project Dropdown */}
        <div className="flex items-center gap-2">
          <span className="text-[11px] font-semibold uppercase tracking-wider" style={{ color: 'var(--muted)' }}>
            Kênh / Dự Án:
          </span>
          <select
            value={selectedProjectOrChannel}
            onChange={e => setSelectedProjectOrChannel(e.target.value)}
            className="px-3 py-1.5 rounded-lg text-xs font-medium outline-none cursor-pointer"
            style={{
              background: 'var(--bg)',
              border: '1px solid var(--border)',
              color: 'var(--text)',
              minWidth: 230,
            }}
          >
            <option value="ALL">🌐 Tất cả Kênh Series & Dự Án ({unifiedProjects.length})</option>
            {unifiedProjects.map(p => (
              <option key={p.id} value={p.id}>
                🎬 {p.name} ({p.aspect_ratio}) — {p.characters.length} @Tag
              </option>
            ))}
          </select>
        </div>

        {/* Aspect Ratio Filter */}
        <div className="flex items-center gap-2">
          <span className="text-[11px] font-semibold uppercase tracking-wider" style={{ color: 'var(--muted)' }}>
            Tỉ lệ:
          </span>
          <select
            value={aspectFilter}
            onChange={e => setAspectFilter(e.target.value)}
            className="px-2.5 py-1.5 rounded-lg text-xs font-medium outline-none cursor-pointer"
            style={{
              background: 'var(--bg)',
              border: '1px solid var(--border)',
              color: 'var(--text)',
            }}
          >
            <option value="ALL">Tất cả tỉ lệ</option>
            <option value="9:16">📱 9:16 Dọc (TikTok/Reels)</option>
            <option value="16:9">🖥️ 16:9 Ngang (Cinema)</option>
          </select>
        </div>

        {/* Status Filter */}
        <div className="flex items-center gap-2">
          <span className="text-[11px] font-semibold uppercase tracking-wider" style={{ color: 'var(--muted)' }}>
            Trạng thái:
          </span>
          <select
            value={statusFilter}
            onChange={e => setStatusFilter(e.target.value as StatusFilter)}
            className="px-2.5 py-1.5 rounded-lg text-xs font-medium outline-none cursor-pointer"
            style={{
              background: 'var(--bg)',
              border: '1px solid var(--border)',
              color: 'var(--text)',
            }}
          >
            <option value="ALL">Tất cả ({unifiedProjects.length})</option>
            <option value="ACTIVE">Đang hoạt động (ACTIVE)</option>
            <option value="ARCHIVED">Lưu trữ (ARCHIVED)</option>
          </select>
        </div>

        {/* Search Input */}
        <div
          className="flex items-center gap-2 px-3 py-1.5 rounded-lg ml-auto"
          style={{
            background: 'var(--bg)',
            border: '1px solid var(--border)',
            minWidth: 250,
          }}
        >
          <Search className="w-3.5 h-3.5 shrink-0" style={{ color: 'var(--muted)' }} />
          <input
            type="text"
            value={searchQuery}
            onChange={e => setSearchQuery(e.target.value)}
            placeholder="Tìm tên dự án, Project ID, @Tag, Media ID..."
            className="bg-transparent border-none outline-none text-xs w-full"
            style={{ color: 'var(--text)' }}
          />
          {searchQuery && (
            <button
              onClick={() => setSearchQuery('')}
              className="text-[10px] px-1.5 py-0.5 rounded cursor-pointer"
              style={{ background: 'rgba(255,255,255,0.08)', color: 'var(--muted)' }}
            >
              Xóa
            </button>
          )}
        </div>
      </div>

      {/* Main List Table Container */}
      <div
        className="rounded-xl overflow-hidden"
        style={{ background: 'var(--surface)', border: '1px solid var(--border)' }}
      >
        {loading ? (
          <div className="p-8 text-center text-xs" style={{ color: 'var(--muted)' }}>
            Đang tải danh sách dự án & nhân vật...
          </div>
        ) : viewMode === 'projects' ? (
          filteredProjects.length === 0 ? (
            <div className="p-8 text-center text-xs" style={{ color: 'var(--muted)' }}>
              Không tìm thấy dự án nào khớp bộ lọc hiện tại.
            </div>
          ) : (
            <div className="overflow-x-auto">
              <table className="w-full border-collapse text-left">
                <thead>
                  <tr
                    className="text-[10px] font-semibold uppercase tracking-wider"
                    style={{
                      background: 'rgba(255,255,255,0.02)',
                      color: 'var(--muted)',
                      borderBottom: '1px solid var(--border)',
                    }}
                  >
                    <th className="py-3 px-3.5 w-10 text-center">#</th>
                    <th className="py-3 px-3.5">Dự Án & Kênh Series</th>
                    <th className="py-3 px-3.5">Google Flow Project ID</th>
                    <th className="py-3 px-3.5">Tỉ Lệ & Style</th>
                    <th className="py-3 px-3.5">Nhân Vật Khóa Cố Định (@Tag)</th>
                    <th className="py-3 px-3.5">Tiến Độ Tập / Clips R2</th>
                    <th className="py-3 px-3.5">Trạng Thái</th>
                    <th className="py-3 px-3.5 text-right">Thao Tác</th>
                  </tr>
                </thead>
                <tbody className="divide-y" style={{ borderColor: 'var(--border)' }}>
                  {paginatedProjects.map((p, idx) => {
                    const rowNumber = startIndex + idx + 1
                    const flowUrl = `https://labs.google/fx/vi/tools/flow/project/${p.id}`
                    const isCopied = copiedKey === `proj-${p.id}`

                    return (
                      <tr
                        key={p.id}
                        className="transition-colors hover:bg-white/[0.02]"
                        style={{ borderBottom: '1px solid var(--border)' }}
                      >
                        {/* # */}
                        <td
                          className="py-3.5 px-3.5 text-xs font-mono text-center"
                          style={{ color: 'var(--muted)' }}
                        >
                          {rowNumber}
                        </td>

                        {/* Dự Án & Kênh Series */}
                        <td className="py-3.5 px-3.5 max-w-[290px]">
                          <div className="flex flex-col gap-1">
                            <div className="flex items-center gap-2 flex-wrap">
                              <span
                                onClick={() => navigate(`/projects/${p.id}`)}
                                className="text-xs font-bold cursor-pointer hover:underline"
                                style={{ color: 'var(--text)' }}
                              >
                                {p.name}
                              </span>
                              {p.channel_slug && (
                                <span
                                  onClick={() => navigate(`/channels/${p.channel_slug}`)}
                                  className="px-1.5 py-0.5 rounded text-[10px] font-mono cursor-pointer"
                                  style={{
                                    background: 'rgba(16,185,129,0.12)',
                                    color: '#34d399',
                                    border: '1px solid rgba(16,185,129,0.28)',
                                  }}
                                  title="Mở Studio Kênh Series"
                                >
                                  /{p.channel_slug}
                                </span>
                              )}
                            </div>
                            {p.description && (
                              <p
                                className="m-0 text-[11px] line-clamp-1"
                                style={{ color: 'var(--muted)' }}
                                title={p.description}
                              >
                                {p.description}
                              </p>
                            )}
                          </div>
                        </td>

                        {/* Google Flow Project ID */}
                        <td className="py-3.5 px-3.5">
                          <div className="flex items-center gap-1.5">
                            <code
                              className="px-2 py-1 rounded text-[11px] font-mono"
                              style={{
                                background: 'var(--bg)',
                                border: '1px solid var(--border)',
                                color: '#93c5fd',
                              }}
                              title={p.id}
                            >
                              {p.id.slice(0, 8)}...{p.id.slice(-6)}
                            </code>
                            <button
                              onClick={() => copyText(p.id, `proj-${p.id}`)}
                              className="p-1.5 rounded cursor-pointer transition-colors hover:bg-white/10"
                              style={{ color: isCopied ? '#34d399' : 'var(--muted)' }}
                              title="Copy Project UUID"
                            >
                              {isCopied ? <Check className="w-3.5 h-3.5" /> : <Copy className="w-3.5 h-3.5" />}
                            </button>
                            <a
                              href={flowUrl}
                              target="_blank"
                              rel="noreferrer"
                              className="p-1.5 rounded transition-colors hover:bg-white/10"
                              style={{ color: 'var(--muted)' }}
                              title="Mở trên Google Flow"
                            >
                              <ExternalLink className="w-3.5 h-3.5" />
                            </a>
                          </div>
                        </td>

                        {/* Tỉ Lệ & Style */}
                        <td className="py-3.5 px-3.5">
                          <div className="flex flex-wrap items-center gap-1.5">
                            <span
                              className="px-2 py-0.5 rounded text-[10px] font-semibold"
                              style={{
                                background:
                                  p.aspect_ratio === '9:16'
                                    ? 'rgba(168,85,247,0.14)'
                                    : 'rgba(59,130,246,0.14)',
                                color: p.aspect_ratio === '9:16' ? '#c084fc' : '#60a5fa',
                                border: '1px solid rgba(255,255,255,0.08)',
                              }}
                            >
                              {p.aspect_ratio}
                            </span>
                            <span
                              className="px-2 py-0.5 rounded text-[10px] font-mono"
                              style={{
                                background: 'rgba(255,255,255,0.05)',
                                color: 'var(--text)',
                                border: '1px solid var(--border)',
                              }}
                            >
                              {p.material}
                            </span>
                            {p.user_paygate_tier && (
                              <span
                                className="px-1.5 py-0.5 rounded text-[9px] font-semibold"
                                style={{
                                  background: 'rgba(245,158,11,0.12)',
                                  color: '#fbbf24',
                                }}
                              >
                                {p.user_paygate_tier.includes('TWO') ? 'TIER 2' : 'TIER 1'}
                              </span>
                            )}
                          </div>
                        </td>

                        {/* Nhân Vật Khóa Cố Định (@Tag) */}
                        <td className="py-3.5 px-3.5 max-w-[280px]">
                          {p.characters.length === 0 ? (
                            <span className="text-[11px]" style={{ color: 'var(--muted)' }}>
                              Chưa cấu hình @Tag
                            </span>
                          ) : (
                            <div className="flex flex-wrap gap-1">
                              {p.characters.map(c => {
                                const mid = c.locked_media_id || c.default_media_id || ''
                                const charCopyKey = `char-${p.id}-${c.tag}`
                                return (
                                  <button
                                    key={c.tag}
                                    onClick={() => copyText(mid || c.tag, charCopyKey)}
                                    className="px-2 py-0.5 rounded text-[10px] font-mono flex items-center gap-1 cursor-pointer transition-opacity hover:opacity-90"
                                    style={{
                                      background: 'rgba(245,158,11,0.12)',
                                      color: '#fbbf24',
                                      border: '1px solid rgba(245,158,11,0.28)',
                                    }}
                                    title={`${c.name} — Media ID: ${mid || 'N/A'} (Bấm để copy)`}
                                  >
                                    <Lock className="w-2.5 h-2.5 shrink-0" />
                                    <span>{c.tag}</span>
                                    {copiedKey === charCopyKey && (
                                      <Check className="w-2.5 h-2.5 text-emerald-400" />
                                    )}
                                  </button>
                                )
                              })}
                            </div>
                          )}
                        </td>

                        {/* Tiến Độ Tập / Clips R2 */}
                        <td className="py-3.5 px-3.5">
                          <div className="flex flex-col gap-1 text-[11px]">
                            <div className="flex items-center gap-2">
                              <span className="font-semibold" style={{ color: 'var(--text)' }}>
                                {p.merged_episodes}/{p.total_episodes} tập
                              </span>
                              <span style={{ color: 'var(--muted)' }}>·</span>
                              <span style={{ color: 'var(--muted)' }}>
                                {p.rendered_clips}/{p.total_clips} clips
                              </span>
                            </div>
                            <div className="flex items-center gap-1.5">
                              <span
                                className="px-1.5 py-0.5 rounded text-[10px] font-medium flex items-center gap-1"
                                style={{
                                  background:
                                    p.r2_synced_clips > 0
                                      ? 'rgba(56,189,248,0.12)'
                                      : 'rgba(255,255,255,0.04)',
                                  color: p.r2_synced_clips > 0 ? '#38bdf8' : 'var(--muted)',
                                }}
                              >
                                <Cloud className="w-2.5 h-2.5" />
                                {p.r2_synced_clips} R2 clips · {p.r2_merged_episodes} R2 tập
                              </span>
                            </div>
                          </div>
                        </td>

                        {/* Trạng Thái */}
                        <td className="py-3.5 px-3.5">
                          <div className="flex flex-col gap-1">
                            {p.is_running ? (
                              <span
                                className="inline-flex items-center gap-1.5 px-2 py-0.5 rounded text-[10px] font-semibold w-fit"
                                style={{
                                  background: 'rgba(16,185,129,0.18)',
                                  color: '#34d399',
                                  border: '1px solid rgba(16,185,129,0.35)',
                                }}
                              >
                                <Sparkles className="w-3 h-3 animate-spin" />
                                ĐANG RENDER
                              </span>
                            ) : (
                              <span
                                className="inline-flex items-center gap-1.5 px-2 py-0.5 rounded text-[10px] font-semibold w-fit"
                                style={{
                                  background:
                                    p.status === 'ACTIVE'
                                      ? 'rgba(16,185,129,0.12)'
                                      : 'rgba(255,255,255,0.06)',
                                  color: p.status === 'ACTIVE' ? '#34d399' : 'var(--muted)',
                                }}
                              >
                                <span
                                  className="w-1.5 h-1.5 rounded-full"
                                  style={{
                                    background: p.status === 'ACTIVE' ? '#34d399' : 'var(--muted)',
                                  }}
                                />
                                {p.status}
                              </span>
                            )}
                            <span className="text-[10px]" style={{ color: 'var(--muted)' }}>
                              {formatDate(p.created_at)}
                            </span>
                          </div>
                        </td>

                        {/* Thao Tác */}
                        <td className="py-3.5 px-3.5 text-right">
                          <div className="flex items-center justify-end gap-1.5">
                            <button
                              onClick={() => navigate(`/projects/${p.id}`)}
                              className="px-2.5 py-1 rounded-md text-[11px] font-semibold flex items-center gap-1 cursor-pointer transition-opacity hover:opacity-90"
                              style={{
                                background: 'rgba(59,130,246,0.15)',
                                color: '#60a5fa',
                                border: '1px solid rgba(59,130,246,0.3)',
                              }}
                            >
                              Chi tiết
                              <ArrowRight className="w-3 h-3" />
                            </button>

                            {p.channel_slug && (
                              <button
                                onClick={() => navigate(`/channels/${p.channel_slug}`)}
                                className="px-2.5 py-1 rounded-md text-[11px] font-semibold flex items-center gap-1 cursor-pointer transition-opacity hover:opacity-90"
                                style={{
                                  background: 'rgba(16,185,129,0.15)',
                                  color: '#34d399',
                                  border: '1px solid rgba(16,185,129,0.3)',
                                }}
                                title="Quản lý tập & kịch bản trên Studio Kênh"
                              >
                                <Tv className="w-3 h-3" />
                                Studio
                              </button>
                            )}

                            {p.channel_slug && (
                              <button
                                onClick={() => navigate(`/gallery`)}
                                className="px-2 py-1 rounded-md text-[11px] font-medium flex items-center gap-1 cursor-pointer transition-opacity hover:opacity-90"
                                style={{
                                  background: 'var(--bg)',
                                  color: 'var(--text)',
                                  border: '1px solid var(--border)',
                                }}
                                title="Xem Thư Viện Video R2"
                              >
                                <Film className="w-3 h-3" />
                              </button>
                            )}
                          </div>
                        </td>
                      </tr>
                    )
                  })}
                </tbody>
              </table>
            </div>
          )
        ) : /* Characters List Table */
        filteredCharacters.length === 0 ? (
          <div className="p-8 text-center text-xs" style={{ color: 'var(--muted)' }}>
            Không tìm thấy nhân vật @Character nào khớp bộ lọc.
          </div>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full border-collapse text-left">
              <thead>
                <tr
                  className="text-[10px] font-semibold uppercase tracking-wider"
                  style={{
                    background: 'rgba(255,255,255,0.02)',
                    color: 'var(--muted)',
                    borderBottom: '1px solid var(--border)',
                  }}
                >
                  <th className="py-3 px-3.5 w-10 text-center">#</th>
                  <th className="py-3 px-3.5">Thẻ @Character & Tên</th>
                  <th className="py-3 px-3.5">Dự Án / Kênh Series</th>
                  <th className="py-3 px-3.5">Mã Media ID Khóa Cố Định (Google Flow)</th>
                  <th className="py-3 px-3.5">Mô Tả Ngoại Hình Cố Định</th>
                  <th className="py-3 px-3.5 text-right">Thao Tác</th>
                </tr>
              </thead>
              <tbody className="divide-y" style={{ borderColor: 'var(--border)' }}>
                {paginatedCharacters.map((c, idx) => {
                  const rowNumber = startIndex + idx + 1
                  const isCopiedMid = copiedKey === `mid-${c.key}`
                  const isCopiedTag = copiedKey === `tag-${c.key}`

                  return (
                    <tr
                      key={c.key}
                      className="transition-colors hover:bg-white/[0.02]"
                      style={{ borderBottom: '1px solid var(--border)' }}
                    >
                      <td
                        className="py-3 px-3.5 text-xs font-mono text-center"
                        style={{ color: 'var(--muted)' }}
                      >
                        {rowNumber}
                      </td>

                      {/* Thẻ @Character & Tên */}
                      <td className="py-3 px-3.5">
                        <div className="flex items-center gap-2">
                          <span
                            className="px-2 py-0.5 rounded text-[11px] font-mono font-semibold flex items-center gap-1"
                            style={{
                              background: 'rgba(245,158,11,0.14)',
                              color: '#fbbf24',
                              border: '1px solid rgba(245,158,11,0.3)',
                            }}
                          >
                            <Lock className="w-2.5 h-2.5" />
                            {c.tag}
                          </span>
                          <span className="text-xs font-semibold" style={{ color: 'var(--text)' }}>
                            {c.name}
                          </span>
                        </div>
                      </td>

                      {/* Dự Án / Kênh Series */}
                      <td className="py-3 px-3.5">
                        <div className="flex items-center gap-1.5">
                          <span
                            onClick={() => navigate(`/projects/${c.project_id}`)}
                            className="text-xs font-medium cursor-pointer hover:underline"
                            style={{ color: 'var(--text)' }}
                          >
                            {c.project_name}
                          </span>
                          <span
                            className="px-1.5 py-0.5 rounded text-[9px] font-mono"
                            style={{
                              background: 'rgba(255,255,255,0.05)',
                              color: 'var(--muted)',
                            }}
                          >
                            {c.aspect_ratio}
                          </span>
                        </div>
                      </td>

                      {/* Mã Media ID */}
                      <td className="py-3 px-3.5">
                        {c.media_id ? (
                          <div className="flex items-center gap-1.5">
                            <code
                              className="px-2 py-1 rounded text-[11px] font-mono"
                              style={{
                                background: 'var(--bg)',
                                border: '1px solid var(--border)',
                                color: '#34d399',
                              }}
                            >
                              {c.media_id}
                            </code>
                            <button
                              onClick={() => copyText(c.media_id, `mid-${c.key}`)}
                              className="p-1.5 rounded cursor-pointer hover:bg-white/10"
                              style={{ color: isCopiedMid ? '#34d399' : 'var(--muted)' }}
                              title="Copy Media ID"
                            >
                              {isCopiedMid ? (
                                <Check className="w-3.5 h-3.5" />
                              ) : (
                                <Copy className="w-3.5 h-3.5" />
                              )}
                            </button>
                          </div>
                        ) : (
                          <span className="text-[11px]" style={{ color: 'var(--muted)' }}>
                            Chưa khóa Media ID
                          </span>
                        )}
                      </td>

                      {/* Mô Tả Ngoại Hình */}
                      <td className="py-3 px-3.5 max-w-[360px]">
                        <p
                          className="m-0 text-[11px] line-clamp-2"
                          style={{ color: 'var(--muted)' }}
                          title={c.description}
                        >
                          {c.description || '—'}
                        </p>
                      </td>

                      {/* Thao Tác */}
                      <td className="py-3 px-3.5 text-right">
                        <div className="flex items-center justify-end gap-1.5">
                          <button
                            onClick={() => copyText(c.tag, `tag-${c.key}`)}
                            className="px-2 py-1 rounded text-[10px] font-mono cursor-pointer"
                            style={{
                              background: 'var(--bg)',
                              border: '1px solid var(--border)',
                              color: isCopiedTag ? '#34d399' : 'var(--text)',
                            }}
                          >
                            {isCopiedTag ? 'Đã copy @Tag' : 'Copy @Tag'}
                          </button>
                          <button
                            onClick={() => navigate(`/projects/${c.project_id}?tab=characters`)}
                            className="px-2.5 py-1 rounded text-[10px] font-semibold cursor-pointer"
                            style={{
                              background: 'rgba(59,130,246,0.14)',
                              color: '#60a5fa',
                              border: '1px solid rgba(59,130,246,0.3)',
                            }}
                          >
                            Mở Dự Án
                          </button>
                        </div>
                      </td>
                    </tr>
                  )
                })}
              </tbody>
            </table>
          </div>
        )}

        {/* Pagination Bar */}
        {totalItems > 0 && (
          <div
            className="px-4 py-3 flex flex-wrap items-center justify-between gap-3 text-xs"
            style={{
              background: 'rgba(255,255,255,0.015)',
              borderTop: '1px solid var(--border)',
            }}
          >
            <div className="flex items-center gap-3">
              <span style={{ color: 'var(--muted)' }}>
                Hiển thị{' '}
                <strong style={{ color: 'var(--text)' }}>
                  {startIndex + 1}–{Math.min(startIndex + pageSize, totalItems)}
                </strong>{' '}
                trên tổng số <strong style={{ color: 'var(--text)' }}>{totalItems}</strong>{' '}
                {viewMode === 'projects' ? 'dự án' : 'nhân vật'}
              </span>

              <div className="flex items-center gap-1.5">
                <span className="text-[11px]" style={{ color: 'var(--muted)' }}>
                  Số dòng:
                </span>
                <select
                  value={pageSize}
                  onChange={e => setPageSize(Number(e.target.value))}
                  className="px-2 py-1 rounded text-xs outline-none cursor-pointer"
                  style={{
                    background: 'var(--bg)',
                    border: '1px solid var(--border)',
                    color: 'var(--text)',
                  }}
                >
                  <option value={10}>10 / trang</option>
                  <option value={20}>20 / trang</option>
                  <option value={50}>50 / trang</option>
                </select>
              </div>
            </div>

            <div className="flex items-center gap-1.5">
              <button
                disabled={safePage <= 1}
                onClick={() => setCurrentPage(1)}
                className="px-2.5 py-1 rounded text-xs cursor-pointer disabled:opacity-40"
                style={{
                  background: 'var(--bg)',
                  border: '1px solid var(--border)',
                  color: 'var(--text)',
                }}
              >
                Đầu
              </button>
              <button
                disabled={safePage <= 1}
                onClick={() => setCurrentPage(p => Math.max(1, p - 1))}
                className="px-2.5 py-1 rounded text-xs cursor-pointer disabled:opacity-40"
                style={{
                  background: 'var(--bg)',
                  border: '1px solid var(--border)',
                  color: 'var(--text)',
                }}
              >
                ‹ Trước
              </button>

              {Array.from({ length: totalPages }, (_, i) => i + 1)
                .filter(p => Math.abs(p - safePage) <= 2 || p === 1 || p === totalPages)
                .map((p, idx, arr) => {
                  const prev = arr[idx - 1]
                  const showEllipsis = prev !== undefined && p - prev > 1
                  return (
                    <span key={p} className="flex items-center gap-1">
                      {showEllipsis && (
                        <span className="px-1 text-xs" style={{ color: 'var(--muted)' }}>
                          ...
                        </span>
                      )}
                      <button
                        onClick={() => setCurrentPage(p)}
                        className="w-7 h-7 rounded text-xs font-semibold cursor-pointer"
                        style={{
                          background:
                            p === safePage ? 'rgba(16,185,129,0.2)' : 'var(--bg)',
                          color: p === safePage ? '#34d399' : 'var(--text)',
                          border:
                            p === safePage
                              ? '1px solid rgba(16,185,129,0.45)'
                              : '1px solid var(--border)',
                        }}
                      >
                        {p}
                      </button>
                    </span>
                  )
                })}

              <button
                disabled={safePage >= totalPages}
                onClick={() => setCurrentPage(p => Math.min(totalPages, p + 1))}
                className="px-2.5 py-1 rounded text-xs cursor-pointer disabled:opacity-40"
                style={{
                  background: 'var(--bg)',
                  border: '1px solid var(--border)',
                  color: 'var(--text)',
                }}
              >
                Sau ›
              </button>
              <button
                disabled={safePage >= totalPages}
                onClick={() => setCurrentPage(totalPages)}
                className="px-2.5 py-1 rounded text-xs cursor-pointer disabled:opacity-40"
                style={{
                  background: 'var(--bg)',
                  border: '1px solid var(--border)',
                  color: 'var(--text)',
                }}
              >
                Cuối
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}
