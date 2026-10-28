const rawApiBase = (import.meta.env.VITE_API_BASE_URL as string | undefined)?.trim() ?? ''
export const API_BASE_URL = rawApiBase.replace(/\/+$/, '')

const rawWsBase = (import.meta.env.VITE_WS_BASE_URL as string | undefined)?.trim() ?? ''
export const WS_BASE_URL = rawWsBase
  ? rawWsBase.replace(/\/+$/, '')
  : API_BASE_URL
    ? API_BASE_URL.replace(/^http/i, 'ws')
    : `${window.location.protocol === 'https:' ? 'wss:' : 'ws:'}//${window.location.host}`

export function resolveApiUrl(path: string | null | undefined): string {
  if (!path) return ''
  if (/^https?:\/\//i.test(path)) return path
  const normalized = path.startsWith('/') ? path : `/${path}`
  return `${API_BASE_URL}${normalized}`
}

export const CMS_TOKEN_KEY = 'flowkit_cms_token'

export function getCmsToken(): string | null {
  try {
    return localStorage.getItem(CMS_TOKEN_KEY)
  } catch {
    return null
  }
}

export function setCmsToken(token: string | null) {
  try {
    if (token) localStorage.setItem(CMS_TOKEN_KEY, token)
    else localStorage.removeItem(CMS_TOKEN_KEY)
  } catch {
    // ignore storage errors
  }
}

export async function fetchAPI<T>(path: string, options?: RequestInit): Promise<T> {
  const token = getCmsToken()
  const authHeaders: Record<string, string> = {}
  if (token) {
    authHeaders['Authorization'] = `Bearer ${token}`
    authHeaders['X-CMS-Token'] = token
  }
  const url = resolveApiUrl(path)
  const res = await fetch(url, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...authHeaders,
      ...((options?.headers as Record<string, string>) || {}),
    },
  })
  if (!res.ok) {
    const err = await res.text().catch(() => res.statusText)
    throw new Error(`API ${res.status} (${url}): ${err}`)
  }
  return res.json()
}

export async function patchAPI<T>(path: string, body: Record<string, unknown>): Promise<T> {
  return fetchAPI<T>(path, { method: 'PATCH', body: JSON.stringify(body) })
}
