import { createApp } from 'vue'

// 导入重置样式css文件
import "normalize.css"
import App from '@/App.vue'
import router from '@/router'
import store from '@/store'
import '@/assets/css/base.css'

// 每次启动时 加载浏览器缓存到vuex中
store.dispatch("loadLocalStorage");

createApp(App).use(store).use(router).mount('#app')
