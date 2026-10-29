import { useState, useEffect, type FormEvent } from 'react'
import {
  Lock,
  User,
  ShieldCheck,
  AlertCircle,
  Sparkles,
  Eye,
  EyeOff,
  CheckCircle2,
  Tv,
  Layers,
  Terminal,
  Server,
  ArrowRight,
} from 'lucide-react'
import { fetchAPI, setCmsToken, API_BASE_URL } from '../api/client'

export interface CmsUser {
  id: string
  username: string
  display_name: string
  role: string
}

interface LoginPageProps {
  onLoginSuccess: (user: CmsUser, token: string) => void
}

export default function LoginPage({ onLoginSuccess }: LoginPageProps) {
  const [username, setUsername] = useState('admin')
  const [password, setPassword] = useState('admin123')
  const [showPassword, setShowPassword] = useState(false)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [health, setHealth] = useState<{ status?: string; extension_connected?: boolean } | null>(null)

  useEffect(() => {
    document.title = 'Đăng Nhập Quản Trị | FlowKit Studio CMS'
    fetchAPI<{ status?: string; extension_connected?: boolean }>('/health')
      .then(res => setHealth(res))
      .catch(() => setHealth(null))
  }, [])

  async function handleSubmit(e: FormEvent) {
    e.preventDefault()
    setError(null)
    setLoading(true)
    try {
      const res = await fetchAPI<{ ok: boolean; token: string; user: CmsUser }>('/api/cms/auth/login', {
        method: 'POST',
        body: JSON.stringify({ username, password }),
      })
      if (res.ok && res.token) {
        setCmsToken(res.token)
        onLoginSuccess(res.user, res.token)
      }
    } catch (err) {
      const msg = err instanceof Error ? err.message : 'Đăng nhập thất bại'
      if (msg.includes('401')) {
        setError('Tài khoản hoặc mật khẩu không chính xác!')
      } else {
        setError(msg)
      }
    } finally {
      setLoading(false)
    }
  }

  return (
    <div
      className="min-h-screen w-full flex items-center justify-center p-4 md:p-8 relative overflow-hidden"
      style={{
        background:
          'radial-gradient(circle at 15% 15%, rgba(99, 102, 241, 0.16) 0%, transparent 45%), radial-gradient(circle at 85% 80%, rgba(139, 92, 246, 0.14) 0%, transparent 45%), var(--bg)',
        color: 'var(--text)',
      }}
    >
      {/* Subtle decorative grid */}
      <div
        className="pointer-events-none absolute inset-0 opacity-20"
        style={{
          backgroundImage:
            'linear-gradient(to right, rgba(255,255,255,0.04) 1px, transparent 1px), linear-gradient(to bottom, rgba(255,255,255,0.04) 1px, transparent 1px)',
          backgroundSize: '40px 40px',
        }}
      />

      <div className="w-full max-w-5xl grid grid-cols-1 lg:grid-cols-12 rounded-3xl overflow-hidden border border-white/10 shadow-2xl relative z-10 studio-glass">
        {/* Left Showcase Panel */}
        <div
          className="lg:col-span-7 p-8 md:p-10 flex flex-col justify-between border-b lg:border-b-0 lg:border-r border-white/10"
          style={{
            background:
              'linear-gradient(145deg, rgba(99, 102, 241, 0.12) 0%, rgba(13, 17, 26, 0.85) 60%, rgba(6, 182, 212, 0.08) 100%)',
          }}
        >
          <div className="flex flex-col gap-6">
            {/* Brand Badge */}
            <div className="flex items-center gap-3">
              <img
                src="/logo.png"
                alt="FlowKit Studio"
                className="w-12 h-12 rounded-2xl object-contain bg-white p-0.5 shadow-lg shrink-0"
              />
              <div>
                <div className="flex items-center gap-2">
                  <span className="text-base font-extrabold tracking-tight text-white">FLOWKIT STUDIO</span>
                  <span className="px-2 py-0.5 text-[10px] font-bold uppercase tracking-wider rounded-full bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
                    PRO CMS v2.0
                  </span>
                </div>
                <p className="text-xs text-slate-400">Hệ thống Sản Xuất & Quản Trị Kênh TikTok Series Tự Động</p>
              </div>
            </div>

            <div className="space-y-2 mt-2">
              <h1 className="text-2xl md:text-3xl font-extrabold tracking-tight text-white leading-tight">
                Quản lý đa kênh, khóa nhân vật &{' '}
                <span className="bg-gradient-to-r from-indigo-400 via-purple-400 to-cyan-400 bg-clip-text text-transparent">
                  tự động ghép tập Full MP4
                </span>
              </h1>
              <p className="text-xs md:text-sm text-slate-400 leading-relaxed">
                Điều khiển toàn bộ 6 kênh phim hoạt hình 3D từ một giao diện duy nhất: chỉnh kịch bản từng cảnh, khóa cứng{' '}
                <code className="text-indigo-300">@Character</code>, theo dõi tiến trình thời gian thực và nối liền mạch các
                clip nhỏ thành tập hoàn chỉnh.
              </p>
            </div>

            {/* Feature Cards Grid */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
              <div className="p-3.5 rounded-2xl bg-white/[0.03] border border-white/[0.07] flex items-start gap-3">
                <div className="p-2 rounded-xl bg-indigo-500/15 text-indigo-400 shrink-0">
                  <Tv size={16} />
                </div>
                <div>
                  <div className="text-xs font-bold text-slate-100">Theo Dõi 6 Kênh Series</div>
                  <div className="text-[11px] text-slate-400 mt-0.5">
                    Mít & Đú 1970, 365 Ngày VN, Mẹ & Bé, Phèo & Nở, Tây Du Ký, Biệt Đội Gara.
                  </div>
                </div>
              </div>

              <div className="p-3.5 rounded-2xl bg-white/[0.03] border border-white/[0.07] flex items-start gap-3">
                <div className="p-2 rounded-xl bg-amber-500/15 text-amber-400 shrink-0">
                  <Lock size={16} />
                </div>
                <div>
                  <div className="text-xs font-bold text-slate-100">Khóa Nhân Vật (@Character)</div>
                  <div className="text-[11px] text-slate-400 mt-0.5">
                    Giữ nguyên tạo hình @Mit, @Đú, @Nở xuyên suốt mọi tập với Ingredients R2V + I2V.
                  </div>
                </div>
              </div>

              <div className="p-3.5 rounded-2xl bg-white/[0.03] border border-white/[0.07] flex items-start gap-3">
                <div className="p-2 rounded-xl bg-emerald-500/15 text-emerald-400 shrink-0">
                  <Layers size={16} />
                </div>
                <div>
                  <div className="text-xs font-bold text-slate-100">Tự Động Ghép Tập (FFmpeg)</div>
                  <div className="text-[11px] text-slate-400 mt-0.5">
                    Tự động nối các clip nhỏ 8-10s thành 1 file tập hoàn chỉnh ngay khi render xong.
                  </div>
                </div>
              </div>

              <div className="p-3.5 rounded-2xl bg-white/[0.03] border border-white/[0.07] flex items-start gap-3">
                <div className="p-2 rounded-xl bg-cyan-500/15 text-cyan-400 shrink-0">
                  <Terminal size={16} />
                </div>
                <div>
                  <div className="text-xs font-bold text-slate-100">Lưu Log SQLite & Live Stream</div>
                  <div className="text-[11px] text-slate-400 mt-0.5">
                    Lưu trữ toàn bộ lịch sử tạo video, mã media_id và nhật ký từng kênh trong DB.
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Live Backend Connection Footer */}
          <div className="mt-8 pt-4 border-t border-white/10 flex flex-wrap items-center justify-between gap-2 text-[11px] text-slate-400">
            <div className="flex items-center gap-2">
              <Server size={13} className="text-indigo-400" />
              <span>Backend (.env):</span>
              <code className="px-2 py-0.5 rounded-md bg-black/40 text-slate-200 border border-white/10">
                {API_BASE_URL || window.location.origin}
              </code>
            </div>
            <div className="flex items-center gap-2">
              <span
                className={`inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[10px] font-semibold border ${
                  health
                    ? 'bg-emerald-500/10 text-emerald-300 border-emerald-500/30'
                    : 'bg-rose-500/10 text-rose-300 border-rose-500/30'
                }`}
              >
                <span className={`w-1.5 h-1.5 rounded-full ${health ? 'bg-emerald-400' : 'bg-rose-400'}`} />
                {health ? 'API Online' : 'Đang kết nối API...'}
              </span>
              {health?.extension_connected && (
                <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold bg-indigo-500/15 text-indigo-300 border border-indigo-500/30">
                  <CheckCircle2 size={10} /> Extension Ready
                </span>
              )}
            </div>
          </div>
        </div>

        {/* Right Login Form Panel */}
        <div className="lg:col-span-5 p-8 md:p-10 flex flex-col justify-center bg-[#0b0f19]/90">
          <div className="flex flex-col gap-6 max-w-sm mx-auto w-full">
            <div className="flex flex-col gap-1.5">
              <div className="inline-flex items-center gap-1.5 text-xs font-semibold text-indigo-400 uppercase tracking-wider">
                <ShieldCheck size={15} />
                <span>Xác Thực Quản Trị Viên</span>
              </div>
              <h2 className="text-xl font-bold text-white">Đăng nhập vào Studio</h2>
              <p className="text-xs text-slate-400">
                Nhập thông tin tài khoản quản trị để truy cập bảng điều khiển sản xuất video.
              </p>
            </div>

            {error && (
              <div className="flex items-center gap-2.5 px-3.5 py-3 rounded-xl text-xs bg-rose-500/10 border border-rose-500/30 text-rose-300">
                <AlertCircle size={15} className="shrink-0 text-rose-400" />
                <span>{error}</span>
              </div>
            )}

            <form onSubmit={handleSubmit} className="flex flex-col gap-4">
              <div className="flex flex-col gap-1.5">
                <label className="text-xs font-medium text-slate-300">Tài khoản (Username)</label>
                <div className="flex items-center gap-2.5 px-3.5 py-2.5 rounded-xl bg-slate-900/90 border border-slate-800 focus-within:border-indigo-500 focus-within:ring-2 focus-within:ring-indigo-500/20 transition-all">
                  <User size={15} className="text-slate-400 shrink-0" />
                  <input
                    type="text"
                    value={username}
                    onChange={e => setUsername(e.target.value)}
                    placeholder="admin"
                    required
                    className="bg-transparent text-xs text-white outline-none w-full placeholder:text-slate-600"
                  />
                </div>
              </div>

              <div className="flex flex-col gap-1.5">
                <label className="text-xs font-medium text-slate-300">Mật khẩu (Password)</label>
                <div className="flex items-center gap-2.5 px-3.5 py-2.5 rounded-xl bg-slate-900/90 border border-slate-800 focus-within:border-indigo-500 focus-within:ring-2 focus-within:ring-indigo-500/20 transition-all">
                  <Lock size={15} className="text-slate-400 shrink-0" />
                  <input
                    type={showPassword ? 'text' : 'password'}
                    value={password}
                    onChange={e => setPassword(e.target.value)}
                    placeholder="••••••••"
                    required
                    className="bg-transparent text-xs text-white outline-none w-full placeholder:text-slate-600"
                  />
                  <button
                    type="button"
                    onClick={() => setShowPassword(v => !v)}
                    className="text-slate-400 hover:text-slate-200 transition-colors"
                    title={showPassword ? 'Ẩn mật khẩu' : 'Hiện mật khẩu'}
                  >
                    {showPassword ? <EyeOff size={14} /> : <Eye size={14} />}
                  </button>
                </div>
              </div>

              <button
                type="submit"
                disabled={loading}
                className="w-full mt-1 py-2.5 px-4 rounded-xl font-semibold text-xs flex items-center justify-center gap-2 studio-glow-btn disabled:opacity-50 cursor-pointer"
              >
                <span>{loading ? 'Đang xác thực phiên làm việc...' : 'Đăng Nhập Vào Hệ Thống CMS'}</span>
                {!loading && <ArrowRight size={14} />}
              </button>
            </form>

            {/* Quick Fill Default Credentials Box */}
            <div className="rounded-2xl p-3.5 bg-slate-900/70 border border-slate-800/90 flex flex-col gap-2 text-xs">
              <div className="flex items-center justify-between">
                <span className="inline-flex items-center gap-1.5 font-semibold text-slate-200 text-[11px]">
                  <Sparkles size={13} className="text-amber-400" />
                  Tài khoản Admin mặc định
                </span>
                <button
                  type="button"
                  onClick={() => {
                    setUsername('admin')
                    setPassword('admin123')
                  }}
                  className="text-[10px] px-2 py-0.5 rounded-md bg-indigo-500/15 text-indigo-300 hover:bg-indigo-500/25 border border-indigo-500/30 transition-colors cursor-pointer"
                >
                  Điền nhanh
                </button>
              </div>
              <div className="flex items-center gap-3 text-[11px] text-slate-400">
                <span>
                  User: <code className="px-1.5 py-0.5 rounded bg-black/40 text-amber-300">admin</code>
                </span>
                <span>•</span>
                <span>
                  Pass: <code className="px-1.5 py-0.5 rounded bg-black/40 text-amber-300">admin123</code>
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
