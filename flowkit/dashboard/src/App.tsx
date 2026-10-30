import { useState, useEffect } from 'react'
import { BrowserRouter, NavLink, Routes, Route, useLocation } from 'react-router-dom'
import {
  LayoutDashboard,
  FolderOpen,
  Film,
  ScrollText,
  BookOpen,
  SlidersHorizontal,
  Tv,
  LogOut,
  KeyRound,
  Cpu,
  Radio,
  Sparkles,
  CheckCircle2,
  AlertCircle,
} from 'lucide-react'
import { TooltipProvider } from '@/components/ui/tooltip'
import { WebSocketProvider } from './api/WebSocketContext'
import { useWebSocketContext } from './api/useWebSocketContext'
import { LanguageProvider } from './i18n/LanguageContext'
import { useTranslation } from './i18n/useTranslation'
import { LANGS, LANG_LABELS, type Lang } from './i18n/translations'
import { fetchAPI, getCmsToken, setCmsToken, API_BASE_URL } from './api/client'
import ChannelsCMSPage from './pages/ChannelsCMSPage'
import LoginPage, { type CmsUser } from './pages/LoginPage'
import DashboardPage from './pages/DashboardPage'
import ProjectsPage from './pages/ProjectsPage'
import LogsPage from './pages/LogsPage'
import GalleryPage from './pages/GalleryPage'
import GuidePage from './pages/GuidePage'
import SettingsPage from './pages/SettingsPage'

const STUDIO_NAV = [
  { to: '/', icon: Tv, label: 'Studio Kênh Series', badge: 'CMS', exact: true },
  { to: '/logs', icon: ScrollText, label: 'Nhật Ký & Log SQLite', badge: 'Live', exact: false },
  { to: '/projects', icon: FolderOpen, label: 'Dự Án & Nhân Vật', exact: false },
  { to: '/gallery', icon: Film, label: 'Thư Viện Media', exact: false },
]

const SYSTEM_NAV = [
  { to: '/console', icon: LayoutDashboard, label: 'Hàng Đợi Worker', exact: false },
  { to: '/guide', icon: BookOpen, label: 'Hướng Dẫn Vận Hành', exact: false },
  { to: '/settings', icon: SlidersHorizontal, label: 'Cài Đặt Hệ Thống', exact: false },
]

function useClock() {
  const [now, setNow] = useState(() => new Date())
  useEffect(() => {
    const id = setInterval(() => setNow(new Date()), 1000)
    return () => clearInterval(id)
  }, [])
  return now
}

function LanguageSwitcher() {
  const { lang, setLang } = useTranslation()
  return (
    <select
      value={lang}
      onChange={e => setLang(e.target.value as Lang)}
      className="text-[11px] px-2.5 py-1.5 rounded-lg outline-none w-full bg-slate-900/90 text-slate-300 border border-slate-800 hover:border-slate-700 transition-colors cursor-pointer"
    >
      {LANGS.map(l => (
        <option key={l} value={l}>
          {LANG_LABELS[l]}
        </option>
      ))}
    </select>
  )
}

interface SidebarProps {
  user: CmsUser
  onLogout: () => void
}

function Sidebar({ user, onLogout }: SidebarProps) {
  const { worker } = useWebSocketContext()
  const [health, setHealth] = useState<{ extension_connected: boolean } | null>(null)
  const [showPwdBox, setShowPwdBox] = useState(false)
  const [curPwd, setCurPwd] = useState('')
  const [newPwd, setNewPwd] = useState('')
  const [pwdMsg, setPwdMsg] = useState<string | null>(null)

  useEffect(() => {
    const check = () =>
      fetchAPI<{ extension_connected: boolean }>('/health')
        .then(setHealth)
        .catch(() => setHealth(null))
    check()
    const id = setInterval(check, 8000)
    return () => clearInterval(id)
  }, [])

  async function handleChangePassword() {
    setPwdMsg(null)
    try {
      await fetchAPI('/api/cms/auth/change-password', {
        method: 'POST',
        body: JSON.stringify({ current_password: curPwd, new_password: newPwd }),
      })
      setPwdMsg('✅ Đã đổi mật khẩu!')
      setCurPwd('')
      setNewPwd('')
      setTimeout(() => setShowPwdBox(false), 1200)
    } catch {
      setPwdMsg('❌ Mật khẩu cũ không đúng!')
    }
  }

  const initials = (user.display_name || user.username || 'A').slice(0, 2).toUpperCase()

  return (
    <aside className="w-64 flex-shrink-0 flex flex-col border-r border-slate-800/80 bg-[#090d16] select-none">
      {/* Studio Brand Header */}
      <div className="px-5 py-4 flex items-center gap-3 border-b border-slate-800/80">
        <img
          src="/logo.png"
          alt="FlowKit Studio"
          className="w-10 h-10 rounded-xl object-contain bg-white p-0.5 shadow-lg shrink-0"
        />
        <div className="flex flex-col min-w-0">
          <div className="flex items-center gap-1.5">
            <span className="text-xs font-extrabold tracking-wider text-white truncate">FLOWKIT STUDIO</span>
            <span className="px-1.5 py-0.2 rounded text-[9px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
              PRO
            </span>
          </div>
          <span className="text-[10px] text-slate-400 truncate">AI TikTok Series Production</span>
        </div>
      </div>

      {/* Navigation Sections */}
      <div className="flex-1 overflow-y-auto px-3 py-4 flex flex-col gap-5">
        <div className="flex flex-col gap-1">
          <span className="px-3 text-[10px] font-bold uppercase tracking-wider text-slate-500 mb-1">
            Sản Xuất & Kênh
          </span>
          {STUDIO_NAV.map(({ to, icon: Icon, label, badge, exact }) => (
            <NavLink
              key={to}
              to={to}
              end={exact}
              className={({ isActive }) =>
                `group flex items-center justify-between px-3 py-2.5 rounded-xl text-xs font-medium transition-all ${
                  isActive
                    ? 'bg-indigo-600/15 text-white border border-indigo-500/40 shadow-sm'
                    : 'text-slate-400 hover:text-slate-200 hover:bg-white/[0.03] border border-transparent'
                }`
              }
            >
              {({ isActive }) => (
                <>
                  <div className="flex items-center gap-2.5 truncate">
                    <Icon
                      size={15}
                      className={isActive ? 'text-indigo-400' : 'text-slate-400 group-hover:text-slate-200'}
                    />
                    <span className="truncate">{label}</span>
                  </div>
                  {badge && (
                    <span
                      className={`px-1.5 py-0.5 rounded-md text-[9px] font-bold ${
                        isActive
                          ? 'bg-indigo-500 text-white'
                          : 'bg-slate-800 text-slate-400 group-hover:bg-slate-700 group-hover:text-slate-200'
                      }`}
                    >
                      {badge}
                    </span>
                  )}
                </>
              )}
            </NavLink>
          ))}
        </div>

        <div className="flex flex-col gap-1">
          <span className="px-3 text-[10px] font-bold uppercase tracking-wider text-slate-500 mb-1">
            Hệ Thống & Công Cụ
          </span>
          {SYSTEM_NAV.map(({ to, icon: Icon, label, exact }) => (
            <NavLink
              key={to}
              to={to}
              end={exact}
              className={({ isActive }) =>
                `group flex items-center gap-2.5 px-3 py-2.5 rounded-xl text-xs font-medium transition-all ${
                  isActive
                    ? 'bg-indigo-600/15 text-white border border-indigo-500/40 shadow-sm'
                    : 'text-slate-400 hover:text-slate-200 hover:bg-white/[0.03] border border-transparent'
                }`
              }
            >
              {({ isActive }) => (
                <>
                  <Icon
                    size={15}
                    className={isActive ? 'text-indigo-400' : 'text-slate-400 group-hover:text-slate-200'}
                  />
                  <span className="truncate">{label}</span>
                </>
              )}
            </NavLink>
          ))}
        </div>
      </div>

      {/* Bottom Telemetry & User Profile */}
      <div className="p-3.5 border-t border-slate-800/80 flex flex-col gap-3 bg-[#070a12]">
        {/* System Telemetry Box */}
        <div className="p-3 rounded-xl bg-slate-900/70 border border-slate-800/80 flex flex-col gap-2 text-[11px]">
          <div className="flex items-center justify-between">
            <span className="text-slate-400 flex items-center gap-1.5">
              <Cpu size={12} className="text-indigo-400" />
              Workers
            </span>
            <span className="font-mono font-semibold text-slate-200">
              {worker ? `${worker.active}/${worker.active + worker.slots} active` : '0/2 active'}
            </span>
          </div>

          <div className="flex items-center justify-between">
            <span className="text-slate-400 flex items-center gap-1.5">
              <Radio size={12} className={health?.extension_connected ? 'text-emerald-400' : 'text-rose-400'} />
              Chrome Ext
            </span>
            <span
              className={`inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold ${
                health?.extension_connected
                  ? 'bg-emerald-500/15 text-emerald-300 border border-emerald-500/30'
                  : 'bg-rose-500/15 text-rose-300 border border-rose-500/30'
              }`}
            >
              <span
                className={`w-1.5 h-1.5 rounded-full ${
                  health?.extension_connected ? 'bg-emerald-400' : 'bg-rose-400'
                }`}
              />
              {health?.extension_connected ? 'Đã kết nối' : 'Chưa kết nối'}
            </span>
          </div>
        </div>

        {/* User Profile Card */}
        <div className="p-3 rounded-xl bg-slate-900/90 border border-slate-800 flex flex-col gap-2.5">
          <div className="flex items-center gap-2.5">
            <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center text-xs font-bold text-white shrink-0">
              {initials}
            </div>
            <div className="flex flex-col min-w-0 flex-1">
              <span className="text-xs font-bold text-white truncate">{user.display_name || user.username}</span>
              <span className="text-[10px] text-slate-400 truncate">@{user.username} • Admin</span>
            </div>
          </div>

          <div className="grid grid-cols-2 gap-1.5 pt-1 border-t border-slate-800/80">
            <button
              onClick={() => setShowPwdBox(v => !v)}
              className="px-2 py-1.5 rounded-lg text-[10px] font-medium bg-slate-800/70 hover:bg-slate-800 text-slate-300 flex items-center justify-center gap-1 transition-colors cursor-pointer"
              title="Đổi mật khẩu"
            >
              <KeyRound size={11} /> Đổi MK
            </button>
            <button
              onClick={onLogout}
              className="px-2 py-1.5 rounded-lg text-[10px] font-medium bg-rose-500/10 hover:bg-rose-500/20 text-rose-300 border border-rose-500/20 flex items-center justify-center gap-1 transition-colors cursor-pointer"
              title="Đăng xuất"
            >
              <LogOut size={11} /> Đăng xuất
            </button>
          </div>

          {showPwdBox && (
            <div className="pt-2 border-t border-slate-800 flex flex-col gap-1.5">
              <input
                type="password"
                placeholder="Mật khẩu hiện tại"
                value={curPwd}
                onChange={e => setCurPwd(e.target.value)}
                className="px-2.5 py-1.5 rounded-lg text-[11px] bg-slate-950 border border-slate-800 text-white outline-none focus:border-indigo-500"
              />
              <input
                type="password"
                placeholder="Mật khẩu mới"
                value={newPwd}
                onChange={e => setNewPwd(e.target.value)}
                className="px-2.5 py-1.5 rounded-lg text-[11px] bg-slate-950 border border-slate-800 text-white outline-none focus:border-indigo-500"
              />
              <button
                onClick={handleChangePassword}
                className="px-2.5 py-1.5 rounded-lg text-[11px] font-semibold studio-glow-btn cursor-pointer"
              >
                Lưu mật khẩu mới
              </button>
              {pwdMsg && <span className="text-[10px] text-center">{pwdMsg}</span>}
            </div>
          )}
        </div>

        <LanguageSwitcher />
      </div>
    </aside>
  )
}

const CHANNEL_TITLES: Record<string, string> = {
  'mit-va-du-1970': 'Mít Và Đú 1970',
  '365ngayvietnam': '365 Ngày Việt Nam',
  'me-va-be': 'Mẹ Và Bé',
  'pheo-va-no-meo': '365 Ngày Phèo Làm Nội Trợ',
  'tay-du-ky-2026': 'Tây Du Ký 2026',
  'biet-doi-gara': 'Biệt Đội Gara',
  'ke-song-sot': 'Kẻ Sống Sót',
}

function Header({ user }: { user: CmsUser }) {
  const { isConnected } = useWebSocketContext()
  const loc = useLocation()
  const clock = useClock()

  const channelSlug = loc.pathname.startsWith('/channels/')
    ? decodeURIComponent(loc.pathname.replace('/channels/', '').split('/')[0])
    : null
  const channelDisplayName = channelSlug ? CHANNEL_TITLES[channelSlug] || channelSlug : null

  const pageMeta =
    loc.pathname === '/'
      ? {
          badge: 'DANH SÁCH KÊNH',
          title: 'Bảng Quản Lý Kênh TikTok Series (List Table)',
          subtitle: 'Tổng hợp tiến độ render clips, khóa nhân vật (@Character) và trạng thái ghép tập của 6 kênh',
          docTitle: 'Danh Sách Kênh TikTok Series | FlowKit Studio CMS',
        }
      : channelSlug
        ? {
            badge: 'STUDIO CHI TIẾT',
            title: `Studio Sản Xuất Kênh: ${channelDisplayName}`,
            subtitle: `Tạo kịch bản prompt tập mới, khóa nhân vật cố định & tự động ghép tập FULL MP4 (${channelSlug})`,
            docTitle: `${channelDisplayName} — Studio Kênh | FlowKit Studio CMS`,
          }
        : loc.pathname.startsWith('/logs')
          ? {
              badge: 'SQLITE LOGS',
              title: 'Nhật Ký Hoạt Động & Log Theo Kênh',
              subtitle: 'Theo dõi lịch sử tạo video, mã media_id và tự động ghép tập theo thời gian thực',
              docTitle: 'Nhật Ký & Log Kênh | FlowKit Studio CMS',
            }
          : loc.pathname.startsWith('/projects')
            ? {
                badge: 'PROJECTS',
                title: 'Quản Lý Dự Án & Thư Viện Nhân Vật',
                subtitle: 'Quản lý danh sách dự án Google Flow và hồ sơ nguyên liệu đầu vào',
                docTitle: 'Dự Án & Nhân Vật | FlowKit Studio CMS',
              }
            : loc.pathname.startsWith('/gallery')
              ? {
                  badge: 'MEDIA GALLERY',
                  title: 'Thư Viện Video & Hình Ảnh Đã Kết Xuất',
                  subtitle: 'Xem trước và tải xuống toàn bộ media đã tạo từ các dự án',
                  docTitle: 'Thư Viện Media | FlowKit Studio CMS',
                }
              : loc.pathname.startsWith('/console')
                ? {
                    badge: 'WORKER QUEUE',
                    title: 'Hàng Đợi Tiến Trình Worker',
                    subtitle: 'Giám sát các tác vụ đang xử lý ngầm và trạng thái worker',
                    docTitle: 'Hàng Đợi Worker | FlowKit Studio CMS',
                  }
                : loc.pathname.startsWith('/guide')
                  ? {
                      badge: 'DOCS',
                      title: 'Hướng Dẫn Vận Hành Hệ Thống',
                      subtitle: 'Quy trình chuẩn tạo series hoạt hình 3D tự động trên FlowKit',
                      docTitle: 'Hướng Dẫn Vận Hành | FlowKit Studio CMS',
                    }
                  : {
                      badge: 'SETTINGS',
                      title: 'Cài Đặt Hệ Thống & Kết Nối',
                      subtitle: 'Tùy chỉnh thông số kết nối và cấu hình mặc định',
                      docTitle: 'Cài Đặt Hệ Thống | FlowKit Studio CMS',
                    }

  useEffect(() => {
    document.title = pageMeta.docTitle
  }, [pageMeta.docTitle])

  return (
    <header className="flex items-center justify-between gap-4 px-6 h-16 flex-shrink-0 border-b border-slate-800/80 studio-glass sticky top-0 z-20">
      <div className="flex flex-col min-w-0">
        <div className="flex items-center gap-2">
          <span className="px-2 py-0.5 rounded-md text-[9px] font-extrabold uppercase tracking-wider bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 shrink-0">
            {pageMeta.badge}
          </span>
          <Sparkles size={14} className="text-indigo-400 shrink-0" />
          <h1 className="text-sm font-bold text-white truncate">{pageMeta.title}</h1>
        </div>
        <p className="text-[11px] text-slate-400 truncate hidden sm:block">{pageMeta.subtitle}</p>
      </div>

      <div className="flex items-center gap-3 text-xs shrink-0">
        <div className="hidden xl:flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-slate-900/90 border border-slate-800 text-[11px] text-slate-400">
          <span>API:</span>
          <code className="text-indigo-300 font-mono">{API_BASE_URL || window.location.origin}</code>
        </div>

        <div className="hidden md:flex items-center gap-2 px-3 py-1 rounded-lg bg-slate-900/90 border border-slate-800 text-[11px] text-slate-300 font-mono">
          <span>{clock.toLocaleTimeString('vi-VN')}</span>
        </div>

        <div
          className={`flex items-center gap-1.5 px-3 py-1 rounded-full text-[11px] font-semibold border ${
            isConnected
              ? 'bg-emerald-500/10 text-emerald-300 border-emerald-500/30'
              : 'bg-rose-500/10 text-rose-300 border-rose-500/30'
          }`}
        >
          {isConnected ? (
            <CheckCircle2 size={12} className="text-emerald-400" />
          ) : (
            <AlertCircle size={12} className="text-rose-400" />
          )}
          <span>{isConnected ? 'REALTIME LIVE' : 'WS OFFLINE'}</span>
        </div>

        <div className="hidden sm:flex items-center gap-2 pl-2 border-l border-slate-800 text-xs text-slate-300">
          <span className="text-slate-400">Xin chào,</span>
          <span className="font-semibold text-white">{user.display_name || user.username}</span>
        </div>
      </div>
    </header>
  )
}

function Layout({ user, onLogout }: { user: CmsUser; onLogout: () => void }) {
  return (
    <div className="flex h-screen overflow-hidden bg-[#07090e] text-slate-100">
      <Sidebar user={user} onLogout={onLogout} />
      <div className="flex flex-col flex-1 overflow-hidden">
        <Header user={user} />
        <main className="flex-1 overflow-y-auto p-6">
          <Routes>
            <Route path="/" element={<ChannelsCMSPage />} />
            <Route path="/channels/:slug" element={<ChannelsCMSPage />} />
            <Route path="/console" element={<DashboardPage />} />
            <Route path="/projects" element={<ProjectsPage />} />
            <Route path="/projects/:id" element={<ProjectsPage />} />
            <Route path="/gallery" element={<GalleryPage />} />
            <Route path="/logs" element={<LogsPage />} />
            <Route path="/guide" element={<GuidePage />} />
            <Route path="/settings" element={<SettingsPage />} />
          </Routes>
        </main>
      </div>
    </div>
  )
}

export default function App() {
  const [user, setUser] = useState<CmsUser | null>(null)
  const [checkingAuth, setCheckingAuth] = useState<boolean>(true)

  useEffect(() => {
    const token = getCmsToken()
    if (!token) {
      setCheckingAuth(false)
      return
    }
    fetchAPI<{ ok: boolean; user: CmsUser }>('/api/cms/auth/me')
      .then(res => {
        if (res.ok && res.user) setUser(res.user)
        else setCmsToken(null)
      })
      .catch(() => {
        setCmsToken(null)
      })
      .finally(() => {
        setCheckingAuth(false)
      })
  }, [])

  async function handleLogout() {
    try {
      await fetchAPI('/api/cms/auth/logout', { method: 'POST' })
    } catch {
      // ignore
    }
    setCmsToken(null)
    setUser(null)
  }

  if (checkingAuth) {
    return (
      <div className="min-h-screen flex flex-col items-center justify-center gap-3 bg-[#07090e] text-slate-400">
        <div className="w-10 h-10 rounded-2xl flex items-center justify-center studio-glow-btn animate-pulse">
          <Film size={20} />
        </div>
        <span className="text-xs font-medium">Đang tải không gian làm việc FlowKit Studio CMS...</span>
      </div>
    )
  }

  if (!user) {
    return <LoginPage onLoginSuccess={u => setUser(u)} />
  }

  return (
    <BrowserRouter>
      <LanguageProvider>
        <WebSocketProvider>
          <TooltipProvider>
            <Layout user={user} onLogout={handleLogout} />
          </TooltipProvider>
        </WebSocketProvider>
      </LanguageProvider>
    </BrowserRouter>
  )
}
