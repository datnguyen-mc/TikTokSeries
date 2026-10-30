import { useState, useEffect, useCallback } from 'react'
import { Trash2, RefreshCw, ChevronDown, ChevronRight, Search, Pause, Play, Database } from 'lucide-react'
import { fetchAPI } from '../../api/client'
import { useWebSocketContext } from '../../api/useWebSocketContext'
import { ScrollArea } from '../ui/scroll-area'

interface CmsLogRow {
  id: number
  channel_slug: string
  project_id?: string | null
  episode?: number | null
  clip_num?: number | null
  level: string
  category: string
  message: string
  details?: Record<string, string> | null
  created_at: string
}

const CHANNEL_OPTIONS = [
  { value: 'ALL', label: 'Tất Cả Kênh', short: 'ALL', dot: 'bg-indigo-400' },
  { value: 'mit-va-du-1970', label: 'Mít Và Đú 1970', short: '9:16', dot: 'bg-amber-400' },
  { value: '365ngayvietnam', label: '365 Ngày Việt Nam', short: '9:16', dot: 'bg-emerald-400' },
  { value: 'me-va-be', label: 'Mẹ Và Bé', short: '9:16', dot: 'bg-pink-400' },
  { value: 'pheo-va-no-meo', label: 'Phèo Làm Nội Trợ', short: '9:16', dot: 'bg-purple-400' },
  { value: 'tay-du-ky-2026', label: 'Tây Du Ký 2026', short: '9:16', dot: 'bg-sky-400' },
  { value: 'biet-doi-gara', label: 'Biệt Đội Gara', short: '16:9', dot: 'bg-cyan-400' },
  { value: 'ke-song-sot', label: 'Kẻ Sống Sót', short: '16:9', dot: 'bg-rose-400' },
  { value: 'system', label: 'Hệ Thống', short: 'SYS', dot: 'bg-slate-400' },
]

export default function LogViewer() {
  const { lastEvent } = useWebSocketContext()
  const [logs, setLogs] = useState<CmsLogRow[]>([])
  const [channelFilter, setChannelFilter] = useState<string>('ALL')
  const [levelFilter, setLevelFilter] = useState<string>('ALL')
  const [categoryFilter, setCategoryFilter] = useState<string>('ALL')
  const [query, setQuery] = useState<string>('')
  const [paused, setPaused] = useState<boolean>(false)
  const [expandedIds, setExpandedIds] = useState<Record<number, boolean>>({})

  const load = useCallback(async () => {
    const params = new URLSearchParams()
    if (channelFilter !== 'ALL') params.set('channel_slug', channelFilter)
    if (levelFilter !== 'ALL') params.set('level', levelFilter)
    if (categoryFilter !== 'ALL') params.set('category', categoryFilter)
    if (query.trim()) params.set('search', query.trim())
    params.set('limit', '350')

    try {
      const res = await fetchAPI<{ logs: CmsLogRow[] }>(`/api/cms/logs?${params.toString()}`)
      setLogs(res.logs)
    } catch (e) {
      console.error('Failed to load CMS logs:', e)
    }
  }, [channelFilter, levelFilter, categoryFilter, query])

  useEffect(() => {
    load()
  }, [load])

  useEffect(() => {
    if (paused || !lastEvent) return
    if (lastEvent.type === 'cms_log' && lastEvent.data) {
      const newLog = lastEvent.data as unknown as CmsLogRow
      if (channelFilter !== 'ALL' && newLog.channel_slug !== channelFilter) return
      if (levelFilter !== 'ALL' && newLog.level !== levelFilter) return
      if (categoryFilter !== 'ALL' && newLog.category !== categoryFilter) return
      if (
        query.trim() &&
        !`${newLog.message} ${JSON.stringify(newLog.details || {})}`
          .toLowerCase()
          .includes(query.trim().toLowerCase())
      ) {
        return
      }
      setLogs(prev => [newLog, ...prev.filter(x => x.id !== newLog.id)].slice(0, 350))
    }
  }, [lastEvent, paused, channelFilter, levelFilter, categoryFilter, query])

  async function handleClearLogs() {
    if (!window.confirm('Bạn có chắc muốn xóa lịch sử log hiện tại?')) return
    const q = channelFilter !== 'ALL' ? `?channel_slug=${channelFilter}` : ''
    await fetchAPI(`/api/cms/logs${q}`, { method: 'DELETE' })
    load()
  }

  function toggleExpand(id: number) {
    setExpandedIds(prev => ({ ...prev, [id]: !prev[id] }))
  }

  const successCount = logs.filter(l => l.level === 'SUCCESS').length
  const errorCount = logs.filter(l => l.level === 'ERROR').length
  const mergeCount = logs.filter(l => l.category === 'MERGE').length

  return (
    <div className="flex flex-col gap-4 max-w-[1600px] mx-auto" style={{ height: 'calc(100vh - 120px)' }}>
      {/* Top Channel Select Dropdown & Filter Bar */}
      <div className="studio-card rounded-2xl p-4 flex flex-wrap items-center justify-between gap-3">
        <div className="flex items-center gap-2.5 flex-wrap">
          <div className="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-slate-950/95 border border-indigo-500/40 text-xs">
            <span className="text-slate-400 font-semibold shrink-0">Kênh Series:</span>
            <select
              value={channelFilter}
              onChange={e => setChannelFilter(e.target.value)}
              className="bg-transparent font-extrabold text-white outline-none cursor-pointer min-w-[200px]"
            >
              {CHANNEL_OPTIONS.map(opt => (
                <option key={opt.value} value={opt.value} className="bg-slate-950 text-white">
                  {opt.value === 'ALL' ? '📺 ' : opt.value === 'system' ? '⚙️ ' : '🎬 '}
                  {opt.label} [{opt.short}]
                </option>
              ))}
            </select>
          </div>

          <div className="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-slate-950/90 border border-slate-800 text-xs">
              <Search size={13} className="text-slate-400" />
              <input
                value={query}
                onChange={e => setQuery(e.target.value)}
                placeholder="Tìm nội dung log, media_id, tên tập..."
                className="bg-transparent outline-none text-white placeholder:text-slate-500 w-56"
              />
            </div>

            <select
              value={categoryFilter}
              onChange={e => setCategoryFilter(e.target.value)}
              className="text-xs px-3 py-1.5 rounded-xl outline-none bg-slate-950/90 text-slate-200 border border-slate-800 cursor-pointer"
            >
              <option value="ALL">Tất cả danh mục (All Categories)</option>
              <option value="RUNNER">RUNNER (Tiến trình tạo video)</option>
              <option value="API_BOX">API_BOX (Chi tiết Request / Khóa nhân vật)</option>
              <option value="MERGE">MERGE (Tự động ghép tập hoàn chỉnh)</option>
              <option value="R2_UPLOAD">R2_UPLOAD (Đồng bộ Cloudflare R2)</option>
              <option value="JOB">JOB (Quản lý tiến trình CMS)</option>
              <option value="PROMPT">PROMPT (Lưu kịch bản clip)</option>
              <option value="CONFIG">CONFIG (Cấu hình kênh)</option>
              <option value="AUTH">AUTH (Đăng nhập / Bảo mật)</option>
            </select>

            <div className="flex items-center p-1 rounded-xl bg-slate-950/90 border border-slate-800 text-[11px]">
              {(['ALL', 'INFO', 'SUCCESS', 'WARN', 'ERROR'] as const).map(lv => (
                <button
                  key={lv}
                  onClick={() => setLevelFilter(lv)}
                  className={`px-2.5 py-1 rounded-lg font-semibold transition-colors cursor-pointer ${
                    levelFilter === lv ? 'bg-indigo-600 text-white' : 'text-slate-400 hover:text-slate-200'
                  }`}
                >
                  {lv === 'ALL' ? 'Tất cả' : lv}
                </button>
              ))}
            </div>
        </div>

        <div className="flex items-center gap-2">
          <button
            onClick={load}
            className="px-3 py-1.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-xs font-medium text-slate-200 flex items-center gap-1.5 cursor-pointer"
          >
            <RefreshCw size={12} /> Tải lại
          </button>
          <button
            onClick={() => setPaused(p => !p)}
            className={`px-3 py-1.5 rounded-xl border text-xs font-medium flex items-center gap-1.5 cursor-pointer ${
              paused
                ? 'bg-amber-500/15 border-amber-500/30 text-amber-300'
                : 'bg-slate-900 hover:bg-slate-800 border-slate-800 text-slate-200'
            }`}
          >
            {paused ? <Play size={12} /> : <Pause size={12} />}
            {paused ? 'Tiếp tục Live' : 'Tạm dừng Live'}
          </button>
          <button
            onClick={handleClearLogs}
            className="px-3 py-1.5 rounded-xl bg-rose-500/10 hover:bg-rose-500/20 border border-rose-500/30 text-xs font-medium text-rose-300 flex items-center gap-1.5 cursor-pointer"
          >
            <Trash2 size={12} /> Xóa Log
          </button>
        </div>
      </div>

      {/* Main Log Table Card */}
      <div className="studio-card rounded-3xl flex-1 min-h-0 overflow-hidden flex flex-col">
        <div
          className="grid gap-3 px-5 py-3 text-[10px] font-bold uppercase tracking-wider bg-slate-950/80 border-b border-slate-800/90 text-slate-400"
          style={{
            gridTemplateColumns: '145px 150px 90px 100px 95px 1fr',
          }}
        >
          <span>Thời Gian</span>
          <span>Kênh Series</span>
          <span>Mức Độ</span>
          <span>Danh Mục</span>
          <span>Tập / Clip</span>
          <span>Nội Dung Chi Tiết</span>
        </div>

        <ScrollArea className="h-full">
          <div className="divide-y divide-slate-800/60">
            {logs.length === 0 ? (
              <div className="py-16 text-center text-xs text-slate-500">
                Chưa có bản ghi log nào khớp bộ lọc hiện tại.
              </div>
            ) : (
              logs.map(row => {
                const hasDetails = row.details && Object.keys(row.details).length > 0
                const isExpanded = Boolean(expandedIds[row.id])
                return (
                  <div key={row.id} className="transition-colors hover:bg-white/[0.02]">
                    <div
                      onClick={() => hasDetails && toggleExpand(row.id)}
                      className={`grid gap-3 px-5 py-2.5 text-xs items-center ${hasDetails ? 'cursor-pointer' : ''}`}
                      style={{ gridTemplateColumns: '145px 150px 90px 100px 95px 1fr' }}
                    >
                      <span className="font-mono text-[11px] text-slate-500">{row.created_at}</span>
                      <span className="font-semibold text-slate-200 truncate">{row.channel_slug}</span>
                      <span>
                        <span
                          className={`px-2 py-0.5 rounded-md text-[10px] font-bold border ${
                            row.level === 'ERROR'
                              ? 'bg-rose-500/15 text-rose-300 border-rose-500/30'
                              : row.level === 'WARN'
                                ? 'bg-amber-500/15 text-amber-300 border-amber-500/30'
                                : row.level === 'SUCCESS'
                                  ? 'bg-emerald-500/15 text-emerald-300 border-emerald-500/30'
                                  : 'bg-indigo-500/15 text-indigo-300 border-indigo-500/30'
                          }`}
                        >
                          {row.level}
                        </span>
                      </span>
                      <span className="text-[11px] font-mono text-slate-400">{row.category}</span>
                      <span className="text-[11px] font-mono text-amber-300">
                        {row.episode ? `Tập ${row.episode}${row.clip_num ? `•C${row.clip_num}` : ''}` : '—'}
                      </span>
                      <span className="flex items-center gap-1.5 text-slate-200">
                        {hasDetails &&
                          (isExpanded ? (
                            <ChevronDown size={13} className="text-indigo-400 shrink-0" />
                          ) : (
                            <ChevronRight size={13} className="text-slate-500 shrink-0" />
                          ))}
                        <span className="break-words">{row.message}</span>
                      </span>
                    </div>

                    {hasDetails && isExpanded && (
                      <div className="mx-5 mb-3 p-3.5 rounded-2xl bg-slate-950/90 border border-slate-800 text-[11px] font-mono grid grid-cols-1 md:grid-cols-2 gap-2">
                        {Object.entries(row.details || {}).map(([k, v]) => (
                          <div key={k} className="truncate">
                            <span className="text-slate-500">{k}: </span>
                            <span className="text-indigo-300">{v}</span>
                          </div>
                        ))}
                      </div>
                    )}
                  </div>
                )
              })
            )}
          </div>
        </ScrollArea>
      </div>

      {/* Footer Status Bar */}
      <div className="flex flex-wrap items-center justify-between gap-3 text-xs text-slate-400 px-1">
        <div className="flex items-center gap-4">
          <span className="flex items-center gap-1.5">
            <Database size={13} className="text-indigo-400" />
            Đang hiển thị <strong className="text-white">{logs.length}</strong> bản ghi từ SQLite (<code>cms_log</code>)
          </span>
          <span>
            Thành công: <strong className="text-emerald-400">{successCount}</strong>
          </span>
          <span>
            Ghép tập FULL: <strong className="text-amber-400">{mergeCount}</strong>
          </span>
          <span>
            Lỗi: <strong className="text-rose-400">{errorCount}</strong>
          </span>
        </div>
        <span>{paused ? '⏸️ Đã tạm dừng tự động cuộn' : '🟢 Đang nhận log trực tiếp qua WebSocket'}</span>
      </div>
    </div>
  )
}
