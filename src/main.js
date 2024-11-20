import '@/assets/css/reset.css'
import 'element-plus/dist/index.css'
import '@/assets/css/index.less'
import envVariables from '../public/env-variables.js'
import ElementPlus from 'element-plus'
import App from './App.vue'
import { registerLicense } from '@syncfusion/ej2-base';
import { createApp } from 'vue'
import { setupRouter } from './router/index'
import { setupStore } from '@/store'
import { registerGlobComp } from '@/components/registerGlobComp'

// 挂载环境变量
window.envVariables = envVariables

// 环境及打包信息
console.log(`${envVariables.title}  ${buildTime}  ${import.meta.env.MODE}`)

function bootstrap() {
  // License
  registerLicense('Ngo9BigBOggjHTQxAR8/V1NDaF1cX2hIfEx3Qnxbf1x0ZFRHalxVTnNYUj0eQnxTdEFiWH5ZcndVQmVUWEF0Ww==');
  const app = createApp(App)
  // 路由
  setupRouter(app)
  // store
  setupStore(app)
  // 全局组件注册
  registerGlobComp(app)
  app.use(ElementPlus).mount('#app')
}
bootstrap()
