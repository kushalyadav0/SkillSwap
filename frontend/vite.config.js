import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'
// https://vite.dev/config/
export default defineConfig({
  plugins: [react(),tailwindcss()],
  build: {
    outDir: 'dist', // Vite default, but make sure Django looks for this
    emptyOutDir: true,
  },

      
})


