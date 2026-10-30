import { useState, useEffect, useCallback, useMemo } from 'react'
import { useNavigate } from 'react-router-dom'
import {
  Film,
  Tv,
  Image as ImageIcon,
  Music,
  Play,
  ExternalLink,
  Copy,
  Check,
  Search,
  RefreshCw,
  X,
  ChevronLeft,
  ChevronRight,
  ChevronsLeft,
  ChevronsRight,
  Sparkles,
  Layers,
  Cloud,
  HardDrive,
  SlidersHorizontal,
  ArrowUpDown,
} from 'lucide-react'
import { fetchAPI, API_BASE_URL } from '../api/client'

const DEFAULT_R2_PUBLIC_BASE = 'https://pub-53dae622644845c09c48558d8a42fe29.r2.dev'
const LEGACY_R2_BASES = [
  'https://pub-31538b394ab64f96ba3dff5f02ecab44.r2.dev/flowkit',
  'https://pub-31538b394ab64f96ba3dff5f02ecab44.r2.dev',
]

export interface GalleryChannelSummary {
  slug: string
  name: string
  aspect_ratio: string
  ep_prefix: string
  description: string
  full_episodes_count: number
  clips_count: number
  images_count: number
  total_media_count: number
}

export interface GalleryMediaItem {
  id: string
  channel_slug: string
  channel_name: string
  aspect_ratio: string
  episode_num: number
  episode_label: string
  folder_name: string
  clip_num: number | null
  category: 'full_episode' | 'clip' | 'frame'
  title: string
  file_name: string
  url: string
  r2_url?: string | null
  r2_key?: string | null
  thumbnail_url?: string | null
  media_kind: 'video' | 'image' | 'audio'
  media_type: string
  ext: string
  size_mb?: number | null
  prompt_preview?: string
}

interface GalleryResponse {
  channels: GalleryChannelSummary[]
  items: GalleryMediaItem[]
  total_items: number
}

const CHANNEL_ACCENTS: Record<
  string,
  {
    badge: string
    bar: string
    iconBg: string
    borderActive: string
    glow: string
    shortTag: string
  }
> = {
  'mit-va-du-1970': {
    badge: 'bg-amber-500/15 text-amber-300 border-amber-500/30',
    bar: 'from-amber-400 to-orange-500',
    iconBg: 'from-amber-500/30 to-orange-600/20 text-amber-300 border-amber-500/40',
    borderActive: 'border-amber-400/80 bg-gradient-to-br from-amber-500/20 via-slate-900/95 to-orange-500/10',
    glow: 'shadow-[0_0_24px_-4px_rgba(245,158,11,0.35)]',
    shortTag: 'Miền Tây 1970',
  },
  '365ngayvietnam': {
    badge: 'bg-emerald-500/15 text-emerald-300 border-emerald-500/30',
    bar: 'from-emerald-400 to-teal-500',
    iconBg: 'from-emerald-500/30 to-teal-600/20 text-emerald-300 border-emerald-500/40',
    borderActive: 'border-emerald-400/80 bg-gradient-to-br from-emerald-500/20 via-slate-900/95 to-teal-500/10',
    glow: 'shadow-[0_0_24px_-4px_rgba(16,185,129,0.35)]',
    shortTag: 'Xuyên Việt',
  },
  'me-va-be': {
    badge: 'bg-pink-500/15 text-pink-300 border-pink-500/30',
    bar: 'from-pink-400 to-rose-500',
    iconBg: 'from-pink-500/30 to-rose-600/20 text-pink-300 border-pink-500/40',
    borderActive: 'border-pink-400/80 bg-gradient-to-br from-pink-500/20 via-slate-900/95 to-rose-500/10',
    glow: 'shadow-[0_0_24px_-4px_rgba(236,72,153,0.35)]',
    shortTag: 'Mẹ & Bé',
  },
  'pheo-va-no-meo': {
    badge: 'bg-purple-500/15 text-purple-300 border-purple-500/30',
    bar: 'from-purple-400 to-indigo-500',
    iconBg: 'from-purple-500/30 to-indigo-600/20 text-purple-300 border-purple-500/40',
    borderActive: 'border-purple-400/80 bg-gradient-to-br from-purple-500/20 via-slate-900/95 to-indigo-500/10',
    glow: 'shadow-[0_0_24px_-4px_rgba(168,85,247,0.35)]',
    shortTag: 'Mèo Đầu Bếp',
  },
  'tay-du-ky-2026': {
    badge: 'bg-sky-500/15 text-sky-300 border-sky-500/30',
    bar: 'from-sky-400 to-indigo-500',
    iconBg: 'from-sky-500/30 to-indigo-600/20 text-sky-300 border-sky-500/40',
    borderActive: 'border-sky-400/80 bg-gradient-to-br from-sky-500/20 via-slate-900/95 to-indigo-500/10',
    glow: 'shadow-[0_0_24px_-4px_rgba(14,165,233,0.35)]',
    shortTag: 'Tây Du 2026',
  },
  'biet-doi-gara': {
    badge: 'bg-cyan-500/15 text-cyan-300 border-cyan-500/30',
    bar: 'from-cyan-400 to-blue-500',
    iconBg: 'from-cyan-500/30 to-blue-600/20 text-cyan-300 border-cyan-500/40',
    borderActive: 'border-cyan-400/80 bg-gradient-to-br from-cyan-500/20 via-slate-900/95 to-blue-500/10',
    glow: 'shadow-[0_0_24px_-4px_rgba(6,182,212,0.35)]',
    shortTag: 'Hành Động 16:9',
  },
  'ke-song-sot': {
    badge: 'bg-rose-500/15 text-rose-300 border-rose-500/30',
    bar: 'from-rose-400 to-red-600',
    iconBg: 'from-rose-500/30 to-red-600/20 text-rose-300 border-rose-500/40',
    borderActive: 'border-rose-400/80 bg-gradient-to-br from-rose-500/20 via-slate-900/95 to-red-500/10',
    glow: 'shadow-[0_0_24px_-4px_rgba(244,63,94,0.35)]',
    shortTag: 'Sinh Tồn 16:9',
  },
}

function normalizeMediaUrl(rawUrl?: string | null): string {
  if (!rawUrl) return ''
  let u = rawUrl.trim()
  for (const legacy of LEGACY_R2_BASES) {
    if (u.startsWith(legacy + '/')) {
      u = DEFAULT_R2_PUBLIC_BASE + '/' + u.slice(legacy.length + 1)
      break
    }
  }
  u = u.replace(`${DEFAULT_R2_PUBLIC_BASE}/flowkit/series/`, `${DEFAULT_R2_PUBLIC_BASE}/series/`)
  if (u.startsWith('http://') || u.startsWith('https://')) return u
  return `${API_BASE_URL}${u}`
}

function resolveItemMediaInfo(item: GalleryMediaItem): {
  url: string
  kind: 'video' | 'image' | 'audio'
  mimeType: string
  extLabel: string
} {
  const url = normalizeMediaUrl(item.r2_url || item.url)
  const clean = url.split('?')[0].split('#')[0].toLowerCase()

  if (clean.endsWith('.png')) {
    return { url, kind: 'image', mimeType: 'image/png', extLabel: 'PNG' }
  }
  if (clean.endsWith('.webp')) {
    return { url, kind: 'image', mimeType: 'image/webp', extLabel: 'WEBP' }
  }
  if (clean.endsWith('.gif')) {
    return { url, kind: 'image', mimeType: 'image/gif', extLabel: 'GIF' }
  }
  if (clean.endsWith('.jpg') || clean.endsWith('.jpeg') || item.category === 'frame' || item.media_kind === 'image') {
    return { url, kind: 'image', mimeType: item.media_type || 'image/jpeg', extLabel: item.ext || 'JPG' }
  }
  if (clean.endsWith('.mp3') || clean.endsWith('.wav') || clean.endsWith('.m4a') || item.media_kind === 'audio') {
    return {
      url,
      kind: 'audio',
      mimeType: item.media_type || (clean.endsWith('.wav') ? 'audio/wav' : 'audio/mpeg'),
      extLabel: item.ext || (clean.endsWith('.wav') ? 'WAV' : 'MP3'),
    }
  }
  if (clean.endsWith('.webm')) {
    return { url, kind: 'video', mimeType: 'video/webm', extLabel: 'WEBM' }
  }
  if (clean.endsWith('.mov')) {
    return { url, kind: 'video', mimeType: 'video/quicktime', extLabel: 'MOV' }
  }
  return {
    url,
    kind: 'video',
    mimeType: item.media_type || 'video/mp4',
    extLabel: item.ext || 'MP4',
  }
}

export default function GalleryPage() {
  const navigate = useNavigate()
  const [channels, setChannels] = useState<GalleryChannelSummary[]>([])
  const [items, setItems] = useState<GalleryMediaItem[]>([])
  const [loading, setLoading] = useState(true)

  // Filters & Sorting
  const [selectedChannel, setSelectedChannel] = useState<string>('ALL')
  const [categoryFilter, setCategoryFilter] = useState<'ALL' | 'full_episode' | 'clip' | 'frame' | 'audio'>('ALL')
  const [formatFilter, setFormatFilter] = useState<string>('ALL')
  const [episodeFilter, setEpisodeFilter] = useState<string>('ALL')
  const [searchQuery, setSearchQuery] = useState<string>('')
  const [sortOrder, setSortOrder] = useState<'ep_desc' | 'ep_asc' | 'size_desc'>('ep_desc')

  // Pagination state
  const [currentPage, setCurrentPage] = useState<number>(1)
  const [pageSize, setPageSize] = useState<number>(20)

  const [copiedId, setCopiedId] = useState<string | null>(null)

  // Active modal item index in filteredItems (ONLY loads video when modal is opened!)
  const [activeModalIdx, setActiveModalIdx] = useState<number | null>(null)

  const loadGallery = useCallback(async () => {
    setLoading(true)
    try {
      const res = await fetchAPI<GalleryResponse>('/api/cms/gallery')
      setChannels(res.channels || [])
      setItems(res.items || [])
    } catch (err) {
      console.error('Failed to load CMS gallery:', err)
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => {
    loadGallery()
  }, [loadGallery])

  // Reset episode filter & page when switching channel or filters
  useEffect(() => {
    setEpisodeFilter('ALL')
    setCurrentPage(1)
  }, [selectedChannel])

  useEffect(() => {
    setCurrentPage(1)
  }, [categoryFilter, formatFilter, episodeFilter, searchQuery, pageSize, sortOrder])

  function copyLink(text: string, id: string) {
    navigator.clipboard.writeText(text)
    setCopiedId(id)
    setTimeout(() => setCopiedId(null), 1800)
  }

  const channelScopedItems = useMemo(() => {
    if (selectedChannel === 'ALL') return items
    return items.filter(it => it.channel_slug === selectedChannel)
  }, [items, selectedChannel])

  const availableEpisodes = useMemo(() => {
    const map = new Map<number, string>()
    for (const it of channelScopedItems) {
      if (it.episode_num > 0 && !map.has(it.episode_num)) {
        map.set(it.episode_num, it.episode_label)
      }
    }
    return Array.from(map.entries()).sort((a, b) => a[0] - b[0])
  }, [channelScopedItems])

  const availableFormats = useMemo(() => {
    const counts: Record<string, number> = {}
    for (const it of channelScopedItems) {
      const info = resolveItemMediaInfo(it)
      counts[info.extLabel] = (counts[info.extLabel] || 0) + 1
    }
    return Object.entries(counts).sort((a, b) => b[1] - a[1])
  }, [channelScopedItems])

  const countsByCategory = useMemo(() => {
    let full = 0
    let clip = 0
    let frame = 0
    let audio = 0
    for (const it of channelScopedItems) {
      const info = resolveItemMediaInfo(it)
      if (info.kind === 'audio') audio++
      else if (it.category === 'full_episode') full++
      else if (it.category === 'clip') clip++
      else if (it.category === 'frame' || info.kind === 'image') frame++
    }
    return {
      all: channelScopedItems.length,
      full,
      clip,
      frame,
      audio,
    }
  }, [channelScopedItems])

  const filteredItems = useMemo(() => {
    const list = channelScopedItems.filter(it => {
      const info = resolveItemMediaInfo(it)
      if (categoryFilter === 'full_episode' && it.category !== 'full_episode') return false
      if (categoryFilter === 'clip' && it.category !== 'clip') return false
      if (categoryFilter === 'frame' && it.category !== 'frame' && info.kind !== 'image') return false
      if (categoryFilter === 'audio' && info.kind !== 'audio') return false

      if (formatFilter !== 'ALL' && info.extLabel !== formatFilter) return false
      if (episodeFilter !== 'ALL' && String(it.episode_num) !== episodeFilter) return false

      if (searchQuery.trim()) {
        const q = searchQuery.trim().toLowerCase()
        const hay = `${it.title} ${it.file_name} ${it.channel_name} ${it.episode_label} ${it.prompt_preview || ''} ${info.mimeType}`.toLowerCase()
        if (!hay.includes(q)) return false
      }
      return true
    })

    return [...list].sort((a, b) => {
      if (sortOrder === 'size_desc') {
        return (b.size_mb || 0) - (a.size_mb || 0)
      }
      if (a.channel_slug !== b.channel_slug && selectedChannel === 'ALL') {
        return a.channel_slug.localeCompare(b.channel_slug)
      }
      if (a.episode_num !== b.episode_num) {
        return sortOrder === 'ep_desc' ? b.episode_num - a.episode_num : a.episode_num - b.episode_num
      }
      // Full episode comes before individual clips within the same episode
      if (a.category === 'full_episode' && b.category !== 'full_episode') return -1
      if (b.category === 'full_episode' && a.category !== 'full_episode') return 1
      return (a.clip_num || 0) - (b.clip_num || 0)
    })
  }, [channelScopedItems, categoryFilter, formatFilter, episodeFilter, searchQuery, sortOrder, selectedChannel])

  const totalPages = Math.max(1, Math.ceil(filteredItems.length / pageSize))
  const safePage = Math.min(currentPage, totalPages)
  const startIdx = (safePage - 1) * pageSize
  const endIdx = Math.min(startIdx + pageSize, filteredItems.length)
  const paginatedItems = useMemo(
    () => filteredItems.slice(startIdx, endIdx),
    [filteredItems, startIdx, endIdx],
  )

  const pageNumbers = useMemo(() => {
    const pages: number[] = []
    const maxButtons = 7
    let start = Math.max(1, safePage - Math.floor(maxButtons / 2))
    const end = Math.min(totalPages, start + maxButtons - 1)
    if (end - start + 1 < maxButtons) {
      start = Math.max(1, end - maxButtons + 1)
    }
    for (let p = start; p <= end; p++) pages.push(p)
    return pages
  }, [safePage, totalPages])

  const totalAllMedia = useMemo(
    () => channels.reduce((acc, c) => acc + c.total_media_count, 0),
    [channels],
  )
  const totalFullEps = useMemo(
    () => channels.reduce((acc, c) => acc + c.full_episodes_count, 0),
    [channels],
  )
  const totalClips = useMemo(
    () => channels.reduce((acc, c) => acc + c.clips_count, 0),
    [channels],
  )

  const activeModalItem = activeModalIdx !== null ? filteredItems[activeModalIdx] ?? null : null

  return (
    <div className="flex flex-col gap-5 pb-12 max-w-[1600px] mx-auto">
      {/* ═══════════════════════════════════════════════════════════════════
          1. COMPACT CHANNEL SELECT DROPDOWN BAR (THANH CHỌN KÊNH SERIES)
         ═══════════════════════════════════════════════════════════════════ */}
      <div className="studio-card rounded-2xl px-5 py-4 flex flex-wrap items-center justify-between gap-4 border border-slate-800/90">
        <div className="flex items-center gap-3 flex-wrap">
          <div className="w-9 h-9 rounded-xl bg-gradient-to-br from-indigo-500/30 to-purple-500/20 border border-indigo-500/40 flex items-center justify-center text-indigo-300 shrink-0">
            <Tv size={17} />
          </div>

          <div className="flex flex-col gap-0.5">
            <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400">
              Chọn Kênh Series
            </span>
            <select
              value={selectedChannel}
              onChange={e => setSelectedChannel(e.target.value)}
              className="px-3.5 py-2 rounded-xl bg-slate-950/95 hover:bg-slate-900 border border-indigo-500/40 focus:border-indigo-400 text-xs font-extrabold text-white outline-none cursor-pointer shadow-inner min-w-[290px]"
            >
              <option value="ALL" className="bg-slate-950 text-white">
                📺 Tất cả các kênh Series ({totalAllMedia} files • {totalFullEps} Tập FULL • {totalClips} Clips)
              </option>
              {channels.map(ch => {
                const ratioLabel = ch.aspect_ratio === 'VIDEO_ASPECT_RATIO_PORTRAIT' ? '9:16 Dọc' : '16:9 Ngang'
                return (
                  <option key={ch.slug} value={ch.slug} className="bg-slate-950 text-white">
                    🎬 {ch.name} [{ratioLabel}] — {ch.total_media_count} files ({ch.full_episodes_count} FULL • {ch.clips_count} Clips)
                  </option>
                )
              })}
            </select>
          </div>

          {/* Quick Selected Channel Stats Badges */}
          <div className="hidden md:flex items-center gap-2 pl-2 border-l border-slate-800">
            <span className="px-2.5 py-1 rounded-lg bg-amber-500/15 text-amber-300 border border-amber-500/30 text-xs font-bold font-mono">
              🎞️ {countsByCategory.full} Tập FULL
            </span>
            <span className="px-2.5 py-1 rounded-lg bg-emerald-500/15 text-emerald-300 border border-emerald-500/30 text-xs font-bold font-mono">
              🎬 {countsByCategory.clip} Clips
            </span>
            {countsByCategory.frame > 0 && (
              <span className="px-2.5 py-1 rounded-lg bg-pink-500/15 text-pink-300 border border-pink-500/30 text-xs font-bold font-mono">
                🖼️ {countsByCategory.frame} Ảnh
              </span>
            )}
          </div>
        </div>

        <div className="flex items-center gap-2">
          {selectedChannel !== 'ALL' && (
            <button
              onClick={() => navigate(`/channels/${selectedChannel}`)}
              className="px-3.5 py-2 rounded-xl text-xs font-bold studio-glow-btn flex items-center gap-1.5 cursor-pointer"
            >
              <Sparkles size={13} />
              Mở Studio Kênh Này
            </button>
          )}
          <button
            onClick={loadGallery}
            className="px-3.5 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700/80 text-xs font-semibold text-slate-200 flex items-center gap-1.5 transition-colors cursor-pointer"
          >
            <RefreshCw size={13} className={loading ? 'animate-spin text-indigo-400' : 'text-indigo-400'} />
            Làm mới
          </button>
        </div>
      </div>

      {/* ═══════════════════════════════════════════════════════════════════
          2. MEDIA FORMAT & CATEGORY FILTER BAR (BỘ LỌC THEO ĐỊNH DẠNG FILE)
         ═══════════════════════════════════════════════════════════════════ */}
      <div className="studio-card rounded-2xl p-4 flex flex-wrap items-center justify-between gap-3 border border-slate-800/90">
        {/* Category / Media Type Tabs */}
        <div className="flex items-center gap-1.5 flex-wrap">
          <button
            type="button"
            onClick={() => setCategoryFilter('ALL')}
            className={`px-3 py-1.5 rounded-xl text-xs font-bold flex items-center gap-1.5 border transition-all cursor-pointer ${
              categoryFilter === 'ALL'
                ? 'bg-indigo-600 text-white border-indigo-500 shadow-sm'
                : 'bg-slate-950/80 text-slate-300 border-slate-800 hover:border-slate-700'
            }`}
          >
            <Layers size={13} />
            <span>Tất cả Media</span>
            <span className="px-1.5 py-0.2 rounded-md text-[10px] bg-black/30 font-mono">{countsByCategory.all}</span>
          </button>

          <button
            type="button"
            onClick={() => setCategoryFilter('full_episode')}
            className={`px-3 py-1.5 rounded-xl text-xs font-bold flex items-center gap-1.5 border transition-all cursor-pointer ${
              categoryFilter === 'full_episode'
                ? 'bg-amber-500 text-slate-950 border-amber-400 shadow-sm'
                : 'bg-slate-950/80 text-amber-300 border-slate-800 hover:border-amber-500/40'
            }`}
          >
            <Film size={13} />
            <span>Tập Hoàn Chỉnh (FULL .MP4)</span>
            <span className="px-1.5 py-0.2 rounded-md text-[10px] bg-black/25 font-mono">{countsByCategory.full}</span>
          </button>

          <button
            type="button"
            onClick={() => setCategoryFilter('clip')}
            className={`px-3 py-1.5 rounded-xl text-xs font-bold flex items-center gap-1.5 border transition-all cursor-pointer ${
              categoryFilter === 'clip'
                ? 'bg-emerald-500 text-slate-950 border-emerald-400 shadow-sm'
                : 'bg-slate-950/80 text-emerald-300 border-slate-800 hover:border-emerald-500/40'
            }`}
          >
            <Play size={13} />
            <span>Clip Phân Cảnh (.MP4)</span>
            <span className="px-1.5 py-0.2 rounded-md text-[10px] bg-black/25 font-mono">{countsByCategory.clip}</span>
          </button>

          <button
            type="button"
            onClick={() => setCategoryFilter('frame')}
            className={`px-3 py-1.5 rounded-xl text-xs font-bold flex items-center gap-1.5 border transition-all cursor-pointer ${
              categoryFilter === 'frame'
                ? 'bg-pink-500 text-white border-pink-400 shadow-sm'
                : 'bg-slate-950/80 text-pink-300 border-slate-800 hover:border-pink-500/40'
            }`}
          >
            <ImageIcon size={13} />
            <span>Hình Ảnh / Frame (.JPG/.PNG)</span>
            <span className="px-1.5 py-0.2 rounded-md text-[10px] bg-black/25 font-mono">{countsByCategory.frame}</span>
          </button>

          {countsByCategory.audio > 0 && (
            <button
              type="button"
              onClick={() => setCategoryFilter('audio')}
              className={`px-3 py-1.5 rounded-xl text-xs font-bold flex items-center gap-1.5 border transition-all cursor-pointer ${
                categoryFilter === 'audio'
                  ? 'bg-cyan-500 text-slate-950 border-cyan-400 shadow-sm'
                  : 'bg-slate-950/80 text-cyan-300 border-slate-800 hover:border-cyan-500/40'
              }`}
            >
              <Music size={13} />
              <span>Âm Thanh (.MP3/.WAV)</span>
              <span className="px-1.5 py-0.2 rounded-md text-[10px] bg-black/25 font-mono">
                {countsByCategory.audio}
              </span>
            </button>
          )}
        </div>

        {/* Right Side: File Extension Pill Filter + Episode Filter + Sort + Search */}
        <div className="flex items-center gap-2 flex-wrap">
          {/* Exact File Format Extension Selector */}
          <div className="flex items-center gap-1 p-1 rounded-xl bg-slate-950/90 border border-slate-800 text-[11px]">
            <span className="px-2 text-slate-400 flex items-center gap-1">
              <SlidersHorizontal size={11} /> Định dạng:
            </span>
            <button
              type="button"
              onClick={() => setFormatFilter('ALL')}
              className={`px-2 py-0.5 rounded-lg font-mono font-bold cursor-pointer ${
                formatFilter === 'ALL' ? 'bg-indigo-600 text-white' : 'text-slate-400 hover:text-white'
              }`}
            >
              ALL
            </button>
            {availableFormats.map(([ext, cnt]) => (
              <button
                key={ext}
                type="button"
                onClick={() => setFormatFilter(ext)}
                className={`px-2 py-0.5 rounded-lg font-mono font-bold cursor-pointer ${
                  formatFilter === ext ? 'bg-indigo-600 text-white' : 'text-slate-400 hover:text-white'
                }`}
              >
                .{ext} ({cnt})
              </button>
            ))}
          </div>

          {/* Episode Dropdown */}
          {availableEpisodes.length > 0 && (
            <select
              value={episodeFilter}
              onChange={e => setEpisodeFilter(e.target.value)}
              className="px-3 py-1.5 rounded-xl bg-slate-950/90 border border-slate-800 text-xs font-semibold text-slate-200 outline-none focus:border-indigo-500 cursor-pointer"
            >
              <option value="ALL">Tất cả tập ({availableEpisodes.length} tập)</option>
              {availableEpisodes.map(([epNum, epLabel]) => (
                <option key={epNum} value={String(epNum)}>
                  {epLabel}
                </option>
              ))}
            </select>
          )}

          {/* Sort Order */}
          <div className="flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl bg-slate-950/90 border border-slate-800 text-xs text-slate-300">
            <ArrowUpDown size={12} className="text-indigo-400" />
            <select
              value={sortOrder}
              onChange={e => setSortOrder(e.target.value as 'ep_desc' | 'ep_asc' | 'size_desc')}
              className="bg-transparent outline-none font-semibold text-slate-200 cursor-pointer"
            >
              <option value="ep_desc" className="bg-slate-900">Tập mới nhất trước</option>
              <option value="ep_asc" className="bg-slate-900">Tập 1 → cuối</option>
              <option value="size_desc" className="bg-slate-900">Dung lượng giảm dần</option>
            </select>
          </div>

          {/* Search Input */}
          <div className="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-slate-950/90 border border-slate-800 text-xs">
            <Search size={13} className="text-slate-400" />
            <input
              type="text"
              value={searchQuery}
              onChange={e => setSearchQuery(e.target.value)}
              placeholder="Tìm tên file .mp4, tập, clip..."
              className="bg-transparent outline-none text-white placeholder:text-slate-500 w-44"
            />
            {searchQuery && (
              <button onClick={() => setSearchQuery('')} className="text-slate-400 hover:text-white cursor-pointer">
                <X size={12} />
              </button>
            )}
          </div>
        </div>
      </div>

      {/* ═══════════════════════════════════════════════════════════════════
          3. PAGINATED LIST TABLE (BẢNG DANH SÁCH PHÂN TRANG DỄ KIỂM SOÁT)
         ═══════════════════════════════════════════════════════════════════ */}
      {loading ? (
        <div className="studio-card rounded-3xl p-16 text-center flex flex-col items-center justify-center gap-3 text-slate-400">
          <RefreshCw size={24} className="animate-spin text-indigo-400" />
          <span className="text-xs font-semibold">Đang tải danh sách media từ Cloudflare R2 &amp; CMS...</span>
        </div>
      ) : filteredItems.length === 0 ? (
        <div className="studio-card rounded-3xl p-16 text-center flex flex-col items-center justify-center gap-3 text-slate-400">
          <Film size={28} className="text-slate-500" />
          <div className="text-sm font-bold text-slate-200">Không tìm thấy file media nào khớp bộ lọc hiện tại</div>
          <p className="text-xs text-slate-400">
            Thử chuyển sang kênh khác hoặc chọn bộ lọc &ldquo;Tất cả Media&rdquo; để xem toàn bộ {items.length} file.
          </p>
        </div>
      ) : (
        <div className="studio-card rounded-3xl overflow-hidden border border-slate-800/90 flex flex-col">
          {/* Top Table Pagination & Summary Bar */}
          <div className="px-5 py-3.5 bg-slate-950/80 border-b border-slate-800/90 flex flex-wrap items-center justify-between gap-3 text-xs">
            <div className="flex items-center gap-2 text-slate-300">
              <span>
                Hiển thị <strong className="text-white font-mono">{startIdx + 1}</strong>–
                <strong className="text-white font-mono">{endIdx}</strong> trên tổng{' '}
                <strong className="text-indigo-300 font-mono">{filteredItems.length}</strong> files
              </span>
              <span className="text-slate-600">•</span>
              <span className="text-slate-400">
                Trang <strong className="text-white font-mono">{safePage}</strong>/{totalPages}
              </span>
            </div>

            <div className="flex items-center gap-3 flex-wrap">
              <div className="flex items-center gap-1.5 text-slate-400">
                <span>Số dòng / trang:</span>
                <select
                  value={pageSize}
                  onChange={e => setPageSize(Number(e.target.value))}
                  className="px-2.5 py-1 rounded-lg bg-slate-900 border border-slate-700 text-white font-mono font-bold outline-none cursor-pointer"
                >
                  {[15, 20, 30, 50, 100].map(sz => (
                    <option key={sz} value={sz}>
                      {sz} dòng
                    </option>
                  ))}
                </select>
              </div>

              {/* Quick Page Navigation */}
              <div className="flex items-center gap-1">
                <button
                  type="button"
                  disabled={safePage <= 1}
                  onClick={() => setCurrentPage(1)}
                  className="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-300 disabled:opacity-35 cursor-pointer"
                  title="Trang đầu"
                >
                  <ChevronsLeft size={13} />
                </button>
                <button
                  type="button"
                  disabled={safePage <= 1}
                  onClick={() => setCurrentPage(p => Math.max(1, p - 1))}
                  className="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-300 disabled:opacity-35 cursor-pointer"
                  title="Trang trước"
                >
                  <ChevronLeft size={13} />
                </button>
                {pageNumbers.map(pNum => (
                  <button
                    key={pNum}
                    type="button"
                    onClick={() => setCurrentPage(pNum)}
                    className={`min-w-[28px] h-7 px-2 rounded-lg font-mono text-xs font-bold border transition-colors cursor-pointer ${
                      pNum === safePage
                        ? 'bg-indigo-600 text-white border-indigo-500 shadow-sm'
                        : 'bg-slate-900 hover:bg-slate-800 text-slate-300 border-slate-800'
                    }`}
                  >
                    {pNum}
                  </button>
                ))}
                <button
                  type="button"
                  disabled={safePage >= totalPages}
                  onClick={() => setCurrentPage(p => Math.min(totalPages, p + 1))}
                  className="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-300 disabled:opacity-35 cursor-pointer"
                  title="Trang sau"
                >
                  <ChevronRight size={13} />
                </button>
                <button
                  type="button"
                  disabled={safePage >= totalPages}
                  onClick={() => setCurrentPage(totalPages)}
                  className="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-300 disabled:opacity-35 cursor-pointer"
                  title="Trang cuối"
                >
                  <ChevronsRight size={13} />
                </button>
              </div>
            </div>
          </div>

          {/* Main Paginated List Table */}
          <div className="overflow-x-auto">
            <table className="w-full text-left border-collapse">
              <thead>
                <tr className="border-b border-slate-800 bg-slate-950/95 text-[11px] uppercase tracking-wider text-slate-400">
                  <th className="py-3.5 px-4 w-12 text-center">#</th>
                  <th className="py-3.5 px-3 w-14">Thumb</th>
                  <th className="py-3.5 px-4">Kênh Series</th>
                  <th className="py-3.5 px-4">Tập / Phân Cảnh</th>
                  <th className="py-3.5 px-4">Tiêu Đề &amp; Tên File</th>
                  <th className="py-3.5 px-4">Định Dạng &amp; Nguồn</th>
                  <th className="py-3.5 px-4">Dung Lượng</th>
                  <th className="py-3.5 px-5 text-right">Thao Tác</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-800/70 text-xs">
                {paginatedItems.map((item, localIdx) => {
                  const globalIdx = startIdx + localIdx
                  const media = resolveItemMediaInfo(item)
                  const accent = CHANNEL_ACCENTS[item.channel_slug] || CHANNEL_ACCENTS['mit-va-du-1970']
                  const isFullEp = item.category === 'full_episode'
                  const isPortrait = item.aspect_ratio === 'VIDEO_ASPECT_RATIO_PORTRAIT'
                  const thumbUrl = item.thumbnail_url ? normalizeMediaUrl(item.thumbnail_url) : null

                  return (
                    <tr
                      key={item.id}
                      onClick={() => setActiveModalIdx(globalIdx)}
                      className="hover:bg-slate-900/75 transition-colors cursor-pointer group"
                    >
                      {/* Col 1: Row Index */}
                      <td className="py-3 px-4 text-center font-mono text-[11px] text-slate-500">
                        {globalIdx + 1}
                      </td>

                      {/* Col 2: Lightweight Thumbnail / Format Icon (NO <video> preload!) */}
                      <td className="py-3 px-3">
                        <div className="w-10 h-10 rounded-xl bg-slate-900 border border-slate-800 group-hover:border-indigo-500/60 flex items-center justify-center overflow-hidden relative shrink-0">
                          {media.kind === 'image' ? (
                            <img
                              src={media.url}
                              alt={item.title}
                              loading="lazy"
                              className="w-full h-full object-cover"
                            />
                          ) : thumbUrl ? (
                            <img
                              src={thumbUrl}
                              alt={item.title}
                              loading="lazy"
                              className="w-full h-full object-cover"
                            />
                          ) : isFullEp ? (
                            <Film size={16} className="text-amber-400 group-hover:scale-110 transition-transform" />
                          ) : media.kind === 'audio' ? (
                            <Music size={16} className="text-cyan-400 group-hover:scale-110 transition-transform" />
                          ) : (
                            <Play
                              size={15}
                              className="text-indigo-400 group-hover:text-white group-hover:scale-110 transition-all ml-0.5"
                            />
                          )}
                        </div>
                      </td>

                      {/* Col 3: Channel Name & Aspect Ratio */}
                      <td className="py-3 px-4">
                        <div className="flex flex-col gap-1">
                          <span className={`px-2 py-0.5 rounded-md text-[10px] font-bold border w-fit ${accent.badge}`}>
                            {item.channel_name}
                          </span>
                          <span className="text-[10px] font-mono text-slate-500">
                            {isPortrait ? '9:16 Dọc' : '16:9 Ngang'}
                          </span>
                        </div>
                      </td>

                      {/* Col 4: Episode & Clip Badge */}
                      <td className="py-3 px-4">
                        <div className="flex items-center gap-1.5 flex-wrap">
                          <span className="px-2 py-0.5 rounded-md text-[11px] font-bold bg-slate-900 text-slate-200 border border-slate-800">
                            {item.episode_label}
                          </span>
                          {isFullEp ? (
                            <span className="px-2 py-0.5 rounded-md text-[10px] font-extrabold bg-amber-500/20 text-amber-300 border border-amber-500/40">
                              🎞️ TẬP FULL
                            </span>
                          ) : media.kind === 'image' ? (
                            <span className="px-2 py-0.5 rounded-md text-[10px] font-extrabold bg-pink-500/20 text-pink-300 border border-pink-500/40">
                              🖼️ FRAME
                            </span>
                          ) : (
                            <span className="px-2 py-0.5 rounded-md text-[10px] font-extrabold bg-indigo-500/20 text-indigo-300 border border-indigo-500/40">
                              🎬 Clip {item.clip_num ? String(item.clip_num).padStart(2, '0') : ''}
                            </span>
                          )}
                        </div>
                      </td>

                      {/* Col 5: Title & File Name */}
                      <td className="py-3 px-4 max-w-[340px]">
                        <div className="flex flex-col gap-0.5">
                          <span className="font-bold text-white truncate group-hover:text-indigo-200 transition-colors">
                            {item.title}
                          </span>
                          <code className="text-[11px] font-mono text-indigo-300 truncate">{item.file_name}</code>
                        </div>
                      </td>

                      {/* Col 6: Format & Cloud Storage Badge */}
                      <td className="py-3 px-4">
                        <div className="flex items-center gap-1.5 flex-wrap">
                          <span className="px-2 py-0.5 rounded-md text-[10px] font-mono font-bold bg-emerald-500/15 text-emerald-300 border border-emerald-500/30">
                            .{media.extLabel} • {media.mimeType}
                          </span>
                          <span
                            className={`px-2 py-0.5 rounded-md text-[10px] font-bold border ${
                              item.r2_url
                                ? 'bg-cyan-500/15 text-cyan-300 border-cyan-500/30'
                                : 'bg-slate-900 text-slate-400 border-slate-700'
                            }`}
                          >
                            {item.r2_url ? '☁️ R2' : '💾 Local'}
                          </span>
                        </div>
                      </td>

                      {/* Col 7: File Size */}
                      <td className="py-3 px-4 font-mono text-[11px] text-slate-300">
                        {item.size_mb ? `${item.size_mb} MB` : '—'}
                      </td>

                      {/* Col 8: Actions */}
                      <td className="py-3 px-5 text-right" onClick={e => e.stopPropagation()}>
                        <div className="inline-flex items-center gap-1.5">
                          <button
                            type="button"
                            onClick={() => setActiveModalIdx(globalIdx)}
                            className="px-2.5 py-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-[11px] font-bold flex items-center gap-1 transition-colors cursor-pointer shadow-sm"
                            title="Mở trình phát media"
                          >
                            <Play size={11} /> Phát
                          </button>

                          <button
                            type="button"
                            onClick={() => copyLink(media.url, item.id)}
                            className="px-2.5 py-1.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-[11px] font-semibold text-slate-200 flex items-center gap-1 transition-colors cursor-pointer"
                            title="Copy link .mp4 / media trực tiếp"
                          >
                            {copiedId === item.id ? (
                              <>
                                <Check size={11} className="text-emerald-400" />
                                <span className="text-emerald-300">Đã copy</span>
                              </>
                            ) : (
                              <>
                                <Copy size={11} />
                                <span>Copy Link</span>
                              </>
                            )}
                          </button>

                          <a
                            href={media.url}
                            target="_blank"
                            rel="noreferrer"
                            className="p-1.5 rounded-xl bg-cyan-500/15 hover:bg-cyan-500/25 border border-cyan-500/30 text-cyan-200 transition-colors"
                            title={`Mở trực tiếp file .${media.extLabel.toLowerCase()} (${media.mimeType})`}
                          >
                            <ExternalLink size={13} />
                          </a>
                        </div>
                      </td>
                    </tr>
                  )
                })}
              </tbody>
            </table>
          </div>

          {/* Bottom Table Pagination Footer */}
          <div className="px-5 py-3.5 bg-slate-950/90 border-t border-slate-800/90 flex flex-wrap items-center justify-between gap-3 text-xs">
            <div className="text-slate-400">
              Tổng cộng <strong className="text-white font-mono">{filteredItems.length}</strong> files (
              <span className="text-amber-300 font-semibold">{countsByCategory.full} Tập FULL</span> •{' '}
              <span className="text-emerald-300 font-semibold">{countsByCategory.clip} Clips</span>
              {countsByCategory.frame > 0 ? ` • ${countsByCategory.frame} Ảnh` : ''})
            </div>

            <div className="flex items-center gap-1">
              <button
                type="button"
                disabled={safePage <= 1}
                onClick={() => setCurrentPage(1)}
                className="px-2.5 py-1.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-300 disabled:opacity-35 cursor-pointer"
              >
                Đầu
              </button>
              <button
                type="button"
                disabled={safePage <= 1}
                onClick={() => setCurrentPage(p => Math.max(1, p - 1))}
                className="px-2.5 py-1.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-300 disabled:opacity-35 flex items-center gap-1 cursor-pointer"
              >
                <ChevronLeft size={13} /> Trước
              </button>
              {pageNumbers.map(pNum => (
                <button
                  key={pNum}
                  type="button"
                  onClick={() => setCurrentPage(pNum)}
                  className={`min-w-[32px] h-8 px-2.5 rounded-xl font-mono text-xs font-bold border transition-colors cursor-pointer ${
                    pNum === safePage
                      ? 'bg-indigo-600 text-white border-indigo-500 shadow-sm'
                      : 'bg-slate-900 hover:bg-slate-800 text-slate-300 border-slate-800'
                  }`}
                >
                  {pNum}
                </button>
              ))}
              <button
                type="button"
                disabled={safePage >= totalPages}
                onClick={() => setCurrentPage(p => Math.min(totalPages, p + 1))}
                className="px-2.5 py-1.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-300 disabled:opacity-35 flex items-center gap-1 cursor-pointer"
              >
                Sau <ChevronRight size={13} />
              </button>
              <button
                type="button"
                disabled={safePage >= totalPages}
                onClick={() => setCurrentPage(totalPages)}
                className="px-2.5 py-1.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-300 disabled:opacity-35 cursor-pointer"
              >
                Cuối
              </button>
            </div>
          </div>
        </div>
      )}

      {/* ═══════════════════════════════════════════════════════════════════
          4. ON-DEMAND MODAL PLAYER (CHỈ LOAD 1 VIDEO DUY NHẤT KHI BẤM XEM)
         ═══════════════════════════════════════════════════════════════════ */}
      {activeModalItem && activeModalIdx !== null && (
        <div
          className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/85 backdrop-blur-md"
          onClick={() => setActiveModalIdx(null)}
        >
          <div
            className="studio-card rounded-3xl max-w-4xl w-full p-5 border border-slate-700/80 flex flex-col gap-4 shadow-2xl"
            onClick={e => e.stopPropagation()}
          >
            {(() => {
              const modalMedia = resolveItemMediaInfo(activeModalItem)
              return (
                <>
                  {/* Modal Header */}
                  <div className="flex items-center justify-between gap-3 border-b border-slate-800 pb-3">
                    <div className="flex flex-col min-w-0">
                      <div className="flex items-center gap-2 flex-wrap">
                        <span className="px-2 py-0.5 rounded-md text-[10px] font-extrabold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
                          {activeModalItem.channel_name}
                        </span>
                        <span className="px-2 py-0.5 rounded-md text-[10px] font-mono font-bold bg-emerald-500/15 text-emerald-300 border border-emerald-500/30">
                          .{modalMedia.extLabel} • {modalMedia.mimeType}
                        </span>
                        <h3 className="text-sm font-extrabold text-white truncate">{activeModalItem.title}</h3>
                      </div>
                      <code className="text-[11px] font-mono text-slate-400 truncate mt-0.5">
                        {modalMedia.url}
                      </code>
                    </div>

                    <div className="flex items-center gap-2 shrink-0">
                      <button
                        type="button"
                        disabled={activeModalIdx <= 0}
                        onClick={() => setActiveModalIdx(i => (i !== null && i > 0 ? i - 1 : i))}
                        className="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-slate-200 disabled:opacity-40 cursor-pointer"
                        title="File trước"
                      >
                        <ChevronLeft size={15} />
                      </button>
                      <span className="text-xs font-mono text-slate-400">
                        {activeModalIdx + 1}/{filteredItems.length}
                      </span>
                      <button
                        type="button"
                        disabled={activeModalIdx >= filteredItems.length - 1}
                        onClick={() =>
                          setActiveModalIdx(i => (i !== null && i < filteredItems.length - 1 ? i + 1 : i))
                        }
                        className="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-slate-200 disabled:opacity-40 cursor-pointer"
                        title="File kế tiếp"
                      >
                        <ChevronRight size={15} />
                      </button>
                      <button
                        type="button"
                        onClick={() => setActiveModalIdx(null)}
                        className="p-2 rounded-xl bg-rose-500/15 hover:bg-rose-500/25 border border-rose-500/30 text-rose-200 cursor-pointer"
                      >
                        <X size={15} />
                      </button>
                    </div>
                  </div>

                  {/* Modal Media Viewport */}
                  <div className="rounded-2xl overflow-hidden bg-black border border-slate-800 flex items-center justify-center max-h-[70vh]">
                    {modalMedia.kind === 'video' ? (
                      <video
                        key={modalMedia.url}
                        controls
                        autoPlay
                        playsInline
                        className="w-full max-h-[68vh] object-contain bg-black"
                      >
                        <source src={modalMedia.url} type={modalMedia.mimeType} />
                      </video>
                    ) : modalMedia.kind === 'image' ? (
                      <img
                        src={modalMedia.url}
                        alt={activeModalItem.title}
                        className="w-full max-h-[68vh] object-contain bg-black"
                      />
                    ) : (
                      <div className="p-10 w-full flex flex-col items-center gap-4">
                        <Music size={42} className="text-cyan-400" />
                        <audio key={modalMedia.url} controls autoPlay className="w-full max-w-lg">
                          <source src={modalMedia.url} type={modalMedia.mimeType} />
                        </audio>
                      </div>
                    )}
                  </div>

                  {/* Modal Footer Actions */}
                  <div className="flex flex-wrap items-center justify-between gap-3 pt-1">
                    <div className="flex items-center gap-2 text-xs text-slate-400">
                      {activeModalItem.r2_url ? (
                        <span className="inline-flex items-center gap-1 text-cyan-300 font-semibold">
                          <Cloud size={13} /> Lưu trữ trên Cloudflare R2 ({activeModalItem.file_name})
                        </span>
                      ) : (
                        <span className="inline-flex items-center gap-1 text-slate-300">
                          <HardDrive size={13} /> Lưu trữ trên ổ đĩa cục bộ ({activeModalItem.file_name})
                        </span>
                      )}
                    </div>

                    <div className="flex items-center gap-2 flex-wrap">
                      <button
                        type="button"
                        onClick={() => copyLink(modalMedia.url, activeModalItem.id)}
                        className="px-3.5 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-xs font-semibold text-white flex items-center gap-1.5 cursor-pointer"
                      >
                        {copiedId === activeModalItem.id ? (
                          <>
                            <Check size={13} className="text-emerald-400" />
                            <span>Đã Copy Link .{modalMedia.extLabel}</span>
                          </>
                        ) : (
                          <>
                            <Copy size={13} />
                            <span>Copy Link .{modalMedia.extLabel}</span>
                          </>
                        )}
                      </button>

                      <a
                        href={modalMedia.url}
                        target="_blank"
                        rel="noreferrer"
                        className="px-3.5 py-2 rounded-xl bg-cyan-500/15 hover:bg-cyan-500/25 border border-cyan-500/40 text-xs font-bold text-cyan-200 flex items-center gap-1.5"
                      >
                        <ExternalLink size={13} />
                        Mở Trực Tiếp File .{modalMedia.extLabel}
                      </a>

                      <button
                        type="button"
                        onClick={() => {
                          setActiveModalIdx(null)
                          navigate(`/channels/${activeModalItem.channel_slug}`)
                        }}
                        className="px-3.5 py-2 rounded-xl studio-glow-btn text-xs font-bold flex items-center gap-1.5 cursor-pointer"
                      >
                        <Tv size={13} />
                        Mở Trong Studio Kênh
                      </button>
                    </div>
                  </div>
                </>
              )
            })()}
          </div>
        </div>
      )}
    </div>
  )
}
