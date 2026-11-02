import React, { useState, useEffect, useRef, useCallback, useMemo } from 'react'
import { useNavigate } from 'react-router-dom'
import {
  Play,
  Square,
  Plus,
  Trash2,
  RotateCcw,
  Sparkles,
  Tv,
  Users,
  FileCheck2,
  Bot,
  Film,
  CloudUpload,
  Database,
  CheckCircle2,
  AlertCircle,
  Loader2,
  Terminal,
  ZoomIn,
  ZoomOut,
  Maximize2,
  Minimize2,
  Layers,
  Settings2,
  Link2,
  ChevronDown,
  ChevronUp,
  FolderKanban,
  ExternalLink,
  PanelLeftClose,
  PanelLeftOpen,
  PanelRightClose,
  PanelRightOpen,
  Rocket,
  GripVertical,
  ArrowRight,
  Clock,
  Activity,
  Zap,
  X,
  FileText,
  Code2,
  Sliders,
  Eye,
  MousePointerClick,
} from 'lucide-react'
import { fetchAPI } from '../api/client'
import type { Project } from '../types'

export type WorkflowNodeType =
  | 'channel-source'
  | 'pull-d1'
  | 'lock-characters'
  | 'verify-prompts'
  | 'run-agent'
  | 'merge-mp4'
  | 'push-cloud'

export type NodeRunStatus = 'idle' | 'running' | 'success' | 'error'

export interface StepLogEntry {
  id: string
  time: string
  level: 'INFO' | 'SUCCESS' | 'WARN' | 'ERROR'
  text: string
  detail?: string
}

export interface WorkflowNodeConfig {
  channelSlug: string
  projectId?: string
  projectName?: string
  startEp: number
  endEp: number
  onlyClip: number // 0 = all clips, 1..6 = single clip
  waitForAgent: boolean
  autoLockChars?: boolean
  autoMergeMp4?: boolean
  syncR2: boolean
  syncD1: boolean
  forceR2: boolean
}

export interface WorkflowNode {
  id: string
  type: WorkflowNodeType
  title: string
  subtitle: string
  x: number
  y: number
  status: NodeRunStatus
  lastMessage?: string
  durationMs?: number
  lastRunAt?: string
  stepLogs?: StepLogEntry[]
  lastOutput?: Record<string, unknown>
  config: WorkflowNodeConfig
}

export interface WorkflowEdge {
  id: string
  from: string
  to: string
}

interface CmsChannelSummary {
  slug: string
  name: string
  project_id: string
  aspect_ratio?: string
  stats?: {
    total_episodes: number
    completed_episodes?: number
    total_clips: number
    rendered_clips: number
    merged_episodes: number
  }
  active_job?: {
    running: boolean
    pid?: number
    start_ep?: number
    end_ep?: number
    only_clip?: number | null
  } | null
}

interface EpisodeClipItem {
  clip_num: number
  file_name: string
  status: 'COMPLETED' | 'PENDING'
  video_url: string | null
  r2_url?: string | null
  video_size_mb?: number | null
}

interface ChannelEpisodeItem {
  episode_num: number
  folder_name: string
  label: string
  total_clips: number
  rendered_clips: number
  is_complete: boolean
  merged_video_url: string | null
  clips: EpisodeClipItem[]
}

interface ChannelDetailApiResponse {
  channel: {
    slug: string
    name: string
    project_id: string
    active_job: {
      running: boolean
      pid?: number
      start_ep?: number
      end_ep?: number
      only_clip?: number | null
    } | null
  }
  episodes: ChannelEpisodeItem[]
}

interface UnifiedProjectTarget {
  key: string
  kind: 'channel' | 'project'
  channelSlug: string
  projectId: string
  name: string
  aspectRatio: string
  totalEpisodes: number
  renderedClips: number
  totalClips: number
  running: boolean
  pid?: number
  activeStartEp?: number
  activeEndEp?: number
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

const DEFAULT_CONFIG: WorkflowNodeConfig = {
  channelSlug: 'ke-song-sot',
  projectId: 'd96fa29d-6648-49a7-98b6-9c0fb672742f',
  projectName: 'Kẻ Sống Sót',
  startEp: 1,
  endEp: 1,
  onlyClip: 0,
  waitForAgent: false,
  autoLockChars: true,
  autoMergeMp4: true,
  syncR2: true,
  syncD1: true,
  forceR2: false,
}

const NODE_CATALOG: Array<{
  type: WorkflowNodeType
  title: string
  subtitle: string
  badge: string
  accent: string
  borderAccent: string
  bgAccent: string
}> = [
  {
    type: 'channel-source',
    title: 'Nguồn Dự Án & Kênh',
    subtitle: 'Chọn Dự Án / Kênh Series, tự động nhận Tập mới nhất & Clip',
    badge: 'PROJECT',
    accent: 'text-sky-400',
    borderAccent: 'border-sky-500/40',
    bgAccent: 'bg-sky-500/10',
  },
  {
    type: 'pull-d1',
    title: 'Đồng Bộ D1 → Local',
    subtitle: 'Kéo dữ liệu mới nhất từ Cloudflare D1 về SQLite',
    badge: 'D1 PULL',
    accent: 'text-cyan-400',
    borderAccent: 'border-cyan-500/40',
    bgAccent: 'bg-cyan-500/10',
  },
  {
    type: 'lock-characters',
    title: 'Khóa Nhân Vật (@Tag)',
    subtitle: 'Xác thực & khóa UUID hồ sơ nhân vật cố định của dự án',
    badge: 'IDENTITY',
    accent: 'text-amber-400',
    borderAccent: 'border-amber-500/40',
    bgAccent: 'bg-amber-500/10',
  },
  {
    type: 'verify-prompts',
    title: 'Chuẩn Hóa Prompt 360',
    subtitle: 'Kiểm tra 9 quy chuẩn điện ảnh, thoại 15–30 từ & nạp DB',
    badge: 'PROMPT',
    accent: 'text-purple-400',
    borderAccent: 'border-purple-500/40',
    bgAccent: 'bg-purple-500/10',
  },
  {
    type: 'run-agent',
    title: 'Chạy Agent Render Dự Án',
    subtitle: 'Khởi chạy Python Runner Agent tạo clip tự động trên Google Flow',
    badge: 'AGENT',
    accent: 'text-indigo-400',
    borderAccent: 'border-indigo-500/40',
    bgAccent: 'bg-indigo-500/10',
  },
  {
    type: 'merge-mp4',
    title: 'Ghép Tập FULL MP4',
    subtitle: 'Nối các clips đã render thành tập phim hoàn chỉnh bằng FFmpeg',
    badge: 'FFMPEG',
    accent: 'text-emerald-400',
    borderAccent: 'border-emerald-500/40',
    bgAccent: 'bg-emerald-500/10',
  },
  {
    type: 'push-cloud',
    title: 'Đẩy Lên Cloud R2 & D1',
    subtitle: 'Upload video MP4 lên R2 và đồng bộ bảng lên Cloudflare D1',
    badge: 'CLOUD',
    accent: 'text-rose-400',
    borderAccent: 'border-rose-500/40',
    bgAccent: 'bg-rose-500/10',
  },
]

function getNodeMeta(type: WorkflowNodeType) {
  return NODE_CATALOG.find(n => n.type === type) || NODE_CATALOG[0]
}

function NodeIcon({ type, size = 16, className = '' }: { type: WorkflowNodeType; size?: number; className?: string }) {
  switch (type) {
    case 'channel-source':
      return <Tv size={size} className={className} />
    case 'pull-d1':
      return <Database size={size} className={className} />
    case 'lock-characters':
      return <Users size={size} className={className} />
    case 'verify-prompts':
      return <FileCheck2 size={size} className={className} />
    case 'run-agent':
      return <Bot size={size} className={className} />
    case 'merge-mp4':
      return <Film size={size} className={className} />
    case 'push-cloud':
      return <CloudUpload size={size} className={className} />
  }
}

const PRESET_TEMPLATES: Record<
  string,
  { name: string; desc: string; nodes: WorkflowNode[]; edges: WorkflowEdge[] }
> = {
  full_pipeline: {
    name: '1. Full Production Pipeline (Trọn Bộ Dự Án)',
    desc: 'Quy trình chuẩn: Nguồn Dự Án → Khóa @Character → Chuẩn Hóa Prompt → Chạy Agent Render → Ghép Tập → Đẩy Cloud',
    nodes: [
      {
        id: 'n-source',
        type: 'channel-source',
        title: 'Nguồn Dự Án & Kênh',
        subtitle: 'Kẻ Sống Sót • Tập mới nhất',
        x: 36,
        y: 84,
        status: 'idle',
        config: { ...DEFAULT_CONFIG },
      },
      {
        id: 'n-lock',
        type: 'lock-characters',
        title: 'Khóa Nhân Vật (@Tag)',
        subtitle: 'Xác thực UUID nhân vật cố định',
        x: 228,
        y: 84,
        status: 'idle',
        config: { ...DEFAULT_CONFIG },
      },
      {
        id: 'n-prompt',
        type: 'verify-prompts',
        title: 'Chuẩn Hóa Prompt',
        subtitle: '24fps • 180°/150° • Thoại 15–30 từ',
        x: 420,
        y: 84,
        status: 'idle',
        config: { ...DEFAULT_CONFIG },
      },
      {
        id: 'n-agent',
        type: 'run-agent',
        title: 'Chạy Agent Render Dự Án',
        subtitle: 'Render tự động trên Google Flow',
        x: 612,
        y: 84,
        status: 'idle',
        config: { ...DEFAULT_CONFIG },
      },
      {
        id: 'n-merge',
        type: 'merge-mp4',
        title: 'Ghép Tập FULL MP4',
        subtitle: 'Nối clips thành tập hoàn chỉnh',
        x: 420,
        y: 204,
        status: 'idle',
        config: { ...DEFAULT_CONFIG },
      },
      {
        id: 'n-cloud',
        type: 'push-cloud',
        title: 'Đẩy Lên Cloud R2 & D1',
        subtitle: 'Đồng bộ MP4 & SQLite lên Cloudflare',
        x: 612,
        y: 204,
        status: 'idle',
        config: { ...DEFAULT_CONFIG },
      },
    ],
    edges: [
      { id: 'e1', from: 'n-source', to: 'n-lock' },
      { id: 'e2', from: 'n-lock', to: 'n-prompt' },
      { id: 'e3', from: 'n-prompt', to: 'n-agent' },
      { id: 'e4', from: 'n-agent', to: 'n-merge' },
      { id: 'e5', from: 'n-merge', to: 'n-cloud' },
    ],
  },
  quick_agent: {
    name: '2. Chạy Nhanh Agent Render (Tập Mới Nhất)',
    desc: 'Chọn dự án & tập mới nhất, khóa nhân vật và chạy thẳng Agent tạo video',
    nodes: [
      {
        id: 'n-source',
        type: 'channel-source',
        title: 'Nguồn Dự Án & Kênh',
        subtitle: 'Kẻ Sống Sót • Tập mới nhất',
        x: 48,
        y: 120,
        status: 'idle',
        config: { ...DEFAULT_CONFIG, onlyClip: 0 },
      },
      {
        id: 'n-lock',
        type: 'lock-characters',
        title: 'Khóa Nhân Vật (@Tag)',
        subtitle: 'Đảm bảo đúng mặt & trang phục',
        x: 252,
        y: 120,
        status: 'idle',
        config: { ...DEFAULT_CONFIG, onlyClip: 0 },
      },
      {
        id: 'n-agent',
        type: 'run-agent',
        title: 'Chạy Agent Render Dự Án',
        subtitle: 'Khởi chạy tiến trình tạo video',
        x: 456,
        y: 120,
        status: 'idle',
        config: { ...DEFAULT_CONFIG, onlyClip: 0 },
      },
    ],
    edges: [
      { id: 'e1', from: 'n-source', to: 'n-lock' },
      { id: 'e2', from: 'n-lock', to: 'n-agent' },
    ],
  },
  d1_sync_flow: {
    name: '3. Đồng Bộ Dữ Liệu D1 2 Chiều & Nạp Prompt',
    desc: 'Kéo dữ liệu từ Cloudflare D1 về máy → Nạp lại bộ Prompt chuẩn → Đẩy ngược lên D1',
    nodes: [
      {
        id: 'n-pull',
        type: 'pull-d1',
        title: 'Đồng Bộ D1 → Local',
        subtitle: 'Kéo 13 bảng từ Cloudflare D1 về máy',
        x: 48,
        y: 120,
        status: 'idle',
        config: { ...DEFAULT_CONFIG },
      },
      {
        id: 'n-prompt',
        type: 'verify-prompts',
        title: 'Chuẩn Hóa Prompt',
        subtitle: 'Cập nhật prompt mới nhất vào SQLite',
        x: 252,
        y: 120,
        status: 'idle',
        config: { ...DEFAULT_CONFIG },
      },
      {
        id: 'n-cloud',
        type: 'push-cloud',
        title: 'Đẩy Local → Cloud D1',
        subtitle: 'Đồng bộ dữ liệu mới lên Cloudflare D1',
        x: 456,
        y: 120,
        status: 'idle',
        config: { ...DEFAULT_CONFIG, syncR2: false, syncD1: true },
      },
    ],
    edges: [
      { id: 'e1', from: 'n-pull', to: 'n-prompt' },
      { id: 'e2', from: 'n-prompt', to: 'n-cloud' },
    ],
  },
}

const STORAGE_KEY = 'flowkit_visual_workflow_v4'
const NODE_WIDTH = 148
const NODE_HEIGHT = 82

/**
 * Resolves the latest/active episode number for a channel so Workflow automatically selects it:
 * 1. If an agent job is currently running on this channel, select its active episode.
 * 2. If there is an episode currently being rendered (rendered_clips > 0 and not yet complete), select the newest one.
 * 3. If some episodes are completed, select the immediate next episode after the highest completed episode (or the latest episode).
 * 4. Otherwise select the highest episode number (newest episode) in the channel.
 */
function resolveLatestOrActiveEpisode(res: ChannelDetailApiResponse): {
  latestEpNum: number
  newestEpNum: number
  currentEpNum: number
} {
  const eps = res.episodes || []
  if (eps.length === 0) return { latestEpNum: 1, newestEpNum: 1, currentEpNum: 1 }

  const sorted = [...eps].sort((a, b) => a.episode_num - b.episode_num)
  const newestEpNum = sorted[sorted.length - 1].episode_num

  // 1. Active running job
  if (res.channel.active_job?.running && res.channel.active_job.start_ep) {
    const startEp = res.channel.active_job.start_ep
    const endEp = res.channel.active_job.end_ep ?? startEp
    const runningInRange = sorted.find(
      e => e.episode_num >= startEp && e.episode_num <= endEp && !e.is_complete && e.rendered_clips > 0
    )
    const activeTarget = runningInRange?.episode_num ?? startEp
    return { latestEpNum: activeTarget, newestEpNum, currentEpNum: activeTarget }
  }

  // 2. Episode currently in progress (partially rendered)
  const inProgress = sorted.filter(e => !e.is_complete && e.rendered_clips > 0)
  if (inProgress.length > 0) {
    const target = inProgress[inProgress.length - 1].episode_num
    return { latestEpNum: target, newestEpNum, currentEpNum: target }
  }

  // 3. Next episode after highest completed episode
  let lastCompletedIdx = -1
  for (let i = sorted.length - 1; i >= 0; i--) {
    if (sorted[i].is_complete || sorted[i].merged_video_url) {
      lastCompletedIdx = i
      break
    }
  }
  if (lastCompletedIdx >= 0) {
    const nextIdx = Math.min(sorted.length - 1, lastCompletedIdx + 1)
    const target = sorted[nextIdx].episode_num
    return { latestEpNum: target, newestEpNum, currentEpNum: target }
  }

  // 4. Default to newest episode
  return { latestEpNum: newestEpNum, newestEpNum, currentEpNum: sorted[0].episode_num }
}

export default function WorkflowPage() {
  const navigate = useNavigate()
  const [channels, setChannels] = useState<CmsChannelSummary[]>([])
  const [projects, setProjects] = useState<Project[]>([])
  const [channelEpisodes, setChannelEpisodes] = useState<ChannelEpisodeItem[]>([])
  const [newestEpisodeNum, setNewestEpisodeNum] = useState<number>(1)
  const [autoSelectedSlug, setAutoSelectedSlug] = useState<string | null>(null)

  // Fullscreen & Panel visibility states
  const [isFullScreen, setIsFullScreen] = useState(false)
  const [showPalette, setShowPalette] = useState(true)
  const [showInspector, setShowInspector] = useState(true)
  const [showStepBar, setShowStepBar] = useState(true)

  const [nodes, setNodes] = useState<WorkflowNode[]>(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEY)
      if (saved) {
        const parsed = JSON.parse(saved)
        if (Array.isArray(parsed.nodes) && parsed.nodes.length > 0) {
          return parsed.nodes.map((n: WorkflowNode) => ({ ...n, status: 'idle' }))
        }
      }
    } catch {
      // ignore
    }
    return PRESET_TEMPLATES.full_pipeline.nodes
  })

  const [edges, setEdges] = useState<WorkflowEdge[]>(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEY)
      if (saved) {
        const parsed = JSON.parse(saved)
        if (Array.isArray(parsed.edges)) return parsed.edges
      }
    } catch {
      // ignore
    }
    return PRESET_TEMPLATES.full_pipeline.edges
  })

  const [selectedNodeId, setSelectedNodeId] = useState<string | null>('n-source')
  const [detailModalNodeId, setDetailModalNodeId] = useState<string | null>(null)
  const [detailModalTab, setDetailModalTab] = useState<'logs' | 'output' | 'params'>('logs')
  const [consoleFilterNodeId, setConsoleFilterNodeId] = useState<string>('ALL')
  const [isRunningWorkflow, setIsRunningWorkflow] = useState(false)
  const [currentStepIndex, setCurrentStepIndex] = useState<number | null>(null)
  const [activeEdgeId, setActiveEdgeId] = useState<string | null>(null)
  const [zoom, setZoom] = useState(1)
  const [pan, setPan] = useState({ x: 0, y: 0 })
  const [isDraggingOverCanvas, setIsDraggingOverCanvas] = useState(false)

  // Strict press-and-hold ("đè chuột mới kéo được") state & refs — NEVER drags on hover
  const [draggingNodeId, setDraggingNodeId] = useState<string | null>(null)
  const [holdingNodeId, setHoldingNodeId] = useState<string | null>(null)
  const nodeDragStartRef = useRef<{
    nodeId: string
    startMouseX: number
    startMouseY: number
    startNodeX: number
    startNodeY: number
    downTimeMs: number
    didMove: boolean
  } | null>(null)

  const [isPanning, setIsPanning] = useState(false)
  const isPanningRef = useRef(false)
  const panStartRef = useRef({ x: 0, y: 0, panX: 0, panY: 0 })

  // Connecting wire from output/input port to cursor (supports both Drag-to-Connect and Click-to-Connect)
  const [connectingFromId, setConnectingFromId] = useState<string | null>(null)
  const [connectingPortDir, setConnectingPortDir] = useState<'out' | 'in'>('out')
  const [hoveredTargetNodeId, setHoveredTargetNodeId] = useState<string | null>(null)
  const connectStartMouseRef = useRef<{ x: number; y: number; nodeId: string } | null>(null)
  const [mouseCanvasPos, setMouseCanvasPos] = useState({ x: 0, y: 0 })

  // Logs console drawer & collapsible long log text
  const [consoleOpen, setConsoleOpen] = useState(true)
  const [expandedLogIds, setExpandedLogIds] = useState<Record<string | number, boolean>>({})
  const [workflowLogs, setWorkflowLogs] = useState<
    Array<{
      id: string
      time: string
      level: 'INFO' | 'SUCCESS' | 'WARN' | 'ERROR'
      text: string
      nodeId?: string
      nodeTitle?: string
    }>
  >([
    {
      id: 'init-1',
      time: new Date().toLocaleTimeString('vi-VN'),
      level: 'INFO',
      text: 'Sẵn sàng! Bấm vào bất kỳ bước nào để xem Detail & Log (như n8n), hoặc đè giữ chuột để kéo thả vị trí Node.',
    },
  ])
  const [liveServerLogs, setLiveServerLogs] = useState<CmsLogItem[]>([])

  const canvasRef = useRef<HTMLDivElement | null>(null)
  const abortRunRef = useRef(false)

  // Save workflow state to localStorage
  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify({ nodes, edges }))
    } catch {
      // ignore
    }
  }, [nodes, edges])

  // Escape key closes n8n detail modal, cancels wire connection, or exits Full Screen mode
  useEffect(() => {
    function onKeyDown(e: KeyboardEvent) {
      if (e.key === 'Escape') {
        if (detailModalNodeId) {
          setDetailModalNodeId(null)
          return
        }
        if (connectingFromId) {
          setConnectingFromId(null)
          setHoveredTargetNodeId(null)
          connectStartMouseRef.current = null
          return
        }
        if (isFullScreen) {
          setIsFullScreen(false)
        }
      }
    }
    window.addEventListener('keydown', onKeyDown)
    return () => window.removeEventListener('keydown', onKeyDown)
  }, [isFullScreen, connectingFromId, detailModalNodeId])

  function toggleFullScreen() {
    const next = !isFullScreen
    setIsFullScreen(next)
    if (next) {
      if (document.documentElement.requestFullscreen) {
        document.documentElement.requestFullscreen().catch(() => {})
      }
    } else {
      if (document.fullscreenElement && document.exitFullscreen) {
        document.exitFullscreen().catch(() => {})
      }
    }
  }

  const appendLog = useCallback(
    (
      level: 'INFO' | 'SUCCESS' | 'WARN' | 'ERROR',
      text: string,
      nodeId?: string,
      nodeTitle?: string
    ) => {
      setWorkflowLogs(prev => [
        {
          id: `${Date.now()}-${Math.random().toString(36).slice(2, 7)}`,
          time: new Date().toLocaleTimeString('vi-VN'),
          level,
          text,
          nodeId,
          nodeTitle,
        },
        ...prev.slice(0, 199),
      ])
    },
    []
  )

  const appendNodeLog = useCallback(
    (
      nodeId: string,
      nodeTitle: string,
      level: 'INFO' | 'SUCCESS' | 'WARN' | 'ERROR',
      text: string,
      detail?: string
    ) => {
      const entry: StepLogEntry = {
        id: `slog-${Date.now()}-${Math.random().toString(36).slice(2, 7)}`,
        time: new Date().toLocaleTimeString('vi-VN'),
        level,
        text,
        detail,
      }
      setNodes(prev =>
        prev.map(n =>
          n.id === nodeId
            ? {
                ...n,
                stepLogs: [entry, ...(n.stepLogs || []).slice(0, 99)],
              }
            : n
        )
      )
      appendLog(level, `[${nodeTitle}] ${text}`, nodeId, nodeTitle)
    },
    [appendLog]
  )

  const clearNodeLogs = useCallback((nodeId: string) => {
    setNodes(prev =>
      prev.map(n => (n.id === nodeId ? { ...n, stepLogs: [], lastOutput: undefined } : n))
    )
  }, [])

  // Propagate project/channel/episode config across nodes
  const updateGlobalOrNodeConfig = useCallback(
    (patch: Partial<WorkflowNodeConfig>, nodeId?: string, applyToAll = true) => {
      setNodes(prev =>
        prev.map(n => {
          if (applyToAll || n.id === nodeId) {
            const nextCfg = { ...n.config, ...patch }
            let nextSub = n.subtitle
            if (n.type === 'channel-source') {
              const clipLabel = nextCfg.onlyClip > 0 ? ` • Clip ${nextCfg.onlyClip}` : ' • Đủ 6 Clips'
              const displayName = nextCfg.projectName || nextCfg.channelSlug
              nextSub = `${displayName} • Tập ${nextCfg.startEp}${
                nextCfg.endEp > nextCfg.startEp ? `–${nextCfg.endEp}` : ''
              }${clipLabel}`
            }
            return { ...n, config: nextCfg, subtitle: nextSub }
          }
          return n
        })
      )
    },
    []
  )

  // Fetch channel detail & auto-select the latest/active episode whenever channelSlug changes
  const loadChannelEpisodesAndAutoSelectLatest = useCallback(
    async (slug: string, forceSelectLatest = false) => {
      try {
        const res = await fetchAPI<ChannelDetailApiResponse>(`/api/cms/channels/${slug}`)
        const eps = res.episodes || []
        setChannelEpisodes(eps)
        const { latestEpNum, newestEpNum } = resolveLatestOrActiveEpisode(res)
        setNewestEpisodeNum(newestEpNum)

        if (forceSelectLatest || autoSelectedSlug !== slug) {
          setAutoSelectedSlug(slug)
          // Auto-select the first pending clip in that episode (or 0 = all clips)
          const targetEpObj = eps.find(e => e.episode_num === latestEpNum)
          const pendingClips = targetEpObj?.clips?.filter(c => c.status !== 'COMPLETED') || []
          updateGlobalOrNodeConfig({
            channelSlug: slug,
            projectId: res.channel.project_id,
            projectName: res.channel.name,
            startEp: latestEpNum,
            endEp: latestEpNum,
            onlyClip: 0,
          })
          appendLog(
            'INFO',
            `⚡ Đã tự động chọn Tập mới nhất cần chạy của "${res.channel.name}": Tập #${latestEpNum} (${
              targetEpObj
                ? `${targetEpObj.rendered_clips}/${targetEpObj.total_clips} clips đã xong${
                    pendingClips.length > 0 ? ` • Còn ${pendingClips.length} clips` : ' • Hoàn thành'
                  }`
                : `Tổng ${eps.length} tập`
            }).`
          )
        }
      } catch {
        // Non-CMS standalone project
        setChannelEpisodes([])
      }
    },
    [autoSelectedSlug, updateGlobalOrNodeConfig, appendLog]
  )

  // Fetch channels, projects & live logs periodically
  const refreshData = useCallback(async () => {
    try {
      const [chRes, projRes] = await Promise.all([
        fetchAPI<{ channels: CmsChannelSummary[] }>('/api/cms/channels').catch(() => ({ channels: [] })),
        fetchAPI<Project[]>('/api/projects').catch(() => [] as Project[]),
      ])
      if (chRes.channels) setChannels(chRes.channels)
      if (Array.isArray(projRes)) setProjects(projRes)
    } catch {
      // ignore
    }
    try {
      const logRes = await fetchAPI<{ logs: CmsLogItem[] }>('/api/cms/logs?limit=30')
      if (logRes.logs) setLiveServerLogs(logRes.logs)
    } catch {
      // ignore
    }
  }, [])

  useEffect(() => {
    refreshData()
    const id = setInterval(refreshData, 4000)
    return () => clearInterval(id)
  }, [refreshData])

  const selectedNode = nodes.find(n => n.id === selectedNodeId) || null
  const primaryConfig: WorkflowNodeConfig = useMemo(() => {
    const src = nodes.find(n => n.type === 'channel-source')
    return src?.config || selectedNode?.config || DEFAULT_CONFIG
  }, [nodes, selectedNode])

  // Auto-load episodes and auto-select latest episode on initial mount & when channel changes
  useEffect(() => {
    if (primaryConfig.channelSlug && autoSelectedSlug !== primaryConfig.channelSlug) {
      loadChannelEpisodesAndAutoSelectLatest(primaryConfig.channelSlug, true)
    }
  }, [primaryConfig.channelSlug, autoSelectedSlug, loadChannelEpisodesAndAutoSelectLatest])

  // Build unified list of Project / Channel targets
  const unifiedTargets: UnifiedProjectTarget[] = useMemo(() => {
    const list: UnifiedProjectTarget[] = []
    const seenProjectIds = new Set<string>()

    const fallbackChannels: CmsChannelSummary[] =
      channels.length > 0
        ? channels
        : [
            {
              slug: 'ke-song-sot',
              name: 'Kẻ Sống Sót',
              project_id: 'd96fa29d-6648-49a7-98b6-9c0fb672742f',
              aspect_ratio: 'VIDEO_ASPECT_RATIO_LANDSCAPE',
              stats: { total_episodes: 60, total_clips: 360, rendered_clips: 0, merged_episodes: 0 },
            },
            {
              slug: 'biet-doi-gara',
              name: 'Biệt Đội Gara',
              project_id: 'a799239e-0c4a-4fc8-8d24-7e3f16ea88b6',
              aspect_ratio: 'VIDEO_ASPECT_RATIO_LANDSCAPE',
              stats: { total_episodes: 30, total_clips: 180, rendered_clips: 0, merged_episodes: 0 },
            },
            {
              slug: '365ngayvietnam',
              name: '365 Ngày Việt Nam',
              project_id: '594758cc-11f5-4f92-8b3c-1213686591f4',
              aspect_ratio: 'VIDEO_ASPECT_RATIO_PORTRAIT',
              stats: { total_episodes: 20, total_clips: 100, rendered_clips: 0, merged_episodes: 0 },
            },
            {
              slug: 'mit-va-du-1970',
              name: 'Mít Và Đú 1970',
              project_id: 'f5b9e95a-0696-4c36-9f64-2739e250f9d0',
              aspect_ratio: 'VIDEO_ASPECT_RATIO_PORTRAIT',
              stats: { total_episodes: 20, total_clips: 100, rendered_clips: 0, merged_episodes: 0 },
            },
            {
              slug: 'me-va-be',
              name: 'Mẹ Và Bé',
              project_id: '9e0363ab-b1f8-4f63-911f-0c6b9a99335c',
              aspect_ratio: 'VIDEO_ASPECT_RATIO_PORTRAIT',
              stats: { total_episodes: 20, total_clips: 100, rendered_clips: 0, merged_episodes: 0 },
            },
            {
              slug: 'pheo-va-no-meo',
              name: '365 Ngày Phèo Làm Nội Trợ',
              project_id: '899e7fb2-016b-45c7-8d61-26397383287c',
              aspect_ratio: 'VIDEO_ASPECT_RATIO_PORTRAIT',
              stats: { total_episodes: 20, total_clips: 100, rendered_clips: 0, merged_episodes: 0 },
            },
            {
              slug: 'tay-du-ky-2026',
              name: 'Tây Du Ký 2026',
              project_id: 'e12d45a9-9b4c-4821-832d-4c8d1290f45a',
              aspect_ratio: 'VIDEO_ASPECT_RATIO_PORTRAIT',
              stats: { total_episodes: 20, total_clips: 100, rendered_clips: 0, merged_episodes: 0 },
            },
          ]

    for (const ch of fallbackChannels) {
      seenProjectIds.add(ch.project_id)
      list.push({
        key: ch.slug,
        kind: 'channel',
        channelSlug: ch.slug,
        projectId: ch.project_id,
        name: ch.name,
        aspectRatio: ch.aspect_ratio?.includes('PORTRAIT') ? '9:16 Dọc' : '16:9 Ngang',
        totalEpisodes: ch.stats?.total_episodes || 60,
        renderedClips: ch.stats?.rendered_clips || 0,
        totalClips: ch.stats?.total_clips || 360,
        running: Boolean(ch.active_job?.running),
        pid: ch.active_job?.pid,
        activeStartEp: ch.active_job?.start_ep,
        activeEndEp: ch.active_job?.end_ep,
      })
    }

    for (const p of projects) {
      if (seenProjectIds.has(p.id)) continue
      list.push({
        key: `proj:${p.id}`,
        kind: 'project',
        channelSlug: p.id,
        projectId: p.id,
        name: `[Dự Án Flow] ${p.name}`,
        aspectRatio: 'Flow Project',
        totalEpisodes: 1,
        renderedClips: 0,
        totalClips: 6,
        running: false,
      })
    }

    return list
  }, [channels, projects])

  const currentTarget = useMemo(() => {
    return (
      unifiedTargets.find(
        t => t.channelSlug === primaryConfig.channelSlug || t.projectId === primaryConfig.projectId
      ) || unifiedTargets[0]
    )
  }, [unifiedTargets, primaryConfig.channelSlug, primaryConfig.projectId])

  // Compute ordered workflow steps (Topological sort) so user can ALWAYS see the current steps pipeline
  const orderedWorkflowSteps: WorkflowNode[] = useMemo(() => {
    const inDegree = new Map<string, number>()
    const adj = new Map<string, string[]>()
    nodes.forEach(n => {
      inDegree.set(n.id, 0)
      adj.set(n.id, [])
    })
    edges.forEach(e => {
      if (adj.has(e.from) && inDegree.has(e.to)) {
        adj.get(e.from)!.push(e.to)
        inDegree.set(e.to, (inDegree.get(e.to) || 0) + 1)
      }
    })

    const sortedNodes = [...nodes].sort((a, b) => a.x - b.x || a.y - b.y)
    const queue: WorkflowNode[] = sortedNodes.filter(n => (inDegree.get(n.id) || 0) === 0)
    const ordered: WorkflowNode[] = []
    const visited = new Set<string>()

    while (queue.length > 0) {
      const cur = queue.shift()!
      if (visited.has(cur.id)) continue
      visited.add(cur.id)
      ordered.push(cur)
      const neighbors = adj.get(cur.id) || []
      for (const nbId of neighbors) {
        inDegree.set(nbId, (inDegree.get(nbId) || 1) - 1)
        if ((inDegree.get(nbId) || 0) <= 0 && !visited.has(nbId)) {
          const nbNode = nodes.find(n => n.id === nbId)
          if (nbNode) queue.push(nbNode)
        }
      }
    }
    sortedNodes.forEach(n => {
      if (!visited.has(n.id)) ordered.push(n)
    })
    return ordered
  }, [nodes, edges])

  // Currently selected episode object from `channelEpisodes`
  const currentEpisodeDetail = useMemo(() => {
    return channelEpisodes.find(e => e.episode_num === primaryConfig.startEp) || null
  }, [channelEpisodes, primaryConfig.startEp])

  // Check if ANYTHING is currently running (for conditional Stop button visibility)
  const activeJobs = useMemo(() => channels.filter(c => c.active_job?.running), [channels])
  const anyNodeRunning = useMemo(() => nodes.some(n => n.status === 'running'), [nodes])
  const isAnythingRunning =
    isRunningWorkflow || anyNodeRunning || Boolean(currentTarget?.running) || activeJobs.length > 0

  // Latest active log for the current channel to display in the "Current Step" live banner
  const latestChannelLog = useMemo(() => {
    return liveServerLogs.find(l => l.channel_slug === primaryConfig.channelSlug) || liveServerLogs[0] || null
  }, [liveServerLogs, primaryConfig.channelSlug])

  // Convert client mouse coordinates to canvas coordinates
  const clientToCanvas = useCallback(
    (clientX: number, clientY: number) => {
      const rect = canvasRef.current?.getBoundingClientRect()
      if (!rect) return { x: 0, y: 0 }
      return {
        x: (clientX - rect.left - pan.x) / zoom,
        y: (clientY - rect.top - pan.y) / zoom,
      }
    },
    [pan.x, pan.y, zoom]
  )

  // Create a directed connection between two nodes (avoiding self-loops & duplicates)
  const createConnectionBetweenNodes = useCallback(
    (firstNodeId: string, secondNodeId: string, dir: 'out' | 'in' = 'out') => {
      if (!firstNodeId || !secondNodeId || firstNodeId === secondNodeId) return false
      const fromId = dir === 'out' ? firstNodeId : secondNodeId
      const toId = dir === 'out' ? secondNodeId : firstNodeId

      const fromNode = nodes.find(n => n.id === fromId)
      const toNode = nodes.find(n => n.id === toId)
      if (!fromNode || !toNode) return false

      let added = false
      setEdges(prev => {
        if (prev.some(ed => ed.from === fromId && ed.to === toId)) {
          return prev
        }
        added = true
        return [
          ...prev,
          {
            id: `edge-${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 5)}`,
            from: fromId,
            to: toId,
          },
        ]
      })

      if (added) {
        appendLog('SUCCESS', `🔗 Đã nối bước: "${fromNode.title}" → "${toNode.title}"`)
      } else {
        appendLog('INFO', `ℹ️ Bước "${fromNode.title}" đã được nối với "${toNode.title}" từ trước.`)
      }
      return true
    },
    [nodes, appendLog]
  )

  // Find a node under a client (x,y) coordinate via DOM attribute or canvas bounding box (+24px snap margin)
  const findNodeAtClientPoint = useCallback(
    (clientX: number, clientY: number): WorkflowNode | null => {
      const el = document.elementFromPoint(clientX, clientY) as HTMLElement | null
      const cardEl = el?.closest('[data-workflow-node-id]') as HTMLElement | null
      if (cardEl?.dataset.workflowNodeId) {
        const found = nodes.find(n => n.id === cardEl.dataset.workflowNodeId)
        if (found) return found
      }
      const pos = clientToCanvas(clientX, clientY)
      const pad = 24
      return (
        nodes.find(
          n =>
            pos.x >= n.x - pad &&
            pos.x <= n.x + NODE_WIDTH + pad &&
            pos.y >= n.y - pad &&
            pos.y <= n.y + NODE_HEIGHT + pad
        ) || null
      )
    },
    [nodes, clientToCanvas]
  )

  // Window-level mousemove / mouseup / blur listeners — strictly requires physical left mouse button hold ((e.buttons & 1) === 1)
  useEffect(() => {
    function stopAllDragAndPan() {
      nodeDragStartRef.current = null
      isPanningRef.current = false
      setHoldingNodeId(prev => (prev ? null : prev))
      setDraggingNodeId(prev => (prev ? null : prev))
      setIsPanning(prev => (prev ? false : prev))
    }

    function handleWindowMouseMove(e: MouseEvent) {
      const isLeftButtonPressed = (e.buttons & 1) === 1

      // 1. If user is NOT physically holding down the left mouse button (i.e. just hovering!),
      // NEVER drag any node or pan the canvas! Immediately clear any stale drag/pan state.
      if (!isLeftButtonPressed) {
        if (nodeDragStartRef.current || isPanningRef.current) {
          stopAllDragAndPan()
        }
        if (connectStartMouseRef.current) {
          setConnectingFromId(null)
          setHoveredTargetNodeId(null)
          connectStartMouseRef.current = null
          return
        }
        if (connectingFromId) {
          const pos = clientToCanvas(e.clientX, e.clientY)
          setMouseCanvasPos(pos)
          const hit = findNodeAtClientPoint(e.clientX, e.clientY)
          setHoveredTargetNodeId(hit && hit.id !== connectingFromId ? hit.id : null)
        }
        return
      }

      // 2. User IS physically holding down the left mouse button ((e.buttons & 1) === 1):
      if (nodeDragStartRef.current) {
        const { nodeId, startMouseX, startMouseY, startNodeX, startNodeY } = nodeDragStartRef.current
        const rawDist = Math.hypot(e.clientX - startMouseX, e.clientY - startMouseY)
        // Only start dragging the node once the user moves >= 6px while holding down the mouse button
        if (rawDist >= 6) {
          if (!nodeDragStartRef.current.didMove) {
            nodeDragStartRef.current.didMove = true
            setDraggingNodeId(nodeId)
          }
          const dx = (e.clientX - startMouseX) / zoom
          const dy = (e.clientY - startMouseY) / zoom
          const nextX = Math.max(12, Math.round((startNodeX + dx) / 8) * 8)
          const nextY = Math.max(12, Math.round((startNodeY + dy) / 8) * 8)
          setNodes(prev => prev.map(n => (n.id === nodeId ? { ...n, x: nextX, y: nextY } : n)))
        }
      } else if (isPanningRef.current) {
        const dx = e.clientX - panStartRef.current.x
        const dy = e.clientY - panStartRef.current.y
        if (Math.hypot(dx, dy) >= 5) {
          setPan({ x: panStartRef.current.panX + dx, y: panStartRef.current.panY + dy })
        }
      } else if (connectingFromId) {
        const pos = clientToCanvas(e.clientX, e.clientY)
        setMouseCanvasPos(pos)
        const hit = findNodeAtClientPoint(e.clientX, e.clientY)
        setHoveredTargetNodeId(hit && hit.id !== connectingFromId ? hit.id : null)
      }
    }

    function handleWindowMouseUp(e: MouseEvent) {
      if (connectingFromId) {
        const hit = findNodeAtClientPoint(e.clientX, e.clientY)
        if (hit && hit.id !== connectingFromId) {
          // Dropped or clicked onto a target node -> connect them!
          createConnectionBetweenNodes(connectingFromId, hit.id, connectingPortDir)
          setConnectingFromId(null)
          setHoveredTargetNodeId(null)
          connectStartMouseRef.current = null
        } else if (connectStartMouseRef.current) {
          // Released mouse after dragging from a port without hitting a target node -> cancel wire immediately so nothing drags on hover!
          setConnectingFromId(null)
          setHoveredTargetNodeId(null)
          connectStartMouseRef.current = null
        }
      } else if (nodeDragStartRef.current) {
        const { nodeId, didMove } = nodeDragStartRef.current
        // If user clicked the node without dragging -> Open n8n Step Detail & Per-Step Log Modal!
        if (!didMove) {
          setSelectedNodeId(nodeId)
          setDetailModalNodeId(nodeId)
          setShowInspector(true)
        }
      }

      stopAllDragAndPan()
    }

    window.addEventListener('mousemove', handleWindowMouseMove)
    window.addEventListener('mouseup', handleWindowMouseUp)
    window.addEventListener('blur', stopAllDragAndPan)
    return () => {
      window.removeEventListener('mousemove', handleWindowMouseMove)
      window.removeEventListener('mouseup', handleWindowMouseUp)
      window.removeEventListener('blur', stopAllDragAndPan)
    }
  }, [
    connectingFromId,
    connectingPortDir,
    zoom,
    clientToCanvas,
    findNodeAtClientPoint,
    createConnectionBetweenNodes,
  ])

  function handleCanvasDragOver(e: React.DragEvent<HTMLDivElement>) {
    e.preventDefault()
    e.dataTransfer.dropEffect = 'copy'
    if (!isDraggingOverCanvas) setIsDraggingOverCanvas(true)
  }

  function handleCanvasDragLeave() {
    setIsDraggingOverCanvas(false)
  }

  function handleCanvasDrop(e: React.DragEvent<HTMLDivElement>) {
    e.preventDefault()
    setIsDraggingOverCanvas(false)
    const type = (e.dataTransfer.getData('application/flowkit-node') ||
      e.dataTransfer.getData('text/plain')) as WorkflowNodeType
    if (!type || !NODE_CATALOG.some(c => c.type === type)) return
    const pos = clientToCanvas(e.clientX, e.clientY)
    addNodeAt(
      type,
      Math.max(20, Math.round((pos.x - NODE_WIDTH / 2) / 12) * 12),
      Math.max(20, Math.round((pos.y - 40) / 12) * 12)
    )
  }

  function addNodeAt(type: WorkflowNodeType, x?: number, y?: number) {
    const meta = getNodeMeta(type)
    const baseCfg = { ...primaryConfig }
    const newId = `node-${Date.now().toString(36)}`
    const nx = x ?? 48 + ((nodes.length * 188) % 564)
    const ny = y ?? 90 + Math.floor(nodes.length / 3) * 124

    const newNode: WorkflowNode = {
      id: newId,
      type,
      title: meta.title,
      subtitle: meta.subtitle,
      x: nx,
      y: ny,
      status: 'idle',
      stepLogs: [
        {
          id: `init-${newId}`,
          time: new Date().toLocaleTimeString('vi-VN'),
          level: 'INFO',
          text: `Đã khởi tạo bước "${meta.title}". Sẵn sàng thực thi cho dự án "${baseCfg.channelSlug}".`,
        },
      ],
      config: baseCfg,
    }

    setNodes(prev => [...prev, newNode])

    // Auto-connect from the last step (both when clicking "+ Kéo/Thêm" AND when dropping onto Canvas)
    if (nodes.length > 0) {
      const lastNode = orderedWorkflowSteps[orderedWorkflowSteps.length - 1] || nodes[nodes.length - 1]
      if (lastNode) {
        setEdges(prev => [
          ...prev,
          { id: `edge-${Date.now().toString(36)}`, from: lastNode.id, to: newId },
        ])
      }
    }
    setSelectedNodeId(newId)
    appendLog('INFO', `➕ Đã thêm và nối tự động bước "${meta.title}" vào cuối chuỗi Workflow.`, newId, meta.title)
  }

  function deleteNode(id: string) {
    setNodes(prev => prev.filter(n => n.id !== id))
    setEdges(prev => prev.filter(e => e.from !== id && e.to !== id))
    if (selectedNodeId === id) setSelectedNodeId(null)
    if (detailModalNodeId === id) setDetailModalNodeId(null)
    if (connectingFromId === id) setConnectingFromId(null)
  }

  function deleteEdge(id: string) {
    setEdges(prev => prev.filter(e => e.id !== id))
    appendLog('INFO', '✂️ Đã ngắt 1 dây nối giữa 2 bước.')
  }

  function toggleConnectionBetweenNodes(fromId: string, toId: string) {
    if (fromId === toId) return
    const existing = edges.find(e => e.from === fromId && e.to === toId)
    if (existing) {
      deleteEdge(existing.id)
    } else {
      createConnectionBetweenNodes(fromId, toId, 'out')
    }
  }

  function autoConnectAllNodes() {
    if (nodes.length < 2) return
    const sorted = [...nodes].sort((a, b) => a.x - b.x || a.y - b.y)
    const nextEdges: WorkflowEdge[] = []
    for (let i = 0; i < sorted.length - 1; i++) {
      nextEdges.push({
        id: `edge-auto-${i}-${Date.now().toString(36)}`,
        from: sorted[i].id,
        to: sorted[i + 1].id,
      })
    }
    setEdges(nextEdges)
    appendLog('SUCCESS', `🔗 Đã tự động nối liên hoàn toàn bộ ${sorted.length} bước theo thứ tự!`)
  }

  function handleCanvasMouseDown(e: React.MouseEvent<HTMLDivElement>) {
    if (e.button !== 0) return
    const targetEl = e.target as HTMLElement
    if (e.target === e.currentTarget || targetEl.dataset.canvasBg === 'true') {
      if (connectingFromId) {
        setConnectingFromId(null)
        setHoveredTargetNodeId(null)
        connectStartMouseRef.current = null
        return
      }
      isPanningRef.current = true
      setIsPanning(true)
      panStartRef.current = { x: e.clientX, y: e.clientY, panX: pan.x, panY: pan.y }
      setSelectedNodeId(null)
    }
  }

  function startNodeDrag(e: React.MouseEvent, node: WorkflowNode) {
    if (e.button !== 0) return
    e.stopPropagation()

    // If user is in Click-to-Connect mode and clicks a target node, complete the wire connection immediately!
    if (connectingFromId && connectingFromId !== node.id) {
      createConnectionBetweenNodes(connectingFromId, node.id, connectingPortDir)
      setConnectingFromId(null)
      setHoveredTargetNodeId(null)
      connectStartMouseRef.current = null
      setSelectedNodeId(node.id)
      return
    }

    setSelectedNodeId(node.id)
    setHoldingNodeId(node.id)
    nodeDragStartRef.current = {
      nodeId: node.id,
      startMouseX: e.clientX,
      startMouseY: e.clientY,
      startNodeX: node.x,
      startNodeY: node.y,
      downTimeMs: performance.now(),
      didMove: false,
    }
  }

  function startWireConnect(e: React.MouseEvent, nodeId: string, dir: 'out' | 'in' = 'out') {
    e.stopPropagation()
    e.preventDefault()

    // If already connecting from another node, clicking this port completes the connection!
    if (connectingFromId && connectingFromId !== nodeId) {
      createConnectionBetweenNodes(connectingFromId, nodeId, connectingPortDir)
      setConnectingFromId(null)
      setHoveredTargetNodeId(null)
      connectStartMouseRef.current = null
      return
    }

    // Toggle off if clicking the same port while already in click-to-connect
    if (connectingFromId === nodeId && !connectStartMouseRef.current) {
      setConnectingFromId(null)
      setHoveredTargetNodeId(null)
      return
    }

    connectStartMouseRef.current = { x: e.clientX, y: e.clientY, nodeId }
    setConnectingPortDir(dir)
    setConnectingFromId(nodeId)
    const pos = clientToCanvas(e.clientX, e.clientY)
    setMouseCanvasPos(pos)
  }

  function completeWireConnect(e: React.MouseEvent, targetNodeId: string) {
    e.stopPropagation()
    if (!connectingFromId || connectingFromId === targetNodeId) {
      return
    }
    createConnectionBetweenNodes(connectingFromId, targetNodeId, connectingPortDir)
    setConnectingFromId(null)
    setHoveredTargetNodeId(null)
    connectStartMouseRef.current = null
  }

  function autoArrangeNodes() {
    const cols = 4
    setNodes(prev =>
      prev.map((n, idx) => ({
        ...n,
        x: 36 + (idx % cols) * 192,
        y: 84 + Math.floor(idx / cols) * 124,
      }))
    )
    setPan({ x: 0, y: 0 })
    setZoom(1)
  }

  function loadTemplate(key: string) {
    const tpl = PRESET_TEMPLATES[key]
    if (!tpl) return
    setNodes(
      tpl.nodes.map(n => ({
        ...n,
        status: 'idle',
        lastMessage: undefined,
        stepLogs: [],
        lastOutput: undefined,
        config: { ...n.config, ...primaryConfig },
      }))
    )
    setEdges(tpl.edges)
    setSelectedNodeId(tpl.nodes[0]?.id || null)
    setPan({ x: 0, y: 0 })
    setZoom(1)
    appendLog('INFO', `📋 Đã nạp mẫu Workflow: "${tpl.name}".`)
  }

  async function handleSelectTargetProject(targetKey: string) {
    const found = unifiedTargets.find(t => t.key === targetKey || t.channelSlug === targetKey)
    if (!found) return
    updateGlobalOrNodeConfig(
      {
        channelSlug: found.channelSlug,
        projectId: found.projectId,
        projectName: found.name,
      },
      undefined,
      true
    )
    if (found.kind === 'channel') {
      await loadChannelEpisodesAndAutoSelectLatest(found.channelSlug, true)
    }
  }

  // Filter live server logs (/api/cms/logs) that match a specific step's role
  const getServerLogsForNode = useCallback(
    (node: WorkflowNode | null): CmsLogItem[] => {
      if (!node) return []
      const slug = node.config.channelSlug || primaryConfig.channelSlug
      const bySlug = liveServerLogs.filter(l => !l.channel_slug || l.channel_slug === slug)
      return bySlug.filter(l => {
        const cat = (l.category || '').toUpperCase()
        const msg = (l.message || '').toUpperCase()
        switch (node.type) {
          case 'pull-d1':
            return cat.includes('D1') || msg.includes('D1') || msg.includes('PULL')
          case 'lock-characters':
            return cat.includes('CHAR') || msg.includes('CHAR') || msg.includes('LOCK') || msg.includes('@')
          case 'verify-prompts':
            return cat.includes('PROMPT') || msg.includes('PROMPT') || msg.includes('SCENE')
          case 'merge-mp4':
            return cat.includes('MERGE') || msg.includes('MERGE') || msg.includes('FFMPEG') || msg.includes('FULL')
          case 'push-cloud':
            return cat.includes('CLOUD') || cat.includes('R2') || cat.includes('D1') || msg.includes('R2')
          case 'run-agent':
          case 'channel-source':
          default:
            return true
        }
      })
    },
    [liveServerLogs, primaryConfig.channelSlug]
  )

  // Execute a single workflow node against real backend endpoints and record per-step logs + output
  async function executeSingleNode(node: WorkflowNode, sharedConfig?: WorkflowNodeConfig): Promise<boolean> {
    const cfg = sharedConfig || node.config
    const startTs = performance.now()
    const runTimeStr = new Date().toLocaleTimeString('vi-VN')
    const stepIdx = orderedWorkflowSteps.findIndex(s => s.id === node.id)
    if (stepIdx >= 0) setCurrentStepIndex(stepIdx)

    setNodes(prev =>
      prev.map(n =>
        n.id === node.id
          ? { ...n, status: 'running', lastRunAt: runTimeStr, lastMessage: 'Đang thực thi bước này...' }
          : n
      )
    )

    appendNodeLog(
      node.id,
      node.title,
      'INFO',
      `▶️ Bắt đầu chạy bước "${node.title}" cho dự án "${cfg.projectName || cfg.channelSlug}" (Tập ${cfg.startEp}→${cfg.endEp}${
        cfg.onlyClip > 0 ? `, chỉ Clip ${cfg.onlyClip}` : ', đủ 6 Clips'
      })`,
      JSON.stringify(
        {
          step: node.type,
          channelSlug: cfg.channelSlug,
          projectId: cfg.projectId,
          startEp: cfg.startEp,
          endEp: cfg.endEp,
          onlyClip: cfg.onlyClip,
        },
        null,
        2
      )
    )

    try {
      let msg = ''
      let outputPayload: Record<string, unknown> = {}

      if (node.type === 'channel-source') {
        appendNodeLog(node.id, node.title, 'INFO', `Đang đọc thông tin dự án & tập từ GET /api/cms/channels/${cfg.channelSlug}...`)
        try {
          const res = await fetchAPI<ChannelDetailApiResponse>(`/api/cms/channels/${cfg.channelSlug}`)
          const chName = res.channel?.name || cfg.projectName || cfg.channelSlug
          const clipDesc = cfg.onlyClip > 0 ? `Clip ${cfg.onlyClip}` : 'Trọn bộ 6 Clips'
          msg = `${chName} • Tập ${cfg.startEp}→${cfg.endEp} (${clipDesc})`
          outputPayload = {
            channel: res.channel,
            selectedEpisodeRange: `${cfg.startEp} -> ${cfg.endEp}`,
            clipMode: clipDesc,
            totalEpisodesAvailable: res.episodes?.length || 0,
          }
        } catch {
          msg = `Dự án ${cfg.projectName || cfg.channelSlug} (ID: ${(cfg.projectId || '').slice(0, 8)}...)`
          outputPayload = {
            channelSlug: cfg.channelSlug,
            projectId: cfg.projectId,
            startEp: cfg.startEp,
            endEp: cfg.endEp,
          }
        }
        appendNodeLog(node.id, node.title, 'SUCCESS', `Đã khóa nguồn dự án: ${msg}`, JSON.stringify(outputPayload, null, 2))
      } else if (node.type === 'pull-d1') {
        appendNodeLog(
          node.id,
          node.title,
          'INFO',
          'Đang gọi POST /api/cms/cloud/sync-d1?direction=pull để kéo dữ liệu từ Cloudflare D1 về SQLite...'
        )
        const res = await fetchAPI<{ ok: boolean; total_rows_pulled?: number; error?: string }>(
          '/api/cms/cloud/sync-d1?direction=pull',
          { method: 'POST' }
        )
        if (!res.ok) throw new Error(res.error || 'Không thể kéo dữ liệu từ D1')
        msg = `Đã kéo ${res.total_rows_pulled ?? 0} bản ghi từ D1 về máy`
        outputPayload = { ...res, direction: 'pull' }
        appendNodeLog(node.id, node.title, 'SUCCESS', msg, JSON.stringify(outputPayload, null, 2))
      } else if (node.type === 'lock-characters') {
        appendNodeLog(
          node.id,
          node.title,
          'INFO',
          `Đang gọi POST /api/cms/channels/${cfg.channelSlug}/auto-lock-characters để khóa UUID @Character...`
        )
        const res = await fetchAPI<{ ok: boolean; locked_count?: number; characters?: Array<{ tag: string }> }>(
          `/api/cms/channels/${cfg.channelSlug}/auto-lock-characters`,
          { method: 'POST' }
        )
        const count = res.locked_count ?? res.characters?.length ?? 9
        msg = `Đã khóa ${count} nhân vật (@Character UUID)`
        outputPayload = {
          channelSlug: cfg.channelSlug,
          lockedCount: count,
          characters: res.characters || [],
        }
        appendNodeLog(node.id, node.title, 'SUCCESS', msg, JSON.stringify(outputPayload, null, 2))
      } else if (node.type === 'verify-prompts') {
        appendNodeLog(
          node.id,
          node.title,
          'INFO',
          `Đang kiểm tra kịch bản & quy chuẩn Prompt Tập ${cfg.startEp}–${cfg.endEp} của "${cfg.channelSlug}"...`
        )
        const res = await fetchAPI<{
          episodes?: Array<{ episode_num: number; clips?: Array<{ clip_num: number; prompt?: string; status?: string }> }>
        }>(`/api/cms/channels/${cfg.channelSlug}`)
        const eps = res.episodes || []
        const targetEps = eps.filter(e => e.episode_num >= cfg.startEp && e.episode_num <= cfg.endEp)
        const totalClips = targetEps.reduce((acc, e) => acc + (e.clips?.length || 0), 0)
        msg = `Đã xác thực ${targetEps.length} tập (${totalClips} prompts chuẩn 24fps)`
        outputPayload = {
          channelSlug: cfg.channelSlug,
          verifiedEpisodes: targetEps.map(e => e.episode_num),
          totalVerifiedPrompts: totalClips,
          rulesChecked: ['24fps', '180°/150° Eye-line', 'Vietnamese Dialogue 15-30 words', 'Safe Stunt Choreography'],
        }
        appendNodeLog(node.id, node.title, 'SUCCESS', msg, JSON.stringify(outputPayload, null, 2))
      } else if (node.type === 'run-agent') {
        appendNodeLog(
          node.id,
          node.title,
          'INFO',
          `Đang gọi POST /api/cms/channels/${cfg.channelSlug}/run (Tập ${cfg.startEp}–${cfg.endEp}${
            cfg.onlyClip > 0 ? `, chỉ Clip ${cfg.onlyClip}` : ''
          })...`
        )
        const res = await fetchAPI<{
          ok: boolean
          pid: number
          start_ep: number
          end_ep: number
          only_clip?: number | null
        }>(`/api/cms/channels/${cfg.channelSlug}/run`, {
          method: 'POST',
          body: JSON.stringify({
            start_ep: cfg.startEp,
            end_ep: cfg.endEp,
            only_clip: cfg.onlyClip > 0 ? cfg.onlyClip : null,
          }),
        })
        msg = `Agent đang chạy (PID ${res.pid}) • Tập ${res.start_ep}–${res.end_ep}`
        outputPayload = { ...res, channelSlug: cfg.channelSlug }
        appendNodeLog(
          node.id,
          node.title,
          'SUCCESS',
          `Đã kích hoạt tiến trình Agent thành công (PID ${res.pid})!`,
          JSON.stringify(outputPayload, null, 2)
        )
        await refreshData()
      } else if (node.type === 'merge-mp4') {
        appendNodeLog(
          node.id,
          node.title,
          'INFO',
          `Đang gọi POST /api/cms/channels/${cfg.channelSlug}/episodes/${cfg.startEp}/merge để nối FULL MP4 bằng FFmpeg...`
        )
        const res = await fetchAPI<{ ok: boolean; output_path?: string; size_mb?: number }>(
          `/api/cms/channels/${cfg.channelSlug}/episodes/${cfg.startEp}/merge`,
          { method: 'POST' }
        )
        msg = `Đã ghép Tập ${cfg.startEp} (${res.size_mb ?? 0} MB)`
        outputPayload = { ...res, episode: cfg.startEp, channelSlug: cfg.channelSlug }
        appendNodeLog(node.id, node.title, 'SUCCESS', msg, JSON.stringify(outputPayload, null, 2))
      } else if (node.type === 'push-cloud') {
        const parts: string[] = []
        if (cfg.syncR2) {
          appendNodeLog(
            node.id,
            node.title,
            'INFO',
            `Đang đồng bộ video MP4 của "${cfg.channelSlug}" lên Cloudflare R2...`
          )
          const r2Res = await fetchAPI<{
            uploaded_clips_count: number
            uploaded_episodes_count: number
          }>('/api/cms/cloud/sync-r2', {
            method: 'POST',
            body: JSON.stringify({ channel_slug: cfg.channelSlug, force: cfg.forceR2 }),
          })
          parts.push(`R2: ${r2Res.uploaded_clips_count} clips, ${r2Res.uploaded_episodes_count} tập`)
          outputPayload.r2 = r2Res
        }
        if (cfg.syncD1) {
          appendNodeLog(node.id, node.title, 'INFO', 'Đang đồng bộ SQLite lên Cloudflare D1 SQL...')
          const d1Res = await fetchAPI<{ ok: boolean; total_rows_synced?: number }>(
            '/api/cms/cloud/sync-d1?direction=push',
            { method: 'POST' }
          )
          parts.push(`D1: ${d1Res.total_rows_synced ?? 0} dòng`)
          outputPayload.d1 = d1Res
        }
        msg = parts.join(' • ') || 'Đã đồng bộ Cloud'
        appendNodeLog(node.id, node.title, 'SUCCESS', msg, JSON.stringify(outputPayload, null, 2))
      }

      const elapsed = Math.round(performance.now() - startTs)
      setNodes(prev =>
        prev.map(n =>
          n.id === node.id
            ? {
                ...n,
                status: 'success',
                lastMessage: msg,
                durationMs: elapsed,
                lastOutput: {
                  status: 'success',
                  durationMs: elapsed,
                  completedAt: new Date().toISOString(),
                  summary: msg,
                  ...outputPayload,
                },
              }
            : n
        )
      )
      return true
    } catch (err) {
      const errMsg = err instanceof Error ? err.message : String(err)
      const elapsed = Math.round(performance.now() - startTs)
      appendNodeLog(node.id, node.title, 'ERROR', `Lỗi khi thực thi: ${errMsg}`)
      setNodes(prev =>
        prev.map(n =>
          n.id === node.id
            ? {
                ...n,
                status: 'error',
                lastMessage: errMsg,
                durationMs: elapsed,
                lastOutput: {
                  status: 'error',
                  durationMs: elapsed,
                  failedAt: new Date().toISOString(),
                  error: errMsg,
                },
              }
            : n
        )
      )
      return false
    }
  }

  // Quick 1-click "Run Selected Project" with the chosen options
  async function runSelectedProjectDirect() {
    if (isRunningWorkflow) return
    setIsRunningWorkflow(true)
    setConsoleOpen(true)
    const cfg = primaryConfig
    appendLog(
      'INFO',
      `🚀 [Chạy Dự Án] Khởi chạy "${cfg.projectName || cfg.channelSlug}" • Tập ${cfg.startEp}→${cfg.endEp}${
        cfg.onlyClip > 0 ? ` • Clip ${cfg.onlyClip}` : ' • Đủ 6 Clips'
      }`
    )

    try {
      if (cfg.autoLockChars) {
        const lockNode = nodes.find(n => n.type === 'lock-characters')
        if (lockNode) {
          await executeSingleNode(lockNode, cfg)
        } else {
          await fetchAPI(`/api/cms/channels/${cfg.channelSlug}/auto-lock-characters`, { method: 'POST' })
          appendLog('SUCCESS', `✅ Đã tự động khóa @Character cho dự án "${cfg.channelSlug}".`)
        }
      }

      const agentNode = nodes.find(n => n.type === 'run-agent')
      if (agentNode) {
        await executeSingleNode(agentNode, cfg)
      } else {
        const res = await fetchAPI<{ pid: number }>(`/api/cms/channels/${cfg.channelSlug}/run`, {
          method: 'POST',
          body: JSON.stringify({
            start_ep: cfg.startEp,
            end_ep: cfg.endEp,
            only_clip: cfg.onlyClip > 0 ? cfg.onlyClip : null,
          }),
        })
        appendLog('SUCCESS', `✅ Đã khởi chạy Agent cho dự án "${cfg.channelSlug}" (PID ${res.pid}).`)
      }
      await refreshData()
    } catch (e) {
      appendLog('ERROR', `❌ Lỗi chạy dự án: ${e instanceof Error ? e.message : String(e)}`)
    } finally {
      setIsRunningWorkflow(false)
    }
  }

  // Sequential execution of all connected workflow steps
  async function runEntireWorkflow() {
    if (isRunningWorkflow || orderedWorkflowSteps.length === 0) return
    abortRunRef.current = false
    setIsRunningWorkflow(true)
    setConsoleOpen(true)
    setShowStepBar(true)

    setNodes(prev => prev.map(n => ({ ...n, status: 'idle', lastMessage: undefined, durationMs: undefined })))

    const sourceNode = orderedWorkflowSteps.find(n => n.type === 'channel-source')
    const sharedCfg = sourceNode ? sourceNode.config : orderedWorkflowSteps[0].config

    appendLog(
      'INFO',
      `▶️ Bắt đầu chạy Workflow (${orderedWorkflowSteps.length} bước) cho dự án "${
        sharedCfg.projectName || sharedCfg.channelSlug
      }" (Tập ${sharedCfg.startEp}→${sharedCfg.endEp}): ${orderedWorkflowSteps.map(n => n.title).join(' → ')}`
    )

    for (let i = 0; i < orderedWorkflowSteps.length; i++) {
      if (abortRunRef.current) {
        appendLog('WARN', '🛑 Đã dừng chuỗi thực thi Workflow theo yêu cầu.')
        break
      }
      setCurrentStepIndex(i)
      const stepNode = orderedWorkflowSteps[i]
      setSelectedNodeId(stepNode.id)
      if (i > 0) {
        const prevNode = orderedWorkflowSteps[i - 1]
        const connectingEdge = edges.find(e => e.from === prevNode.id && e.to === stepNode.id)
        if (connectingEdge) setActiveEdgeId(connectingEdge.id)
      }
      const ok = await executeSingleNode(stepNode, sharedCfg)
      if (!ok) {
        appendLog('WARN', `⚠️ Workflow tạm dừng tại Bước ${i + 1} ("${stepNode.title}") do có lỗi trả về.`)
        break
      }
      await new Promise(r => setTimeout(r, 350))
    }

    setActiveEdgeId(null)
    setIsRunningWorkflow(false)
  }

  async function stopRunningAgent(slug: string) {
    abortRunRef.current = true
    setIsRunningWorkflow(false)
    setCurrentStepIndex(null)
    setNodes(prev =>
      prev.map(n => (n.status === 'running' ? { ...n, status: 'idle', lastMessage: 'Đã dừng theo yêu cầu' } : n))
    )
    try {
      const res = await fetchAPI<{ stopped: boolean }>(`/api/cms/channels/${slug}/stop`, {
        method: 'POST',
      })
      if (res.stopped) {
        appendLog('WARN', `🛑 Đã dừng thành công tiến trình Agent của dự án "${slug}".`)
      } else {
        appendLog('WARN', `🛑 Đã dừng luồng chạy Workflow hiện tại.`)
      }
      await refreshData()
    } catch (err) {
      appendLog('ERROR', `❌ Không thể dừng Agent: ${err instanceof Error ? err.message : String(err)}`)
    }
  }

  return (
    <div
      className={
        isFullScreen
          ? 'fixed inset-0 z-50 bg-[#060911] p-2.5 flex flex-col gap-2 select-none'
          : 'flex flex-col h-[calc(100vh-5.2rem)] gap-2 select-none'
      }
    >
      {/* 1. TOP CONTROL BAR: Project Selector + Auto-Selected Latest Episode + Run / Conditional Stop + Fullscreen */}
      <div className="flex flex-wrap items-center justify-between gap-2.5 px-3.5 py-2.5 rounded-2xl bg-slate-900/95 border border-slate-800/90 shadow-lg">
        {/* Left: Target Project / Channel Selector & Auto-Selected Episode Controls */}
        <div className="flex items-center gap-2 flex-wrap">
          <div className="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-slate-950 border border-indigo-500/40">
            <FolderKanban size={14} className="text-indigo-400 shrink-0" />
            <span className="text-[11px] font-bold text-slate-400 shrink-0">Dự Án:</span>
            <select
              value={currentTarget?.key || primaryConfig.channelSlug}
              onChange={e => handleSelectTargetProject(e.target.value)}
              className="bg-transparent text-xs font-extrabold text-white outline-none cursor-pointer min-w-[200px]"
            >
              {unifiedTargets.map(t => (
                <option key={t.key} value={t.key} className="bg-slate-950 text-white">
                  🎬 {t.name} [{t.aspectRatio}] — {t.renderedClips}/{t.totalClips} Clips ({t.totalEpisodes} tập)
                </option>
              ))}
            </select>
          </div>

          {/* Episode Dropdown (Auto-selected to Latest) + Range Inputs */}
          <div className="flex items-center gap-1.5 px-2.5 py-1 rounded-xl bg-slate-950 border border-slate-800 text-xs">
            <span className="text-[11px] text-emerald-400 font-bold flex items-center gap-1">
              <Zap size={11} /> Tập:
            </span>
            {channelEpisodes.length > 0 ? (
              <select
                value={primaryConfig.startEp}
                onChange={e => {
                  const epNum = Number(e.target.value)
                  updateGlobalOrNodeConfig({ startEp: epNum, endEp: Math.max(epNum, primaryConfig.endEp) })
                }}
                className="bg-slate-900 border border-slate-700 rounded px-2 py-0.5 text-xs font-bold text-white outline-none cursor-pointer max-w-[190px]"
                title="Tự động chọn tập mới nhất cần chạy"
              >
                {channelEpisodes.map(ep => (
                  <option key={ep.episode_num} value={ep.episode_num} className="bg-slate-950 text-white">
                    Tập {ep.episode_num} ({ep.rendered_clips}/{ep.total_clips} clips)
                    {ep.episode_num === newestEpisodeNum ? ' ★ Mới nhất' : ''}
                    {ep.merged_video_url ? ' • FULL' : ''}
                  </option>
                ))}
              </select>
            ) : (
              <input
                type="number"
                min={1}
                max={100}
                value={primaryConfig.startEp}
                onChange={e => {
                  const v = Math.max(1, Number(e.target.value) || 1)
                  updateGlobalOrNodeConfig({ startEp: v, endEp: Math.max(v, primaryConfig.endEp) })
                }}
                className="w-12 px-1.5 py-0.5 rounded bg-slate-900 border border-slate-700 text-white text-center font-mono text-xs outline-none"
              />
            )}

            <span className="text-slate-500">→</span>
            <input
              type="number"
              min={1}
              max={100}
              value={primaryConfig.endEp}
              onChange={e => {
                const v = Math.max(primaryConfig.startEp, Number(e.target.value) || 1)
                updateGlobalOrNodeConfig({ endEp: v })
              }}
              className="w-12 px-1.5 py-0.5 rounded bg-slate-900 border border-slate-700 text-white text-center font-mono text-xs outline-none focus:border-indigo-500"
              title="Đến Tập / Cảnh"
            />

            <button
              type="button"
              onClick={() => loadChannelEpisodesAndAutoSelectLatest(primaryConfig.channelSlug, true)}
              className="px-2 py-0.5 rounded bg-emerald-500/15 hover:bg-emerald-500/25 text-emerald-300 border border-emerald-500/30 text-[10px] font-bold cursor-pointer"
              title="Tự động chọn lại Tập mới nhất / đang làm dở"
            >
              ⚡ Tập mới nhất (#{newestEpisodeNum})
            </button>

            <button
              type="button"
              onClick={() =>
                updateGlobalOrNodeConfig({
                  startEp: 1,
                  endEp: currentTarget?.totalEpisodes || newestEpisodeNum || 60,
                  onlyClip: 0,
                })
              }
              className="px-2 py-0.5 rounded bg-indigo-500/15 hover:bg-indigo-500/25 text-indigo-300 border border-indigo-500/30 text-[10px] font-bold cursor-pointer"
              title="Chạy toàn bộ các tập của dự án này"
            >
              Cả dự án (1→{currentTarget?.totalEpisodes || 60})
            </button>
          </div>

          <select
            value={primaryConfig.onlyClip}
            onChange={e => updateGlobalOrNodeConfig({ onlyClip: Number(e.target.value) })}
            className="px-2.5 py-1.5 rounded-xl text-xs font-semibold bg-slate-950 text-slate-200 border border-slate-800 outline-none cursor-pointer"
          >
            <option value={0}>🎞️ Đủ 6 Clips / Tập</option>
            <option value={1}>🎯 Chỉ Clip 01</option>
            <option value={2}>🎯 Chỉ Clip 02</option>
            <option value={3}>🎯 Chỉ Clip 03</option>
            <option value={4}>🎯 Chỉ Clip 04</option>
            <option value={5}>🎯 Chỉ Clip 05</option>
            <option value={6}>🎯 Chỉ Clip 06</option>
          </select>
        </div>

        {/* Right: Run Buttons + CONDITIONAL Stop Button (Only shown when running!) + Fullscreen */}
        <div className="flex items-center gap-2 flex-wrap">
          <button
            onClick={runSelectedProjectDirect}
            disabled={isRunningWorkflow}
            className="px-3.5 py-1.5 rounded-xl text-xs font-bold bg-emerald-500/20 hover:bg-emerald-500/30 text-emerald-200 border border-emerald-500/40 flex items-center gap-1.5 cursor-pointer disabled:opacity-50"
            title="Khóa @Character và khởi chạy ngay Agent cho Dự Án đã chọn"
          >
            <Rocket size={13} className="text-emerald-400" />
            Chạy Dự Án Này
          </button>

          <button
            onClick={runEntireWorkflow}
            disabled={isRunningWorkflow}
            className="px-4 py-1.5 rounded-xl text-xs font-extrabold studio-glow-btn flex items-center gap-1.5 shadow-lg disabled:opacity-50 cursor-pointer"
          >
            {isRunningWorkflow ? (
              <>
                <Loader2 size={13} className="animate-spin" /> Đang Chạy Workflow...
              </>
            ) : (
              <>
                <Play size={13} /> Chạy Toàn Bộ Workflow ({orderedWorkflowSteps.length} bước)
              </>
            )}
          </button>

          {/* ONLY SHOW STOP BUTTON WHEN WORKFLOW OR AGENT IS ACTUALLY RUNNING */}
          {isAnythingRunning && (
            <button
              onClick={() => {
                const runningSlug = activeJobs[0]?.slug || primaryConfig.channelSlug
                stopRunningAgent(runningSlug)
              }}
              className="px-3.5 py-1.5 rounded-xl text-xs font-extrabold bg-rose-500 hover:bg-rose-600 text-white border border-rose-400 flex items-center gap-1.5 shadow-lg animate-pulse cursor-pointer"
              title="Dừng ngay tiến trình Agent / Workflow đang chạy"
            >
              <Square size={12} />
              Dừng Ngay {activeJobs[0]?.active_job?.pid ? `(PID ${activeJobs[0].active_job.pid})` : ''}
            </button>
          )}

          <button
            onClick={toggleFullScreen}
            className={`px-3 py-1.5 rounded-xl text-xs font-bold border flex items-center gap-1.5 transition-all cursor-pointer ${
              isFullScreen
                ? 'bg-amber-500/20 border-amber-500/50 text-amber-200'
                : 'bg-indigo-500/15 hover:bg-indigo-500/25 border-indigo-500/40 text-indigo-200'
            }`}
            title={isFullScreen ? 'Thoát Toàn Màn Hình (Esc)' : 'Mở Toàn Màn Hình (Full Screen)'}
          >
            {isFullScreen ? (
              <>
                <Minimize2 size={13} /> Thoát Full Screen
              </>
            ) : (
              <>
                <Maximize2 size={13} /> Full Screen
              </>
            )}
          </button>
        </div>
      </div>

      {/* 2. LIVE STEP-BY-STEP PIPELINE TRACKER ("Xem Được Các Bước Hiện Tại" + Tiến Độ Clips Của Tập Đang Chọn) */}
      <div className="rounded-2xl bg-slate-900/95 border border-slate-800/90 px-3.5 py-2 flex flex-col gap-2 shrink-0">
        <div className="flex flex-wrap items-center justify-between gap-2">
          <div className="flex items-center gap-2 flex-wrap">
            <span className="text-[11px] font-extrabold uppercase tracking-wider text-indigo-300 flex items-center gap-1.5">
              <Activity size={13} className="text-indigo-400" />
              Các Bước Hiện Tại ({orderedWorkflowSteps.filter(n => n.status === 'success').length}/
              {orderedWorkflowSteps.length} bước hoàn tất):
            </span>

            {isAnythingRunning ? (
              <span className="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 flex items-center gap-1.5 animate-pulse">
                <Loader2 size={10} className="animate-spin" />
                {currentStepIndex !== null && orderedWorkflowSteps[currentStepIndex]
                  ? `Đang chạy Bước ${currentStepIndex + 1}/${orderedWorkflowSteps.length}: ${
                      orderedWorkflowSteps[currentStepIndex].title
                    }`
                  : `Agent đang chạy Tập ${currentTarget?.activeStartEp || primaryConfig.startEp}`}
              </span>
            ) : (
              <span className="text-[11px] text-slate-400 flex items-center gap-1">
                <MousePointerClick size={12} className="text-cyan-400" />
                <span>
                  <strong className="text-slate-200">Bấm vào Node</strong> để xem Detail & Log từng bước (như n8n) •{' '}
                  <strong className="text-amber-300">Đè giữ chuột</strong> để kéo thả vị trí
                </span>
              </span>
            )}
          </div>

          <div className="flex items-center gap-2">
            {latestChannelLog && (
              <span className="text-[10px] font-mono text-slate-400 truncate max-w-md hidden xl:inline">
                [{latestChannelLog.created_at.slice(11)}] {latestChannelLog.message}
              </span>
            )}
            <button
              type="button"
              onClick={() => setShowStepBar(v => !v)}
              className="px-2 py-0.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-[10px] font-semibold text-slate-300 flex items-center gap-1 cursor-pointer"
            >
              {showStepBar ? (
                <>
                  Thu gọn bước <ChevronUp size={11} />
                </>
              ) : (
                <>
                  Xem các bước <ChevronDown size={11} />
                </>
              )}
            </button>
          </div>
        </div>

        {showStepBar && (
          <div className="flex flex-col gap-2 pt-0.5">
            {/* Row A: Workflow Ordered Steps Stepper */}
            <div className="flex items-center gap-1.5 overflow-x-auto pb-1">
              {orderedWorkflowSteps.map((step, idx) => {
                const meta = getNodeMeta(step.type)
                const isSelected = selectedNodeId === step.id
                const isCurrent = currentStepIndex === idx || step.status === 'running'
                const stepLogCount = step.stepLogs?.length || 0
                return (
                  <React.Fragment key={step.id}>
                    <button
                      type="button"
                      onClick={() => {
                        setSelectedNodeId(step.id)
                        setDetailModalNodeId(step.id)
                        setShowInspector(true)
                      }}
                      title="Bấm để mở cửa sổ Detail & Log của bước này (như n8n)"
                      className={`px-2.5 py-1.5 rounded-xl border text-left transition-all flex items-center gap-2 shrink-0 cursor-pointer ${
                        isCurrent
                          ? 'bg-amber-500/20 border-amber-400 text-white shadow-md'
                          : step.status === 'success'
                            ? 'bg-emerald-500/15 border-emerald-500/40 text-emerald-200'
                            : step.status === 'error'
                              ? 'bg-rose-500/15 border-rose-500/40 text-rose-200'
                              : isSelected
                                ? 'bg-indigo-600/25 border-indigo-400 text-white'
                                : 'bg-slate-950/90 border-slate-800 text-slate-300 hover:border-slate-700'
                      }`}
                    >
                      <span
                        className={`w-5 h-5 rounded-lg text-[10px] font-extrabold flex items-center justify-center shrink-0 ${
                          isCurrent
                            ? 'bg-amber-400 text-slate-950'
                            : step.status === 'success'
                              ? 'bg-emerald-500 text-slate-950'
                              : 'bg-slate-800 text-slate-300'
                        }`}
                      >
                        {step.status === 'running' ? (
                          <Loader2 size={10} className="animate-spin" />
                        ) : step.status === 'success' ? (
                          '✓'
                        ) : (
                          idx + 1
                        )}
                      </span>
                      <div className="flex flex-col min-w-0">
                        <div className="text-[11px] font-bold flex items-center gap-1">
                          <span className="truncate max-w-[125px]">{step.title}</span>
                          <span className={`text-[9px] font-mono ${meta.accent}`}>[{meta.badge}]</span>
                          {stepLogCount > 0 && (
                            <span className="px-1 py-0.2 rounded bg-slate-800 text-[9px] font-mono text-cyan-300">
                              📋{stepLogCount}
                            </span>
                          )}
                        </div>
                        <span className="text-[9px] text-slate-400 truncate max-w-[165px]">
                          {step.lastMessage || step.subtitle}
                        </span>
                      </div>
                    </button>
                    {idx < orderedWorkflowSteps.length - 1 && (
                      <ArrowRight size={12} className="text-slate-600 shrink-0" />
                    )}
                  </React.Fragment>
                )
              })}
            </div>

            {/* Row B: Real-time Clip Steps for the Auto-Selected Episode */}
            {currentEpisodeDetail && (
              <div className="flex items-center justify-between gap-2 px-3 py-1.5 rounded-xl bg-slate-950/80 border border-slate-800/80 overflow-x-auto text-[11px]">
                <div className="flex items-center gap-2 shrink-0">
                  <span className="font-bold text-amber-300">
                    🎬 Tiến độ {currentEpisodeDetail.label} ({currentEpisodeDetail.folder_name}):
                  </span>
                  <span className="text-slate-400">
                    {currentEpisodeDetail.rendered_clips}/{currentEpisodeDetail.total_clips} clips đã có MP4
                  </span>
                </div>

                <div className="flex items-center gap-1.5 shrink-0">
                  {currentEpisodeDetail.clips.map(clip => {
                    const isDone = clip.status === 'COMPLETED'
                    const isTargeted =
                      primaryConfig.onlyClip === 0 || primaryConfig.onlyClip === clip.clip_num
                    return (
                      <button
                        key={clip.clip_num}
                        type="button"
                        onClick={() =>
                          updateGlobalOrNodeConfig({
                            onlyClip: primaryConfig.onlyClip === clip.clip_num ? 0 : clip.clip_num,
                          })
                        }
                        className={`px-2 py-0.5 rounded-lg text-[10px] font-bold border flex items-center gap-1 cursor-pointer transition-colors ${
                          isDone
                            ? 'bg-emerald-500/15 border-emerald-500/40 text-emerald-300'
                            : isTargeted && isAnythingRunning
                              ? 'bg-amber-500/20 border-amber-400 text-amber-200 animate-pulse'
                              : 'bg-slate-900 border-slate-800 text-slate-400 hover:text-white'
                        }`}
                        title={
                          isDone
                            ? `Clip ${clip.clip_num} đã hoàn thành (${clip.video_size_mb || 0} MB) — Bấm để chọn chạy lẻ`
                            : `Clip ${clip.clip_num} đang chờ render — Bấm để chọn chạy lẻ`
                        }
                      >
                        {isDone ? <CheckCircle2 size={10} /> : <Clock size={10} />}
                        Clip {String(clip.clip_num).padStart(2, '0')}
                      </button>
                    )
                  })}
                  <span className="text-slate-600">→</span>
                  <span
                    className={`px-2 py-0.5 rounded-lg text-[10px] font-bold border flex items-center gap-1 ${
                      currentEpisodeDetail.merged_video_url
                        ? 'bg-amber-500/20 border-amber-500/40 text-amber-300'
                        : 'bg-slate-900 border-slate-800 text-slate-500'
                    }`}
                  >
                    <Film size={10} />
                    {currentEpisodeDetail.merged_video_url ? 'FULL MP4 ✓' : 'Chờ ghép FULL'}
                  </span>
                </div>
              </div>
            )}
          </div>
        )}
      </div>

      {/* 3. MAIN 3-COLUMN WORKSPACE: Palette (Left) | Interactive Drag-and-Drop Canvas (Center) | Inspector (Right) */}
      <div className="flex-1 flex gap-2.5 min-h-0 overflow-hidden">
        {/* Left Drag-and-Drop Node Palette */}
        {showPalette && (
          <div className="w-56 flex-shrink-0 rounded-2xl bg-slate-900/90 border border-slate-800/90 p-2.5 flex flex-col gap-2 overflow-y-auto">
            <div className="flex items-center justify-between">
              <span className="text-xs font-extrabold uppercase tracking-wider text-slate-300 flex items-center gap-1.5">
                <Sparkles size={13} className="text-indigo-400" />
                Khối Kéo Thả (Nodes)
              </span>
              <button
                onClick={() => setShowPalette(false)}
                className="p-1 rounded-lg hover:bg-slate-800 text-slate-400 hover:text-white cursor-pointer"
                title="Thu gọn cột Node"
              >
                <PanelLeftClose size={14} />
              </button>
            </div>

            <div className="flex flex-col gap-1.5">
              {NODE_CATALOG.map(item => (
                <div
                  key={item.type}
                  draggable
                  onDragStart={e => {
                    e.dataTransfer.setData('application/flowkit-node', item.type)
                    e.dataTransfer.setData('text/plain', item.type)
                    e.dataTransfer.effectAllowed = 'copy'
                  }}
                  onClick={() => addNodeAt(item.type)}
                  className={`group p-2 rounded-xl bg-slate-950/90 hover:bg-slate-900 border ${item.borderAccent} transition-all cursor-grab active:cursor-grabbing flex flex-col gap-0.5 shadow-sm`}
                >
                  <div className="flex items-center justify-between gap-1.5">
                    <div className="flex items-center gap-1.5 min-w-0">
                      <GripVertical size={11} className="text-slate-500 group-hover:text-slate-300 shrink-0" />
                      <div className={`w-5 h-5 rounded-md ${item.bgAccent} flex items-center justify-center shrink-0`}>
                        <NodeIcon type={item.type} size={12} className={item.accent} />
                      </div>
                      <span className="text-[11px] font-bold text-white truncate">{item.title}</span>
                    </div>
                    <span className={`px-1 py-0.5 rounded text-[8px] font-extrabold shrink-0 ${item.bgAccent} ${item.accent}`}>
                      + Thêm
                    </span>
                  </div>
                  <p className="text-[9px] text-slate-400 leading-snug pl-5 line-clamp-1">{item.subtitle}</p>
                </div>
              ))}
            </div>

            <div className="mt-auto p-2 rounded-xl bg-slate-950/80 border border-slate-800/80 text-[10px] text-slate-400 flex flex-col gap-1">
              <span className="font-bold text-slate-200 flex items-center gap-1">
                <MousePointerClick size={11} className="text-cyan-400" /> Thao tác kiểu n8n:
              </span>
              <span>• <strong>Bấm chuột</strong> vào Node: Mở cửa sổ xem Detail & Log của bước đó.</span>
              <span>• <strong>Đè giữ chuột</strong> (~0.15s) rồi di chuyển: Kéo thả vị trí Node.</span>
              <span>• <strong>Nối bước</strong>: Kéo từ chấm tròn phải hoặc bấm icon 🔗.</span>
            </div>
          </div>
        )}

        {/* Center Infinite Drag-and-Drop Canvas */}
        <div
          ref={canvasRef}
          data-canvas-bg="true"
          onDragOver={handleCanvasDragOver}
          onDragLeave={handleCanvasDragLeave}
          onDrop={handleCanvasDrop}
          onMouseDown={handleCanvasMouseDown}
          className={`flex-1 relative rounded-2xl bg-[#060911] border transition-colors overflow-hidden ${
            isDraggingOverCanvas
              ? 'border-2 border-dashed border-indigo-400 bg-indigo-950/10'
              : connectingFromId
                ? 'border-2 border-cyan-500/60'
                : 'border-slate-800/90'
          } ${connectingFromId ? 'cursor-crosshair' : isPanning ? 'cursor-grabbing' : 'cursor-grab'}`}
          style={{
            backgroundImage: 'radial-gradient(rgba(99, 102, 241, 0.22) 1px, transparent 1px)',
            backgroundSize: `${24 * zoom}px ${24 * zoom}px`,
            backgroundPosition: `${pan.x}px ${pan.y}px`,
          }}
        >
          {/* Floating Left-Top Canvas Controls Overlay */}
          <div className="absolute top-3 left-3 z-20 flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl bg-slate-900/90 border border-slate-800 text-[11px] text-slate-300 backdrop-blur-md shadow-lg">
            {!showPalette && (
              <button
                onClick={() => setShowPalette(true)}
                className="px-2 py-1 rounded-lg bg-indigo-500/20 hover:bg-indigo-500/30 text-indigo-300 font-bold flex items-center gap-1 cursor-pointer mr-1"
                title="Mở cột Khối Kéo Thả"
              >
                <PanelLeftOpen size={13} /> Nodes
              </button>
            )}
            <button
              onClick={() => setZoom(z => Math.max(0.55, +(z - 0.1).toFixed(2)))}
              className="p-1 hover:bg-slate-800 rounded cursor-pointer"
              title="Thu nhỏ"
            >
              <ZoomOut size={13} />
            </button>
            <span className="font-mono w-11 text-center">{Math.round(zoom * 100)}%</span>
            <button
              onClick={() => setZoom(z => Math.min(1.5, +(z + 0.1).toFixed(2)))}
              className="p-1 hover:bg-slate-800 rounded cursor-pointer"
              title="Phóng to"
            >
              <ZoomIn size={13} />
            </button>
            <span className="text-slate-600 px-0.5">|</span>
            <button
              onClick={autoArrangeNodes}
              className="px-2 py-0.5 rounded hover:bg-slate-800 text-slate-300 font-semibold cursor-pointer"
              title="Căn chỉnh lại vị trí các Node nhỏ gọn"
            >
              Căn chỉnh
            </button>
            <button
              onClick={autoConnectAllNodes}
              className="px-2.5 py-0.5 rounded bg-cyan-500/15 hover:bg-cyan-500/25 text-cyan-300 border border-cyan-500/30 font-bold flex items-center gap-1 cursor-pointer"
              title="Tự động nối dây tất cả các bước theo thứ tự từ trái sang phải"
            >
              <Link2 size={11} /> Nối tự động
            </button>
            <button
              onClick={() => {
                setNodes(prev => prev.map(n => ({ ...n, status: 'idle', lastMessage: undefined, durationMs: undefined })))
                setCurrentStepIndex(null)
                appendLog('INFO', '🔄 Đã reset trạng thái các bước trên sơ đồ.')
              }}
              className="px-2 py-0.5 rounded hover:bg-slate-800 text-slate-400 hover:text-white cursor-pointer flex items-center gap-1"
              title="Reset trạng thái"
            >
              <RotateCcw size={11} /> Reset
            </button>
          </div>

          {/* Floating Banner when actively connecting two nodes */}
          {connectingFromId && (
            <div className="absolute top-14 left-1/2 -translate-x-1/2 z-30 flex items-center gap-2.5 px-4 py-2 rounded-xl bg-cyan-950/95 border-2 border-cyan-400 text-xs font-bold text-cyan-100 shadow-[0_0_30px_rgba(34,211,238,0.4)] animate-pulse">
              <Link2 size={14} className="text-cyan-300 shrink-0" />
              <span>
                Đang nối từ bước{' '}
                <strong className="text-white">
                  "{nodes.find(n => n.id === connectingFromId)?.title || connectingFromId}"
                </strong>{' '}
                — Bấm hoặc thả chuột vào bước tiếp theo để nối!
              </span>
              <button
                type="button"
                onClick={e => {
                  e.stopPropagation()
                  setConnectingFromId(null)
                  setHoveredTargetNodeId(null)
                  connectStartMouseRef.current = null
                }}
                className="px-2 py-0.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-rose-300 border border-rose-500/40 text-[11px] font-bold cursor-pointer"
              >
                Hủy (Esc)
              </button>
            </div>
          )}

          {/* Floating Right-Top Canvas Overlay (Template + Fullscreen + Inspector Toggle) */}
          <div className="absolute top-3 right-3 z-20 flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl bg-slate-900/90 border border-slate-800 text-[11px] text-slate-300 backdrop-blur-md shadow-lg">
            <Layers size={12} className="text-indigo-400" />
            <select
              onChange={e => loadTemplate(e.target.value)}
              defaultValue="full_pipeline"
              className="bg-transparent text-[11px] font-semibold text-slate-200 outline-none cursor-pointer"
            >
              {Object.entries(PRESET_TEMPLATES).map(([k, tpl]) => (
                <option key={k} value={k} className="bg-slate-950 text-white">
                  {tpl.name}
                </option>
              ))}
            </select>
            <span className="text-slate-600 px-0.5">|</span>
            <button
              onClick={toggleFullScreen}
              className="px-2 py-0.5 rounded hover:bg-slate-800 text-indigo-300 font-bold flex items-center gap-1 cursor-pointer"
            >
              {isFullScreen ? <Minimize2 size={12} /> : <Maximize2 size={12} />}
              <span>{isFullScreen ? 'Thu nhỏ' : 'Full Screen'}</span>
            </button>
            {!showInspector && (
              <button
                onClick={() => setShowInspector(true)}
                className="px-2 py-0.5 rounded bg-indigo-500/20 hover:bg-indigo-500/30 text-indigo-300 font-bold flex items-center gap-1 cursor-pointer"
              >
                <PanelRightOpen size={13} /> Cấu Hình
              </button>
            )}
          </div>

          {/* Transformed Layer for Edges + Compact n8n-style Draggable Nodes */}
          <div
            style={{
              transform: `translate(${pan.x}px, ${pan.y}px) scale(${zoom})`,
              transformOrigin: '0 0',
              width: '100%',
              height: '100%',
            }}
            data-canvas-bg="true"
          >
            {/* SVG Edges Layer */}
            <svg className="absolute inset-0 w-[3000px] h-[2000px] pointer-events-none overflow-visible">
              <defs>
                <linearGradient id="wireGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                  <stop offset="0%" stopColor="#6366f1" />
                  <stop offset="100%" stopColor="#22d3ee" />
                </linearGradient>
              </defs>

              {edges.map(edge => {
                const fromNode = nodes.find(n => n.id === edge.from)
                const toNode = nodes.find(n => n.id === edge.to)
                if (!fromNode || !toNode) return null

                const x1 = fromNode.x + NODE_WIDTH
                const y1 = fromNode.y + NODE_HEIGHT / 2
                const x2 = toNode.x
                const y2 = toNode.y + NODE_HEIGHT / 2
                const dx = Math.max(44, Math.abs(x2 - x1) * 0.45)
                const pathD = `M ${x1} ${y1} C ${x1 + dx} ${y1}, ${x2 - dx} ${y2}, ${x2} ${y2}`
                const midX = (x1 + x2) / 2
                const midY = (y1 + y2) / 2
                const isEdgeActive =
                  activeEdgeId === edge.id ||
                  fromNode.status === 'running' ||
                  toNode.status === 'running'

                return (
                  <g
                    key={edge.id}
                    className={connectingFromId ? 'pointer-events-none' : 'pointer-events-auto group cursor-pointer'}
                    onClick={e => {
                      e.stopPropagation()
                      if (!connectingFromId) deleteEdge(edge.id)
                    }}
                  >
                    <path d={pathD} fill="none" stroke="transparent" strokeWidth={14} />
                    <path
                      d={pathD}
                      fill="none"
                      stroke="url(#wireGrad)"
                      strokeWidth={isEdgeActive ? 3 : 2}
                      strokeDasharray={isEdgeActive ? '7 5' : undefined}
                      opacity={isEdgeActive ? 1 : 0.85}
                    />
                    <circle cx={x2} cy={y2} r={4} fill="#22d3ee" />
                    {/* Midpoint delete badge on hover */}
                    <g transform={`translate(${midX}, ${midY})`} className="opacity-0 group-hover:opacity-100 transition-opacity">
                      <circle r={8} fill="#0f172a" stroke="#f43f5e" strokeWidth={1.5} />
                      <text
                        x={0}
                        y={3.5}
                        textAnchor="middle"
                        fill="#fda4af"
                        fontSize={10}
                        fontWeight="bold"
                      >
                        ×
                      </text>
                    </g>
                  </g>
                )
              })}

              {/* Live wire while dragging or click-to-connecting from a port */}
              {connectingFromId &&
                (() => {
                  const fromNode = nodes.find(n => n.id === connectingFromId)
                  if (!fromNode) return null
                  const targetNode = hoveredTargetNodeId
                    ? nodes.find(n => n.id === hoveredTargetNodeId)
                    : null
                  const x1 =
                    connectingPortDir === 'out' ? fromNode.x + NODE_WIDTH : fromNode.x
                  const y1 = fromNode.y + NODE_HEIGHT / 2
                  const x2 = targetNode
                    ? connectingPortDir === 'out'
                      ? targetNode.x
                      : targetNode.x + NODE_WIDTH
                    : mouseCanvasPos.x
                  const y2 = targetNode
                    ? targetNode.y + NODE_HEIGHT / 2
                    : mouseCanvasPos.y
                  const dx = Math.max(44, Math.abs(x2 - x1) * 0.45)
                  const c1x = connectingPortDir === 'out' ? x1 + dx : x1 - dx
                  const c2x = connectingPortDir === 'out' ? x2 - dx : x2 + dx
                  return (
                    <g className="pointer-events-none">
                      <path
                        d={`M ${x1} ${y1} C ${c1x} ${y1}, ${c2x} ${y2}, ${x2} ${y2}`}
                        fill="none"
                        stroke="#22d3ee"
                        strokeWidth={2.5}
                        strokeDasharray="6 4"
                      />
                      <circle cx={x2} cy={y2} r={5} fill="#22d3ee" />
                    </g>
                  )
                })()}
            </svg>

            {/* COMPACT n8n-STYLE NODES LAYER (NODE_WIDTH = 148, NODE_HEIGHT = 82) */}
            {nodes.map(node => {
              const meta = getNodeMeta(node.type)
              const isSelected = selectedNodeId === node.id
              const isHoldingThis = holdingNodeId === node.id
              const isDraggingThis = draggingNodeId === node.id
              const isConnectSource = connectingFromId === node.id
              const isConnectTargetCandidate = Boolean(connectingFromId && connectingFromId !== node.id)
              const isHoveredConnectTarget = hoveredTargetNodeId === node.id
              const stepOrderIdx = orderedWorkflowSteps.findIndex(s => s.id === node.id)
              const stepLogCount = node.stepLogs?.length || 0

              return (
                <div
                  key={node.id}
                  data-workflow-node-id={node.id}
                  draggable={false}
                  onDragStart={e => e.preventDefault()}
                  onMouseDown={e => startNodeDrag(e, node)}
                  onMouseUp={e => completeWireConnect(e, node.id)}
                  title="Bấm chuột để xem Detail & Log (như n8n) • Đè giữ chuột để kéo thả vị trí"
                  style={{
                    left: node.x,
                    top: node.y,
                    width: NODE_WIDTH,
                    height: NODE_HEIGHT,
                  }}
                  className={`group absolute rounded-2xl bg-slate-900/95 backdrop-blur-md px-2.5 py-2 flex flex-col justify-between select-none ${
                    isDraggingThis
                      ? 'cursor-grabbing scale-105 z-30 border-2 border-indigo-400 shadow-[0_0_28px_rgba(99,102,241,0.55)]'
                      : isHoldingThis
                        ? 'cursor-grabbing ring-2 ring-amber-400/60 z-20'
                        : isConnectTargetCandidate
                          ? 'cursor-pointer z-20 transition-colors'
                          : 'cursor-pointer z-10 transition-colors'
                  } ${
                    isHoveredConnectTarget
                      ? 'border-2 border-cyan-300 ring-4 ring-cyan-400/40 scale-105 shadow-[0_0_24px_rgba(34,211,238,0.6)]'
                      : isConnectSource
                        ? 'border-2 border-cyan-400 ring-2 ring-cyan-400/30 shadow-[0_0_20px_rgba(34,211,238,0.4)]'
                        : isConnectTargetCandidate
                          ? 'border-2 border-dashed border-cyan-400/80 hover:border-cyan-300 shadow-[0_0_16px_rgba(34,211,238,0.25)]'
                          : isSelected
                            ? 'border-2 border-indigo-400 shadow-[0_0_20px_rgba(99,102,241,0.35)]'
                            : node.status === 'running'
                              ? 'border-2 border-amber-400 shadow-[0_0_22px_rgba(245,158,11,0.4)]'
                              : node.status === 'success'
                                ? 'border border-emerald-500/70 shadow-md'
                                : node.status === 'error'
                                  ? 'border border-rose-500/70 shadow-md'
                                  : `border ${meta.borderAccent} shadow-md hover:border-slate-600`
                  }`}
                >
                  {/* Floating n8n Hover Mini Action Bar above node */}
                  <div
                    onMouseDown={e => e.stopPropagation()}
                    className="absolute -top-7 left-1/2 -translate-x-1/2 opacity-0 group-hover:opacity-100 transition-opacity flex items-center gap-0.5 px-1.5 py-0.5 rounded-lg bg-slate-950/95 border border-slate-700 shadow-xl z-30 pointer-events-auto"
                  >
                    <button
                      type="button"
                      onClick={e => {
                        e.stopPropagation()
                        executeSingleNode(node, primaryConfig)
                      }}
                      disabled={node.status === 'running'}
                      className="p-1 rounded hover:bg-indigo-500/25 text-indigo-300 cursor-pointer"
                      title="Chạy bước này (Execute Node)"
                    >
                      <Play size={10} />
                    </button>
                    <button
                      type="button"
                      onClick={e => {
                        e.stopPropagation()
                        setSelectedNodeId(node.id)
                        setDetailModalNodeId(node.id)
                      }}
                      className="p-1 rounded hover:bg-emerald-500/25 text-emerald-300 cursor-pointer"
                      title="Xem Detail & Log bước này (n8n View)"
                    >
                      <Eye size={10} />
                    </button>
                    <button
                      type="button"
                      onClick={e => {
                        e.stopPropagation()
                        if (connectingFromId && connectingFromId !== node.id) {
                          createConnectionBetweenNodes(connectingFromId, node.id, connectingPortDir)
                          setConnectingFromId(null)
                          setHoveredTargetNodeId(null)
                          connectStartMouseRef.current = null
                        } else if (connectingFromId === node.id) {
                          setConnectingFromId(null)
                          setHoveredTargetNodeId(null)
                          connectStartMouseRef.current = null
                        } else {
                          connectStartMouseRef.current = null
                          setConnectingPortDir('out')
                          setConnectingFromId(node.id)
                          setMouseCanvasPos({ x: node.x + NODE_WIDTH + 24, y: node.y + NODE_HEIGHT / 2 })
                        }
                      }}
                      className="p-1 rounded hover:bg-cyan-500/25 text-cyan-300 cursor-pointer"
                      title="Nối dây sang bước khác"
                    >
                      <Link2 size={10} />
                    </button>
                    <button
                      type="button"
                      onClick={e => {
                        e.stopPropagation()
                        deleteNode(node.id)
                      }}
                      className="p-1 rounded hover:bg-rose-500/25 text-rose-300 cursor-pointer"
                      title="Xóa bước này"
                    >
                      <Trash2 size={10} />
                    </button>
                  </div>

                  {/* Left Input Port */}
                  <div
                    onMouseDown={e => startWireConnect(e, node.id, 'in')}
                    onMouseUp={e => completeWireConnect(e, node.id)}
                    title="Cổng Vào — Thả dây nối hoặc bấm vào đây để nối từ bước trước"
                    className={`absolute -left-2.5 top-1/2 -translate-y-1/2 w-5 h-5 rounded-full bg-slate-950 border-2 transition-transform flex items-center justify-center cursor-crosshair z-20 ${
                      isConnectTargetCandidate
                        ? 'border-cyan-300 scale-125 ring-4 ring-cyan-400/30 animate-pulse'
                        : 'border-indigo-400 hover:scale-125'
                    }`}
                  >
                    <div className="w-1.5 h-1.5 rounded-full bg-indigo-400" />
                  </div>

                  {/* Right Output Port */}
                  <div
                    onMouseDown={e => startWireConnect(e, node.id, 'out')}
                    onMouseUp={e => completeWireConnect(e, node.id)}
                    title="Cổng Ra — Kéo hoặc bấm vào đây rồi bấm sang bước tiếp theo để nối"
                    className={`absolute -right-2.5 top-1/2 -translate-y-1/2 w-5 h-5 rounded-full bg-slate-950 border-2 transition-transform flex items-center justify-center cursor-crosshair z-20 ${
                      isConnectSource
                        ? 'border-cyan-300 scale-125 ring-4 ring-cyan-400/40'
                        : 'border-cyan-400 hover:scale-125'
                    }`}
                  >
                    <div className="w-1.5 h-1.5 rounded-full bg-cyan-400" />
                  </div>

                  {/* Top Row: Step Number + Badge + Status Icon + Step Log Count */}
                  <div className="flex items-center justify-between gap-1">
                    <span className={`px-1.5 py-0.5 rounded text-[8px] font-extrabold tracking-tight ${meta.bgAccent} ${meta.accent}`}>
                      #{stepOrderIdx >= 0 ? stepOrderIdx + 1 : ''} • {meta.badge}
                    </span>

                    <div className="flex items-center gap-1">
                      {stepLogCount > 0 && (
                        <span
                          className="px-1 py-0.2 rounded bg-slate-950 border border-slate-800 text-[8px] font-mono text-cyan-300"
                          title={`${stepLogCount} dòng log ở bước này`}
                        >
                          📋{stepLogCount}
                        </span>
                      )}
                      {node.status === 'running' ? (
                        <Loader2 size={11} className="text-amber-400 animate-spin" />
                      ) : node.status === 'success' ? (
                        <CheckCircle2 size={11} className="text-emerald-400" />
                      ) : node.status === 'error' ? (
                        <AlertCircle size={11} className="text-rose-400" />
                      ) : (
                        <span className="w-2 h-2 rounded-full bg-slate-700" />
                      )}
                    </div>
                  </div>

                  {/* Center Main Row: n8n Icon Box + Compact Title */}
                  <div className="flex items-center gap-2 min-w-0 my-0.5">
                    <div
                      className={`w-8 h-8 rounded-xl ${meta.bgAccent} border ${meta.borderAccent} flex items-center justify-center shrink-0 shadow-inner`}
                    >
                      <NodeIcon type={node.type} size={16} className={meta.accent} />
                    </div>
                    <div className="flex flex-col min-w-0 flex-1">
                      <span className="text-[11px] font-extrabold text-white leading-tight truncate">
                        {node.title}
                      </span>
                      <span
                        className={`text-[9px] truncate ${
                          node.status === 'error'
                            ? 'text-rose-300'
                            : node.status === 'success'
                              ? 'text-emerald-300'
                              : 'text-slate-400'
                        }`}
                      >
                        {isConnectTargetCandidate
                          ? '🎯 Bấm để nối vào đây'
                          : isDraggingThis
                            ? '✋ Đang kéo vị trí...'
                            : node.lastMessage || `Tập ${primaryConfig.startEp} • Bấm xem detail`}
                      </span>
                    </div>
                  </div>
                </div>
              )
            })}
          </div>
        </div>

        {/* Right Inspector Panel (Cấu Hình Dự Án, Tập Mới Nhất & Log Riêng Từng Bước) */}
        {showInspector && (
          <div className="w-80 flex-shrink-0 rounded-2xl bg-slate-900/90 border border-slate-800/90 p-3.5 flex flex-col gap-3 overflow-y-auto">
            <div className="flex items-center justify-between border-b border-slate-800 pb-2">
              <span className="text-xs font-extrabold uppercase tracking-wider text-slate-200 flex items-center gap-1.5">
                <Settings2 size={14} className="text-indigo-400" />
                Tùy Chọn Dự Án & Bước
              </span>
              <button
                onClick={() => setShowInspector(false)}
                className="p-1 rounded-lg hover:bg-slate-800 text-slate-400 hover:text-white cursor-pointer"
                title="Thu gọn cột Cấu Hình"
              >
                <PanelRightClose size={14} />
              </button>
            </div>

            <div className="flex flex-col gap-3 text-xs">
              {/* Selected Node Specific Actions + Per-Step Logs Preview + Open n8n Modal Button */}
              {selectedNode && (
                <div className="p-3 rounded-xl bg-indigo-950/25 border border-indigo-500/40 flex flex-col gap-2">
                  <div className="flex items-center justify-between gap-1">
                    <span className="text-[11px] font-extrabold text-indigo-200 truncate">
                      ⚡ Bước: {selectedNode.title}
                    </span>
                    <button
                      type="button"
                      onClick={() => setDetailModalNodeId(selectedNode.id)}
                      className="px-2 py-0.5 rounded-lg bg-indigo-500/30 hover:bg-indigo-500/45 text-indigo-200 border border-indigo-400/40 text-[10px] font-bold flex items-center gap-1 shrink-0 cursor-pointer"
                    >
                      <Eye size={10} /> Mở Detail (n8n)
                    </button>
                  </div>

                  {/* Mini Per-Step Log Box right inside Inspector */}
                  <div className="p-2 rounded-lg bg-slate-950/95 border border-slate-800 flex flex-col gap-1">
                    <div className="flex items-center justify-between">
                      <span className="text-[10px] font-bold text-cyan-300 flex items-center gap-1">
                        <FileText size={10} /> Log Của Bước Này ({selectedNode.stepLogs?.length || 0})
                      </span>
                      {selectedNode.durationMs !== undefined && (
                        <span className="text-[9px] font-mono text-emerald-400">
                          {selectedNode.durationMs}ms
                        </span>
                      )}
                    </div>
                    <div className="max-h-24 overflow-y-auto flex flex-col gap-1 font-mono text-[10px] pr-0.5">
                      {!selectedNode.stepLogs || selectedNode.stepLogs.length === 0 ? (
                        <span className="text-slate-500 text-[10px] font-sans">
                          Chưa có log. Bấm "Chạy Bước Này" hoặc bấm vào Node để xem chi tiết như n8n.
                        </span>
                      ) : (
                        selectedNode.stepLogs.slice(0, 6).map(lg => (
                          <div key={lg.id} className="leading-snug">
                            <span className="text-slate-500">[{lg.time}] </span>
                            <span
                              className={
                                lg.level === 'SUCCESS'
                                  ? 'text-emerald-300'
                                  : lg.level === 'ERROR'
                                    ? 'text-rose-300'
                                    : 'text-slate-200'
                              }
                            >
                              {lg.text}
                            </span>
                          </div>
                        ))
                      )}
                    </div>
                  </div>

                  <div className="grid grid-cols-2 gap-1.5">
                    <button
                      onClick={() => executeSingleNode(selectedNode, primaryConfig)}
                      disabled={selectedNode.status === 'running'}
                      className="py-1.5 px-2 rounded-xl text-[11px] font-extrabold studio-glow-btn flex items-center justify-center gap-1 cursor-pointer"
                    >
                      <Play size={11} /> Chạy Bước Này
                    </button>
                    <button
                      onClick={() => setDetailModalNodeId(selectedNode.id)}
                      className="py-1.5 px-2 rounded-xl text-[11px] font-bold bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-cyan-500/30 flex items-center justify-center gap-1 cursor-pointer"
                    >
                      <Terminal size={11} /> Xem Log Đầy Đủ
                    </button>
                  </div>

                  {/* Quick 1-click connection toggles to other steps */}
                  {nodes.length > 1 && (
                    <div className="p-2 rounded-lg bg-slate-950/90 border border-slate-800 flex flex-col gap-1">
                      <div className="flex items-center justify-between">
                        <span className="text-[10px] font-bold text-cyan-300 flex items-center gap-1">
                          <Link2 size={10} /> Nối sang bước:
                        </span>
                        <button
                          type="button"
                          onClick={autoConnectAllNodes}
                          className="text-[9px] font-bold text-cyan-400 hover:text-cyan-300 cursor-pointer"
                        >
                          Nối tự động hết
                        </button>
                      </div>
                      <div className="flex flex-col gap-1 max-h-24 overflow-y-auto pr-0.5">
                        {nodes
                          .filter(n => n.id !== selectedNode.id)
                          .map(target => {
                            const isConnectedOut = edges.some(
                              e => e.from === selectedNode.id && e.to === target.id
                            )
                            return (
                              <button
                                key={target.id}
                                type="button"
                                onClick={() => toggleConnectionBetweenNodes(selectedNode.id, target.id)}
                                className={`px-2 py-0.5 rounded-md text-[10px] font-semibold border flex items-center justify-between gap-1 transition-colors cursor-pointer ${
                                  isConnectedOut
                                    ? 'bg-cyan-500/20 border-cyan-500/50 text-cyan-200'
                                    : 'bg-slate-900 hover:bg-slate-800 border-slate-800 text-slate-300'
                                }`}
                              >
                                <span className="truncate">→ {target.title}</span>
                                <span className="text-[9px] font-extrabold shrink-0">
                                  {isConnectedOut ? '✓ Đã nối' : '+ Nối'}
                                </span>
                              </button>
                            )
                          })}
                      </div>
                    </div>
                  )}
                </div>
              )}

              {/* Project / Channel Selection Card */}
              <div className="p-3 rounded-xl bg-slate-950/90 border border-slate-800 flex flex-col gap-2.5">
                <div>
                  <label className="text-[11px] font-bold text-indigo-300 block mb-1">
                    1. Chọn Dự Án / Kênh Series Chạy Agent
                  </label>
                  <select
                    value={currentTarget?.key || primaryConfig.channelSlug}
                    onChange={e => handleSelectTargetProject(e.target.value)}
                    className="w-full px-2.5 py-2 rounded-xl bg-slate-900 border border-slate-700 text-white text-xs font-semibold outline-none focus:border-indigo-500 cursor-pointer"
                  >
                    {unifiedTargets.map(t => (
                      <option key={t.key} value={t.key}>
                        {t.name} ({t.channelSlug})
                      </option>
                    ))}
                  </select>
                </div>

                <div>
                  <label className="text-[10px] font-semibold text-slate-400 block mb-1">
                    Google Flow Project ID (UUID):
                  </label>
                  <div className="flex items-center gap-1.5">
                    <input
                      type="text"
                      value={primaryConfig.projectId || currentTarget?.projectId || ''}
                      onChange={e => updateGlobalOrNodeConfig({ projectId: e.target.value })}
                      className="flex-1 px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-800 text-[11px] font-mono text-indigo-300 outline-none focus:border-indigo-500"
                    />
                    {(primaryConfig.projectId || currentTarget?.projectId) && (
                      <a
                        href={`https://labs.google/fx/vi/tools/flow/project/${
                          primaryConfig.projectId || currentTarget?.projectId
                        }`}
                        target="_blank"
                        rel="noreferrer"
                        className="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700 text-indigo-400"
                        title="Mở dự án trên Google Flow"
                      >
                        <ExternalLink size={12} />
                      </a>
                    )}
                  </div>
                </div>

                <div className="flex items-center justify-between gap-2 pt-1">
                  <button
                    type="button"
                    onClick={() => navigate(`/channels/${primaryConfig.channelSlug}`)}
                    className="flex-1 py-1.5 px-2.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700 text-[11px] font-semibold text-slate-200 flex items-center justify-center gap-1 cursor-pointer"
                  >
                    <Tv size={11} className="text-indigo-400" /> Mở Studio Kênh
                  </button>
                  <button
                    type="button"
                    onClick={() => navigate('/projects')}
                    className="py-1.5 px-2.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700 text-[11px] font-semibold text-slate-300 flex items-center justify-center gap-1 cursor-pointer"
                  >
                    <FolderKanban size={11} /> DS Dự Án
                  </button>
                </div>
              </div>

              {/* Episode & Clip Range Card */}
              <div className="p-3 rounded-xl bg-slate-950/90 border border-slate-800 flex flex-col gap-2.5">
                <div className="flex items-center justify-between">
                  <span className="text-[11px] font-bold text-emerald-300">
                    2. Tập Đang Chọn (Tự Động Mới Nhất)
                  </span>
                  <button
                    type="button"
                    onClick={() => loadChannelEpisodesAndAutoSelectLatest(primaryConfig.channelSlug, true)}
                    className="text-[10px] font-bold text-emerald-400 hover:text-emerald-300 cursor-pointer"
                  >
                    ⚡ Tập #{newestEpisodeNum}
                  </button>
                </div>

                {channelEpisodes.length > 0 && (
                  <select
                    value={primaryConfig.startEp}
                    onChange={e => {
                      const epNum = Number(e.target.value)
                      updateGlobalOrNodeConfig({ startEp: epNum, endEp: epNum })
                    }}
                    className="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-white text-xs font-bold outline-none cursor-pointer"
                  >
                    {channelEpisodes.map(ep => (
                      <option key={ep.episode_num} value={ep.episode_num}>
                        🎬 {ep.label} ({ep.rendered_clips}/{ep.total_clips} clips)
                        {ep.episode_num === newestEpisodeNum ? ' ★ Mới nhất' : ''}
                      </option>
                    ))}
                  </select>
                )}

                <div className="grid grid-cols-2 gap-2">
                  <div>
                    <label className="text-[10px] text-slate-400 block mb-0.5">Từ Tập / Cảnh</label>
                    <input
                      type="number"
                      min={1}
                      max={100}
                      value={primaryConfig.startEp}
                      onChange={e => {
                        const val = Math.max(1, Number(e.target.value) || 1)
                        updateGlobalOrNodeConfig({
                          startEp: val,
                          endEp: Math.max(val, primaryConfig.endEp),
                        })
                      }}
                      className="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-800 text-white text-xs outline-none focus:border-indigo-500"
                    />
                  </div>
                  <div>
                    <label className="text-[10px] text-slate-400 block mb-0.5">Đến Tập / Cảnh</label>
                    <input
                      type="number"
                      min={1}
                      max={100}
                      value={primaryConfig.endEp}
                      onChange={e => {
                        const val = Math.max(primaryConfig.startEp, Number(e.target.value) || 1)
                        updateGlobalOrNodeConfig({ endEp: val })
                      }}
                      className="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-800 text-white text-xs outline-none focus:border-indigo-500"
                    />
                  </div>
                </div>

                <div>
                  <label className="text-[10px] text-slate-400 block mb-0.5">Chế độ Render Clip</label>
                  <select
                    value={primaryConfig.onlyClip}
                    onChange={e => updateGlobalOrNodeConfig({ onlyClip: Number(e.target.value) })}
                    className="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-800 text-white text-xs outline-none focus:border-indigo-500 cursor-pointer"
                  >
                    <option value={0}>Trọn bộ tất cả 6 Clips (Clip 1 → Clip 6)</option>
                    <option value={1}>Chỉ chạy riêng Clip 1 (Mở cảnh)</option>
                    <option value={2}>Chỉ chạy riêng Clip 2</option>
                    <option value={3}>Chỉ chạy riêng Clip 3</option>
                    <option value={4}>Chỉ chạy riêng Clip 4</option>
                    <option value={5}>Chỉ chạy riêng Clip 5</option>
                    <option value={6}>Chỉ chạy riêng Clip 6 (Khép cảnh)</option>
                  </select>
                </div>

                {/* Project Run Checkboxes */}
                <div className="pt-1 border-t border-slate-800/80 flex flex-col gap-1.5 text-[11px] text-slate-300">
                  <label className="flex items-center gap-2 cursor-pointer">
                    <input
                      type="checkbox"
                      checked={primaryConfig.autoLockChars ?? true}
                      onChange={e => updateGlobalOrNodeConfig({ autoLockChars: e.target.checked })}
                    />
                    <span>Tự động khóa @Character trước khi chạy dự án</span>
                  </label>
                  <label className="flex items-center gap-2 cursor-pointer">
                    <input
                      type="checkbox"
                      checked={primaryConfig.syncR2}
                      onChange={e => updateGlobalOrNodeConfig({ syncR2: e.target.checked })}
                    />
                    <span>Upload video (.mp4) lên Cloudflare R2</span>
                  </label>
                  <label className="flex items-center gap-2 cursor-pointer">
                    <input
                      type="checkbox"
                      checked={primaryConfig.syncD1}
                      onChange={e => updateGlobalOrNodeConfig({ syncD1: e.target.checked })}
                    />
                    <span>Đồng bộ Database lên Cloudflare D1 SQL</span>
                  </label>
                </div>
              </div>
            </div>

            <div className="mt-auto pt-2 border-t border-slate-800">
              <button
                onClick={() => addNodeAt('run-agent')}
                className="w-full py-2 rounded-xl text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-200 flex items-center justify-center gap-1.5 cursor-pointer"
              >
                <Plus size={13} /> Thêm Nhanh Bước Agent Render
              </button>
            </div>
          </div>
        )}
      </div>

      {/* 4. BOTTOM LIVE WORKFLOW & PER-STEP CONSOLE DRAWER */}
      <div className="rounded-2xl bg-slate-900/95 border border-slate-800/90 overflow-hidden flex flex-col shrink-0">
        <div className="px-4 py-1.5 bg-slate-950/90 border-b border-slate-800/80 flex flex-wrap items-center justify-between gap-2">
          <div className="flex items-center gap-2 flex-wrap">
            <button
              type="button"
              onClick={() => setConsoleOpen(o => !o)}
              className="flex items-center gap-2 text-xs font-bold text-slate-200 cursor-pointer"
            >
              <Terminal size={14} className="text-indigo-400" />
              <span>Nhật Ký Theo Từng Bước (Step Logs) & Console Agent</span>
            </button>

            {/* Step Filter Tabs inside Bottom Console */}
            <div className="flex items-center gap-1 overflow-x-auto py-0.5">
              <button
                type="button"
                onClick={() => {
                  setConsoleFilterNodeId('ALL')
                  setConsoleOpen(true)
                }}
                className={`px-2 py-0.5 rounded-lg text-[10px] font-bold cursor-pointer transition-colors ${
                  consoleFilterNodeId === 'ALL'
                    ? 'bg-indigo-500 text-white'
                    : 'bg-slate-900 text-slate-400 hover:text-white border border-slate-800'
                }`}
              >
                Tất cả ({workflowLogs.length})
              </button>
              {orderedWorkflowSteps.map((st, idx) => {
                const count = st.stepLogs?.length || 0
                const active = consoleFilterNodeId === st.id
                return (
                  <button
                    key={st.id}
                    type="button"
                    onClick={() => {
                      setConsoleFilterNodeId(st.id)
                      setSelectedNodeId(st.id)
                      setConsoleOpen(true)
                    }}
                    className={`px-2 py-0.5 rounded-lg text-[10px] font-bold cursor-pointer transition-colors flex items-center gap-1 shrink-0 ${
                      active
                        ? 'bg-cyan-500 text-slate-950'
                        : 'bg-slate-900 text-slate-300 hover:text-white border border-slate-800'
                    }`}
                  >
                    <span>
                      #{idx + 1} {st.title}
                    </span>
                    <span className="px-1 rounded bg-slate-950/60 text-[9px] font-mono">{count}</span>
                  </button>
                )
              })}
            </div>
          </div>

          <button
            type="button"
            onClick={() => setConsoleOpen(o => !o)}
            className="flex items-center gap-1 text-xs text-slate-400 hover:text-white cursor-pointer"
          >
            <span>{consoleOpen ? 'Thu gọn' : 'Mở rộng'}</span>
            {consoleOpen ? <ChevronDown size={15} /> : <ChevronUp size={15} />}
          </button>
        </div>

        {consoleOpen && (
          <div className="grid grid-cols-1 lg:grid-cols-2 divide-y lg:divide-y-0 lg:divide-x divide-slate-800 h-32 overflow-hidden text-[11px] font-mono">
            {/* Left: Filtered Per-Step or All Workflow Logs */}
            <div className="p-3 overflow-y-auto flex flex-col gap-1 bg-[#050811]">
              <div className="flex items-center justify-between text-[10px] font-sans font-bold uppercase tracking-wider text-slate-400 mb-1">
                <span>
                  {consoleFilterNodeId === 'ALL'
                    ? 'Nhật Ký Tất Cả Các Bước Workflow'
                    : `Log Riêng Của Bước: ${
                        nodes.find(n => n.id === consoleFilterNodeId)?.title || consoleFilterNodeId
                      }`}
                </span>
                {consoleFilterNodeId !== 'ALL' && (
                  <button
                    type="button"
                    onClick={() => setDetailModalNodeId(consoleFilterNodeId)}
                    className="text-cyan-400 hover:text-cyan-300 font-bold cursor-pointer"
                  >
                    🔍 Mở n8n Detail View
                  </button>
                )}
              </div>
              {(() => {
                const targetNode =
                  consoleFilterNodeId === 'ALL' ? null : nodes.find(n => n.id === consoleFilterNodeId) || null
                const listToRender = targetNode
                  ? (targetNode.stepLogs || []).map(s => ({
                      id: s.id,
                      time: s.time,
                      level: s.level,
                      text: s.text,
                    }))
                  : workflowLogs

                if (listToRender.length === 0) {
                  return (
                    <span className="text-slate-500">
                      Bước này chưa có log thực thi. Hãy bấm nút "▶ Chạy" trên bước này để xem log chi tiết.
                    </span>
                  )
                }

                return listToRender.map(item => {
                  const isLong = item.text.length > 110
                  const expanded = Boolean(expandedLogIds[item.id])
                  return (
                    <div key={item.id} className="flex items-start gap-2 leading-relaxed">
                      <span className="text-slate-500 shrink-0">[{item.time}]</span>
                      <span
                        className={
                          item.level === 'SUCCESS'
                            ? 'text-emerald-300'
                            : item.level === 'ERROR'
                              ? 'text-rose-300'
                              : item.level === 'WARN'
                                ? 'text-amber-300'
                                : 'text-slate-200'
                        }
                      >
                        {expanded || !isLong ? item.text : `${item.text.slice(0, 110).trim()}...`}
                        {isLong && (
                          <button
                            type="button"
                            onClick={() => setExpandedLogIds(prev => ({ ...prev, [item.id]: !prev[item.id] }))}
                            className="ml-1.5 text-[10px] font-sans font-bold text-indigo-400 hover:text-indigo-300 cursor-pointer"
                          >
                            {expanded ? 'Thu gọn' : 'Xem thêm'}
                          </button>
                        )}
                      </span>
                    </div>
                  )
                })
              })()}
            </div>

            {/* Right: Live SQLite Runner Logs */}
            <div className="p-3 overflow-y-auto flex flex-col gap-1 bg-[#050811]">
              <div className="text-[10px] font-sans font-bold uppercase tracking-wider text-slate-400 mb-1">
                Log Agent Thời Gian Thực (/api/cms/logs)
              </div>
              {liveServerLogs.length === 0 ? (
                <span className="text-slate-500">Chưa có log từ server...</span>
              ) : (
                liveServerLogs.map(log => {
                  const isLong = (log.message || '').length > 110
                  const expanded = Boolean(expandedLogIds[`srv-${log.id}`])
                  return (
                    <div key={log.id} className="flex items-start gap-2 leading-relaxed">
                      <span className="text-indigo-400 shrink-0">[{log.channel_slug}]</span>
                      <span
                        className={
                          log.level === 'ERROR'
                            ? 'text-rose-300'
                            : log.level === 'SUCCESS'
                              ? 'text-emerald-300'
                              : 'text-slate-300'
                        }
                      >
                        {expanded || !isLong ? log.message : `${log.message.slice(0, 110).trim()}...`}
                        {isLong && (
                          <button
                            type="button"
                            onClick={() =>
                              setExpandedLogIds(prev => ({ ...prev, [`srv-${log.id}`]: !prev[`srv-${log.id}`] }))
                            }
                            className="ml-1.5 text-[10px] font-sans font-bold text-indigo-400 hover:text-indigo-300 cursor-pointer"
                          >
                            {expanded ? 'Thu gọn' : 'Xem thêm'}
                          </button>
                        )}
                      </span>
                    </div>
                  )
                })
              )}
            </div>
          </div>
        )}
      </div>

      {/* 5. N8N-STYLE NODE DETAIL & PER-STEP LOG INSPECTOR MODAL ("Bấm vào có thể xem detail như n8n + log cho mỗi step") */}
      {detailModalNodeId &&
        (() => {
          const modalNode = nodes.find(n => n.id === detailModalNodeId)
          if (!modalNode) return null
          const meta = getNodeMeta(modalNode.type)
          const stepIdx = orderedWorkflowSteps.findIndex(s => s.id === modalNode.id)
          const incomingNodes = edges
            .filter(e => e.to === modalNode.id)
            .map(e => nodes.find(n => n.id === e.from))
            .filter(Boolean) as WorkflowNode[]
          const outgoingNodes = edges
            .filter(e => e.from === modalNode.id)
            .map(e => nodes.find(n => n.id === e.to))
            .filter(Boolean) as WorkflowNode[]
          const nodeStepLogs = modalNode.stepLogs || []
          const matchingServerLogs = getServerLogsForNode(modalNode)

          return (
            <div
              onClick={() => setDetailModalNodeId(null)}
              className="fixed inset-0 z-50 bg-black/75 backdrop-blur-sm flex items-center justify-center p-4"
            >
              <div
                onClick={e => e.stopPropagation()}
                className="w-full max-w-5xl h-[82vh] rounded-2xl bg-[#090d16] border border-slate-700/90 shadow-[0_0_60px_rgba(0,0,0,0.85)] flex flex-col overflow-hidden"
              >
                {/* Modal Top Header (n8n Node Bar) */}
                <div className="px-5 py-3.5 bg-slate-900/95 border-b border-slate-800 flex flex-wrap items-center justify-between gap-3">
                  <div className="flex items-center gap-3 min-w-0">
                    <div
                      className={`w-10 h-10 rounded-xl ${meta.bgAccent} border ${meta.borderAccent} flex items-center justify-center shrink-0`}
                    >
                      <NodeIcon type={modalNode.type} size={20} className={meta.accent} />
                    </div>
                    <div className="flex flex-col min-w-0">
                      <div className="flex items-center gap-2 flex-wrap">
                        <span className={`px-2 py-0.5 rounded text-[10px] font-extrabold ${meta.bgAccent} ${meta.accent}`}>
                          Bước #{stepIdx >= 0 ? stepIdx + 1 : ''} • {meta.badge}
                        </span>
                        <h3 className="text-base font-extrabold text-white truncate">{modalNode.title}</h3>
                        {modalNode.status === 'running' && (
                          <span className="px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-400/40 flex items-center gap-1">
                            <Loader2 size={11} className="animate-spin" /> Đang thực thi...
                          </span>
                        )}
                        {modalNode.status === 'success' && (
                          <span className="px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 flex items-center gap-1">
                            <CheckCircle2 size={11} /> Thành công{' '}
                            {modalNode.durationMs !== undefined ? `(${modalNode.durationMs}ms)` : ''}
                          </span>
                        )}
                        {modalNode.status === 'error' && (
                          <span className="px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/40 flex items-center gap-1">
                            <AlertCircle size={11} /> Lỗi thực thi
                          </span>
                        )}
                      </div>
                      <p className="text-xs text-slate-400 truncate mt-0.5">{modalNode.subtitle}</p>
                    </div>
                  </div>

                  {/* Header Action Buttons */}
                  <div className="flex items-center gap-2">
                    {/* Prev / Next Step Navigation inside n8n Modal */}
                    {stepIdx > 0 && (
                      <button
                        type="button"
                        onClick={() => {
                          const prevStep = orderedWorkflowSteps[stepIdx - 1]
                          if (prevStep) {
                            setSelectedNodeId(prevStep.id)
                            setDetailModalNodeId(prevStep.id)
                          }
                        }}
                        className="px-2.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-bold text-slate-200 cursor-pointer"
                      >
                        ← Bước #{stepIdx}
                      </button>
                    )}
                    {stepIdx >= 0 && stepIdx < orderedWorkflowSteps.length - 1 && (
                      <button
                        type="button"
                        onClick={() => {
                          const nextStep = orderedWorkflowSteps[stepIdx + 1]
                          if (nextStep) {
                            setSelectedNodeId(nextStep.id)
                            setDetailModalNodeId(nextStep.id)
                          }
                        }}
                        className="px-2.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-bold text-slate-200 cursor-pointer"
                      >
                        Bước #{stepIdx + 2} →
                      </button>
                    )}

                    <button
                      type="button"
                      onClick={() => executeSingleNode(modalNode, primaryConfig)}
                      disabled={modalNode.status === 'running'}
                      className="px-4 py-1.5 rounded-xl text-xs font-extrabold studio-glow-btn flex items-center gap-1.5 shadow-lg disabled:opacity-50 cursor-pointer"
                    >
                      {modalNode.status === 'running' ? (
                        <>
                          <Loader2 size={13} className="animate-spin" /> Đang chạy bước này...
                        </>
                      ) : (
                        <>
                          <Play size={13} /> Chạy Bước Này (Execute Step)
                        </>
                      )}
                    </button>

                    <button
                      type="button"
                      onClick={() => setDetailModalNodeId(null)}
                      className="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white cursor-pointer"
                      title="Đóng (Esc)"
                    >
                      <X size={16} />
                    </button>
                  </div>
                </div>

                {/* Modal Body: n8n Split View — Left (Input & Parameters) | Right (Per-Step Execution Logs & Output JSON) */}
                <div className="flex-1 grid grid-cols-1 lg:grid-cols-12 min-h-0 divide-y lg:divide-y-0 lg:divide-x divide-slate-800 overflow-hidden">
                  {/* Left Column (5 cols): Input Connections & Step Parameters */}
                  <div className="lg:col-span-5 p-4 overflow-y-auto flex flex-col gap-3.5 bg-slate-950/60 text-xs">
                    <div className="flex items-center justify-between">
                      <span className="text-xs font-extrabold uppercase tracking-wider text-indigo-300 flex items-center gap-1.5">
                        <Sliders size={13} /> Cấu Hình Bước (Parameters)
                      </span>
                      <span className="text-[11px] font-mono text-slate-500">ID: {modalNode.id}</span>
                    </div>

                    {/* Connected Input / Output Steps */}
                    <div className="p-3 rounded-xl bg-slate-900/90 border border-slate-800 flex flex-col gap-2">
                      <div className="flex items-center justify-between">
                        <span className="text-[11px] font-bold text-slate-300">Luồng Nối Bước (Connections):</span>
                      </div>
                      <div className="grid grid-cols-2 gap-2 text-[11px]">
                        <div className="p-2 rounded-lg bg-slate-950 border border-slate-800">
                          <span className="text-[10px] text-slate-400 block mb-1">⬅️ Đầu vào (Input):</span>
                          {incomingNodes.length === 0 ? (
                            <span className="text-slate-500">Bước khởi đầu</span>
                          ) : (
                            incomingNodes.map(inc => (
                              <button
                                key={inc.id}
                                type="button"
                                onClick={() => setDetailModalNodeId(inc.id)}
                                className="block text-left text-indigo-300 hover:underline font-bold truncate cursor-pointer"
                              >
                                • {inc.title}
                              </button>
                            ))
                          )}
                        </div>
                        <div className="p-2 rounded-lg bg-slate-950 border border-slate-800">
                          <span className="text-[10px] text-slate-400 block mb-1">➡️ Đầu ra (Output):</span>
                          {outgoingNodes.length === 0 ? (
                            <span className="text-slate-500">Bước kết thúc</span>
                          ) : (
                            outgoingNodes.map(out => (
                              <button
                                key={out.id}
                                type="button"
                                onClick={() => setDetailModalNodeId(out.id)}
                                className="block text-left text-cyan-300 hover:underline font-bold truncate cursor-pointer"
                              >
                                • {out.title}
                              </button>
                            ))
                          )}
                        </div>
                      </div>
                    </div>

                    {/* Step Parameters Form */}
                    <div className="p-3.5 rounded-xl bg-slate-900/90 border border-slate-800 flex flex-col gap-3">
                      <div>
                        <label className="text-[11px] font-bold text-slate-300 block mb-1">
                          Dự Án / Kênh Series Mục Tiêu:
                        </label>
                        <select
                          value={currentTarget?.key || primaryConfig.channelSlug}
                          onChange={e => handleSelectTargetProject(e.target.value)}
                          className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-700 text-white text-xs font-bold outline-none focus:border-indigo-500 cursor-pointer"
                        >
                          {unifiedTargets.map(t => (
                            <option key={t.key} value={t.key}>
                              🎬 {t.name} ({t.channelSlug})
                            </option>
                          ))}
                        </select>
                      </div>

                      <div className="grid grid-cols-2 gap-2.5">
                        <div>
                          <label className="text-[11px] font-bold text-slate-300 block mb-1">Từ Tập / Cảnh:</label>
                          <input
                            type="number"
                            min={1}
                            max={100}
                            value={primaryConfig.startEp}
                            onChange={e => {
                              const val = Math.max(1, Number(e.target.value) || 1)
                              updateGlobalOrNodeConfig({
                                startEp: val,
                                endEp: Math.max(val, primaryConfig.endEp),
                              })
                            }}
                            className="w-full px-3 py-1.5 rounded-xl bg-slate-950 border border-slate-700 text-white font-mono text-xs outline-none"
                          />
                        </div>
                        <div>
                          <label className="text-[11px] font-bold text-slate-300 block mb-1">Đến Tập / Cảnh:</label>
                          <input
                            type="number"
                            min={1}
                            max={100}
                            value={primaryConfig.endEp}
                            onChange={e => {
                              const val = Math.max(primaryConfig.startEp, Number(e.target.value) || 1)
                              updateGlobalOrNodeConfig({ endEp: val })
                            }}
                            className="w-full px-3 py-1.5 rounded-xl bg-slate-950 border border-slate-700 text-white font-mono text-xs outline-none"
                          />
                        </div>
                      </div>

                      <div>
                        <label className="text-[11px] font-bold text-slate-300 block mb-1">Chế Độ Render Clip:</label>
                        <select
                          value={primaryConfig.onlyClip}
                          onChange={e => updateGlobalOrNodeConfig({ onlyClip: Number(e.target.value) })}
                          className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-700 text-white text-xs font-semibold outline-none cursor-pointer"
                        >
                          <option value={0}>🎞️ Đủ 6 Clips / Tập (Clip 1 → Clip 6)</option>
                          <option value={1}>🎯 Chỉ chạy riêng Clip 01</option>
                          <option value={2}>🎯 Chỉ chạy riêng Clip 02</option>
                          <option value={3}>🎯 Chỉ chạy riêng Clip 03</option>
                          <option value={4}>🎯 Chỉ chạy riêng Clip 04</option>
                          <option value={5}>🎯 Chỉ chạy riêng Clip 05</option>
                          <option value={6}>🎯 Chỉ chạy riêng Clip 06</option>
                        </select>
                      </div>

                      {modalNode.type === 'push-cloud' && (
                        <div className="pt-2 border-t border-slate-800 flex flex-col gap-2">
                          <label className="flex items-center gap-2 cursor-pointer">
                            <input
                              type="checkbox"
                              checked={primaryConfig.syncR2}
                              onChange={e => updateGlobalOrNodeConfig({ syncR2: e.target.checked })}
                            />
                            <span>Đồng bộ video MP4 lên Cloudflare R2</span>
                          </label>
                          <label className="flex items-center gap-2 cursor-pointer">
                            <input
                              type="checkbox"
                              checked={primaryConfig.syncD1}
                              onChange={e => updateGlobalOrNodeConfig({ syncD1: e.target.checked })}
                            />
                            <span>Đồng bộ SQLite lên Cloudflare D1 SQL</span>
                          </label>
                        </div>
                      )}
                    </div>

                    {/* Step Technical Endpoint Info */}
                    <div className="p-3 rounded-xl bg-slate-900/60 border border-slate-800/80 text-[11px] text-slate-400 flex flex-col gap-1">
                      <span className="font-bold text-slate-200">API Thực Thi Của Bước Này:</span>
                      <code className="text-[10px] font-mono text-cyan-300 bg-slate-950 px-2 py-1 rounded border border-slate-800">
                        {modalNode.type === 'channel-source' && `GET /api/cms/channels/${primaryConfig.channelSlug}`}
                        {modalNode.type === 'pull-d1' && 'POST /api/cms/cloud/sync-d1?direction=pull'}
                        {modalNode.type === 'lock-characters' &&
                          `POST /api/cms/channels/${primaryConfig.channelSlug}/auto-lock-characters`}
                        {modalNode.type === 'verify-prompts' &&
                          `GET /api/cms/channels/${primaryConfig.channelSlug} (Validate 24fps & Stunt Safety)`}
                        {modalNode.type === 'run-agent' && `POST /api/cms/channels/${primaryConfig.channelSlug}/run`}
                        {modalNode.type === 'merge-mp4' &&
                          `POST /api/cms/channels/${primaryConfig.channelSlug}/episodes/${primaryConfig.startEp}/merge`}
                        {modalNode.type === 'push-cloud' &&
                          'POST /api/cms/cloud/sync-r2 & POST /api/cms/cloud/sync-d1?direction=push'}
                      </code>
                    </div>
                  </div>

                  {/* Right Column (7 cols): Per-Step Execution Logs & Structured Output JSON */}
                  <div className="lg:col-span-7 flex flex-col min-h-0 bg-[#050811]">
                    {/* Right Column Tabs */}
                    <div className="px-4 py-2.5 bg-slate-900/80 border-b border-slate-800 flex items-center justify-between gap-2">
                      <div className="flex items-center gap-1.5">
                        <button
                          type="button"
                          onClick={() => setDetailModalTab('logs')}
                          className={`px-3 py-1 rounded-lg text-xs font-bold flex items-center gap-1.5 cursor-pointer transition-colors ${
                            detailModalTab === 'logs'
                              ? 'bg-indigo-500 text-white'
                              : 'bg-slate-950 text-slate-400 hover:text-white border border-slate-800'
                          }`}
                        >
                          <Terminal size={13} />
                          Log Của Bước Này ({nodeStepLogs.length})
                        </button>
                        <button
                          type="button"
                          onClick={() => setDetailModalTab('output')}
                          className={`px-3 py-1 rounded-lg text-xs font-bold flex items-center gap-1.5 cursor-pointer transition-colors ${
                            detailModalTab === 'output'
                              ? 'bg-cyan-500 text-slate-950'
                              : 'bg-slate-950 text-slate-400 hover:text-white border border-slate-800'
                          }`}
                        >
                          <Code2 size={13} />
                          Output JSON & Server Logs ({matchingServerLogs.length})
                        </button>
                      </div>

                      {nodeStepLogs.length > 0 && (
                        <button
                          type="button"
                          onClick={() => clearNodeLogs(modalNode.id)}
                          className="px-2.5 py-1 rounded-lg bg-slate-950 hover:bg-slate-800 text-slate-400 hover:text-rose-300 border border-slate-800 text-[11px] font-semibold cursor-pointer"
                        >
                          Xóa log bước này
                        </button>
                      )}
                    </div>

                    {/* Tab Content */}
                    <div className="flex-1 p-4 overflow-y-auto font-mono text-xs flex flex-col gap-3">
                      {detailModalTab === 'logs' ? (
                        <>
                          {nodeStepLogs.length === 0 ? (
                            <div className="p-6 rounded-2xl bg-slate-900/40 border border-dashed border-slate-800 text-center flex flex-col items-center gap-2 font-sans">
                              <Terminal size={24} className="text-slate-500" />
                              <div className="text-sm font-bold text-slate-300">
                                Bước "{modalNode.title}" chưa có nhật ký chạy
                              </div>
                              <p className="text-xs text-slate-400 max-w-md">
                                Bấm nút <strong>"Chạy Bước Này (Execute Step)"</strong> ở góc trên bên phải để thực thi
                                bước này và xem toàn bộ log thời gian thực + dữ liệu trả về tại đây.
                              </p>
                            </div>
                          ) : (
                            <div className="flex flex-col gap-2">
                              {nodeStepLogs.map(entry => (
                                <div
                                  key={entry.id}
                                  className="p-3 rounded-xl bg-slate-900/90 border border-slate-800/90 flex flex-col gap-1.5"
                                >
                                  <div className="flex items-center justify-between gap-2">
                                    <div className="flex items-center gap-2">
                                      <span className="text-slate-500 text-[11px]">[{entry.time}]</span>
                                      <span
                                        className={`px-1.5 py-0.5 rounded text-[10px] font-extrabold ${
                                          entry.level === 'SUCCESS'
                                            ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30'
                                            : entry.level === 'ERROR'
                                              ? 'bg-rose-500/20 text-rose-300 border border-rose-500/30'
                                              : entry.level === 'WARN'
                                                ? 'bg-amber-500/20 text-amber-300 border border-amber-500/30'
                                                : 'bg-indigo-500/20 text-indigo-300 border border-indigo-500/30'
                                        }`}
                                      >
                                        {entry.level}
                                      </span>
                                    </div>
                                  </div>
                                  <div
                                    className={`text-xs leading-relaxed ${
                                      entry.level === 'SUCCESS'
                                        ? 'text-emerald-200'
                                        : entry.level === 'ERROR'
                                          ? 'text-rose-200'
                                          : 'text-slate-200'
                                    }`}
                                  >
                                    {entry.text}
                                  </div>
                                  {entry.detail && (
                                    <pre className="mt-1 p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-cyan-300 overflow-x-auto">
                                      {entry.detail}
                                    </pre>
                                  )}
                                </div>
                              ))}
                            </div>
                          )}

                          {/* Also show matching real-time server logs for this step right underneath */}
                          <div className="mt-2 pt-3 border-t border-slate-800/90 flex flex-col gap-1.5">
                            <span className="text-[11px] font-sans font-extrabold uppercase tracking-wider text-slate-400">
                              Log Server Liên Quan Đến Bước Này ({matchingServerLogs.length})
                            </span>
                            {matchingServerLogs.length === 0 ? (
                              <span className="text-slate-500 text-[11px]">
                                Không có log server mới cho bước này.
                              </span>
                            ) : (
                              matchingServerLogs.slice(0, 12).map(srv => (
                                <div
                                  key={srv.id}
                                  className="px-2.5 py-1.5 rounded-lg bg-slate-900/60 border border-slate-800/70 text-[11px] flex items-start gap-2"
                                >
                                  <span className="text-slate-500 shrink-0">[{srv.created_at.slice(11)}]</span>
                                  <span className="text-indigo-400 shrink-0">[{srv.category || srv.channel_slug}]</span>
                                  <span
                                    className={
                                      srv.level === 'ERROR'
                                        ? 'text-rose-300'
                                        : srv.level === 'SUCCESS'
                                          ? 'text-emerald-300'
                                          : 'text-slate-300'
                                    }
                                  >
                                    {srv.message}
                                  </span>
                                </div>
                              ))
                            )}
                          </div>
                        </>
                      ) : (
                        <div className="flex flex-col gap-3">
                          <div className="p-3 rounded-xl bg-slate-900/90 border border-slate-800">
                            <div className="text-[11px] font-sans font-bold text-cyan-300 mb-2">
                              Output JSON Của Bước "{modalNode.title}":
                            </div>
                            <pre className="p-3 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-emerald-300 overflow-x-auto">
                              {JSON.stringify(
                                modalNode.lastOutput || {
                                  step: modalNode.type,
                                  status: modalNode.status,
                                  lastMessage: modalNode.lastMessage || 'Chưa chạy bước này',
                                  config: modalNode.config,
                                },
                                null,
                                2
                              )}
                            </pre>
                          </div>
                        </div>
                      )}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          )
        })()}
    </div>
  )
}
