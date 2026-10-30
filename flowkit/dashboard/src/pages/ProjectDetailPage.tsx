import { useState, useEffect, useCallback, useMemo } from 'react'
import { useSearchParams, useNavigate } from 'react-router-dom'
import {
  Copy,
  Check,
  ExternalLink,
  Lock,
  Tv,
  Film,
  Cloud,
  Search,
  Play,
  X,
  ArrowLeft,
  RefreshCw,
  Layers,
  CheckCircle2,
  Clock,
  FileText,
} from 'lucide-react'
import { fetchAPI, patchAPI, resolveApiUrl } from '../api/client'
import type { Project, Character, Video, Scene, Request, StatusType } from '../types'
import EditableText from '../components/projects/EditableText'
import PipelineView from '../components/pipeline/PipelineView'
import { count, charStatus, videoStageBreakdown, type SceneStage } from '../lib/stageStats'
import { useTranslation } from '../i18n/useTranslation'
import { statusLabel, stateLabel, projectStatusLabel, stageLowerLabel } from '../i18n/labels'
import { Card, CardHeader, CardTitle, CardContent } from '../components/ui/card'
import { Badge } from '../components/ui/badge'
import { Progress } from '../components/ui/progress'
import { Tabs, TabsList, TabsTrigger, TabsContent } from '../components/ui/tabs'
import { Button } from '../components/ui/button'

type Tab = 'overview' | 'characters' | 'videos' | 'pipeline'
const STAGE_KEYS: ('refs' | SceneStage)[] = ['refs', 'image', 'video', 'upscale']

interface Props {
  projectId: string
  onBack: () => void
}

interface CMSCharacterSpec {
  tag: string
  name: string
  default_media_id?: string
  locked_media_id?: string
  description?: string
  ref_prompt?: string
}

interface CMSClipItem {
  clip_num: number
  file_name: string
  file_path: string
  prompt: string
  status: 'COMPLETED' | 'PENDING'
  video_url: string | null
  r2_url?: string | null
  r2_key?: string | null
  video_size_mb?: number | null
  frame_url?: string | null
  frame_r2_url?: string | null
}

interface CMSEpisodeItem {
  episode_num: number
  folder_name: string
  label: string
  total_clips: number
  rendered_clips: number
  r2_synced_clips?: number
  is_complete: boolean
  merged_video_url?: string | null
  merged_r2_url?: string | null
  merged_r2_key?: string | null
  merged_size_mb?: number | null
  clips?: CMSClipItem[]
}

interface CMSChannelSummary {
  slug: string
  name: string
  project_id: string
  aspect_ratio: string
  runner_script: string
  series_dir?: string
  ep_prefix?: string
  description: string
  characters: CMSCharacterSpec[]
  episodes?: CMSEpisodeItem[]
  stats?: {
    total_episodes: number
    completed_episodes?: number
    total_clips: number
    rendered_clips: number
    r2_synced_clips?: number
    merged_episodes: number
    r2_merged_episodes?: number
  }
}

interface UnifiedCharacterRow {
  id: string
  tag: string | null
  name: string
  entity_type: string
  media_id: string | null
  description: string
  ref_prompt: string | null
  reference_image_url: string | null
  status: StatusType | 'LOCKED'
  updated_at: string
  is_db_char: boolean
}

interface FlattenedPipelineClip {
  key: string
  episode_num: number
  episode_label: string
  folder_name: string
  clip_num: number
  file_name: string
  prompt: string
  status: 'COMPLETED' | 'PENDING'
  video_url: string | null
  r2_url: string | null
  video_size_mb: number | null
  matched_tags: string[]
}

const STATUS_COLOR: Record<string, string> = {
  COMPLETED: 'var(--green)',
  LOCKED: '#fbbf24',
  PROCESSING: 'var(--yellow)',
  FAILED: 'var(--red)',
  PENDING: 'var(--muted)',
}

function normalizeAspectRatio(ar: string | null | undefined): string {
  if (!ar) return '9:16'
  if (ar.includes('PORTRAIT') || ar.includes('9:16')) return '9:16'
  if (ar.includes('LANDSCAPE') || ar.includes('16:9')) return '16:9'
  return ar
}

export default function ProjectDetailPage({ projectId, onBack }: Props) {
  const { t } = useTranslation()
  const navigate = useNavigate()
  const [searchParams, setSearchParams] = useSearchParams()
  const tab = (searchParams.get('tab') as Tab) ?? 'overview'

  const [project, setProject] = useState<Project | null>(null)
  const [allChannels, setAllChannels] = useState<CMSChannelSummary[]>([])
  const [cmsChannel, setCmsChannel] = useState<CMSChannelSummary | null>(null)
  const [characters, setCharacters] = useState<Character[]>([])
  const [videos, setVideos] = useState<Video[]>([])
  const [scenesByVideo, setScenesByVideo] = useState<Record<string, Scene[]>>({})
  const [requests, setRequests] = useState<Request[]>([])
  const [loading, setLoading] = useState(true)
  const [pipelineVideoId, setPipelineVideoId] = useState<string>('')
  const [copiedKey, setCopiedKey] = useState<string | null>(null)

  // Table search & pagination for Characters tab
  const [charSearch, setCharSearch] = useState('')
  const [charPage, setCharPage] = useState(1)
  const [charPageSize, setCharPageSize] = useState(10)
  const [autoLocking, setAutoLocking] = useState(false)
  const [autoLockMsg, setAutoLockMsg] = useState<string | null>(null)

  // Table search & pagination for Videos/Episodes tab
  const [videoSearch, setVideoSearch] = useState('')
  const [videoPage, setVideoPage] = useState(1)
  const [videoPageSize, setVideoPageSize] = useState(15)

  // Table search & pagination for Pipeline tab
  const [pipelineEpisodeFilter, setPipelineEpisodeFilter] = useState<string>('ALL')
  const [pipelineStatusFilter, setPipelineStatusFilter] = useState<string>('ALL')
  const [pipelineSearch, setPipelineSearch] = useState<string>('')
  const [pipelinePage, setPipelinePage] = useState<number>(1)
  const [pipelinePageSize, setPipelinePageSize] = useState<number>(15)
  const [selectedPromptModal, setSelectedPromptModal] = useState<FlattenedPipelineClip | null>(null)

  // On-demand video preview modal (no preloaded <video> in tables)
  const [previewVideo, setPreviewVideo] = useState<{ title: string; url: string } | null>(null)

  const copyText = (text: string, key: string) => {
    navigator.clipboard.writeText(text)
    setCopiedKey(key)
    setTimeout(() => setCopiedKey(null), 1800)
  }

  const fetchAll = useCallback(async () => {
    setLoading(true)
    try {
      const [proj, chars, vids, channelsRes] = await Promise.all([
        fetchAPI<Project>(`/api/projects/${projectId}`).catch(() => null),
        fetchAPI<Character[]>(`/api/projects/${projectId}/characters`).catch(() => [] as Character[]),
        fetchAPI<Video[]>(`/api/videos?project_id=${projectId}`).catch(() => [] as Video[]),
        fetchAPI<{ channels?: CMSChannelSummary[] } | CMSChannelSummary[]>('/api/cms/channels').catch(
          () => ({ channels: [] })
        ),
      ])

      const channelsList = Array.isArray(channelsRes)
        ? channelsRes
        : channelsRes?.channels || []
      setAllChannels(channelsList)

      const matchedChan = channelsList.find(
        c => c.project_id === projectId || c.slug === projectId
      )

      let chanDetail: CMSChannelSummary | null = matchedChan || null
      if (matchedChan?.slug) {
        const fullChanRes = await fetchAPI<{
          channel?: CMSChannelSummary
          episodes?: CMSEpisodeItem[]
        }>(`/api/cms/channels/${matchedChan.slug}`).catch(() => null)

        if (fullChanRes?.channel) {
          chanDetail = {
            ...matchedChan,
            ...fullChanRes.channel,
            episodes: fullChanRes.episodes || [],
          }
        }
      }
      setCmsChannel(chanDetail)

      if (proj) {
        setProject(proj)
      } else if (chanDetail) {
        setProject({
          id: chanDetail.project_id || projectId,
          name: chanDetail.name,
          description: chanDetail.description || '',
          story: chanDetail.description || '',
          thumbnail_url: null,
          language: 'vi',
          status: 'ACTIVE',
          user_paygate_tier: 'PAYGATE_TIER_TWO',
          material: '3d_pixar',
          narrator_voice: null,
          narrator_ref_audio: null,
          created_at: new Date().toISOString(),
          updated_at: new Date().toISOString(),
        })
      }

      const safeVids = Array.isArray(vids) ? vids : []
      const sceneLists = await Promise.all(
        safeVids.map(v => fetchAPI<Scene[]>(`/api/scenes?video_id=${v.id}`).catch(() => [] as Scene[]))
      )
      const sbv: Record<string, Scene[]> = {}
      safeVids.forEach((v, i) => {
        sbv[v.id] = sceneLists[i]
      })
      const reqs = await fetchAPI<Request[]>(`/api/requests?project_id=${projectId}`).catch(
        () => [] as Request[]
      )

      setCharacters(Array.isArray(chars) ? chars : [])
      setVideos(safeVids)
      setScenesByVideo(sbv)
      setRequests(Array.isArray(reqs) ? reqs : [])
      setPipelineVideoId(prev => {
        if (prev && safeVids.some(v => v.id === prev)) return prev
        const activeVid = safeVids.find(v => v.status !== 'completed' && v.status !== 'done')
        return activeVid?.id ?? safeVids[safeVids.length - 1]?.id ?? ''
      })
    } finally {
      setLoading(false)
    }
  }, [projectId])

  useEffect(() => {
    Promise.resolve().then(fetchAll)
  }, [fetchAll])

  function setTab(t: Tab) {
    setSearchParams(prev => {
      const next = new URLSearchParams(prev)
      next.set('tab', t)
      return next
    })
  }

  async function patchProject(field: string, value: string) {
    await patchAPI(`/api/projects/${projectId}`, { [field]: value })
    fetchAll()
  }

  async function patchChar(cid: string, field: string, value: string) {
    await patchAPI(`/api/characters/${cid}`, { [field]: value })
    fetchAll()
  }

  async function handleAutoLockCharacters() {
    if (!cmsChannel?.slug) return
    setAutoLocking(true)
    setAutoLockMsg(null)
    try {
      const res = await fetchAPI<{
        ok: boolean
        locked_count: number
        total_characters: number
        created_now: string[]
        extension_connected: boolean
      }>(`/api/cms/channels/${cmsChannel.slug}/auto-lock-characters`, { method: 'POST' })
      if (res.created_now && res.created_now.length > 0) {
        setAutoLockMsg(
          `✅ Đã tự tạo mới & khóa ${res.created_now.join(', ')} trên Google Flow (${res.locked_count}/${res.total_characters} nhân vật)!`
        )
      } else if (res.locked_count === res.total_characters) {
        setAutoLockMsg(
          `🔒 Đã đồng bộ & khóa đủ ${res.locked_count}/${res.total_characters} nhân vật từ Google Flow Project!`
        )
      } else if (!res.extension_connected) {
        setAutoLockMsg(
          `⚠️ Chrome Extension chưa kết nối với Google Flow tab (https://labs.google/fx/vi/tools/flow/project/${project?.id}). Hãy mở tab Flow rồi bấm lại!`
        )
      } else {
        setAutoLockMsg(
          `🔄 Đã kiểm tra Google Flow Project (${res.locked_count}/${res.total_characters} nhân vật đã khóa).`
        )
      }
      await fetchAll()
    } catch (e) {
      setAutoLockMsg(`❌ Lỗi khi tự tạo nhân vật: ${e instanceof Error ? e.message : String(e)}`)
    } finally {
      setAutoLocking(false)
    }
  }

  // Merge DB `characters` with CMS `cmsChannel.characters`
  const unifiedCharacters = useMemo<UnifiedCharacterRow[]>(() => {
    const rows: UnifiedCharacterRow[] = []
    const seenTagsOrNames = new Set<string>()

    if (cmsChannel?.characters && cmsChannel.characters.length > 0) {
      for (const c of cmsChannel.characters) {
        const mid = c.locked_media_id || c.default_media_id || null
        seenTagsOrNames.add(c.name.toLowerCase())
        seenTagsOrNames.add(c.tag.toLowerCase())
        seenTagsOrNames.add(c.tag.toLowerCase().replace(/^@/, ''))
        if (mid) seenTagsOrNames.add(mid.toLowerCase())
        rows.push({
          id: `cms-${c.tag}`,
          tag: c.tag,
          name: c.name,
          entity_type: 'character',
          media_id: mid,
          description: c.description || '',
          ref_prompt: c.ref_prompt || null,
          reference_image_url: null,
          status: mid ? 'LOCKED' : 'PENDING',
          updated_at: project?.updated_at || new Date().toISOString(),
          is_db_char: false,
        })
      }
      return rows
    }

    for (const ch of characters) {
      if (seenTagsOrNames.has(ch.name.toLowerCase())) continue
      const st = charStatus(ch, requests)
      rows.push({
        id: ch.id,
        tag: `@${ch.name.replace(/\s+/g, '')}`,
        name: ch.name,
        entity_type: ch.entity_type,
        media_id: ch.media_id,
        description: ch.description || '',
        ref_prompt: null,
        reference_image_url: ch.reference_image_url,
        status: st,
        updated_at: ch.updated_at,
        is_db_char: true,
      })
    }

    return rows
  }, [cmsChannel, characters, requests, project])

  const filteredCharacters = useMemo(() => {
    const q = charSearch.trim().toLowerCase()
    if (!q) return unifiedCharacters
    return unifiedCharacters.filter(
      c =>
        c.name.toLowerCase().includes(q) ||
        (c.tag || '').toLowerCase().includes(q) ||
        (c.media_id || '').toLowerCase().includes(q) ||
        c.description.toLowerCase().includes(q)
    )
  }, [unifiedCharacters, charSearch])

  const cmsEpisodes = useMemo<CMSEpisodeItem[]>(() => {
    return cmsChannel?.episodes || []
  }, [cmsChannel])

  const filteredCmsEpisodes = useMemo(() => {
    const q = videoSearch.trim().toLowerCase()
    if (!q) return cmsEpisodes
    return cmsEpisodes.filter(
      ep =>
        (ep.label || '').toLowerCase().includes(q) ||
        (ep.folder_name || '').toLowerCase().includes(q) ||
        `tập ${ep.episode_num}`.includes(q) ||
        `ep${ep.episode_num}`.includes(q)
    )
  }, [cmsEpisodes, videoSearch])

  const filteredDbVideos = useMemo(() => {
    const q = videoSearch.trim().toLowerCase()
    if (!q) return videos
    return videos.filter(
      v => v.title.toLowerCase().includes(q) || v.id.toLowerCase().includes(q)
    )
  }, [videos, videoSearch])

  // Flatten all CMS clips across episodes for `?tab=pipeline`
  const allCmsClips = useMemo<FlattenedPipelineClip[]>(() => {
    const channelTags = (cmsChannel?.characters || []).map(c => c.tag)
    const list: FlattenedPipelineClip[] = []
    for (const ep of cmsEpisodes) {
      const clips = ep.clips || []
      for (const cl of clips) {
        const promptStr = cl.prompt || ''
        const matched = channelTags.filter(tag => promptStr.includes(tag))
        list.push({
          key: `ep${ep.episode_num}-cl${cl.clip_num}`,
          episode_num: ep.episode_num,
          episode_label: ep.label || `Tập ${String(ep.episode_num).padStart(2, '0')}`,
          folder_name: ep.folder_name || '',
          clip_num: cl.clip_num,
          file_name: cl.file_name || `clip-${cl.clip_num}.md`,
          prompt: promptStr,
          status: cl.status,
          video_url: cl.video_url || null,
          r2_url: cl.r2_url || null,
          video_size_mb: cl.video_size_mb ?? null,
          matched_tags: matched.length > 0 ? matched : channelTags,
        })
      }
    }
    return list
  }, [cmsEpisodes, cmsChannel])

  const filteredPipelineClips = useMemo(() => {
    const q = pipelineSearch.trim().toLowerCase()
    return allCmsClips.filter(item => {
      if (pipelineEpisodeFilter !== 'ALL' && String(item.episode_num) !== pipelineEpisodeFilter) {
        return false
      }
      if (pipelineStatusFilter === 'COMPLETED' && item.status !== 'COMPLETED') return false
      if (pipelineStatusFilter === 'PENDING' && item.status !== 'PENDING') return false
      if (pipelineStatusFilter === 'R2' && !item.r2_url) return false

      if (q) {
        const matchPrompt = item.prompt.toLowerCase().includes(q)
        const matchEp = item.episode_label.toLowerCase().includes(q) || item.folder_name.toLowerCase().includes(q)
        const matchClip = `clip ${item.clip_num}`.includes(q) || item.file_name.toLowerCase().includes(q)
        const matchTag = item.matched_tags.some(t => t.toLowerCase().includes(q))
        if (!matchPrompt && !matchEp && !matchClip && !matchTag) return false
      }
      return true
    })
  }, [allCmsClips, pipelineEpisodeFilter, pipelineStatusFilter, pipelineSearch])

  useEffect(() => {
    setCharPage(1)
  }, [charSearch, charPageSize])

  useEffect(() => {
    setVideoPage(1)
  }, [videoSearch, videoPageSize])

  useEffect(() => {
    setPipelinePage(1)
  }, [pipelineEpisodeFilter, pipelineStatusFilter, pipelineSearch, pipelinePageSize])

  if (loading || !project) {
    return (
      <div className="p-6 text-xs" style={{ color: 'var(--muted)' }}>
        {t('projectDetail.loading')}
      </div>
    )
  }

  const allScenes = videos.flatMap(v => scenesByVideo[v.id] ?? [])

  // Compute stageRollup from CMS stats when CMS episodes exist, otherwise fallback to legacy tables
  const lockedCharsCount = unifiedCharacters.filter(c => c.media_id || c.status === 'LOCKED' || c.status === 'COMPLETED').length
  const totalClipsCount = cmsChannel?.stats?.total_clips ?? allCmsClips.length
  const renderedClipsCount =
    cmsChannel?.stats?.rendered_clips ??
    allCmsClips.filter(c => c.status === 'COMPLETED').length
  const totalEpisodesCount = cmsChannel?.stats?.total_episodes ?? cmsEpisodes.length
  const mergedEpisodesCount =
    cmsChannel?.stats?.merged_episodes ??
    cmsEpisodes.filter(e => e.is_complete || e.merged_video_url || e.merged_r2_url).length

  const stageRollup: Record<'refs' | SceneStage, ReturnType<typeof count>> =
    cmsEpisodes.length > 0
      ? {
          refs: {
            done: lockedCharsCount,
            processing: 0,
            failed: 0,
            pending: Math.max(0, unifiedCharacters.length - lockedCharsCount),
            total: unifiedCharacters.length,
          },
          image: {
            done: totalClipsCount,
            processing: 0,
            failed: 0,
            pending: 0,
            total: totalClipsCount,
          },
          video: {
            done: renderedClipsCount,
            processing: 0,
            failed: 0,
            pending: Math.max(0, totalClipsCount - renderedClipsCount),
            total: totalClipsCount,
          },
          upscale: {
            done: mergedEpisodesCount,
            processing: 0,
            failed: 0,
            pending: Math.max(0, totalEpisodesCount - mergedEpisodesCount),
            total: totalEpisodesCount,
          },
        }
      : {
          refs: count(characters.map(c => charStatus(c, requests))),
          ...videoStageBreakdown(allScenes),
        }

  // Pagination calculations for Characters
  const charTotalPages = Math.max(1, Math.ceil(filteredCharacters.length / charPageSize))
  const safeCharPage = Math.min(charPage, charTotalPages)
  const charStartIndex = (safeCharPage - 1) * charPageSize
  const pagedCharacters = filteredCharacters.slice(charStartIndex, charStartIndex + charPageSize)

  // Pagination calculations for Videos / CMS Episodes
  const useCmsEpisodesView = cmsEpisodes.length > 0 && videos.length === 0
  const totalVideoRows = useCmsEpisodesView ? filteredCmsEpisodes.length : filteredDbVideos.length
  const videoTotalPages = Math.max(1, Math.ceil(totalVideoRows / videoPageSize))
  const safeVideoPage = Math.min(videoPage, videoTotalPages)
  const videoStartIndex = (safeVideoPage - 1) * videoPageSize
  const pagedCmsEpisodes = filteredCmsEpisodes.slice(videoStartIndex, videoStartIndex + videoPageSize)
  const pagedDbVideos = filteredDbVideos.slice(videoStartIndex, videoStartIndex + videoPageSize)

  // Pagination calculations for Pipeline Clips
  const pipelineTotalPages = Math.max(1, Math.ceil(filteredPipelineClips.length / pipelinePageSize))
  const safePipelinePage = Math.min(pipelinePage, pipelineTotalPages)
  const pipelineStartIndex = (safePipelinePage - 1) * pipelinePageSize
  const pagedPipelineClips = filteredPipelineClips.slice(
    pipelineStartIndex,
    pipelineStartIndex + pipelinePageSize
  )

  return (
    <div className="flex flex-col gap-4 pb-10">
      {/* Top Project Header */}
      <div
        className="rounded-xl p-4 flex flex-wrap items-start justify-between gap-4"
        style={{ background: 'var(--surface)', border: '1px solid var(--border)' }}
      >
        <div className="flex flex-col gap-1.5">
          <div className="flex flex-wrap items-center gap-2.5">
            <h1 className="m-0 text-lg font-bold" style={{ color: 'var(--text)' }}>
              {project.name}
            </h1>
            <Badge variant="outline">{project.material}</Badge>
            {cmsChannel?.aspect_ratio && (
              <Badge variant="outline">{normalizeAspectRatio(cmsChannel.aspect_ratio)}</Badge>
            )}
            <Badge variant="outline">{projectStatusLabel(t, project.status)}</Badge>
            {cmsChannel?.slug && (
              <span
                onClick={() => navigate(`/channels/${cmsChannel.slug}`)}
                className="px-2 py-0.5 rounded text-[11px] font-mono cursor-pointer flex items-center gap-1"
                style={{
                  background: 'rgba(16,185,129,0.14)',
                  color: '#34d399',
                  border: '1px solid rgba(16,185,129,0.3)',
                }}
              >
                <Tv className="w-3 h-3" />/{cmsChannel.slug}
              </span>
            )}
          </div>

          <div className="flex flex-wrap items-center gap-2 text-[11px]" style={{ color: 'var(--muted)' }}>
            <span>Google Flow Project ID:</span>
            <code
              className="px-2 py-0.5 rounded font-mono text-[11px]"
              style={{
                background: 'var(--bg)',
                border: '1px solid var(--border)',
                color: '#93c5fd',
              }}
            >
              {project.id}
            </code>
            <button
              onClick={() => copyText(project.id, 'header-pid')}
              className="p-1 rounded cursor-pointer hover:bg-white/10"
              style={{ color: copiedKey === 'header-pid' ? '#34d399' : 'var(--muted)' }}
              title="Copy Project ID"
            >
              {copiedKey === 'header-pid' ? (
                <Check className="w-3.5 h-3.5" />
              ) : (
                <Copy className="w-3.5 h-3.5" />
              )}
            </button>
            <a
              href={`https://labs.google/fx/vi/tools/flow/project/${project.id}`}
              target="_blank"
              rel="noreferrer"
              className="inline-flex items-center gap-1 hover:underline"
              style={{ color: '#60a5fa' }}
            >
              Mở Google Flow <ExternalLink className="w-3 h-3" />
            </a>
          </div>
        </div>

        {/* Right Controls: Quick Project Switcher (<select><option>) + Back button */}
        <div className="flex flex-wrap items-center gap-2">
          {allChannels.length > 0 && (
            <select
              value={project.id}
              onChange={e => {
                if (e.target.value) navigate(`/projects/${e.target.value}?tab=${tab}`)
              }}
              className="px-3 py-1.5 rounded-lg text-xs font-medium outline-none cursor-pointer"
              style={{
                background: 'var(--bg)',
                border: '1px solid var(--border)',
                color: 'var(--text)',
              }}
            >
              {allChannels.map(ch => (
                <option key={ch.slug} value={ch.project_id}>
                  🎬 {ch.name} ({normalizeAspectRatio(ch.aspect_ratio)})
                </option>
              ))}
            </select>
          )}

          {cmsChannel?.slug && (
            <Button
              variant="outline"
              size="sm"
              onClick={() => navigate(`/channels/${cmsChannel.slug}`)}
            >
              <Tv className="w-3.5 h-3.5 mr-1.5" />
              Studio Kênh
            </Button>
          )}

          <Button variant="outline" size="sm" onClick={fetchAll}>
            <RefreshCw className="w-3.5 h-3.5 mr-1" />
            Làm mới
          </Button>

          <Button variant="ghost" size="sm" onClick={onBack}>
            <ArrowLeft className="w-3.5 h-3.5 mr-1" />
            Danh sách Dự Án
          </Button>
        </div>
      </div>

      <Tabs value={tab} onValueChange={v => setTab(v as Tab)}>
        <TabsList>
          <TabsTrigger value="overview">{t('projectDetail.tab.overview')}</TabsTrigger>
          <TabsTrigger value="characters">
            Nhân Vật @Tag ({unifiedCharacters.length})
          </TabsTrigger>
          <TabsTrigger value="videos">
            Tập Phim & Videos ({useCmsEpisodesView ? cmsEpisodes.length : videos.length})
          </TabsTrigger>
          <TabsTrigger value="pipeline">
            Pipeline Cảnh Quay ({allCmsClips.length > 0 ? allCmsClips.length : allScenes.length})
          </TabsTrigger>
        </TabsList>

        {/* OVERVIEW TAB */}
        <TabsContent value="overview" className="pt-4">
          <div className="grid gap-4" style={{ gridTemplateColumns: '1.4fr 1fr' }}>
            <Card className="py-4">
              <CardHeader>
                <CardTitle className="text-xs tracking-widest uppercase">
                  {t('projectDetail.card.projectFields')}
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="flex flex-col gap-3.5">
                  {[
                    {
                      label: t('projectDetail.field.name'),
                      value: project.name,
                      field: 'name',
                      multiline: false,
                    },
                    {
                      label: t('projectDetail.field.description'),
                      value: project.description ?? '',
                      field: 'description',
                      multiline: true,
                    },
                    {
                      label: t('projectDetail.field.story'),
                      value: project.story ?? '',
                      field: 'story',
                      multiline: true,
                    },
                  ].map(f => (
                    <div key={f.field} className="flex flex-col gap-1">
                      <span
                        className="text-[9px] tracking-widest"
                        style={{ color: 'var(--muted)' }}
                      >
                        {f.label}
                      </span>
                      <div
                        className="rounded-md px-2.5 py-2 text-xs"
                        style={{
                          background: 'var(--surface)',
                          border: '1px solid var(--border)',
                        }}
                      >
                        <EditableText
                          value={f.value}
                          onSave={v => patchProject(f.field, v)}
                          multiline={f.multiline}
                          className="text-xs"
                        />
                      </div>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>

            <div className="flex flex-col gap-4">
              {cmsChannel && (
                <Card className="py-4">
                  <CardHeader>
                    <CardTitle className="text-xs tracking-widest uppercase">
                      Thống Kê Kênh Series & Cloudflare R2 CDN
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="flex flex-col gap-2 text-xs">
                      <div className="flex justify-between">
                        <span style={{ color: 'var(--muted)' }}>Kênh Series:</span>
                        <strong style={{ color: 'var(--text)' }}>{cmsChannel.name}</strong>
                      </div>
                      <div className="flex justify-between">
                        <span style={{ color: 'var(--muted)' }}>Runner Script:</span>
                        <code style={{ color: '#34d399' }}>{cmsChannel.runner_script}</code>
                      </div>
                      <div className="flex justify-between">
                        <span style={{ color: 'var(--muted)' }}>Số tập hoàn tất (Full):</span>
                        <strong style={{ color: 'var(--text)' }}>
                          {mergedEpisodesCount} / {totalEpisodesCount} tập
                        </strong>
                      </div>
                      <div className="flex justify-between">
                        <span style={{ color: 'var(--muted)' }}>Số clips đã render:</span>
                        <strong style={{ color: 'var(--text)' }}>
                          {renderedClipsCount} / {totalClipsCount} clips
                        </strong>
                      </div>
                      <div className="flex justify-between">
                        <span style={{ color: 'var(--muted)' }}>Đồng bộ R2 Public MP4:</span>
                        <strong style={{ color: '#38bdf8' }}>
                          {cmsChannel.stats?.r2_synced_clips ??
                            allCmsClips.filter(c => c.r2_url).length}{' '}
                          clips ·{' '}
                          {cmsChannel.stats?.r2_merged_episodes ??
                            cmsEpisodes.filter(e => e.merged_r2_url).length}{' '}
                          tập
                        </strong>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              )}

              <Card className="py-4">
                <CardHeader>
                  <CardTitle className="text-xs tracking-widest uppercase">
                    {t('projectDetail.card.stageRollup')}
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="flex flex-col gap-2.5">
                    {STAGE_KEYS.map(key => {
                      const c = stageRollup[key]
                      const pct = c.total > 0 ? Math.round((c.done / c.total) * 100) : 0
                      return (
                        <div
                          key={key}
                          className="grid items-center gap-2.5"
                          style={{ gridTemplateColumns: '75px 1fr 65px' }}
                        >
                          <span
                            className="text-[10px] tracking-wide uppercase"
                            style={{ color: 'var(--text)' }}
                          >
                            {stageLowerLabel(t, key)}
                          </span>
                          <Progress value={pct} className="h-1.5" />
                          <span
                            className="text-[10px] text-right font-mono"
                            style={{ color: 'var(--muted)' }}
                          >
                            {c.done}/{c.total}
                          </span>
                        </div>
                      )
                    })}
                  </div>
                </CardContent>
              </Card>
            </div>
          </div>
        </TabsContent>

        {/* CHARACTERS LIST TABLE TAB */}
        <TabsContent value="characters" className="pt-4">
          <div
            className="rounded-xl overflow-hidden flex flex-col"
            style={{ background: 'var(--surface)', border: '1px solid var(--border)' }}
          >
            {/* Filter Header */}
            <div
              className="p-3.5 flex flex-wrap items-center justify-between gap-3"
              style={{ borderBottom: '1px solid var(--border)' }}
            >
              <div className="flex flex-wrap items-center gap-2">
                <Lock className="w-4 h-4" style={{ color: '#fbbf24' }} />
                <span className="text-xs font-bold" style={{ color: 'var(--text)' }}>
                  Danh Sách Nhân Vật Khóa Cố Định ({filteredCharacters.length})
                </span>
                {cmsChannel?.slug && (
                  <button
                    onClick={handleAutoLockCharacters}
                    disabled={autoLocking}
                    className="px-3 py-1 rounded-lg text-xs font-semibold flex items-center gap-1.5 cursor-pointer disabled:opacity-50"
                    style={{
                      background: 'rgba(245,158,11,0.16)',
                      color: '#fbbf24',
                      border: '1px solid rgba(245,158,11,0.35)',
                    }}
                    title="Đồng bộ và khóa Media ID của các nhân vật bạn đã tạo trong mục Characters trên Google Flow Project"
                  >
                    <RefreshCw className={`w-3.5 h-3.5 ${autoLocking ? 'animate-spin' : ''}`} />
                    {autoLocking
                      ? 'Đang đồng bộ nhân vật từ Google Flow...'
                      : '🔄 Đồng Bộ Nhân Vật (@Tag) Đã Tạo Từ Google Flow'}
                  </button>
                )}
              </div>

              <div
                className="flex items-center gap-2 px-3 py-1.5 rounded-lg"
                style={{
                  background: 'var(--bg)',
                  border: '1px solid var(--border)',
                  minWidth: 260,
                }}
              >
                <Search className="w-3.5 h-3.5" style={{ color: 'var(--muted)' }} />
                <input
                  type="text"
                  value={charSearch}
                  onChange={e => setCharSearch(e.target.value)}
                  placeholder="Tìm @Tag, tên nhân vật, Media ID..."
                  className="bg-transparent border-none outline-none text-xs w-full"
                  style={{ color: 'var(--text)' }}
                />
              </div>
            </div>

            {autoLockMsg && (
              <div
                className="px-4 py-2.5 text-xs font-medium"
                style={{
                  background: 'rgba(245,158,11,0.08)',
                  borderBottom: '1px solid var(--border)',
                  color: 'var(--text)',
                }}
              >
                {autoLockMsg}
              </div>
            )}

            {filteredCharacters.length === 0 ? (
              <div className="p-8 text-center text-xs" style={{ color: 'var(--muted)' }}>
                {t('projectDetail.noCharacters')}
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
                      <th className="py-3 px-3.5">Loại</th>
                      <th className="py-3 px-3.5">Mã Media ID (Google Flow)</th>
                      <th className="py-3 px-3.5">Mô Tả Ngoại Hình Cố Định</th>
                      <th className="py-3 px-3.5">Trạng Thái</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y" style={{ borderColor: 'var(--border)' }}>
                    {pagedCharacters.map((ch, idx) => {
                      const rowNum = charStartIndex + idx + 1
                      const isCopied = copiedKey === `char-mid-${ch.id}`
                      return (
                        <tr
                          key={ch.id}
                          className="transition-colors hover:bg-white/[0.02]"
                          style={{ borderBottom: '1px solid var(--border)' }}
                        >
                          <td
                            className="py-3 px-3.5 text-xs font-mono text-center"
                            style={{ color: 'var(--muted)' }}
                          >
                            {rowNum}
                          </td>

                          <td className="py-3 px-3.5">
                            <div className="flex items-center gap-2">
                              {ch.tag && (
                                <span
                                  onClick={() => copyText(ch.tag!, `char-tag-${ch.id}`)}
                                  className="px-2 py-0.5 rounded text-[11px] font-mono font-semibold flex items-center gap-1 cursor-pointer"
                                  style={{
                                    background: 'rgba(245,158,11,0.14)',
                                    color: '#fbbf24',
                                    border: '1px solid rgba(245,158,11,0.3)',
                                  }}
                                  title="Bấm để copy @Tag"
                                >
                                  <Lock className="w-2.5 h-2.5" />
                                  {ch.tag}
                                </span>
                              )}
                              <span className="text-xs font-semibold" style={{ color: 'var(--text)' }}>
                                {ch.name}
                              </span>
                            </div>
                          </td>

                          <td className="py-3 px-3.5">
                            <Badge variant="outline">{ch.entity_type}</Badge>
                          </td>

                          <td className="py-3 px-3.5">
                            {ch.media_id ? (
                              <div className="flex items-center gap-1.5">
                                <code
                                  className="px-2 py-1 rounded text-[11px] font-mono"
                                  style={{
                                    background: 'var(--bg)',
                                    border: '1px solid var(--border)',
                                    color: '#34d399',
                                  }}
                                >
                                  {ch.media_id}
                                </code>
                                <button
                                  onClick={() => copyText(ch.media_id!, `char-mid-${ch.id}`)}
                                  className="p-1.5 rounded cursor-pointer hover:bg-white/10"
                                  style={{ color: isCopied ? '#34d399' : 'var(--muted)' }}
                                  title="Copy Media ID"
                                >
                                  {isCopied ? (
                                    <Check className="w-3.5 h-3.5" />
                                  ) : (
                                    <Copy className="w-3.5 h-3.5" />
                                  )}
                                </button>
                              </div>
                            ) : (
                              <span className="text-[11px]" style={{ color: 'var(--muted)' }}>
                                —
                              </span>
                            )}
                          </td>

                          <td className="py-3 px-3.5 max-w-[420px]">
                            <div className="flex flex-col gap-1.5">
                              {ch.is_db_char ? (
                                <EditableText
                                  value={ch.description}
                                  onSave={v => patchChar(ch.id, 'description', v)}
                                  multiline
                                  className="text-[11px]"
                                />
                              ) : (
                                <p
                                  className="m-0 text-[11px] line-clamp-2"
                                  style={{ color: 'var(--muted)' }}
                                  title={ch.description}
                                >
                                  {ch.description || '—'}
                                </p>
                              )}
                              {ch.ref_prompt && (
                                <div className="flex items-center gap-1.5 pt-0.5">
                                  <button
                                    onClick={() => copyText(ch.ref_prompt!, `char-prompt-${ch.id}`)}
                                    className="px-2 py-0.5 rounded text-[10px] font-semibold flex items-center gap-1 cursor-pointer"
                                    style={{
                                      background:
                                        copiedKey === `char-prompt-${ch.id}`
                                          ? 'rgba(52,211,153,0.15)'
                                          : 'rgba(56,189,248,0.12)',
                                      color:
                                        copiedKey === `char-prompt-${ch.id}`
                                          ? '#34d399'
                                          : '#38bdf8',
                                      border: '1px solid rgba(56,189,248,0.28)',
                                    }}
                                    title={ch.ref_prompt}
                                  >
                                    {copiedKey === `char-prompt-${ch.id}` ? (
                                      <Check className="w-3 h-3" />
                                    ) : (
                                      <Copy className="w-3 h-3" />
                                    )}
                                    {copiedKey === `char-prompt-${ch.id}`
                                      ? 'Đã copy Prompt Nhân Vật!'
                                      : 'Copy Prompt Tạo Nhân Vật'}
                                  </button>
                                </div>
                              )}
                            </div>
                          </td>

                          <td className="py-3 px-3.5">
                            <span
                              className="inline-flex items-center gap-1.5 px-2 py-0.5 rounded text-[10px] font-semibold"
                              style={{
                                background: 'rgba(255,255,255,0.05)',
                                color: STATUS_COLOR[ch.status] || 'var(--text)',
                              }}
                            >
                              <span
                                className="w-1.5 h-1.5 rounded-full"
                                style={{ background: STATUS_COLOR[ch.status] || 'var(--muted)' }}
                              />
                              {ch.status === 'LOCKED'
                                ? 'ĐÃ KHÓA (LOCKED)'
                                : statusLabel(t, ch.status)}
                            </span>
                          </td>
                        </tr>
                      )
                    })}
                  </tbody>
                </table>
              </div>
            )}

            {/* Pagination Footer for Characters */}
            {filteredCharacters.length > 0 && (
              <div
                className="px-4 py-3 flex flex-wrap items-center justify-between gap-3 text-xs"
                style={{
                  background: 'rgba(255,255,255,0.015)',
                  borderTop: '1px solid var(--border)',
                }}
              >
                <span style={{ color: 'var(--muted)' }}>
                  Hiển thị{' '}
                  <strong style={{ color: 'var(--text)' }}>
                    {charStartIndex + 1}–{Math.min(charStartIndex + charPageSize, filteredCharacters.length)}
                  </strong>{' '}
                  / <strong style={{ color: 'var(--text)' }}>{filteredCharacters.length}</strong> nhân vật
                </span>

                <div className="flex items-center gap-1.5">
                  <select
                    value={charPageSize}
                    onChange={e => setCharPageSize(Number(e.target.value))}
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
                  <button
                    disabled={safeCharPage <= 1}
                    onClick={() => setCharPage(p => Math.max(1, p - 1))}
                    className="px-2.5 py-1 rounded text-xs cursor-pointer disabled:opacity-40"
                    style={{
                      background: 'var(--bg)',
                      border: '1px solid var(--border)',
                      color: 'var(--text)',
                    }}
                  >
                    ‹ Trước
                  </button>
                  <span className="px-2 text-xs font-semibold">
                    Trang {safeCharPage}/{charTotalPages}
                  </span>
                  <button
                    disabled={safeCharPage >= charTotalPages}
                    onClick={() => setCharPage(p => Math.min(charTotalPages, p + 1))}
                    className="px-2.5 py-1 rounded text-xs cursor-pointer disabled:opacity-40"
                    style={{
                      background: 'var(--bg)',
                      border: '1px solid var(--border)',
                      color: 'var(--text)',
                    }}
                  >
                    Sau ›
                  </button>
                </div>
              </div>
            )}
          </div>
        </TabsContent>

        {/* VIDEOS & EPISODES LIST TABLE TAB */}
        <TabsContent value="videos" className="pt-4">
          <div
            className="rounded-xl overflow-hidden flex flex-col"
            style={{ background: 'var(--surface)', border: '1px solid var(--border)' }}
          >
            <div
              className="p-3.5 flex flex-wrap items-center justify-between gap-3"
              style={{ borderBottom: '1px solid var(--border)' }}
            >
              <div className="flex items-center gap-2">
                <Film className="w-4 h-4" style={{ color: '#38bdf8' }} />
                <span className="text-xs font-bold" style={{ color: 'var(--text)' }}>
                  Danh Sách Tập Phim & Videos ({totalVideoRows})
                </span>
              </div>

              <div
                className="flex items-center gap-2 px-3 py-1.5 rounded-lg"
                style={{
                  background: 'var(--bg)',
                  border: '1px solid var(--border)',
                  minWidth: 260,
                }}
              >
                <Search className="w-3.5 h-3.5" style={{ color: 'var(--muted)' }} />
                <input
                  type="text"
                  value={videoSearch}
                  onChange={e => setVideoSearch(e.target.value)}
                  placeholder="Tìm tập phim, tiêu đề video..."
                  className="bg-transparent border-none outline-none text-xs w-full"
                  style={{ color: 'var(--text)' }}
                />
              </div>
            </div>

            {totalVideoRows === 0 ? (
              <div className="p-8 text-center text-xs" style={{ color: 'var(--muted)' }}>
                {t('projectDetail.noVideos')}
              </div>
            ) : useCmsEpisodesView ? (
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
                      <th className="py-3 px-3.5 w-16 text-center">Tập</th>
                      <th className="py-3 px-3.5">Tiêu Đề / Thư Mục Tập Phim</th>
                      <th className="py-3 px-3.5">Tiến Độ Clips</th>
                      <th className="py-3 px-3.5">Cloudflare R2 MP4</th>
                      <th className="py-3 px-3.5">Trạng Thái</th>
                      <th className="py-3 px-3.5 text-right">Thao Tác</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y" style={{ borderColor: 'var(--border)' }}>
                    {pagedCmsEpisodes.map(ep => {
                      const playUrl =
                        ep.merged_r2_url ||
                        (ep.merged_video_url ? resolveApiUrl(ep.merged_video_url) : '')
                      return (
                        <tr
                          key={ep.episode_num}
                          className="transition-colors hover:bg-white/[0.02]"
                          style={{ borderBottom: '1px solid var(--border)' }}
                        >
                          <td className="py-3 px-3.5 text-center">
                            <span
                              className="px-2 py-0.5 rounded text-[11px] font-mono font-bold"
                              style={{
                                background: 'rgba(59,130,246,0.14)',
                                color: '#60a5fa',
                              }}
                            >
                              #{ep.episode_num}
                            </span>
                          </td>
                          <td className="py-3 px-3.5">
                            <div className="flex flex-col gap-0.5">
                              <span className="text-xs font-semibold" style={{ color: 'var(--text)' }}>
                                {ep.label}
                              </span>
                              <span className="text-[10px] font-mono" style={{ color: 'var(--muted)' }}>
                                {ep.folder_name}
                              </span>
                            </div>
                          </td>
                          <td className="py-3 px-3.5 text-xs" style={{ color: 'var(--muted)' }}>
                            {ep.rendered_clips} / {ep.total_clips} clips
                          </td>
                          <td className="py-3 px-3.5">
                            {ep.merged_r2_url ? (
                              <span
                                className="inline-flex items-center gap-1 px-2 py-0.5 rounded text-[10px] font-medium"
                                style={{
                                  background: 'rgba(56,189,248,0.14)',
                                  color: '#38bdf8',
                                }}
                              >
                                <Cloud className="w-3 h-3" /> R2 MP4
                                {ep.merged_size_mb ? ` (${ep.merged_size_mb} MB)` : ''}
                              </span>
                            ) : (
                              <span className="text-[11px]" style={{ color: 'var(--muted)' }}>
                                {ep.r2_synced_clips || 0}/{ep.total_clips} R2 clips
                              </span>
                            )}
                          </td>
                          <td className="py-3 px-3.5">
                            <Badge variant={ep.is_complete ? 'secondary' : 'outline'}>
                              {ep.is_complete ? 'HOÀN TẤT' : 'ĐANG CHỜ'}
                            </Badge>
                          </td>
                          <td className="py-3 px-3.5 text-right">
                            <div className="flex items-center justify-end gap-1.5">
                              {playUrl && (
                                <button
                                  onClick={() =>
                                    setPreviewVideo({
                                      title: `${ep.label} — ${ep.folder_name}`,
                                      url: playUrl,
                                    })
                                  }
                                  className="px-2.5 py-1 rounded text-[11px] font-semibold flex items-center gap-1 cursor-pointer"
                                  style={{
                                    background: 'rgba(16,185,129,0.16)',
                                    color: '#34d399',
                                    border: '1px solid rgba(16,185,129,0.35)',
                                  }}
                                >
                                  <Play className="w-3 h-3" /> Xem MP4
                                </button>
                              )}
                              <button
                                onClick={() => {
                                  setPipelineEpisodeFilter(String(ep.episode_num))
                                  setTab('pipeline')
                                }}
                                className="px-2.5 py-1 rounded text-[11px] font-semibold cursor-pointer"
                                style={{
                                  background: 'rgba(59,130,246,0.15)',
                                  color: '#60a5fa',
                                  border: '1px solid rgba(59,130,246,0.3)',
                                }}
                              >
                                Pipeline Cảnh ({ep.total_clips})
                              </button>
                            </div>
                          </td>
                        </tr>
                      )
                    })}
                  </tbody>
                </table>
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
                      <th className="py-3 px-3.5">{t('projectDetail.table.video')}</th>
                      <th className="py-3 px-3.5">{t('projectDetail.table.scenes')}</th>
                      <th className="py-3 px-3.5">{t('projectDetail.table.progress')}</th>
                      <th className="py-3 px-3.5">{t('projectDetail.table.state')}</th>
                      <th className="py-3 px-3.5 text-right">Thao Tác</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y" style={{ borderColor: 'var(--border)' }}>
                    {pagedDbVideos.map((v, idx) => {
                      const scenes = scenesByVideo[v.id] ?? []
                      const breakdown = videoStageBreakdown(scenes)
                      const stages: SceneStage[] = ['image', 'video', 'upscale']
                      const totalSlots = scenes.length * stages.length
                      const doneSlots = stages.reduce((sum, s) => sum + breakdown[s].done, 0)
                      const pct = totalSlots > 0 ? Math.round((doneSlots / totalSlots) * 100) : 0
                      const anyProcessing = requests.some(
                        r => r.video_id === v.id && r.status === 'PROCESSING'
                      )
                      const state: 'COMPLETED' | 'RUNNING' | 'QUEUED' =
                        pct === 100 && scenes.length > 0
                          ? 'COMPLETED'
                          : anyProcessing
                          ? 'RUNNING'
                          : 'QUEUED'

                      return (
                        <tr
                          key={v.id}
                          className="transition-colors hover:bg-white/[0.02]"
                          style={{ borderBottom: '1px solid var(--border)' }}
                        >
                          <td
                            className="py-3 px-3.5 text-xs font-mono text-center"
                            style={{ color: 'var(--muted)' }}
                          >
                            {videoStartIndex + idx + 1}
                          </td>
                          <td className="py-3 px-3.5">
                            <div className="text-xs font-semibold">{v.title}</div>
                            <div className="text-[10px] font-mono" style={{ color: 'var(--muted)' }}>
                              {v.id.slice(0, 8)}
                            </div>
                          </td>
                          <td className="py-3 px-3.5 text-xs" style={{ color: 'var(--muted)' }}>
                            {scenes.length}
                          </td>
                          <td className="py-3 px-3.5">
                            <div className="flex flex-col gap-1" style={{ width: 120 }}>
                              <span className="text-[10px]" style={{ color: 'var(--muted)' }}>
                                {pct}%
                              </span>
                              <Progress value={pct} className="h-1" />
                            </div>
                          </td>
                          <td className="py-3 px-3.5">
                            <Badge
                              variant={
                                state === 'COMPLETED'
                                  ? 'secondary'
                                  : state === 'RUNNING'
                                  ? 'default'
                                  : 'outline'
                              }
                            >
                              {stateLabel(t, state)}
                            </Badge>
                          </td>
                          <td className="py-3 px-3.5 text-right">
                            <span
                              className="text-xs font-semibold cursor-pointer"
                              style={{ color: 'var(--accent)' }}
                              onClick={() => {
                                setPipelineVideoId(v.id)
                                setTab('pipeline')
                              }}
                            >
                              {t('projectDetail.pipelineLink')}
                            </span>
                          </td>
                        </tr>
                      )
                    })}
                  </tbody>
                </table>
              </div>
            )}

            {/* Pagination Footer for Videos */}
            {totalVideoRows > 0 && (
              <div
                className="px-4 py-3 flex flex-wrap items-center justify-between gap-3 text-xs"
                style={{
                  background: 'rgba(255,255,255,0.015)',
                  borderTop: '1px solid var(--border)',
                }}
              >
                <span style={{ color: 'var(--muted)' }}>
                  Hiển thị{' '}
                  <strong style={{ color: 'var(--text)' }}>
                    {videoStartIndex + 1}–{Math.min(videoStartIndex + videoPageSize, totalVideoRows)}
                  </strong>{' '}
                  / <strong style={{ color: 'var(--text)' }}>{totalVideoRows}</strong> tập phim
                </span>

                <div className="flex items-center gap-1.5">
                  <select
                    value={videoPageSize}
                    onChange={e => setVideoPageSize(Number(e.target.value))}
                    className="px-2 py-1 rounded text-xs outline-none cursor-pointer"
                    style={{
                      background: 'var(--bg)',
                      border: '1px solid var(--border)',
                      color: 'var(--text)',
                    }}
                  >
                    <option value={10}>10 / trang</option>
                    <option value={15}>15 / trang</option>
                    <option value={30}>30 / trang</option>
                    <option value={50}>50 / trang</option>
                  </select>
                  <button
                    disabled={safeVideoPage <= 1}
                    onClick={() => setVideoPage(p => Math.max(1, p - 1))}
                    className="px-2.5 py-1 rounded text-xs cursor-pointer disabled:opacity-40"
                    style={{
                      background: 'var(--bg)',
                      border: '1px solid var(--border)',
                      color: 'var(--text)',
                    }}
                  >
                    ‹ Trước
                  </button>
                  <span className="px-2 text-xs font-semibold">
                    Trang {safeVideoPage}/{videoTotalPages}
                  </span>
                  <button
                    disabled={safeVideoPage >= videoTotalPages}
                    onClick={() => setVideoPage(p => Math.min(videoTotalPages, p + 1))}
                    className="px-2.5 py-1 rounded text-xs cursor-pointer disabled:opacity-40"
                    style={{
                      background: 'var(--bg)',
                      border: '1px solid var(--border)',
                      color: 'var(--text)',
                    }}
                  >
                    Sau ›
                  </button>
                </div>
              </div>
            )}
          </div>
        </TabsContent>

        {/* PIPELINE TAB */}
        <TabsContent value="pipeline" className="pt-4">
          {allCmsClips.length > 0 ? (
            <div className="flex flex-col gap-4">
              {/* 4-Stage Pipeline Progress Rail */}
              <div className="grid gap-3" style={{ gridTemplateColumns: 'repeat(4, minmax(0, 1fr))' }}>
                {[
                  {
                    idx: '01',
                    title: 'NHÂN VẬT @TAG (REFS)',
                    sub: 'Media ID khóa cố định',
                    done: stageRollup.refs.done,
                    total: stageRollup.refs.total,
                    color: '#fbbf24',
                  },
                  {
                    idx: '02',
                    title: 'KỊCH BẢN & PROMPTS',
                    sub: 'Prompts cảnh quay Veo 3.1',
                    done: stageRollup.image.done,
                    total: stageRollup.image.total,
                    color: '#60a5fa',
                  },
                  {
                    idx: '03',
                    title: 'RENDER VEO 3.1 CLIPS',
                    sub: 'Xuất MP4 từng cảnh',
                    done: stageRollup.video.done,
                    total: stageRollup.video.total,
                    color: '#34d399',
                  },
                  {
                    idx: '04',
                    title: 'GHÉP TẬP & R2 CDN',
                    sub: 'Full Episode MP4 trên R2',
                    done: stageRollup.upscale.done,
                    total: stageRollup.upscale.total,
                    color: '#38bdf8',
                  },
                ].map(st => {
                  const pct = st.total > 0 ? Math.round((st.done / st.total) * 100) : 0
                  return (
                    <div
                      key={st.idx}
                      className="rounded-xl p-3.5 flex flex-col gap-2"
                      style={{
                        background: 'var(--surface)',
                        border: '1px solid var(--border)',
                      }}
                    >
                      <div className="flex items-center justify-between">
                        <span
                          className="text-[10px] font-mono font-bold px-1.5 py-0.5 rounded"
                          style={{ background: 'rgba(255,255,255,0.05)', color: st.color }}
                        >
                          STAGE {st.idx}
                        </span>
                        <span className="text-xs font-mono font-bold" style={{ color: st.color }}>
                          {st.done}/{st.total} ({pct}%)
                        </span>
                      </div>
                      <div>
                        <div className="text-xs font-bold" style={{ color: 'var(--text)' }}>
                          {st.title}
                        </div>
                        <div className="text-[10px]" style={{ color: 'var(--muted)' }}>
                          {st.sub}
                        </div>
                      </div>
                      <Progress value={pct} className="h-1.5" />
                    </div>
                  )
                })}
              </div>

              {/* Pipeline Clips List Table */}
              <div
                className="rounded-xl overflow-hidden flex flex-col"
                style={{ background: 'var(--surface)', border: '1px solid var(--border)' }}
              >
                {/* Filter Bar */}
                <div
                  className="p-3.5 flex flex-wrap items-center gap-3"
                  style={{ borderBottom: '1px solid var(--border)' }}
                >
                  <div className="flex items-center gap-2">
                    <Layers className="w-4 h-4" style={{ color: '#34d399' }} />
                    <span className="text-xs font-bold" style={{ color: 'var(--text)' }}>
                      Pipeline Cảnh Quay ({filteredPipelineClips.length})
                    </span>
                  </div>

                  {/* Episode Filter Dropdown (<select><option>) */}
                  <div className="flex items-center gap-1.5">
                    <span
                      className="text-[11px] font-semibold uppercase"
                      style={{ color: 'var(--muted)' }}
                    >
                      Tập phim:
                    </span>
                    <select
                      value={pipelineEpisodeFilter}
                      onChange={e => setPipelineEpisodeFilter(e.target.value)}
                      className="px-3 py-1.5 rounded-lg text-xs font-medium outline-none cursor-pointer"
                      style={{
                        background: 'var(--bg)',
                        border: '1px solid var(--border)',
                        color: 'var(--text)',
                      }}
                    >
                      <option value="ALL">
                        📚 Tất cả Tập ({cmsEpisodes.length} tập — {allCmsClips.length} cảnh)
                      </option>
                      {cmsEpisodes.map(ep => (
                        <option key={ep.episode_num} value={String(ep.episode_num)}>
                          🎬 {ep.label} — {ep.folder_name} ({ep.rendered_clips}/{ep.total_clips}{' '}
                          clips)
                        </option>
                      ))}
                    </select>
                  </div>

                  {/* Status Filter Dropdown (<select><option>) */}
                  <div className="flex items-center gap-1.5">
                    <span
                      className="text-[11px] font-semibold uppercase"
                      style={{ color: 'var(--muted)' }}
                    >
                      Trạng thái:
                    </span>
                    <select
                      value={pipelineStatusFilter}
                      onChange={e => setPipelineStatusFilter(e.target.value)}
                      className="px-2.5 py-1.5 rounded-lg text-xs font-medium outline-none cursor-pointer"
                      style={{
                        background: 'var(--bg)',
                        border: '1px solid var(--border)',
                        color: 'var(--text)',
                      }}
                    >
                      <option value="ALL">Tất cả ({allCmsClips.length})</option>
                      <option value="COMPLETED">✅ Đã render MP4 (COMPLETED)</option>
                      <option value="R2">☁️ Đã đồng bộ R2 CDN</option>
                      <option value="PENDING">⏳ Đang chờ render (PENDING)</option>
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
                    <Search className="w-3.5 h-3.5" style={{ color: 'var(--muted)' }} />
                    <input
                      type="text"
                      value={pipelineSearch}
                      onChange={e => setPipelineSearch(e.target.value)}
                      placeholder="Tìm nội dung prompt, @Tag, tập, cảnh..."
                      className="bg-transparent border-none outline-none text-xs w-full"
                      style={{ color: 'var(--text)' }}
                    />
                  </div>
                </div>

                {/* Table */}
                {filteredPipelineClips.length === 0 ? (
                  <div className="p-8 text-center text-xs" style={{ color: 'var(--muted)' }}>
                    Không tìm thấy cảnh quay nào khớp bộ lọc.
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
                          <th className="py-3 px-3.5 w-12 text-center">#</th>
                          <th className="py-3 px-3.5 w-36">Tập & Cảnh</th>
                          <th className="py-3 px-3.5">Kịch Bản / Prompt Veo 3.1</th>
                          <th className="py-3 px-3.5 w-44">Nhân Vật (@Tag)</th>
                          <th className="py-3 px-3.5 w-40">R2 CDN & File</th>
                          <th className="py-3 px-3.5 w-32">Trạng Thái</th>
                          <th className="py-3 px-3.5 text-right w-44">Thao Tác</th>
                        </tr>
                      </thead>
                      <tbody className="divide-y" style={{ borderColor: 'var(--border)' }}>
                        {pagedPipelineClips.map((cl, idx) => {
                          const rowNum = pipelineStartIndex + idx + 1
                          const playUrl =
                            cl.r2_url || (cl.video_url ? resolveApiUrl(cl.video_url) : '')
                          const isPromptCopied = copiedKey === `prompt-${cl.key}`

                          return (
                            <tr
                              key={cl.key}
                              className="transition-colors hover:bg-white/[0.02]"
                              style={{ borderBottom: '1px solid var(--border)' }}
                            >
                              <td
                                className="py-3 px-3.5 text-xs font-mono text-center"
                                style={{ color: 'var(--muted)' }}
                              >
                                {rowNum}
                              </td>

                              {/* Tập & Cảnh */}
                              <td className="py-3 px-3.5">
                                <div className="flex flex-col gap-1">
                                  <div className="flex items-center gap-1.5">
                                    <span
                                      className="px-1.5 py-0.5 rounded text-[10px] font-mono font-bold"
                                      style={{
                                        background: 'rgba(59,130,246,0.14)',
                                        color: '#60a5fa',
                                      }}
                                    >
                                      {cl.episode_label}
                                    </span>
                                    <span
                                      className="px-1.5 py-0.5 rounded text-[10px] font-mono font-bold"
                                      style={{
                                        background: 'rgba(16,185,129,0.14)',
                                        color: '#34d399',
                                      }}
                                    >
                                      Clip {cl.clip_num}
                                    </span>
                                  </div>
                                  <span
                                    className="text-[10px] font-mono truncate max-w-[130px]"
                                    style={{ color: 'var(--muted)' }}
                                    title={cl.folder_name}
                                  >
                                    {cl.folder_name}
                                  </span>
                                </div>
                              </td>

                              {/* Prompt */}
                              <td className="py-3 px-3.5 max-w-[420px]">
                                {cl.prompt ? (
                                  <div
                                    onClick={() => setSelectedPromptModal(cl)}
                                    className="text-[11px] line-clamp-2 cursor-pointer hover: opacity-90"
                                    style={{ color: 'var(--text)' }}
                                    title="Bấm để xem toàn bộ Prompt"
                                  >
                                    {cl.prompt}
                                  </div>
                                ) : (
                                  <span className="text-[11px]" style={{ color: 'var(--muted)' }}>
                                    (Đã đồng bộ MP4 trên R2 CDN)
                                  </span>
                                )}
                              </td>

                              {/* Nhân vật @Tag */}
                              <td className="py-3 px-3.5">
                                <div className="flex flex-wrap gap-1">
                                  {cl.matched_tags.map(tag => (
                                    <span
                                      key={tag}
                                      className="px-1.5 py-0.5 rounded text-[10px] font-mono flex items-center gap-1"
                                      style={{
                                        background: 'rgba(245,158,11,0.12)',
                                        color: '#fbbf24',
                                        border: '1px solid rgba(245,158,11,0.28)',
                                      }}
                                    >
                                      <Lock className="w-2.5 h-2.5" />
                                      {tag}
                                    </span>
                                  ))}
                                </div>
                              </td>

                              {/* R2 CDN & File */}
                              <td className="py-3 px-3.5">
                                {cl.r2_url ? (
                                  <div className="flex flex-col gap-0.5">
                                    <span
                                      className="inline-flex items-center gap-1 px-2 py-0.5 rounded text-[10px] font-medium w-fit"
                                      style={{
                                        background: 'rgba(56,189,248,0.14)',
                                        color: '#38bdf8',
                                      }}
                                    >
                                      <Cloud className="w-3 h-3" /> R2 MP4
                                    </span>
                                    {cl.video_size_mb && (
                                      <span
                                        className="text-[10px] font-mono"
                                        style={{ color: 'var(--muted)' }}
                                      >
                                        {cl.video_size_mb} MB
                                      </span>
                                    )}
                                  </div>
                                ) : (
                                  <span className="text-[11px]" style={{ color: 'var(--muted)' }}>
                                    {cl.video_url ? 'Local MP4' : '—'}
                                  </span>
                                )}
                              </td>

                              {/* Trạng thái */}
                              <td className="py-3 px-3.5">
                                {cl.status === 'COMPLETED' ? (
                                  <span
                                    className="inline-flex items-center gap-1 px-2 py-0.5 rounded text-[10px] font-semibold"
                                    style={{
                                      background: 'rgba(16,185,129,0.14)',
                                      color: '#34d399',
                                    }}
                                  >
                                    <CheckCircle2 className="w-3 h-3" /> COMPLETED
                                  </span>
                                ) : (
                                  <span
                                    className="inline-flex items-center gap-1 px-2 py-0.5 rounded text-[10px] font-semibold"
                                    style={{
                                      background: 'rgba(255,255,255,0.06)',
                                      color: 'var(--muted)',
                                    }}
                                  >
                                    <Clock className="w-3 h-3" /> PENDING
                                  </span>
                                )}
                              </td>

                              {/* Thao tác */}
                              <td className="py-3 px-3.5 text-right">
                                <div className="flex items-center justify-end gap-1.5">
                                  {playUrl && (
                                    <button
                                      onClick={() =>
                                        setPreviewVideo({
                                          title: `${cl.episode_label} · Clip ${cl.clip_num} (${cl.folder_name})`,
                                          url: playUrl,
                                        })
                                      }
                                      className="px-2.5 py-1 rounded text-[11px] font-semibold flex items-center gap-1 cursor-pointer"
                                      style={{
                                        background: 'rgba(16,185,129,0.16)',
                                        color: '#34d399',
                                        border: '1px solid rgba(16,185,129,0.35)',
                                      }}
                                    >
                                      <Play className="w-3 h-3" /> MP4
                                    </button>
                                  )}

                                  {cl.prompt && (
                                    <button
                                      onClick={() => copyText(cl.prompt, `prompt-${cl.key}`)}
                                      className="p-1.5 rounded cursor-pointer"
                                      style={{
                                        background: 'var(--bg)',
                                        border: '1px solid var(--border)',
                                        color: isPromptCopied ? '#34d399' : 'var(--text)',
                                      }}
                                      title="Copy Prompt"
                                    >
                                      {isPromptCopied ? (
                                        <Check className="w-3.5 h-3.5" />
                                      ) : (
                                        <Copy className="w-3.5 h-3.5" />
                                      )}
                                    </button>
                                  )}

                                  {cl.prompt && (
                                    <button
                                      onClick={() => setSelectedPromptModal(cl)}
                                      className="p-1.5 rounded cursor-pointer"
                                      style={{
                                        background: 'var(--bg)',
                                        border: '1px solid var(--border)',
                                        color: 'var(--muted)',
                                      }}
                                      title="Xem chi tiết Prompt"
                                    >
                                      <FileText className="w-3.5 h-3.5" />
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
                )}

                {/* Pagination Footer for Pipeline Clips */}
                {filteredPipelineClips.length > 0 && (
                  <div
                    className="px-4 py-3 flex flex-wrap items-center justify-between gap-3 text-xs"
                    style={{
                      background: 'rgba(255,255,255,0.015)',
                      borderTop: '1px solid var(--border)',
                    }}
                  >
                    <span style={{ color: 'var(--muted)' }}>
                      Hiển thị{' '}
                      <strong style={{ color: 'var(--text)' }}>
                        {pipelineStartIndex + 1}–
                        {Math.min(
                          pipelineStartIndex + pipelinePageSize,
                          filteredPipelineClips.length
                        )}
                      </strong>{' '}
                      trên tổng số{' '}
                      <strong style={{ color: 'var(--text)' }}>
                        {filteredPipelineClips.length}
                      </strong>{' '}
                      cảnh quay
                    </span>

                    <div className="flex items-center gap-1.5">
                      <select
                        value={pipelinePageSize}
                        onChange={e => setPipelinePageSize(Number(e.target.value))}
                        className="px-2 py-1 rounded text-xs outline-none cursor-pointer"
                        style={{
                          background: 'var(--bg)',
                          border: '1px solid var(--border)',
                          color: 'var(--text)',
                        }}
                      >
                        <option value={10}>10 / trang</option>
                        <option value={15}>15 / trang</option>
                        <option value={30}>30 / trang</option>
                        <option value={50}>50 / trang</option>
                      </select>

                      <button
                        disabled={safePipelinePage <= 1}
                        onClick={() => setPipelinePage(1)}
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
                        disabled={safePipelinePage <= 1}
                        onClick={() => setPipelinePage(p => Math.max(1, p - 1))}
                        className="px-2.5 py-1 rounded text-xs cursor-pointer disabled:opacity-40"
                        style={{
                          background: 'var(--bg)',
                          border: '1px solid var(--border)',
                          color: 'var(--text)',
                        }}
                      >
                        ‹ Trước
                      </button>
                      <span className="px-2 text-xs font-semibold">
                        Trang {safePipelinePage}/{pipelineTotalPages}
                      </span>
                      <button
                        disabled={safePipelinePage >= pipelineTotalPages}
                        onClick={() => setPipelinePage(p => Math.min(pipelineTotalPages, p + 1))}
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
                        disabled={safePipelinePage >= pipelineTotalPages}
                        onClick={() => setPipelinePage(pipelineTotalPages)}
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
          ) : videos.length === 0 ? (
            <div
              className="rounded-xl p-6 flex flex-col items-center justify-center gap-3 text-center"
              style={{ background: 'var(--surface)', border: '1px solid var(--border)' }}
            >
              <span className="text-xs" style={{ color: 'var(--muted)' }}>
                {t('projectDetail.pipeline.noVideos')}
              </span>
              {cmsChannel?.slug && (
                <Button
                  variant="default"
                  size="sm"
                  onClick={() => navigate(`/channels/${cmsChannel.slug}`)}
                >
                  <Tv className="w-3.5 h-3.5 mr-1.5" />
                  Mở Studio Kênh Series ({cmsChannel.name})
                </Button>
              )}
            </div>
          ) : (
            <div className="flex flex-col gap-4">
              <div className="flex items-center gap-2">
                <span className="text-[11px] font-semibold" style={{ color: 'var(--muted)' }}>
                  {t('projectDetail.pipeline.videoLabel')}
                </span>
                <select
                  value={pipelineVideoId}
                  onChange={e => setPipelineVideoId(e.target.value)}
                  className="px-3 py-1.5 rounded-lg text-xs font-medium outline-none cursor-pointer"
                  style={{
                    background: 'var(--surface)',
                    border: '1px solid var(--border)',
                    color: 'var(--text)',
                  }}
                >
                  {videos.map(v => (
                    <option key={v.id} value={v.id}>
                      {v.title}
                    </option>
                  ))}
                </select>
              </div>
              {pipelineVideoId && <PipelineView projectId={projectId} videoId={pipelineVideoId} />}
            </div>
          )}
        </TabsContent>
      </Tabs>

      {/* Prompt Detail Modal */}
      {selectedPromptModal && (
        <div
          className="fixed inset-0 z-50 flex items-center justify-center p-4"
          style={{ background: 'rgba(0,0,0,0.82)' }}
          onClick={() => setSelectedPromptModal(null)}
        >
          <div
            className="rounded-xl overflow-hidden max-w-2xl w-full flex flex-col"
            style={{ background: 'var(--surface)', border: '1px solid var(--border)' }}
            onClick={e => e.stopPropagation()}
          >
            <div
              className="px-4 py-3 flex items-center justify-between"
              style={{ borderBottom: '1px solid var(--border)' }}
            >
              <div className="flex items-center gap-2">
                <span className="text-xs font-bold" style={{ color: 'var(--text)' }}>
                  {selectedPromptModal.episode_label} · Clip {selectedPromptModal.clip_num} (
                  {selectedPromptModal.folder_name})
                </span>
              </div>
              <button
                onClick={() => setSelectedPromptModal(null)}
                className="p-1 rounded cursor-pointer hover:bg-white/10"
                style={{ color: 'var(--muted)' }}
              >
                <X className="w-4 h-4" />
              </button>
            </div>
            <div className="p-4 flex flex-col gap-3">
              <pre
                className="m-0 p-3 rounded-lg text-xs whitespace-pre-wrap font-mono max-h-[60vh] overflow-y-auto"
                style={{
                  background: 'var(--bg)',
                  border: '1px solid var(--border)',
                  color: 'var(--text)',
                }}
              >
                {selectedPromptModal.prompt}
              </pre>
              <div className="flex items-center justify-end gap-2">
                <Button
                  variant="outline"
                  size="sm"
                  onClick={() => copyText(selectedPromptModal.prompt, 'modal-prompt')}
                >
                  {copiedKey === 'modal-prompt' ? (
                    <>
                      <Check className="w-3.5 h-3.5 mr-1.5" /> Đã copy Prompt
                    </>
                  ) : (
                    <>
                      <Copy className="w-3.5 h-3.5 mr-1.5" /> Copy Prompt
                    </>
                  )}
                </Button>
                <Button size="sm" onClick={() => setSelectedPromptModal(null)}>
                  Đóng
                </Button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* On-Demand Video Modal (No Preload in Table) */}
      {previewVideo && (
        <div
          className="fixed inset-0 z-50 flex items-center justify-center p-4"
          style={{ background: 'rgba(0,0,0,0.82)' }}
          onClick={() => setPreviewVideo(null)}
        >
          <div
            className="rounded-xl overflow-hidden max-w-3xl w-full flex flex-col"
            style={{ background: 'var(--surface)', border: '1px solid var(--border)' }}
            onClick={e => e.stopPropagation()}
          >
            <div
              className="px-4 py-3 flex items-center justify-between"
              style={{ borderBottom: '1px solid var(--border)' }}
            >
              <span className="text-xs font-bold" style={{ color: 'var(--text)' }}>
                {previewVideo.title}
              </span>
              <button
                onClick={() => setPreviewVideo(null)}
                className="p-1 rounded cursor-pointer hover:bg-white/10"
                style={{ color: 'var(--muted)' }}
              >
                <X className="w-4 h-4" />
              </button>
            </div>
            <div className="p-4 flex items-center justify-center bg-black">
              <video
                src={previewVideo.url}
                controls
                autoPlay
                playsInline
                className="max-h-[75vh] w-auto rounded"
              />
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
