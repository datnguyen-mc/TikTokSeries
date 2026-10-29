import { useState, useEffect, useCallback } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import {
  Play,
  Square,
  Film,
  Save,
  Plus,
  CheckCircle2,
  Clock,
  Sparkles,
  ExternalLink,
  Layers,
  Terminal,
  RefreshCw,
  Download,
  Lock,
  Settings2,
  Video,
  Search,
  Copy,
  Check,
  Wand2,
  ArrowRight,
  ArrowLeft,
  Tv,
  FileText,
  Activity,
  X,
  Eye,
} from 'lucide-react'
import { fetchAPI, patchAPI, resolveApiUrl } from '../api/client'
import { useWebSocketContext } from '../api/useWebSocketContext'

interface CharacterSpec {
  tag: string
  name: string
  default_media_id?: string
  locked_media_id?: string
  description?: string
}

interface ActiveJob {
  running: boolean
  pid?: number
  start_ep?: number
  end_ep?: number
  only_clip?: number | null
  started_at?: string
}

interface ChannelSummary {
  slug: string
  name: string
  project_id: string
  aspect_ratio: string
  runner_script: string
  series_dir: string
  ep_prefix: string
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
  active_job: ActiveJob | null
  latest_log: {
    level: string
    category: string
    message: string
    created_at: string
  } | null
}

interface ClipItem {
  clip_num: number
  file_name: string
  file_path: string
  prompt: string
  status: 'COMPLETED' | 'PENDING'
  video_url: string | null
  r2_url?: string | null
  r2_key?: string | null
  video_size_mb: number | null
  frame_url: string | null
  frame_r2_url?: string | null
}

interface EpisodeItem {
  episode_num: number
  folder_name: string
  label: string
  total_clips: number
  rendered_clips: number
  r2_synced_clips?: number
  is_complete: boolean
  merged_video_url: string | null
  merged_r2_url?: string | null
  merged_r2_key?: string | null
  merged_video_path: string | null
  merged_size_mb: number | null
  clips: ClipItem[]
}

interface CloudStatusResponse {
  ok: boolean
  config: {
    db_backend: string
    cf_account_id: string
    cf_api_token_set: boolean
    cf_d1_database_id: string
    r2_auto_upload: boolean
    r2_account_id: string
    r2_access_key_id: string
    r2_secret_key_set: boolean
    r2_bucket_name: string
    r2_public_url: string
    r2_endpoint_url: string
    r2_key_prefix: string
  }
  d1: {
    configured: boolean
    ok?: boolean
    database_id?: string
    table_count?: number
    message?: string
    error?: string
  }
  r2: {
    configured: boolean
    ok?: boolean
    bucket?: string
    public_url?: string
    message?: string
    error?: string
  }
  stats: {
    indexed_episodes: number
    r2_merged_episodes: number
    indexed_clips: number
    r2_clips: number
  }
}

interface ChannelDetailResponse {
  channel: {
    slug: string
    name: string
    project_id: string
    aspect_ratio: string
    runner_script: string
    series_dir: string
    ep_prefix: string
    description: string
    characters: CharacterSpec[]
    active_job: ActiveJob | null
  }
  episodes: EpisodeItem[]
}

interface CmsLogItem {
  id: number
  channel_slug: string
  project_id?: string
  episode?: number
  clip_num?: number
  level: string
  category: string
  message: string
  details?: Record<string, string>
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
}

export default function ChannelsCMSPage() {
  const { slug: routeSlug } = useParams<{ slug?: string }>()
  const navigate = useNavigate()
  const { lastEvent } = useWebSocketContext()

  const [channels, setChannels] = useState<ChannelSummary[]>([])
  const [loadingChannels, setLoadingChannels] = useState(true)
  const [channelSearch, setChannelSearch] = useState('')
  const [ratioFilter, setRatioFilter] = useState<'ALL' | 'PORTRAIT' | 'LANDSCAPE'>('ALL')

  // Detail state (only loaded when routeSlug is present)
  const [detail, setDetail] = useState<ChannelDetailResponse | null>(null)
  const [loadingDetail, setLoadingDetail] = useState(false)
  const [selectedEpNum, setSelectedEpNum] = useState<number | null>(null)
  const [epSearch, setEpSearch] = useState('')
  const [selectedClipNum, setSelectedClipNum] = useState<number>(1)
  const [promptDraft, setPromptDraft] = useState<string>('')
  const [savingPrompt, setSavingPrompt] = useState(false)
  const [mergingEp, setMergingEp] = useState(false)
  const [startingJob, setStartingJob] = useState(false)
  const [copiedId, setCopiedId] = useState<string | null>(null)
  const [statusBanner, setStatusBanner] = useState<{ type: 'success' | 'error' | 'info'; text: string } | null>(null)

  // Channel config edit state
  const [showConfigEdit, setShowConfigEdit] = useState(false)
  const [editProjectId, setEditProjectId] = useState('')
  const [editAspectRatio, setEditAspectRatio] = useState('VIDEO_ASPECT_RATIO_PORTRAIT')
  const [editCharacters, setEditCharacters] = useState<CharacterSpec[]>([])

  // New episode & prompt builder state
  const [showNewEpModal, setShowNewEpModal] = useState(false)
  const [newEpNum, setNewEpNum] = useState<number>(17)
  const [newEpClips, setNewEpClips] = useState<number>(5)
  const [newEpSuffix, setNewEpSuffix] = useState<string>('')
  const [newEpStoryIdea, setNewEpStoryIdea] = useState<string>('')
  const [newEpSetting, setNewEpSetting] = useState<string>('')
  const [newEpSceneBeats, setNewEpSceneBeats] = useState<string[]>(['', '', '', '', ''])
  const [generatedPrompts, setGeneratedPrompts] = useState<string[]>([])
  const [previewClipIdx, setPreviewClipIdx] = useState<number>(0)
  const [generatingPrompts, setGeneratingPrompts] = useState<boolean>(false)

  // Batch range run state
  const [rangeStart, setRangeStart] = useState<number>(16)
  const [rangeEnd, setRangeEnd] = useState<number>(16)

  // Live logs & console tabs
  const [logTab, setLogTab] = useState<'logs' | 'terminal'>('logs')
  const [channelLogs, setChannelLogs] = useState<CmsLogItem[]>([])
  const [terminalLines, setTerminalLines] = useState<string[]>([])

  // Cloudflare R2 Storage & D1 SQL state
  const [cloudStatus, setCloudStatus] = useState<CloudStatusResponse | null>(null)
  const [showCloudModal, setShowCloudModal] = useState(false)
  const [savingCloud, setSavingCloud] = useState(false)
  const [syncingD1, setSyncingD1] = useState(false)
  const [syncingR2, setSyncingR2] = useState(false)
  const [cloudFeedback, setCloudFeedback] = useState<{ ok: boolean; text: string } | null>(null)
  const [cfAccountId, setCfAccountId] = useState('')
  const [cfApiToken, setCfApiToken] = useState('')
  const [cfD1DbId, setCfD1DbId] = useState('')
  const [r2AutoUpload, setR2AutoUpload] = useState(true)
  const [r2AccessKeyId, setR2AccessKeyId] = useState('')
  const [r2SecretKey, setR2SecretKey] = useState('')
  const [r2BucketName, setR2BucketName] = useState('tiktok-series')
  const [r2PublicUrl, setR2PublicUrl] = useState('')
  const [r2EndpointUrl, setR2EndpointUrl] = useState('')

  const loadCloudStatus = useCallback(async (live = false) => {
    try {
      const res = await fetchAPI<CloudStatusResponse>(`/api/cms/cloud/status?live=${live}`)
      setCloudStatus(res)
      setCfAccountId(res.config.cf_account_id || '')
      setCfD1DbId(res.config.cf_d1_database_id || '')
      setR2AutoUpload(res.config.r2_auto_upload ?? true)
      setR2AccessKeyId(res.config.r2_access_key_id || '')
      setR2BucketName(res.config.r2_bucket_name || 'tiktok-series')
      setR2PublicUrl(res.config.r2_public_url || '')
      setR2EndpointUrl(res.config.r2_endpoint_url || '')
    } catch (e) {
      console.error('Failed to load cloud status:', e)
    }
  }, [])

  async function handleSaveCloudConfig() {
    setSavingCloud(true)
    setCloudFeedback(null)
    try {
      const res = await fetchAPI<{
        ok: boolean
        d1: { ok?: boolean; message?: string; error?: string }
        r2: { ok?: boolean; message?: string; error?: string }
      }>('/api/cms/cloud/config', {
        method: 'POST',
        body: JSON.stringify({
          db_backend: 'd1',
          cf_account_id: cfAccountId,
          cf_api_token: cfApiToken || undefined,
          cf_d1_database_id: cfD1DbId,
          r2_auto_upload: r2AutoUpload,
          r2_access_key_id: r2AccessKeyId,
          r2_secret_access_key: r2SecretKey || undefined,
          r2_bucket_name: r2BucketName,
          r2_public_url: r2PublicUrl,
          r2_endpoint_url: r2EndpointUrl,
        }),
      })
      await loadCloudStatus(true)
      const d1Text = res.d1?.ok ? 'D1 SQL: Đã kết nối' : res.d1?.error || 'D1 SQL: Chờ thông tin'
      const r2Text = res.r2?.ok ? 'R2 Storage: Đã kết nối' : res.r2?.error || 'R2 Storage: Chờ thông tin'
      setCloudFeedback({ ok: Boolean(res.d1?.ok || res.r2?.ok), text: `✅ Đã lưu cấu hình! (${d1Text} • ${r2Text})` })
    } catch (err) {
      setCloudFeedback({ ok: false, text: err instanceof Error ? err.message : 'Lỗi khi lưu cấu hình Cloud' })
    } finally {
      setSavingCloud(false)
    }
  }

  async function handleSyncD1() {
    setSyncingD1(true)
    setCloudFeedback(null)
    try {
      const res = await fetchAPI<{
        ok: boolean
        total_rows_synced?: number
        error?: string
        indexed_locally?: { episodes_indexed: number; clips_indexed: number }
      }>('/api/cms/cloud/sync-d1?direction=push', { method: 'POST' })
      await loadCloudStatus(false)
      if (res.ok) {
        setCloudFeedback({
          ok: true,
          text: `🎉 Đã đồng bộ ${res.total_rows_synced || 0} bản ghi từ tất cả bảng sang Cloudflare D1 SQL!`,
        })
      } else {
        setCloudFeedback({
          ok: false,
          text: res.error || 'Chưa thể đồng bộ lên Cloudflare D1 SQL.',
        })
      }
    } catch (err) {
      setCloudFeedback({ ok: false, text: err instanceof Error ? err.message : 'Lỗi đồng bộ D1 SQL' })
    } finally {
      setSyncingD1(false)
    }
  }

  async function handleSyncR2(channelSlug?: string, epNum?: number) {
    setSyncingR2(true)
    setCloudFeedback(null)
    try {
      const res = await fetchAPI<{
        ok: boolean
        uploaded_clips_count: number
        uploaded_episodes_count: number
        errors?: string[]
      }>('/api/cms/cloud/sync-r2', {
        method: 'POST',
        body: JSON.stringify({
          channel_slug: channelSlug || 'ALL',
          episode_num: epNum ?? null,
          force: false,
        }),
      })
      await loadCloudStatus(false)
      await loadChannels()
      if (routeSlug) await loadChannelDetail(routeSlug, selectedEpNum)
      const msg = `☁️ Đã upload lên Cloudflare R2: ${res.uploaded_clips_count} video clips & ${res.uploaded_episodes_count} tập FULL!`
      setCloudFeedback({ ok: true, text: msg })
      setStatusBanner({ type: 'success', text: msg })
    } catch (err) {
      const errMsg = err instanceof Error ? err.message : 'Lỗi upload video lên R2 Storage'
      setCloudFeedback({ ok: false, text: errMsg })
      setStatusBanner({ type: 'error', text: errMsg })
    } finally {
      setSyncingR2(false)
    }
  }

  const loadChannels = useCallback(async () => {
    try {
      const res = await fetchAPI<{ channels: ChannelSummary[] }>('/api/cms/channels')
      setChannels(res.channels)
    } catch (e) {
      console.error('Failed to load channels:', e)
    } finally {
      setLoadingChannels(false)
    }
  }, [])

  const resolveCurrentOrLastEpisodeNum = useCallback((res: ChannelDetailResponse): number | null => {
    if (!res.episodes || res.episodes.length === 0) return null
    const eps = res.episodes

    // 1. If a job is actively running on this channel, prioritize its active episode range
    if (res.channel.active_job?.running && res.channel.active_job.start_ep) {
      const startEp = res.channel.active_job.start_ep
      const endEp = res.channel.active_job.end_ep ?? startEp
      const runningInRange = eps.find(
        e => e.episode_num >= startEp && e.episode_num <= endEp && !e.is_complete && e.rendered_clips > 0,
      )
      if (runningInRange) return runningInRange.episode_num
      const firstIncompleteInRange = eps.find(
        e => e.episode_num >= startEp && e.episode_num <= endEp && !e.is_complete,
      )
      if (firstIncompleteInRange) return firstIncompleteInRange.episode_num
    }

    // 2. Episode currently being rendered (has some rendered clips but not yet complete)
    const inProgressEps = eps.filter(e => !e.is_complete && e.rendered_clips > 0)
    if (inProgressEps.length > 0) {
      return inProgressEps[inProgressEps.length - 1].episode_num
    }

    // 3. Immediate next episode after the highest completed episode
    let lastCompletedIdx = -1
    for (let i = eps.length - 1; i >= 0; i--) {
      if (eps[i].is_complete) {
        lastCompletedIdx = i
        break
      }
    }
    if (lastCompletedIdx >= 0) {
      if (lastCompletedIdx + 1 < eps.length) {
        return eps[lastCompletedIdx + 1].episode_num
      }
      return eps[eps.length - 1].episode_num
    }

    // 4. Fallback to the last episode in the series
    return eps[eps.length - 1].episode_num
  }, [])

  const resolveCurrentOrLastClipNum = useCallback((ep: EpisodeItem | null | undefined): number => {
    if (!ep || !ep.clips || ep.clips.length === 0) return 1
    // If episode has some clips done, activate the first pending clip (current clip)
    const firstPending = ep.clips.find(c => c.status !== 'COMPLETED')
    if (firstPending) return firstPending.clip_num
    // If all clips are completed, activate the last clip
    return ep.clips[ep.clips.length - 1].clip_num
  }, [])

  const loadChannelDetail = useCallback(async (slug: string, preserveEp?: number | null) => {
    setLoadingDetail(true)
    try {
      const res = await fetchAPI<ChannelDetailResponse>(`/api/cms/channels/${slug}`)
      setDetail(res)
      setEditProjectId(res.channel.project_id)
      setEditAspectRatio(res.channel.aspect_ratio)
      setEditCharacters(res.channel.characters.map(c => ({ ...c })))

      if (res.episodes.length > 0) {
        const defaultEp = resolveCurrentOrLastEpisodeNum(res) ?? res.episodes[res.episodes.length - 1].episode_num
        const targetEp =
          preserveEp && res.episodes.some(e => e.episode_num === preserveEp)
            ? preserveEp
            : defaultEp
        const targetEpObj = res.episodes.find(e => e.episode_num === targetEp) ?? null
        const maxEp = Math.max(...res.episodes.map(e => e.episode_num))

        setSelectedEpNum(targetEp)
        if (!preserveEp) {
          setSelectedClipNum(resolveCurrentOrLastClipNum(targetEpObj))
        }
        setRangeStart(targetEp)
        setRangeEnd(maxEp)
        setNewEpNum(maxEp + 1)
      } else {
        setSelectedEpNum(null)
        setNewEpNum(1)
      }
    } catch (e) {
      console.error('Failed to load channel detail:', e)
    } finally {
      setLoadingDetail(false)
    }
  }, [resolveCurrentOrLastEpisodeNum, resolveCurrentOrLastClipNum])

  const loadChannelLogs = useCallback(async (slug: string) => {
    try {
      const res = await fetchAPI<{ logs: CmsLogItem[] }>(`/api/cms/logs?channel_slug=${slug}&limit=60`)
      setChannelLogs(res.logs)
    } catch (e) {
      console.error('Failed to load channel logs:', e)
    }
  }, [])

  useEffect(() => {
    loadChannels()
    loadCloudStatus(false)
  }, [loadChannels, loadCloudStatus])

  useEffect(() => {
    if (routeSlug) {
      setTerminalLines([])
      setShowConfigEdit(false)
      setShowNewEpModal(false)
      loadChannelDetail(routeSlug, null)
      loadChannelLogs(routeSlug)
    } else {
      setDetail(null)
    }
  }, [routeSlug, loadChannelDetail, loadChannelLogs])

  const activeOrLastEpNum = detail ? resolveCurrentOrLastEpisodeNum(detail) : null
  const currentEpisode = detail?.episodes.find(e => e.episode_num === selectedEpNum) ?? null
  const currentClip = currentEpisode?.clips.find(c => c.clip_num === selectedClipNum) ?? null

  // Auto-scroll the Episode List sidebar to keep the active/selected episode visible
  useEffect(() => {
    if (!selectedEpNum || !detail) return
    const timer = setTimeout(() => {
      const el = document.getElementById(`cms-ep-card-${selectedEpNum}`)
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'nearest' })
      }
    }, 80)
    return () => clearTimeout(timer)
  }, [routeSlug, detail?.channel.slug, selectedEpNum])

  useEffect(() => {
    if (currentClip) {
      setPromptDraft(currentClip.prompt || '')
    } else {
      setPromptDraft('')
    }
  }, [routeSlug, selectedEpNum, selectedClipNum, currentClip?.prompt])

  // Real-time WebSocket updates
  useEffect(() => {
    if (!lastEvent) return
    const evType = lastEvent.type
    const evData = lastEvent.data as Record<string, unknown> | undefined

    if (evType === 'cms_log' && evData) {
      const logItem = evData as unknown as CmsLogItem
      if (routeSlug && logItem.channel_slug === routeSlug) {
        setChannelLogs(prev => [logItem, ...prev.filter(x => x.id !== logItem.id)].slice(0, 80))
      }
      if (logItem.category === 'MERGE') {
        loadChannels()
        if (routeSlug) loadChannelDetail(routeSlug, null)
      } else if (logItem.category === 'JOB' || logItem.level === 'SUCCESS') {
        loadChannels()
        if (routeSlug) loadChannelDetail(routeSlug, selectedEpNum)
      }
    } else if (evType === 'cms_terminal' && evData) {
      if (routeSlug && evData.channel_slug === routeSlug && typeof evData.line === 'string') {
        setTerminalLines(prev => [...prev.slice(-150), evData.line as string])
      }
    } else if (evType === 'cms_episode_merged' || evType === 'cms_episode_synced') {
      loadChannels()
      if (routeSlug) loadChannelDetail(routeSlug, selectedEpNum)
    } else if (evType === 'cms_clip_synced' || evType === 'cms_job_status') {
      loadChannels()
      if (routeSlug) loadChannelDetail(routeSlug, selectedEpNum)
    }
  }, [lastEvent, routeSlug, selectedEpNum, loadChannels, loadChannelDetail])

  async function handleSaveChannelConfig() {
    if (!detail || !routeSlug) return
    try {
      await patchAPI(`/api/cms/channels/${routeSlug}`, {
        project_id: editProjectId,
        aspect_ratio: editAspectRatio,
        characters: editCharacters,
      })
      setShowConfigEdit(false)
      setStatusBanner({
        type: 'success',
        text: `✅ Đã lưu cấu hình Project ID (${editProjectId.slice(0, 8)}...) & Khóa nhân vật cho kênh ${detail.channel.name}!`,
      })
      loadChannels()
      loadChannelDetail(routeSlug, selectedEpNum)
    } catch (err) {
      setStatusBanner({ type: 'error', text: err instanceof Error ? err.message : 'Lỗi khi lưu cấu hình kênh' })
    }
  }

  async function handleGeneratePromptsPreview() {
    if (!routeSlug) return
    setGeneratingPrompts(true)
    try {
      const res = await fetchAPI<{ ok: boolean; prompts: string[] }>(
        `/api/cms/channels/${routeSlug}/generate-prompts`,
        {
          method: 'POST',
          body: JSON.stringify({
            episode_num: newEpNum,
            clip_count: newEpClips,
            story_idea: newEpStoryIdea,
            setting: newEpSetting,
            scene_beats: newEpSceneBeats.slice(0, newEpClips),
          }),
        },
      )
      if (res.prompts && res.prompts.length > 0) {
        setGeneratedPrompts(res.prompts)
        setPreviewClipIdx(0)
        setStatusBanner({
          type: 'info',
          text: `✨ Đã sinh tự động ${res.prompts.length} kịch bản prompt chuẩn khóa nhân vật cho Tập ${newEpNum}! Bạn có thể xem/chỉnh sửa bên dưới rồi bấm Lưu.`,
        })
      }
    } catch (err) {
      setStatusBanner({
        type: 'error',
        text: err instanceof Error ? err.message : 'Lỗi khi sinh bộ prompt tự động',
      })
    } finally {
      setGeneratingPrompts(false)
    }
  }

  async function handleCreateEpisode() {
    if (!routeSlug) return
    try {
      const res = await fetchAPI<{ ok: boolean; episode_num: number; folder_name: string }>(
        `/api/cms/channels/${routeSlug}/episodes`,
        {
          method: 'POST',
          body: JSON.stringify({
            episode_num: newEpNum,
            clip_count: newEpClips,
            folder_suffix: newEpSuffix || null,
            story_idea: newEpStoryIdea,
            setting: newEpSetting,
            scene_beats: newEpSceneBeats.slice(0, newEpClips),
            clip_prompts: generatedPrompts.length > 0 ? generatedPrompts : null,
            overwrite: true,
          }),
        },
      )
      setShowNewEpModal(false)
      setGeneratedPrompts([])
      setStatusBanner({
        type: 'success',
        text: `✅ Đã tạo & lưu trọn bộ kịch bản Tập ${res.episode_num} (${res.folder_name}) với ${newEpClips} clips khóa sẵn nhân vật!`,
      })
      await loadChannels()
      await loadChannelDetail(routeSlug, res.episode_num)
      setSelectedClipNum(1)
    } catch (err) {
      setStatusBanner({ type: 'error', text: err instanceof Error ? err.message : 'Lỗi tạo tập mới' })
    }
  }

  async function handleSavePrompt() {
    if (!routeSlug || selectedEpNum === null) return
    setSavingPrompt(true)
    try {
      await fetchAPI(`/api/cms/channels/${routeSlug}/episodes/${selectedEpNum}/clips/${selectedClipNum}`, {
        method: 'PUT',
        body: JSON.stringify({ prompt: promptDraft }),
      })
      setStatusBanner({
        type: 'success',
        text: `💾 Đã lưu kịch bản Tập ${selectedEpNum} - Clip ${selectedClipNum} thành công!`,
      })
      await loadChannelDetail(routeSlug, selectedEpNum)
    } catch (err) {
      setStatusBanner({ type: 'error', text: err instanceof Error ? err.message : 'Lỗi lưu kịch bản' })
    } finally {
      setSavingPrompt(false)
    }
  }

  async function handleAddClipToEpisode() {
    if (!routeSlug || selectedEpNum === null || !currentEpisode || !detail) return
    const nextClipNum = currentEpisode.clips.length > 0 ? Math.max(...currentEpisode.clips.map(c => c.clip_num)) + 1 : 1
    const charTags = detail.channel.characters.map(c => c.tag).join(' ')
    const defaultPrompt =
      `Continue the scene seamlessly from the exact last frame of Clip ${nextClipNum - 1}.\n\n` +
      `[CHARACTER ANCHORS]\n` +
      detail.channel.characters.map(c => `- ${c.tag}: ${c.description || ''}`).join('\n') +
      `\n\n[SCENE — TẬP ${selectedEpNum} CLIP ${nextClipNum}]\n` +
      `Mô tả diễn biến của ${charTags}...\n`

    try {
      await fetchAPI(`/api/cms/channels/${routeSlug}/episodes/${selectedEpNum}/clips/${nextClipNum}`, {
        method: 'PUT',
        body: JSON.stringify({ prompt: defaultPrompt }),
      })
      await loadChannelDetail(routeSlug, selectedEpNum)
      setSelectedClipNum(nextClipNum)
      setStatusBanner({ type: 'success', text: `➕ Đã thêm Clip ${nextClipNum} vào Tập ${selectedEpNum}!` })
    } catch (err) {
      setStatusBanner({ type: 'error', text: err instanceof Error ? err.message : 'Lỗi thêm clip' })
    }
  }

  async function handleRunJob(startEp: number, endEp: number, onlyClip?: number) {
    if (!routeSlug) return
    setStartingJob(true)
    try {
      if (onlyClip && selectedEpNum === startEp && selectedClipNum === onlyClip && promptDraft.trim()) {
        await fetchAPI(`/api/cms/channels/${routeSlug}/episodes/${selectedEpNum}/clips/${selectedClipNum}`, {
          method: 'PUT',
          body: JSON.stringify({ prompt: promptDraft }),
        })
      }
      await fetchAPI(`/api/cms/channels/${routeSlug}/run`, {
        method: 'POST',
        body: JSON.stringify({ start_ep: startEp, end_ep: endEp, only_clip: onlyClip ?? null }),
      })
      setStatusBanner({
        type: 'info',
        text: onlyClip
          ? `🚀 Đang tạo & ghi đè riêng Tập ${startEp} • Clip ${String(onlyClip).padStart(2, '0')} (Chỉ ghi đè đúng file clip-${onlyClip} & tự động cập nhật tập ghép khi đủ clip)...`
          : `🚀 Đang chạy tự động Tập ${startEp}${endEp > startEp ? ` → Tập ${endEp}` : ''} — Tự động ghép các clip nhỏ thành 1 tập hoàn chỉnh ngay khi xong!`,
      })
      loadChannels()
      loadChannelDetail(routeSlug, selectedEpNum)
    } catch (err) {
      setStatusBanner({ type: 'error', text: err instanceof Error ? err.message : 'Không thể khởi chạy tiến trình' })
    } finally {
      setStartingJob(false)
    }
  }

  async function handleStopJob() {
    if (!routeSlug) return
    try {
      await fetchAPI(`/api/cms/channels/${routeSlug}/stop`, { method: 'POST' })
      setStatusBanner({ type: 'info', text: '🛑 Đã gửi lệnh dừng tiến trình tạo video.' })
      loadChannels()
      loadChannelDetail(routeSlug, selectedEpNum)
    } catch (err) {
      setStatusBanner({ type: 'error', text: err instanceof Error ? err.message : 'Lỗi khi dừng tiến trình' })
    }
  }

  async function handleMarkEpisodeStatus(epNum: number, status: 'COMPLETED' | 'PENDING', upTo = false) {
    if (!routeSlug) return
    try {
      const res = await fetchAPI<{ ok: boolean; message: string }>(
        `/api/cms/channels/${routeSlug}/episodes/${epNum}/mark-status`,
        {
          method: 'POST',
          body: JSON.stringify({ status, up_to: upTo }),
        }
      )
      setStatusBanner({
        type: status === 'COMPLETED' ? 'success' : 'info',
        text: res.message,
      })
      await loadChannels()
      await loadChannelDetail(routeSlug, epNum)
    } catch (err) {
      setStatusBanner({
        type: 'error',
        text: err instanceof Error ? err.message : 'Lỗi cập nhật trạng thái tập',
      })
    }
  }

  async function handleMergeEpisodeNow(epNum: number) {
    if (!routeSlug) return
    setMergingEp(true)
    try {
      const res = await fetchAPI<{
        ok: boolean
        merged_video_url: string
        clip_count: number
        size_mb: number
        duration_s: number
      }>(`/api/cms/channels/${routeSlug}/episodes/${epNum}/merge`, { method: 'POST' })
      setStatusBanner({
        type: 'success',
        text: `🎞️ Đã ghép thành công ${res.clip_count} clip nhỏ thành Tập ${epNum} hoàn chỉnh (${res.duration_s}s • ${res.size_mb} MB)!`,
      })
      await loadChannels()
      await loadChannelDetail(routeSlug, epNum)
    } catch (err) {
      setStatusBanner({
        type: 'error',
        text:
          err instanceof Error
            ? err.message
            : 'Chưa có đủ file clip .mp4 trong thư mục output_videos để ghép tập này!',
      })
    } finally {
      setMergingEp(false)
    }
  }

  function insertIntoPrompt(snippet: string) {
    setPromptDraft(prev => (prev ? `${prev.trimEnd()}\n${snippet}\n` : `${snippet}\n`))
  }

  function copyText(text: string) {
    navigator.clipboard.writeText(text)
    setCopiedId(text)
    setTimeout(() => setCopiedId(null), 1500)
  }

  const totalEpisodesAll = channels.reduce((acc, c) => acc + c.stats.total_episodes, 0)
  const totalClipsAll = channels.reduce((acc, c) => acc + c.stats.total_clips, 0)
  const totalRenderedAll = channels.reduce((acc, c) => acc + c.stats.rendered_clips, 0)
  const totalMergedAll = channels.reduce((acc, c) => acc + c.stats.merged_episodes, 0)
  const runningChannelsCount = channels.filter(c => c.active_job?.running).length
  const renderProgressPct = totalClipsAll > 0 ? Math.round((totalRenderedAll / totalClipsAll) * 100) : 0

  const filteredChannels = channels.filter(ch => {
    if (ratioFilter === 'PORTRAIT' && !ch.aspect_ratio.includes('PORTRAIT')) return false
    if (ratioFilter === 'LANDSCAPE' && !ch.aspect_ratio.includes('LANDSCAPE')) return false
    if (!channelSearch.trim()) return true
    const q = channelSearch.toLowerCase()
    return (
      ch.name.toLowerCase().includes(q) ||
      ch.slug.toLowerCase().includes(q) ||
      ch.characters.some(c => c.tag.toLowerCase().includes(q) || c.name.toLowerCase().includes(q))
    )
  })

  const filteredEpisodes = (detail?.episodes || []).filter(ep => {
    if (!epSearch.trim()) return true
    const q = epSearch.toLowerCase()
    return ep.label.toLowerCase().includes(q) || ep.folder_name.toLowerCase().includes(q) || String(ep.episode_num) === q
  })

  const activeChannelJob = detail?.channel.active_job

  // ═══════════════════════════════════════════════════════════════════════════
  // VIEW 1: MASTER LIST TABLE VIEW (When no channel is selected: `/`)
  // ═══════════════════════════════════════════════════════════════════════════
  if (!routeSlug) {
    return (
      <div className="flex flex-col gap-6 pb-12 max-w-[1600px] mx-auto">
        {/* Top Bento KPI Row */}
        <div className="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-4">
          <div className="studio-card rounded-2xl p-4 flex items-center justify-between">
            <div className="flex flex-col gap-1">
              <span className="text-[11px] font-semibold uppercase tracking-wider text-slate-400">
                Hệ Thống Kênh Series
              </span>
              <div className="flex items-baseline gap-2">
                <span className="text-2xl font-extrabold text-white">{channels.length}</span>
                <span className="text-xs text-slate-400">kênh hoạt hình 3D</span>
              </div>
              <span className="text-[11px] text-indigo-400 font-medium">
                {runningChannelsCount > 0 ? `⚡ ${runningChannelsCount} kênh đang render` : 'Sẵn sàng nhận lệnh sản xuất'}
              </span>
            </div>
            <div className="w-11 h-11 rounded-2xl bg-indigo-500/15 border border-indigo-500/30 flex items-center justify-center text-indigo-400">
              <Tv size={20} />
            </div>
          </div>

          <div className="studio-card rounded-2xl p-4 flex items-center justify-between">
            <div className="flex flex-col gap-1">
              <span className="text-[11px] font-semibold uppercase tracking-wider text-slate-400">
                Tổng Tập & Kịch Bản
              </span>
              <div className="flex items-baseline gap-2">
                <span className="text-2xl font-extrabold text-emerald-400">{totalMergedAll}</span>
                <span className="text-xs text-slate-400">/ {totalEpisodesAll} tập (folder)</span>
              </div>
              <span className="text-[11px] text-cyan-400 font-medium">
                Tổng cộng {totalClipsAll} phân cảnh (.txt)
              </span>
            </div>
            <div className="w-11 h-11 rounded-2xl bg-cyan-500/15 border border-cyan-500/30 flex items-center justify-center text-cyan-400">
              <FileText size={20} />
            </div>
          </div>

          <div className="studio-card rounded-2xl p-4 flex flex-col justify-between gap-2">
            <div className="flex items-center justify-between">
              <div className="flex flex-col gap-0.5">
                <span className="text-[11px] font-semibold uppercase tracking-wider text-slate-400">
                  Clips Nhỏ Đã Render
                </span>
                <div className="flex items-baseline gap-2">
                  <span className="text-2xl font-extrabold text-emerald-400">{totalRenderedAll}</span>
                  <span className="text-xs text-slate-400">/ {totalClipsAll} clips (.mp4)</span>
                </div>
              </div>
              <div className="w-11 h-11 rounded-2xl bg-emerald-500/15 border border-emerald-500/30 flex items-center justify-center text-emerald-400">
                <Video size={20} />
              </div>
            </div>
            <div className="w-full h-1.5 rounded-full bg-slate-800 overflow-hidden">
              <div
                className="h-full rounded-full bg-gradient-to-r from-emerald-500 to-teal-400 transition-all duration-500"
                style={{ width: `${renderProgressPct}%` }}
              />
            </div>
          </div>

          <div className="studio-card rounded-2xl p-4 flex items-center justify-between">
            <div className="flex flex-col gap-1">
              <span className="text-[11px] font-semibold uppercase tracking-wider text-slate-400">
                Tập Hoàn Chỉnh (FULL MP4)
              </span>
              <div className="flex items-baseline gap-2">
                <span className="text-2xl font-extrabold text-amber-400">{totalMergedAll}</span>
                <span className="text-xs text-slate-400">tập đã ghép nối</span>
              </div>
              <span className="text-[11px] text-amber-300/80 font-medium">
                Tự động ghép bằng FFmpeg khi xong tập
              </span>
            </div>
            <div className="w-11 h-11 rounded-2xl bg-amber-500/15 border border-amber-500/30 flex items-center justify-center text-amber-400">
              <Film size={20} />
            </div>
          </div>
        </div>

        {/* Channels List Table Card */}
        <div className="studio-card rounded-3xl overflow-hidden flex flex-col">
          {/* Table Header Toolbar */}
          <div className="p-5 border-b border-slate-800/80 flex flex-wrap items-center justify-between gap-3">
            <div className="flex items-center gap-3">
              <div className="p-2.5 rounded-xl bg-indigo-500/15 text-indigo-400 border border-indigo-500/30">
                <Layers size={16} />
              </div>
              <div>
                <h2 className="text-sm font-bold text-white">Bảng Quản Lý Kênh TikTok Series</h2>
                <p className="text-xs text-slate-400">
                  Bấm vào nút <strong className="text-indigo-300">"Chi Tiết & Sản Xuất"</strong> ở từng dòng để mở Studio
                  chỉnh kịch bản, khóa nhân vật và ghép tập
                </p>
              </div>
            </div>

            <div className="flex items-center gap-2.5 flex-wrap">
              <div className="flex items-center gap-2 px-3.5 py-2 rounded-xl bg-slate-950/90 border border-slate-800 text-xs">
                <Search size={13} className="text-slate-400" />
                <input
                  type="text"
                  value={channelSearch}
                  onChange={e => setChannelSearch(e.target.value)}
                  placeholder="Tìm kênh, slug hoặc @NhânVật..."
                  className="bg-transparent outline-none text-white placeholder:text-slate-500 w-52"
                />
              </div>

              <div className="flex items-center p-1 rounded-xl bg-slate-950/90 border border-slate-800 text-[11px]">
                {(['ALL', 'PORTRAIT', 'LANDSCAPE'] as const).map(mode => (
                  <button
                    key={mode}
                    onClick={() => setRatioFilter(mode)}
                    className={`px-3 py-1 rounded-lg font-semibold transition-colors cursor-pointer ${
                      ratioFilter === mode ? 'bg-indigo-600 text-white' : 'text-slate-400 hover:text-slate-200'
                    }`}
                  >
                    {mode === 'ALL' ? 'Tất cả' : mode === 'PORTRAIT' ? '9:16 Dọc' : '16:9 Ngang'}
                  </button>
                ))}
              </div>

              <button
                onClick={() => {
                  setShowCloudModal(v => !v)
                  loadCloudStatus(true)
                }}
                className="px-3.5 py-2 rounded-xl bg-cyan-500/15 hover:bg-cyan-500/25 border border-cyan-500/40 text-xs font-semibold text-cyan-200 flex items-center gap-1.5 transition-colors cursor-pointer"
              >
                <Sparkles size={13} className="text-cyan-400" />
                <span>
                  ☁️ Cloudflare R2 & D1 SQL
                  {cloudStatus?.d1?.configured || cloudStatus?.r2?.configured ? ' (Đã bật)' : ''}
                </span>
              </button>

              <button
                onClick={() => {
                  loadChannels()
                  loadCloudStatus(false)
                }}
                className="px-3.5 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-xs font-medium text-slate-200 flex items-center gap-1.5 transition-colors cursor-pointer"
              >
                <RefreshCw size={13} /> Làm mới
              </button>
            </div>
          </div>

          {/* Expandable Cloudflare R2 Storage & D1 SQL Configuration & One-Click Sync Panel */}
          {showCloudModal && (
            <div className="p-5 border-b border-slate-800/90 bg-slate-950/90 flex flex-col gap-4">
              <div className="flex flex-wrap items-center justify-between gap-3">
                <div>
                  <h3 className="text-sm font-bold text-cyan-300 flex items-center gap-2">
                    ☁️ Đồng Bộ Toàn Bộ Dữ Liệu: Cloudflare D1 SQL Database & R2 Video Storage
                  </h3>
                  <p className="text-xs text-slate-400 mt-0.5">
                    Tự động upload mọi video clip & tập FULL (.mp4) vừa tạo xong lên R2 Storage và lưu toàn bộ kịch bản,
                    nhân vật, trạng thái vào Cloudflare D1 SQL.
                  </p>
                </div>
                <div className="flex items-center gap-2 flex-wrap">
                  <button
                    disabled={syncingD1}
                    onClick={handleSyncD1}
                    className="px-3.5 py-2 rounded-xl bg-indigo-500/20 hover:bg-indigo-500/30 border border-indigo-500/40 text-xs font-bold text-indigo-200 flex items-center gap-1.5 cursor-pointer disabled:opacity-50"
                  >
                    <RefreshCw size={13} className={syncingD1 ? 'animate-spin' : ''} />
                    {syncingD1 ? 'Đang đồng bộ D1 SQL...' : '🗄️ Đồng Bộ Tất Cả Bảng Lên D1 SQL'}
                  </button>
                  <button
                    disabled={syncingR2}
                    onClick={() => handleSyncR2('ALL')}
                    className="px-3.5 py-2 rounded-xl bg-amber-500/20 hover:bg-amber-500/30 border border-amber-500/40 text-xs font-bold text-amber-200 flex items-center gap-1.5 cursor-pointer disabled:opacity-50"
                  >
                    <Download size={13} />
                    {syncingR2 ? 'Đang upload video lên R2...' : '☁️ Upload Tất Cả Video (.MP4) Lên R2'}
                  </button>
                </div>
              </div>

              {cloudFeedback && (
                <div
                  className={`px-3.5 py-2.5 rounded-xl border text-xs font-medium ${
                    cloudFeedback.ok
                      ? 'bg-emerald-500/15 border-emerald-500/40 text-emerald-200'
                      : 'bg-rose-500/15 border-rose-500/40 text-rose-200'
                  }`}
                >
                  {cloudFeedback.text}
                </div>
              )}

              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-3 text-xs">
                <div>
                  <label className="text-[11px] text-slate-400 font-semibold">Cloudflare Account ID</label>
                  <input
                    value={cfAccountId}
                    onChange={e => setCfAccountId(e.target.value)}
                    placeholder="VD: 8a9b0c1d2e3f..."
                    className="w-full mt-1 px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-white font-mono text-xs outline-none focus:border-cyan-500"
                  />
                </div>
                <div>
                  <label className="text-[11px] text-slate-400 font-semibold">Cloudflare D1 Database ID</label>
                  <input
                    value={cfD1DbId}
                    onChange={e => setCfD1DbId(e.target.value)}
                    placeholder="UUID của D1 Database..."
                    className="w-full mt-1 px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-white font-mono text-xs outline-none focus:border-cyan-500"
                  />
                </div>
                <div>
                  <label className="text-[11px] text-slate-400 font-semibold">
                    Cloudflare API Token {cloudStatus?.config.cf_api_token_set ? '(Đã lưu ✓)' : ''}
                  </label>
                  <input
                    type="password"
                    value={cfApiToken}
                    onChange={e => setCfApiToken(e.target.value)}
                    placeholder={
                      cloudStatus?.config.cf_api_token_set ? '•••••••• (Để trống nếu giữ nguyên)' : 'Nhập CF_API_TOKEN...'
                    }
                    className="w-full mt-1 px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-white font-mono text-xs outline-none focus:border-cyan-500"
                  />
                </div>
                <div>
                  <label className="text-[11px] text-slate-400 font-semibold">R2 Bucket Name</label>
                  <input
                    value={r2BucketName}
                    onChange={e => setR2BucketName(e.target.value)}
                    placeholder="tiktok-series"
                    className="w-full mt-1 px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-white font-mono text-xs outline-none focus:border-cyan-500"
                  />
                </div>
                <div>
                  <label className="text-[11px] text-slate-400 font-semibold">R2 S3 Access Key ID</label>
                  <input
                    value={r2AccessKeyId}
                    onChange={e => setR2AccessKeyId(e.target.value)}
                    placeholder="S3 Access Key ID..."
                    className="w-full mt-1 px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-white font-mono text-xs outline-none focus:border-cyan-500"
                  />
                </div>
                <div>
                  <label className="text-[11px] text-slate-400 font-semibold">
                    R2 S3 Secret Access Key {cloudStatus?.config.r2_secret_key_set ? '(Đã lưu ✓)' : ''}
                  </label>
                  <input
                    type="password"
                    value={r2SecretKey}
                    onChange={e => setR2SecretKey(e.target.value)}
                    placeholder={
                      cloudStatus?.config.r2_secret_key_set
                        ? '•••••••• (Để trống nếu giữ nguyên)'
                        : 'S3 Secret Access Key...'
                    }
                    className="w-full mt-1 px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-white font-mono text-xs outline-none focus:border-cyan-500"
                  />
                </div>
                <div>
                  <label className="text-[11px] text-slate-400 font-semibold">R2 Public Domain URL (CDN / r2.dev)</label>
                  <input
                    value={r2PublicUrl}
                    onChange={e => setR2PublicUrl(e.target.value)}
                    placeholder="https://pub-xxx.r2.dev"
                    className="w-full mt-1 px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-white font-mono text-xs outline-none focus:border-cyan-500"
                  />
                </div>
                <div>
                  <label className="text-[11px] text-slate-400 font-semibold">R2 S3 Endpoint URL (Tự động theo Account ID)</label>
                  <input
                    value={r2EndpointUrl}
                    onChange={e => setR2EndpointUrl(e.target.value)}
                    placeholder="https://<account_id>.r2.cloudflarestorage.com"
                    className="w-full mt-1 px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-white font-mono text-xs outline-none focus:border-cyan-500"
                  />
                </div>
              </div>

              <div className="flex flex-wrap items-center justify-between gap-3 pt-1">
                <div className="flex items-center gap-4 text-[11px] text-slate-400">
                  <label className="inline-flex items-center gap-2 cursor-pointer text-slate-200 font-medium">
                    <input
                      type="checkbox"
                      checked={r2AutoUpload}
                      onChange={e => setR2AutoUpload(e.target.checked)}
                    />
                    Tự động upload video clip & tập FULL lên R2 ngay khi render xong
                  </label>
                  {cloudStatus && (
                    <span>
                      Đã lập chỉ mục: <strong className="text-white">{cloudStatus.stats.indexed_episodes}</strong> tập &{' '}
                      <strong className="text-white">{cloudStatus.stats.indexed_clips}</strong> clips • Đã lên R2:{' '}
                      <strong className="text-cyan-300">{cloudStatus.stats.r2_clips}</strong> clips &{' '}
                      <strong className="text-amber-300">{cloudStatus.stats.r2_merged_episodes}</strong> tập FULL
                    </span>
                  )}
                </div>

                <button
                  disabled={savingCloud}
                  onClick={handleSaveCloudConfig}
                  className="px-4 py-2 rounded-xl text-xs font-bold studio-glow-btn cursor-pointer disabled:opacity-50"
                >
                  {savingCloud ? 'Đang lưu & kiểm tra kết nối...' : '💾 Lưu Cấu Hình R2 & D1 SQL Vào .env'}
                </button>
              </div>
            </div>
          )}

          {/* Data Table */}
          <div className="overflow-x-auto">
            <table className="w-full text-left border-collapse">
              <thead>
                <tr className="bg-slate-950/70 border-b border-slate-800/90 text-[11px] font-bold uppercase tracking-wider text-slate-400">
                  <th className="py-3.5 px-5">Kênh Series</th>
                  <th className="py-3.5 px-4">Khung Hình & Project ID</th>
                  <th className="py-3.5 px-4">Nhân Vật Khóa (@Character)</th>
                  <th className="py-3.5 px-4">Số Tập</th>
                  <th className="py-3.5 px-4 min-w-[170px]">Tiến Độ Render Clips</th>
                  <th className="py-3.5 px-4">Tập FULL MP4</th>
                  <th className="py-3.5 px-4">Trạng Thái & Log Mới Nhất</th>
                  <th className="py-3.5 px-5 text-right">Thao Tác</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-800/60 text-xs">
                {loadingChannels ? (
                  <tr>
                    <td colSpan={8} className="py-12 text-center text-slate-400">
                      Đang tải danh sách kênh...
                    </td>
                  </tr>
                ) : filteredChannels.length === 0 ? (
                  <tr>
                    <td colSpan={8} className="py-12 text-center text-slate-500">
                      Không tìm thấy kênh nào khớp từ khóa.
                    </td>
                  </tr>
                ) : (
                  filteredChannels.map(ch => {
                    const is916 = ch.aspect_ratio.includes('PORTRAIT')
                    const pct =
                      ch.stats.total_clips > 0 ? Math.round((ch.stats.rendered_clips / ch.stats.total_clips) * 100) : 0
                    const accent = CHANNEL_ACCENTS[ch.slug] || CHANNEL_ACCENTS['mit-va-du-1970']

                    return (
                      <tr
                        key={ch.slug}
                        onClick={() => navigate(`/channels/${ch.slug}`)}
                        className="group hover:bg-white/[0.03] transition-colors cursor-pointer"
                      >
                        {/* Col 1: Channel Name & Slug */}
                        <td className="py-4 px-5">
                          <div className="flex items-start gap-3">
                            <span className={`w-2.5 h-2.5 rounded-full mt-1.5 shrink-0 ${accent.dot}`} />
                            <div className="flex flex-col gap-0.5">
                              <span className="font-bold text-white text-sm group-hover:text-indigo-300 transition-colors">
                                {ch.name}
                              </span>
                              <div className="flex items-center gap-2 text-[11px] text-slate-400">
                                <code className="text-slate-300">{ch.slug}</code>
                                <span>•</span>
                                <span className="font-mono text-[10px] text-slate-500">{ch.runner_script}</span>
                              </div>
                            </div>
                          </div>
                        </td>

                        {/* Col 2: Aspect Ratio & Project ID */}
                        <td className="py-4 px-4" onClick={e => e.stopPropagation()}>
                          <div className="flex flex-col items-start gap-1.5">
                            <span
                              className={`px-2 py-0.5 rounded-md text-[10px] font-bold border ${
                                is916
                                  ? 'bg-indigo-500/15 text-indigo-300 border-indigo-500/30'
                                  : 'bg-cyan-500/15 text-cyan-300 border-cyan-500/30'
                              }`}
                            >
                              {is916 ? '9:16 DỌC (TikTok)' : '16:9 NGANG'}
                            </span>
                            <div className="flex items-center gap-1.5 text-[11px] text-slate-400 font-mono">
                              <span>{ch.project_id.slice(0, 8)}...</span>
                              <button
                                onClick={() => copyText(ch.project_id)}
                                className="p-1 rounded hover:bg-slate-800 text-slate-400 hover:text-white transition-colors cursor-pointer"
                                title="Copy Project ID"
                              >
                                {copiedId === ch.project_id ? (
                                  <Check size={11} className="text-emerald-400" />
                                ) : (
                                  <Copy size={11} />
                                )}
                              </button>
                              <a
                                href={`https://labs.google/fx/vi/tools/flow/project/${ch.project_id}`}
                                target="_blank"
                                rel="noreferrer"
                                className="p-1 rounded hover:bg-slate-800 text-indigo-400 hover:text-indigo-300 transition-colors"
                                title="Mở trên Google Flow"
                              >
                                <ExternalLink size={11} />
                              </a>
                            </div>
                          </div>
                        </td>

                        {/* Col 3: Locked Characters */}
                        <td className="py-4 px-4">
                          <div className="flex items-center gap-1.5 flex-wrap max-w-[230px]">
                            {ch.characters.map(c => (
                              <span
                                key={c.tag}
                                className={`inline-flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-md border font-semibold ${accent.badge}`}
                                title={`${c.name} — ID: ${c.locked_media_id || 'Tự động'}`}
                              >
                                <Lock size={9} />
                                {c.tag}
                              </span>
                            ))}
                          </div>
                        </td>

                        {/* Col 4: Episodes Count */}
                        <td className="py-4 px-4">
                          <div className="flex items-baseline gap-1">
                            <span className="text-sm font-extrabold text-emerald-400">
                              {ch.stats.completed_episodes ?? ch.stats.merged_episodes}
                            </span>
                            <span className="text-xs font-bold text-slate-500">/</span>
                            <span className="text-sm font-extrabold text-white">{ch.stats.total_episodes}</span>
                            <span className="text-[11px] text-slate-400">tập</span>
                          </div>
                        </td>

                        {/* Col 5: Clips Render Progress */}
                        <td className="py-4 px-4">
                          <div className="flex flex-col gap-1.5 w-40">
                            <div className="flex items-center justify-between text-[11px]">
                              <span className="text-slate-300 font-semibold">
                                {ch.stats.rendered_clips}/{ch.stats.total_clips}{' '}
                                <span className="text-slate-500 font-normal">clips</span>
                              </span>
                              <span className="font-mono text-[10px] text-emerald-400 font-bold">{pct}%</span>
                            </div>
                            <div className="w-full h-1.5 rounded-full bg-slate-800 overflow-hidden">
                              <div
                                className={`h-full rounded-full bg-gradient-to-r ${accent.bar} transition-all duration-500`}
                                style={{ width: `${pct}%` }}
                              />
                            </div>
                          </div>
                        </td>

                        {/* Col 6: Merged Full Episodes */}
                        <td className="py-4 px-4">
                          {ch.stats.merged_episodes > 0 ? (
                            <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-amber-500/15 text-amber-300 border border-amber-500/30 text-[11px] font-bold">
                              <Film size={12} />
                              {ch.stats.merged_episodes} tập FULL
                            </span>
                          ) : (
                            <span className="text-[11px] text-slate-500">Chưa ghép tập</span>
                          )}
                        </td>

                        {/* Col 7: Live Status & Latest Log */}
                        <td className="py-4 px-4 max-w-[260px]">
                          <div className="flex flex-col gap-1">
                            {ch.active_job?.running ? (
                              <span className="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 w-fit animate-pulse">
                                ● Đang Render Tập {ch.active_job.start_ep}
                              </span>
                            ) : (
                              <span className="inline-flex items-center gap-1.5 text-[11px] text-slate-400">
                                <span className="w-1.5 h-1.5 rounded-full bg-slate-500" />
                                Sẵn sàng
                              </span>
                            )}
                            {ch.latest_log && (
                              <div
                                className="text-[10px] text-slate-500 truncate font-mono"
                                title={ch.latest_log.message}
                              >
                                [{ch.latest_log.created_at.slice(11)}] {ch.latest_log.message}
                              </div>
                            )}
                          </div>
                        </td>

                        {/* Col 8: Action Button */}
                        <td className="py-4 px-5 text-right" onClick={e => e.stopPropagation()}>
                          <button
                            onClick={() => navigate(`/channels/${ch.slug}`)}
                            title={`Xem chi tiết ${ch.name}`}
                            aria-label={`Xem chi tiết ${ch.name}`}
                            className="inline-flex items-center justify-center w-9 h-9 rounded-xl studio-glow-btn cursor-pointer"
                          >
                            <Eye size={15} />
                          </button>
                        </td>
                      </tr>
                    )
                  })
                )}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    )
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // VIEW 2: CHANNEL DETAIL STUDIO (When user clicks into a channel: `/channels/:slug`)
  // ═══════════════════════════════════════════════════════════════════════════
  return (
    <div className="flex flex-col gap-5 pb-12 max-w-[1600px] mx-auto">
      {/* Top Back Navigation & Quick Channel Switcher Bar */}
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div className="flex items-center gap-3">
          <button
            onClick={() => navigate('/')}
            className="inline-flex items-center gap-2 px-3.5 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700/80 text-xs font-semibold text-white transition-colors cursor-pointer"
          >
            <ArrowLeft size={14} className="text-indigo-400" />
            Quay lại Danh sách Kênh
          </button>

          <div className="hidden sm:flex items-center gap-2 text-xs text-slate-400">
            <span>Studio Kênh Series</span>
            <span>/</span>
            <span className="font-bold text-white">{detail?.channel.name || routeSlug}</span>
          </div>
        </div>

        <div className="flex items-center gap-2.5">
          <span className="text-xs text-slate-400">Chuyển nhanh kênh:</span>
          <select
            value={routeSlug}
            onChange={e => navigate(`/channels/${e.target.value}`)}
            className="px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-700/80 text-xs font-semibold text-white outline-none cursor-pointer"
          >
            {channels.map(c => (
              <option key={c.slug} value={c.slug}>
                {c.name} ({c.slug})
              </option>
            ))}
          </select>

          <button
            disabled={syncingR2}
            onClick={() => handleSyncR2(routeSlug)}
            className="px-3 py-1.5 rounded-xl bg-cyan-500/15 hover:bg-cyan-500/25 border border-cyan-500/40 text-xs font-semibold text-cyan-200 flex items-center gap-1.5 transition-colors cursor-pointer disabled:opacity-50"
          >
            <Download size={12} />
            {syncingR2 ? 'Đang đồng bộ R2...' : '☁️ Đồng Bộ Video Kênh Lên R2'}
          </button>

          <button
            onClick={() => {
              loadChannels()
              loadChannelDetail(routeSlug, selectedEpNum)
              loadChannelLogs(routeSlug)
            }}
            className="px-3 py-1.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-xs font-medium text-slate-200 flex items-center gap-1.5 transition-colors cursor-pointer"
          >
            <RefreshCw size={12} /> Làm mới
          </button>
        </div>
      </div>

      {/* Status Notification Banner */}
      {statusBanner && (
        <div
          className={`flex items-center justify-between px-4 py-3 rounded-2xl border text-xs font-medium shadow-lg transition-all ${
            statusBanner.type === 'error'
              ? 'bg-rose-500/10 border-rose-500/40 text-rose-200'
              : statusBanner.type === 'success'
                ? 'bg-emerald-500/10 border-emerald-500/40 text-emerald-200'
                : 'bg-indigo-500/15 border-indigo-500/40 text-indigo-200'
          }`}
        >
          <span>{statusBanner.text}</span>
          <button
            onClick={() => setStatusBanner(null)}
            className="p-1 rounded-lg hover:bg-white/10 text-slate-300 transition-colors cursor-pointer"
          >
            <X size={14} />
          </button>
        </div>
      )}

      {loadingDetail && !detail ? (
        <div className="studio-card rounded-3xl p-12 text-center text-xs text-slate-400">
          Đang tải dữ liệu chi tiết của kênh <code className="text-indigo-300">{routeSlug}</code>...
        </div>
      ) : detail ? (
        <div className="flex flex-col gap-5">
          {/* Studio Header & Locked Characters Showcase */}
          <div className="studio-card rounded-3xl p-5 flex flex-col gap-4">
            <div className="flex flex-wrap items-start justify-between gap-4">
              <div className="flex flex-col gap-1">
                <div className="flex items-center gap-2.5 flex-wrap">
                  <span className="px-2.5 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
                    CHI TIẾT KÊNH
                  </span>
                  <h3 className="text-base md:text-lg font-extrabold text-white">{detail.channel.name}</h3>
                  <code className="text-[11px] px-2 py-0.5 rounded-lg bg-slate-900 border border-slate-800 text-slate-300">
                    {detail.channel.runner_script}
                  </code>
                </div>
                <p className="text-xs text-slate-400">{detail.channel.description}</p>
              </div>

              <div className="flex items-center gap-2 flex-wrap">
                <a
                  href={`https://labs.google/fx/vi/tools/flow/project/${detail.channel.project_id}`}
                  target="_blank"
                  rel="noreferrer"
                  className="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-xl text-xs font-medium bg-slate-900 hover:bg-slate-800 border border-slate-700/80 text-slate-200 transition-colors"
                >
                  <ExternalLink size={13} className="text-indigo-400" />
                  Mở Google Flow Project
                </a>
                <button
                  onClick={() => setShowConfigEdit(v => !v)}
                  className={`inline-flex items-center gap-1.5 px-3.5 py-2 rounded-xl text-xs font-medium border transition-colors cursor-pointer ${
                    showConfigEdit
                      ? 'bg-indigo-600/20 border-indigo-500 text-white'
                      : 'bg-slate-900 hover:bg-slate-800 border-slate-700/80 text-slate-200'
                  }`}
                >
                  <Settings2 size={13} />
                  Cấu Hình Kênh & Khóa ID
                </button>
                <button
                  onClick={() => setShowNewEpModal(v => !v)}
                  className="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-xl text-xs font-semibold studio-glow-btn cursor-pointer"
                >
                  <Wand2 size={14} />
                  Tạo Tập Mới & Soạn Prompt
                </button>
              </div>
            </div>

            {/* Locked Characters Grid */}
            <div className="p-4 rounded-2xl bg-slate-950/70 border border-slate-800/90 flex flex-col gap-3">
              <div className="flex flex-wrap items-center justify-between gap-2">
                <div className="flex items-center gap-2 text-xs font-bold text-slate-200">
                  <Lock size={14} className="text-amber-400" />
                  <span>Bộ Nhân Vật Cố Định Đã Khóa Cho Kênh Này (Ingredients R2V + Seamless I2V)</span>
                </div>
                <div className="flex items-center gap-2 text-[11px] text-slate-400">
                  <span>Google Flow Project ID:</span>
                  <code className="px-2 py-0.5 rounded bg-slate-900 border border-slate-800 text-indigo-300 font-mono">
                    {detail.channel.project_id}
                  </code>
                </div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
                {detail.channel.characters.map(c => (
                  <div
                    key={c.tag}
                    className="p-3.5 rounded-xl bg-slate-900/90 border border-slate-800/90 hover:border-slate-700 transition-all flex flex-col justify-between gap-2"
                  >
                    <div className="flex flex-col gap-1">
                      <div className="flex items-center justify-between gap-2">
                        <span className="text-xs font-extrabold text-amber-300">
                          {c.tag} — <span className="text-white">{c.name}</span>
                        </span>
                        <span className="px-2 py-0.5 rounded-full text-[9px] font-bold bg-emerald-500/15 text-emerald-300 border border-emerald-500/30">
                          ĐÃ KHÓA ID
                        </span>
                      </div>

                      {c.description && <p className="text-[11px] text-slate-400 line-clamp-2">{c.description}</p>}
                    </div>

                    <div className="pt-2 border-t border-slate-800/80 flex items-center justify-between gap-2">
                      <div className="text-[10px] font-mono text-slate-400 truncate">
                        ID: <span className="text-slate-200">{c.locked_media_id || 'Tự động tạo'}</span>
                      </div>
                      <div className="flex items-center gap-1 shrink-0">
                        {c.locked_media_id && (
                          <button
                            onClick={() => copyText(c.locked_media_id!)}
                            className="p-1 rounded-md bg-slate-800 hover:bg-slate-700 text-slate-300 transition-colors cursor-pointer"
                            title="Copy media_id"
                          >
                            {copiedId === c.locked_media_id ? (
                              <Check size={11} className="text-emerald-400" />
                            ) : (
                              <Copy size={11} />
                            )}
                          </button>
                        )}
                        <button
                          onClick={() => insertIntoPrompt(`${c.tag} (${c.description || c.name})`)}
                          className="px-2 py-0.5 rounded-md bg-indigo-500/15 hover:bg-indigo-500/25 text-indigo-300 border border-indigo-500/30 text-[10px] font-semibold transition-colors cursor-pointer"
                          title="Chèn nhân vật này vào kịch bản đang mở"
                        >
                          + Chèn {c.tag}
                        </button>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Channel Config & Character Lock Editor Drawer */}
            {showConfigEdit && (
              <div className="p-4 rounded-2xl bg-indigo-950/20 border border-indigo-500/40 flex flex-col gap-4">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold text-indigo-300 uppercase tracking-wider">
                    ⚙️ Chỉnh Sửa Cấu Hình Kênh & Khóa Mã Media ID Nhân Vật
                  </span>
                  <button
                    onClick={() => setShowConfigEdit(false)}
                    className="text-xs text-slate-400 hover:text-white cursor-pointer"
                  >
                    Đóng
                  </button>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                  <div className="flex flex-col gap-1">
                    <label className="text-[11px] font-medium text-slate-300">Google Flow Project ID (UUID)</label>
                    <input
                      type="text"
                      value={editProjectId}
                      onChange={e => setEditProjectId(e.target.value)}
                      className="px-3 py-2 rounded-xl text-xs bg-slate-950 border border-slate-800 text-white font-mono outline-none focus:border-indigo-500"
                    />
                  </div>
                  <div className="flex flex-col gap-1">
                    <label className="text-[11px] font-medium text-slate-300">Tỉ lệ khung hình (Aspect Ratio)</label>
                    <select
                      value={editAspectRatio}
                      onChange={e => setEditAspectRatio(e.target.value)}
                      className="px-3 py-2 rounded-xl text-xs bg-slate-950 border border-slate-800 text-white outline-none focus:border-indigo-500"
                    >
                      <option value="VIDEO_ASPECT_RATIO_PORTRAIT">9:16 Dọc (TikTok / Reels / Shorts)</option>
                      <option value="VIDEO_ASPECT_RATIO_LANDSCAPE">16:9 Ngang (YouTube / Điện ảnh)</option>
                    </select>
                  </div>
                </div>

                <div className="flex flex-col gap-2">
                  <span className="text-[11px] font-semibold text-slate-300">
                    Danh sách Nhân Vật Cố Định (Mã <code className="text-amber-300">locked_media_id</code> trên Google
                    Flow):
                  </span>
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-2.5">
                    {editCharacters.map((ch, idx) => (
                      <div
                        key={ch.tag}
                        className="p-3 rounded-xl bg-slate-950/90 border border-slate-800 flex flex-col gap-1.5"
                      >
                        <div className="text-xs font-bold text-amber-300">
                          {ch.tag} — {ch.name}
                        </div>
                        <input
                          type="text"
                          placeholder="locked_media_id (UUID)"
                          value={ch.locked_media_id || ''}
                          onChange={e => {
                            const next = [...editCharacters]
                            next[idx] = { ...next[idx], locked_media_id: e.target.value }
                            setEditCharacters(next)
                          }}
                          className="px-2.5 py-1.5 rounded-lg text-[11px] font-mono bg-slate-900 border border-slate-800 text-white outline-none focus:border-indigo-500"
                        />
                        <input
                          type="text"
                          placeholder="Mô tả ngoại hình cố định..."
                          value={ch.description || ''}
                          onChange={e => {
                            const next = [...editCharacters]
                            next[idx] = { ...next[idx], description: e.target.value }
                            setEditCharacters(next)
                          }}
                          className="px-2.5 py-1.5 rounded-lg text-[11px] bg-slate-900 border border-slate-800 text-slate-300 outline-none focus:border-indigo-500"
                        />
                      </div>
                    ))}
                  </div>
                </div>

                <div className="flex justify-end">
                  <button
                    onClick={handleSaveChannelConfig}
                    className="px-4 py-2 rounded-xl text-xs font-semibold studio-glow-btn flex items-center gap-1.5 cursor-pointer"
                  >
                    <Save size={13} /> Lưu Cấu Hình & Cập Nhật Runner Script
                  </button>
                </div>
              </div>
            )}

            {/* Create New Episode & Smart Prompt Builder Studio */}
            {showNewEpModal && (
              <div className="p-5 rounded-2xl bg-indigo-950/25 border border-indigo-500/40 flex flex-col gap-4">
                <div className="flex items-center justify-between border-b border-indigo-500/20 pb-3">
                  <div className="flex items-center gap-2">
                    <Wand2 size={16} className="text-indigo-400" />
                    <span className="text-xs font-extrabold text-indigo-200 uppercase tracking-wider">
                      ✨ Trình Tạo Tập Mới & Sinh Bộ Kịch Bản Prompt Tự Động ({detail.channel.name})
                    </span>
                  </div>
                  <button
                    onClick={() => setShowNewEpModal(false)}
                    className="text-xs text-slate-400 hover:text-white cursor-pointer"
                  >
                    Đóng
                  </button>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
                  <div className="flex flex-col gap-1">
                    <label className="text-[11px] font-semibold text-slate-300">Số Thứ Tự Tập Mới</label>
                    <input
                      type="number"
                      min={1}
                      value={newEpNum}
                      onChange={e => setNewEpNum(Number(e.target.value))}
                      className="px-3 py-2 rounded-xl text-xs bg-slate-950 border border-slate-800 text-white outline-none focus:border-indigo-500"
                    />
                  </div>
                  <div className="flex flex-col gap-1">
                    <label className="text-[11px] font-semibold text-slate-300">Số Lượng Clips (8-10s/clip)</label>
                    <input
                      type="number"
                      min={1}
                      max={15}
                      value={newEpClips}
                      onChange={e => {
                        const cnt = Math.max(1, Math.min(15, Number(e.target.value)))
                        setNewEpClips(cnt)
                        setNewEpSceneBeats(prev => {
                          const next = [...prev]
                          while (next.length < cnt) next.push('')
                          return next
                        })
                      }}
                      className="px-3 py-2 rounded-xl text-xs bg-slate-950 border border-slate-800 text-white outline-none focus:border-indigo-500"
                    />
                  </div>
                  <div className="flex flex-col gap-1">
                    <label className="text-[11px] font-semibold text-slate-300">
                      Tên Gợi Nhớ Thư Mục (Tùy chọn, VD: bat-ca-muong)
                    </label>
                    <input
                      type="text"
                      value={newEpSuffix}
                      onChange={e => setNewEpSuffix(e.target.value)}
                      placeholder="Để trống sẽ tạo chuẩn tap-17"
                      className="px-3 py-2 rounded-xl text-xs bg-slate-950 border border-slate-800 text-white outline-none focus:border-indigo-500"
                    />
                  </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                  <div className="flex flex-col gap-1">
                    <label className="text-[11px] font-semibold text-slate-300">
                      Ý Tưởng / Cốt Truyện Chính Của Tập {newEpNum}
                    </label>
                    <textarea
                      rows={2}
                      value={newEpStoryIdea}
                      onChange={e => setNewEpStoryIdea(e.target.value)}
                      placeholder="VD: Ba con @Mit, @Đú và chó con @Nở làm diều giấy ngoài sân nhà lá, gió thổi diều vướng lên ngọn dừa thấp khiến cả nhà tìm cách lấy xuống đầy hài hước..."
                      className="p-2.5 rounded-xl text-xs bg-slate-950 border border-slate-800 text-white outline-none focus:border-indigo-500 resize-none"
                    />
                  </div>
                  <div className="flex flex-col gap-1">
                    <label className="text-[11px] font-semibold text-slate-300">
                      Bối Cảnh (Setting — Để trống sẽ dùng bối cảnh mặc định của kênh)
                    </label>
                    <textarea
                      rows={2}
                      value={newEpSetting}
                      onChange={e => setNewEpSetting(e.target.value)}
                      placeholder="VD: Sân đất trước căn nhà lá miền Tây năm 1970, bên bờ kênh có xuồng ba lá và hàng dừa xanh trong nắng sớm..."
                      className="p-2.5 rounded-xl text-xs bg-slate-950 border border-slate-800 text-white outline-none focus:border-indigo-500 resize-none"
                    />
                  </div>
                </div>

                {/* Per-Clip Beat Inputs */}
                <div className="flex flex-col gap-2">
                  <span className="text-[11px] font-semibold text-slate-300">
                    Diễn biến từng phân cảnh (Tùy chọn nhập tóm tắt 1 dòng cho từng Clip — hệ thống sẽ tự động đóng gói
                    vào <code className="text-amber-300">[FORMAT]</code>,{' '}
                    <code className="text-amber-300">[CHARACTERS]</code>,{' '}
                    <code className="text-amber-300">[SHOT LIST]</code> & nối cảnh mượt):
                  </span>
                  <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-2">
                    {Array.from({ length: newEpClips }).map((_, i) => (
                      <div key={i} className="flex items-center gap-2 bg-slate-950/90 border border-slate-800 rounded-xl px-3 py-1.5">
                        <span className="text-[10px] font-bold text-indigo-300 shrink-0">Clip {i + 1}:</span>
                        <input
                          type="text"
                          value={newEpSceneBeats[i] || ''}
                          onChange={e => {
                            const next = [...newEpSceneBeats]
                            next[i] = e.target.value
                            setNewEpSceneBeats(next)
                          }}
                          placeholder={`Diễn biến cảnh ${i + 1}...`}
                          className="bg-transparent text-xs text-white outline-none w-full placeholder:text-slate-600"
                        />
                      </div>
                    ))}
                  </div>
                </div>

                <div className="flex flex-wrap items-center justify-between gap-3 pt-1">
                  <button
                    type="button"
                    disabled={generatingPrompts}
                    onClick={handleGeneratePromptsPreview}
                    className="px-4 py-2 rounded-xl text-xs font-semibold bg-indigo-500/20 hover:bg-indigo-500/30 text-indigo-200 border border-indigo-500/40 flex items-center gap-1.5 transition-colors cursor-pointer"
                  >
                    <Wand2 size={14} />
                    {generatingPrompts
                      ? 'Đang sinh kịch bản...'
                      : `✨ Sinh Tự Động Bộ Prompt Chuẩn Cho ${newEpClips} Clips (Xem Trước & Chỉnh Sửa)`}
                  </button>

                  <button
                    type="button"
                    onClick={handleCreateEpisode}
                    className="px-5 py-2 rounded-xl text-xs font-bold studio-glow-btn flex items-center gap-1.5 cursor-pointer"
                  >
                    <Save size={14} />
                    💾 Lưu Kịch Bản & Tạo Tập {newEpNum} Ngay
                  </button>
                </div>

                {/* Generated Prompts Preview & Editor Tabs */}
                {generatedPrompts.length > 0 && (
                  <div className="mt-2 p-4 rounded-2xl bg-slate-950/90 border border-slate-800 flex flex-col gap-3">
                    <div className="flex items-center justify-between flex-wrap gap-2">
                      <span className="text-xs font-bold text-emerald-400">
                        ✅ Xem Trước & Tinh Chỉnh Kịch Bản Tập {newEpNum} ({generatedPrompts.length} Clips đã khóa{' '}
                        {detail.channel.characters.map(c => c.tag).join(' ')}):
                      </span>
                      <div className="flex items-center gap-1.5 flex-wrap">
                        {generatedPrompts.map((_, idx) => (
                          <button
                            key={idx}
                            type="button"
                            onClick={() => setPreviewClipIdx(idx)}
                            className={`px-2.5 py-1 rounded-lg text-xs font-bold border cursor-pointer ${
                              previewClipIdx === idx
                                ? 'bg-indigo-600 text-white border-indigo-500'
                                : 'bg-slate-900 text-slate-400 border-slate-800 hover:text-white'
                            }`}
                          >
                            Clip {String(idx + 1).padStart(2, '0')}
                          </button>
                        ))}
                      </div>
                    </div>

                    <textarea
                      rows={11}
                      value={generatedPrompts[previewClipIdx] || ''}
                      onChange={e => {
                        const next = [...generatedPrompts]
                        next[previewClipIdx] = e.target.value
                        setGeneratedPrompts(next)
                      }}
                      className="w-full p-3 rounded-xl bg-slate-900/90 border border-slate-800 text-xs font-mono text-slate-100 leading-relaxed outline-none focus:border-indigo-500"
                    />
                  </div>
                )}
              </div>
            )}
          </div>

          {/* Main Studio Grid: Left (3 cols) = Episodes List & Batch Runner, Right (9 cols) = Storyboard + Editor + Console */}
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-5">
            {/* Left Column: Episode Navigator & Batch Runner */}
            <div className="lg:col-span-3 studio-card rounded-3xl p-4 flex flex-col gap-3.5 h-fit">
              <div className="flex items-center justify-between gap-2">
                <span className="text-xs font-bold uppercase tracking-wider text-white">
                  Danh Sách Tập ({detail.episodes.filter(e => e.is_complete).length}/{detail.episodes.length})
                </span>
                {activeOrLastEpNum !== null ? (
                  <button
                    type="button"
                    onClick={() => {
                      const targetObj = detail.episodes.find(e => e.episode_num === activeOrLastEpNum) ?? null
                      setSelectedEpNum(activeOrLastEpNum)
                      setSelectedClipNum(resolveCurrentOrLastClipNum(targetObj))
                    }}
                    className="text-[10px] px-2 py-0.5 rounded-lg font-semibold bg-indigo-500/20 hover:bg-indigo-500/30 text-indigo-300 border border-indigo-500/30 transition-colors cursor-pointer"
                    title="Chuyển nhanh tới tập hiện tại hoặc tập cuối"
                  >
                    ⚡ Tập hiện tại (#{activeOrLastEpNum})
                  </button>
                ) : (
                  <span className="text-[11px] text-slate-400">Chọn tập để sửa</span>
                )}
              </div>

              <div className="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-slate-950/90 border border-slate-800 text-xs">
                <Search size={12} className="text-slate-400" />
                <input
                  type="text"
                  value={epSearch}
                  onChange={e => setEpSearch(e.target.value)}
                  placeholder="Tìm số tập (VD: 16)..."
                  className="bg-transparent outline-none text-white placeholder:text-slate-500 w-full text-xs"
                />
              </div>

              <div className="flex flex-col gap-2 max-h-[460px] overflow-y-auto pr-1">
                {filteredEpisodes.map(ep => {
                  const isEpSelected = ep.episode_num === selectedEpNum
                  const isCurrentTarget = ep.episode_num === activeOrLastEpNum
                  const epPct = ep.total_clips > 0 ? Math.round((ep.rendered_clips / ep.total_clips) * 100) : 0
                  return (
                    <div
                      id={`cms-ep-card-${ep.episode_num}`}
                      key={ep.episode_num}
                      onClick={() => {
                        setSelectedEpNum(ep.episode_num)
                        setSelectedClipNum(resolveCurrentOrLastClipNum(ep))
                      }}
                      className={`p-3 rounded-2xl border cursor-pointer transition-all flex flex-col gap-2 ${
                        isEpSelected
                          ? 'bg-indigo-600/15 border-indigo-500/60 shadow-sm'
                          : isCurrentTarget
                            ? 'bg-indigo-950/40 border-indigo-500/30 hover:border-indigo-500/50'
                            : 'bg-slate-900/60 border-slate-800/80 hover:border-slate-700'
                      }`}
                    >
                      <div className="flex items-center justify-between gap-2">
                        <div className="flex items-center gap-1.5 flex-wrap">
                          <span className="text-xs font-bold text-white">{ep.label}</span>
                          <span className="text-[10px] text-slate-400 font-mono">({ep.folder_name})</span>
                          {isCurrentTarget && (
                            <span className="px-1.5 py-0.2 rounded text-[9px] font-bold bg-indigo-500/25 text-indigo-300 border border-indigo-400/40">
                              ⚡ HIỆN TẠI
                            </span>
                          )}
                        </div>

                        {ep.merged_video_url ? (
                          <span className="px-2 py-0.5 rounded-md text-[9px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">
                            🎞️ FULL MP4
                          </span>
                        ) : ep.is_complete ? (
                          <span className="px-2 py-0.5 rounded-md text-[9px] font-bold bg-emerald-500/15 text-emerald-300 border border-emerald-500/30">
                            ✓ Hoàn thành
                          </span>
                        ) : (
                          <span className="text-[10px] text-slate-400 font-mono">
                            {ep.rendered_clips}/{ep.total_clips}
                          </span>
                        )}
                      </div>

                      <div className="w-full h-1 rounded-full bg-slate-800 overflow-hidden">
                        <div
                          className={`h-full rounded-full transition-all ${
                            ep.merged_video_url
                              ? 'bg-amber-400'
                              : ep.is_complete
                                ? 'bg-emerald-400'
                                : 'bg-indigo-500'
                          }`}
                          style={{ width: `${epPct}%` }}
                        />
                      </div>
                    </div>
                  )
                })}
              </div>

              {/* Batch Multi-Episode Runner */}
              <div className="pt-3 border-t border-slate-800/80 flex flex-col gap-2.5">
                <span className="text-xs font-bold text-slate-200 flex items-center gap-1.5">
                  <Sparkles size={13} className="text-indigo-400" />
                  Chạy Liên Tiếp Nhiều Tập
                </span>
                <div className="grid grid-cols-2 gap-2">
                  <div>
                    <label className="text-[10px] text-slate-400">Từ Tập</label>
                    <input
                      type="number"
                      min={1}
                      value={rangeStart}
                      onChange={e => setRangeStart(Number(e.target.value))}
                      className="w-full mt-0.5 px-2.5 py-1.5 rounded-xl text-xs bg-slate-950 border border-slate-800 text-white outline-none focus:border-indigo-500"
                    />
                  </div>
                  <div>
                    <label className="text-[10px] text-slate-400">Đến Tập</label>
                    <input
                      type="number"
                      min={1}
                      value={rangeEnd}
                      onChange={e => setRangeEnd(Number(e.target.value))}
                      className="w-full mt-0.5 px-2.5 py-1.5 rounded-xl text-xs bg-slate-950 border border-slate-800 text-white outline-none focus:border-indigo-500"
                    />
                  </div>
                </div>
                {activeChannelJob?.running ? (
                  <button
                    onClick={handleStopJob}
                    className="w-full py-2 px-3 rounded-xl text-xs font-semibold bg-rose-500 hover:bg-rose-600 text-white flex items-center justify-center gap-1.5 transition-colors cursor-pointer"
                  >
                    <Square size={12} /> Dừng Tiến Trình Đang Chạy
                  </button>
                ) : (
                  <button
                    disabled={startingJob}
                    onClick={() => handleRunJob(rangeStart, rangeEnd)}
                    className="w-full py-2 px-3 rounded-xl text-xs font-semibold studio-glow-btn flex items-center justify-center gap-1.5 cursor-pointer disabled:opacity-50"
                  >
                    <Play size={12} /> Chạy Tự Động Tập {rangeStart} → {rangeEnd}
                  </button>
                )}
              </div>
            </div>

            {/* Right Column (9 cols): Storyboard Pipeline + Full Episode Player + Prompt Studio + Live Dock */}
            <div className="lg:col-span-9 flex flex-col gap-5">
              {currentEpisode ? (
                <>
                  {/* Episode Action Header & Storyboard Pipeline */}
                  <div className="studio-card rounded-3xl p-5 flex flex-col gap-4">
                    <div className="flex flex-wrap items-center justify-between gap-3">
                      <div>
                        <div className="flex items-center gap-2.5">
                          <span className="text-base font-extrabold text-white">
                            🎬 {currentEpisode.label} ({currentEpisode.folder_name})
                          </span>
                          <span
                            className={`text-[11px] px-2.5 py-0.5 rounded-full font-semibold border ${
                              currentEpisode.is_complete
                                ? 'bg-emerald-500/15 text-emerald-300 border-emerald-500/30'
                                : 'bg-slate-800 text-slate-300 border-slate-700'
                            }`}
                          >
                            {currentEpisode.rendered_clips}/{currentEpisode.total_clips} Clips đã có MP4
                          </span>
                        </div>
                        <p className="text-xs text-slate-400 mt-1">
                          Khi các clip nhỏ hoàn tất, hệ thống tự động ghép nối bằng FFmpeg thành tập hoàn chỉnh:{' '}
                          <code className="text-amber-300 font-mono">
                            {routeSlug}_tap-{String(currentEpisode.episode_num).padStart(2, '0')}_FULL.mp4
                          </code>
                        </p>
                      </div>

                      <div className="flex items-center gap-2.5 flex-wrap">
                        {activeChannelJob?.running ? (
                          <button
                            onClick={handleStopJob}
                            className="px-4 py-2 rounded-xl text-xs font-semibold bg-rose-500 hover:bg-rose-600 text-white flex items-center gap-1.5 cursor-pointer"
                          >
                            <Square size={13} /> Dừng Render (PID {activeChannelJob.pid})
                          </button>
                        ) : (
                          <button
                            disabled={startingJob}
                            onClick={() => handleRunJob(currentEpisode.episode_num, currentEpisode.episode_num)}
                            className="px-4 py-2 rounded-xl text-xs font-semibold studio-glow-btn flex items-center gap-1.5 cursor-pointer disabled:opacity-50"
                          >
                            <Play size={13} /> Tạo Video Cả {currentEpisode.label} & Tự Ghép FULL
                          </button>
                        )}

                        <button
                          disabled={mergingEp || currentEpisode.rendered_clips === 0}
                          onClick={() => handleMergeEpisodeNow(currentEpisode.episode_num)}
                          className="px-4 py-2 rounded-xl text-xs font-semibold bg-amber-500/15 hover:bg-amber-500/25 text-amber-300 border border-amber-500/40 flex items-center gap-1.5 transition-colors cursor-pointer disabled:opacity-40"
                        >
                          <Film size={13} />
                          {mergingEp
                            ? 'Đang ghép tập...'
                            : `Ghép ${currentEpisode.rendered_clips} Clip Nhỏ Thành Tập FULL`}
                        </button>

                        {currentEpisode.is_complete ? (
                          <button
                            onClick={() => handleMarkEpisodeStatus(currentEpisode.episode_num, 'PENDING', false)}
                            className="px-3.5 py-2 rounded-xl text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 flex items-center gap-1.5 transition-colors cursor-pointer"
                            title="Đặt lại tập này về Chờ Render trên mọi máy local (D1 SQL)"
                          >
                            <RefreshCw size={12} /> Đặt Lại Chưa Xong
                          </button>
                        ) : (
                          <button
                            onClick={() => handleMarkEpisodeStatus(currentEpisode.episode_num, 'COMPLETED', false)}
                            className="px-3.5 py-2 rounded-xl text-xs font-semibold bg-emerald-500/15 hover:bg-emerald-500/25 text-emerald-300 border border-emerald-500/40 flex items-center gap-1.5 transition-colors cursor-pointer"
                            title="Đánh dấu hoàn thành tập này để đồng bộ trạng thái giữa nhiều máy local (D1 SQL)"
                          >
                            <CheckCircle2 size={13} /> Đánh Dấu Đã Xong {currentEpisode.label}
                          </button>
                        )}
                      </div>
                    </div>

                    {/* Visual Storyboard Pipeline Bar */}
                    <div className="p-3.5 rounded-2xl bg-slate-950/70 border border-slate-800/80 flex items-center gap-2 overflow-x-auto">
                      {currentEpisode.clips.map((clip, idx) => {
                        const isActive = clip.clip_num === selectedClipNum
                        const isDone = clip.status === 'COMPLETED'
                        return (
                          <div key={clip.clip_num} className="flex items-center gap-2 shrink-0">
                            <button
                              onClick={() => setSelectedClipNum(clip.clip_num)}
                              className={`px-3 py-2 rounded-xl border text-left transition-all flex items-center gap-2.5 cursor-pointer ${
                                isActive
                                  ? 'bg-indigo-600/25 border-indigo-500 text-white shadow-md'
                                  : isDone
                                    ? 'bg-emerald-500/10 border-emerald-500/30 text-emerald-200 hover:border-emerald-500/50'
                                    : 'bg-slate-900/90 border-slate-800 text-slate-400 hover:text-slate-200'
                              }`}
                            >
                              {isDone ? (
                                <CheckCircle2 size={15} className="text-emerald-400 shrink-0" />
                              ) : (
                                <Clock size={15} className="text-slate-500 shrink-0" />
                              )}
                              <div>
                                <div className="text-xs font-bold">Clip {String(clip.clip_num).padStart(2, '0')}</div>
                                <div className="text-[10px] opacity-75">
                                  {isDone ? (clip.video_size_mb ? `${clip.video_size_mb} MB` : 'Đã hoàn thành') : 'Chờ render'}
                                </div>
                              </div>
                            </button>
                            {idx < currentEpisode.clips.length - 1 && (
                              <ArrowRight size={13} className="text-slate-600 shrink-0" />
                            )}
                          </div>
                        )
                      })}

                      <ArrowRight size={14} className="text-amber-500/60 shrink-0 mx-1" />

                      {/* Final Merged Node in Storyboard */}
                      <div
                        className={`px-3.5 py-2 rounded-xl border shrink-0 flex items-center gap-2 ${
                          currentEpisode.merged_video_url
                            ? 'bg-amber-500/15 border-amber-500/50 text-amber-200'
                            : 'bg-slate-900/50 border-slate-800 text-slate-500'
                        }`}
                      >
                        <Film size={15} className={currentEpisode.merged_video_url ? 'text-amber-400' : ''} />
                        <div>
                          <div className="text-xs font-bold">TẬP FULL MP4</div>
                          <div className="text-[10px]">
                            {currentEpisode.merged_video_url
                              ? `${currentEpisode.merged_size_mb} MB (Sẵn sàng)`
                              : 'Tự ghép khi xong'}
                          </div>
                        </div>
                      </div>
                    </div>

                    {/* Full Episode Merged Cinema Player */}
                    {currentEpisode.merged_video_url && (
                      <div
                        className="p-4 rounded-2xl border border-amber-500/40 flex flex-col md:flex-row gap-5 items-center"
                        style={{
                          background:
                            'linear-gradient(135deg, rgba(245, 158, 11, 0.12) 0%, rgba(15, 23, 42, 0.95) 100%)',
                        }}
                      >
                        <video
                          key={currentEpisode.merged_video_url}
                          src={resolveApiUrl(currentEpisode.merged_video_url)}
                          controls
                          className="rounded-xl border border-amber-500/30 bg-black max-h-60 w-auto shadow-xl"
                        />
                        <div className="flex flex-col gap-2.5 flex-1">
                          <div className="inline-flex items-center gap-2 text-xs font-extrabold uppercase tracking-wider text-amber-300">
                            <Sparkles size={15} />
                            <span>Tập Phim Hoàn Chỉnh Đã Ghép Tự Động (FULL EPISODE)</span>
                          </div>
                          <div className="text-xs text-slate-200">
                            Tên file xuất bản:{' '}
                            <code className="px-2 py-0.5 rounded-md bg-black/40 border border-white/10 text-amber-300 font-mono">
                              {routeSlug}_tap-{String(currentEpisode.episode_num).padStart(2, '0')}_FULL.mp4
                            </code>
                          </div>
                          <div className="text-xs text-slate-400">
                            Dung lượng: <strong className="text-white">{currentEpisode.merged_size_mb} MB</strong> • Đã
                            nối liền mạch từ{' '}
                            <strong className="text-white">{currentEpisode.rendered_clips} clips nhỏ</strong>
                          </div>
                          <div className="pt-1 flex items-center gap-2.5 flex-wrap">
                            <a
                              href={resolveApiUrl(currentEpisode.merged_video_url)}
                              download
                              className="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl text-xs font-bold bg-amber-400 hover:bg-amber-300 text-slate-950 transition-colors shadow-lg"
                            >
                              <Download size={14} /> Tải Tập Hoàn Chỉnh (.MP4) Về Máy
                            </a>
                            {currentEpisode.merged_r2_url && (
                              <a
                                href={currentEpisode.merged_r2_url}
                                target="_blank"
                                rel="noreferrer"
                                className="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-xl text-xs font-bold bg-cyan-500/20 hover:bg-cyan-500/30 border border-cyan-500/40 text-cyan-200 transition-colors"
                              >
                                <ExternalLink size={13} /> ☁️ Mở Link R2 Storage
                              </a>
                            )}
                          </div>
                        </div>
                      </div>
                    )}
                  </div>

                  {/* Clip Prompt Editor & Media Preview Studio */}
                  {currentClip && (
                    <div className="studio-card rounded-3xl p-5 flex flex-col gap-4">
                      <div className="flex flex-wrap items-center justify-between gap-2 pb-3 border-b border-slate-800/80">
                        <div className="flex items-center gap-2">
                          <span className="px-2.5 py-1 rounded-lg bg-indigo-500/20 text-indigo-300 font-bold text-xs border border-indigo-500/30">
                            Clip {String(currentClip.clip_num).padStart(2, '0')}
                          </span>
                          <span className="text-sm font-bold text-white">
                            Kịch Bản Phân Cảnh ({currentClip.file_name})
                          </span>
                        </div>

                        <div className="flex items-center gap-1.5 flex-wrap">
                          <span className="text-[11px] text-slate-400 mr-1 flex items-center gap-1">
                            <Wand2 size={12} className="text-indigo-400" /> Chèn nhanh:
                          </span>
                          {detail.channel.characters.map(c => (
                            <button
                              key={c.tag}
                              onClick={() => insertIntoPrompt(c.tag)}
                              className="px-2 py-1 rounded-lg text-[11px] font-semibold bg-slate-900 hover:bg-slate-800 text-amber-300 border border-slate-700 transition-colors cursor-pointer"
                            >
                              + {c.tag}
                            </button>
                          ))}
                          <button
                            onClick={handleAddClipToEpisode}
                            className="px-2.5 py-1 rounded-lg text-[11px] font-semibold bg-indigo-500/15 hover:bg-indigo-500/25 text-indigo-300 border border-indigo-500/30 flex items-center gap-1 transition-colors cursor-pointer ml-2"
                          >
                            <Plus size={12} /> Thêm Clip Tiếp Theo
                          </button>
                        </div>
                      </div>

                      <div className="grid grid-cols-1 lg:grid-cols-12 gap-5">
                        {/* Left 7 cols: Prompt Editor */}
                        <div className="lg:col-span-7 flex flex-col gap-3">
                          <textarea
                            value={promptDraft}
                            onChange={e => setPromptDraft(e.target.value)}
                            onKeyDown={e => {
                              if ((e.metaKey || e.ctrlKey) && e.key === 's') {
                                e.preventDefault()
                                handleSavePrompt()
                              }
                            }}
                            rows={15}
                            className="w-full p-4 rounded-2xl bg-slate-950/90 border border-slate-800 focus:border-indigo-500 text-xs font-mono text-slate-100 leading-relaxed outline-none resize-y shadow-inner"
                            placeholder="Nhập kịch bản prompt cho phân cảnh này..."
                          />

                          <div className="flex items-center justify-between gap-2 flex-wrap">
                            <div className="flex items-center gap-2">
                              <button
                                disabled={savingPrompt}
                                onClick={handleSavePrompt}
                                className="px-4 py-2 rounded-xl text-xs font-semibold bg-slate-900 hover:bg-slate-800 border border-slate-700 text-white flex items-center gap-1.5 transition-colors cursor-pointer"
                              >
                                <Save size={13} className="text-indigo-400" />
                                {savingPrompt ? 'Đang lưu...' : 'Lưu Kịch Bản (Ctrl+S)'}
                              </button>
                              <span className="text-[11px] text-slate-500 font-mono">{promptDraft.length} ký tự</span>
                            </div>

                            <button
                              disabled={startingJob || Boolean(activeChannelJob?.running)}
                              onClick={() =>
                                handleRunJob(
                                  currentEpisode.episode_num,
                                  currentEpisode.episode_num,
                                  currentClip.clip_num,
                                )
                              }
                              className="px-4 py-2 rounded-xl text-xs font-semibold studio-glow-btn flex items-center gap-1.5 cursor-pointer disabled:opacity-50"
                              title="Chỉ tạo và ghi đè đúng duy nhất clip này, giữ nguyên các clip khác trong tập"
                            >
                              {currentClip.video_url || currentClip.status === 'COMPLETED' ? (
                                <>
                                  <RefreshCw size={13} /> Tạo Lại & Ghi Đè Clip{' '}
                                  {String(currentClip.clip_num).padStart(2, '0')} Này
                                </>
                              ) : (
                                <>
                                  <Play size={13} /> Tạo Video Riêng Clip{' '}
                                  {String(currentClip.clip_num).padStart(2, '0')} Này
                                </>
                              )}
                            </button>
                          </div>
                        </div>

                        {/* Right 5 cols: Clip Video Player & Last Frame Preview */}
                        <div className="lg:col-span-5 flex flex-col gap-3.5">
                          <div className="text-xs font-bold text-slate-200 flex items-center justify-between">
                            <span className="flex items-center gap-1.5">
                              <Video size={14} className="text-indigo-400" />
                              Xem Trước Clip {String(currentClip.clip_num).padStart(2, '0')}
                            </span>
                            {currentClip.video_size_mb && (
                              <span className="text-[11px] font-mono text-emerald-400">
                                {currentClip.video_size_mb} MB
                              </span>
                            )}
                          </div>

                          {currentClip.video_url ? (
                            <div className="p-3 rounded-2xl bg-slate-950/90 border border-slate-800 flex flex-col gap-2.5">
                              <video
                                key={currentClip.video_url}
                                src={resolveApiUrl(currentClip.video_url)}
                                controls
                                className="w-full max-h-64 rounded-xl bg-black"
                              />
                              <div className="flex items-center justify-between gap-2 flex-wrap text-[11px] text-slate-400 px-1">
                                <span>Đã kết xuất thành công</span>
                                <div className="flex items-center gap-3">
                                  <button
                                    disabled={startingJob || Boolean(activeChannelJob?.running)}
                                    onClick={() =>
                                      handleRunJob(
                                        currentEpisode.episode_num,
                                        currentEpisode.episode_num,
                                        currentClip.clip_num,
                                      )
                                    }
                                    className="text-amber-400 hover:text-amber-300 font-semibold flex items-center gap-1 cursor-pointer disabled:opacity-50"
                                    title="Tạo lại và ghi đè trực tiếp lên đúng file clip này"
                                  >
                                    <RefreshCw size={12} /> Tạo lại & ghi đè clip này
                                  </button>
                                  <a
                                    href={resolveApiUrl(currentClip.video_url)}
                                    download
                                    className="text-indigo-400 hover:text-indigo-300 font-semibold flex items-center gap-1"
                                  >
                                    <Download size={12} /> Tải clip lẻ (.mp4)
                                  </a>
                                </div>
                              </div>
                            </div>
                          ) : (
                            <div className="p-8 rounded-2xl bg-slate-950/60 border border-dashed border-slate-800 text-center flex flex-col items-center justify-center gap-2.5 h-56">
                              <div className="w-10 h-10 rounded-2xl bg-slate-900 border border-slate-800 flex items-center justify-center text-slate-500">
                                <Video size={20} />
                              </div>
                              <div className="text-xs font-semibold text-slate-300">
                                Clip {String(currentClip.clip_num).padStart(2, '0')} chưa có video .mp4
                              </div>
                              <p className="text-[11px] text-slate-500 max-w-xs">
                                Nhấn <strong>"Tạo Video Riêng Clip Này"</strong> hoặc{' '}
                                <strong>"Tạo Video Cả Tập"</strong> để bắt đầu kết xuất.
                              </p>
                            </div>
                          )}
                        </div>
                      </div>
                    </div>
                  )}
                </>
              ) : null}

              {/* Real-Time Channel Logs & Console Dock */}
              <div className="studio-card rounded-3xl p-5 flex flex-col gap-3.5">
                <div className="flex flex-wrap items-center justify-between gap-2">
                  <div className="flex items-center gap-2">
                    <button
                      onClick={() => setLogTab('logs')}
                      className={`px-3 py-1.5 rounded-xl text-xs font-bold flex items-center gap-1.5 transition-colors cursor-pointer ${
                        logTab === 'logs'
                          ? 'bg-indigo-600 text-white'
                          : 'bg-slate-900 text-slate-400 hover:text-slate-200'
                      }`}
                    >
                      <Activity size={13} />
                      Nhật Ký Kênh ({channelLogs.length})
                    </button>
                    <button
                      onClick={() => setLogTab('terminal')}
                      className={`px-3 py-1.5 rounded-xl text-xs font-bold flex items-center gap-1.5 transition-colors cursor-pointer ${
                        logTab === 'terminal'
                          ? 'bg-indigo-600 text-white'
                          : 'bg-slate-900 text-slate-400 hover:text-slate-200'
                      }`}
                    >
                      <Terminal size={13} />
                      Console Output ({terminalLines.length})
                    </button>
                  </div>

                  <span className="text-[11px] text-slate-400 font-mono">
                    Lưu trữ tự động trong SQLite (cms_log)
                  </span>
                </div>

                {logTab === 'terminal' ? (
                  <div className="p-4 rounded-2xl bg-[#05070b] border border-slate-800 font-mono text-[11px] max-h-64 overflow-y-auto flex flex-col gap-1 text-slate-300">
                    {terminalLines.length === 0 ? (
                      <div className="text-slate-500 py-6 text-center">
                        Chưa có dòng lệnh stdout nào trong phiên hiện tại. Khi bạn bấm chạy tập, log trực tiếp từ
                        runner sẽ hiển thị tại đây.
                      </div>
                    ) : (
                      terminalLines.map((ln, idx) => (
                        <div key={idx} className="whitespace-pre-wrap leading-relaxed">
                          {ln}
                        </div>
                      ))
                    )}
                  </div>
                ) : (
                  <div className="flex flex-col gap-1.5 max-h-64 overflow-y-auto pr-1">
                    {channelLogs.length === 0 ? (
                      <div className="text-xs py-8 text-center text-slate-500">
                        Chưa có bản ghi log nào cho kênh này.
                      </div>
                    ) : (
                      channelLogs.map(item => (
                        <div
                          key={item.id}
                          className="px-3.5 py-2 rounded-xl bg-slate-950/80 border border-slate-800/80 text-xs flex items-start gap-2.5"
                        >
                          <span className="font-mono text-[10px] text-slate-500 shrink-0 mt-0.5">
                            {item.created_at}
                          </span>
                          <span
                            className={`px-2 py-0.5 rounded-md text-[9px] font-bold shrink-0 ${
                              item.level === 'ERROR'
                                ? 'bg-rose-500/15 text-rose-300 border border-rose-500/30'
                                : item.level === 'WARN'
                                  ? 'bg-amber-500/15 text-amber-300 border border-amber-500/30'
                                  : item.level === 'SUCCESS'
                                    ? 'bg-emerald-500/15 text-emerald-300 border border-emerald-500/30'
                                    : 'bg-indigo-500/15 text-indigo-300 border border-indigo-500/30'
                            }`}
                          >
                            {item.level}
                          </span>
                          {item.episode ? (
                            <span className="text-[10px] font-mono font-semibold text-amber-300 shrink-0 mt-0.5">
                              [Tập {item.episode}
                              {item.clip_num ? `•C${item.clip_num}` : ''}]
                            </span>
                          ) : null}
                          <span className="flex-1 text-slate-200 break-words">{item.message}</span>
                        </div>
                      ))
                    )}
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      ) : null}
    </div>
  )
}
