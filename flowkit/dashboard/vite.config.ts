import path from 'node:path'
import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '')
  const apiTarget = env.VITE_API_BASE_URL || 'http://127.0.0.1:8200'
  const wsTarget = env.VITE_WS_BASE_URL || apiTarget.replace(/^http/i, 'ws')

  return {
    plugins: [react(), tailwindcss()],
    resolve: {
      alias: {
        '@': path.resolve(__dirname, './src'),
      },
    },
    server: {
      port: 5173,
      proxy: {
        '/api': apiTarget,
        '/ws': { target: wsTarget, ws: true },
        '/health': apiTarget,
      },
    },
    build: { outDir: 'dist' },
  }
})
