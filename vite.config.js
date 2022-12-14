import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  base:'./dist/',
  plugins: [
    vue()
  ],
  build:{
    minify:false//不进行压缩混淆，便于debug
  }
})
