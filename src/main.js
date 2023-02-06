import { createApp } from 'vue'
import App from './App.vue'
//vite的入口文件

const app = createApp(App)

/*  ElementPlus组件库 */
import ElementPlus from 'element-plus'
import zhCN from 'element-plus/es/locale/lang/zh-cn'
import 'element-plus/dist/index.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

app.use(ElementPlus,{
    locale: zhCN,
    size:"large"
})
for(const [key,component] of Object.entries(ElementPlusIconsVue)){
    app.component(key,component)
}

/*  全局配置文件  */
const CONFIG = require("../experiment.config")
app.config.globalProperties.config = CONFIG

/*  启动！ */
app.mount('#app')


