import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

const base = process.env.VITE_BASE ?? '/'

// https://vitejs.dev/config/
export default defineConfig({
  base: "/",
  plugins: [svelte()]
})
