import { createApp } from 'vue'
import App from './App.vue'
//vite的入口文件

const app = createApp(App)

/*  ElementPlus组件库 */
import ElementPlus from 'element-plus'
import zhCN from 'element-plus/es/locale/lang/zh-cn'
import 'element-plus/dist/index.css'

app.use(ElementPlus,{
    locale: zhCN,
})

/*  全局配置文件  */
import CONFIG from "../experiment.config"
app.config.globalProperties.config = CONFIG

/*  启动！ */
app.mount('#app')


