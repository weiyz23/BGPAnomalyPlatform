import { createRouter, createWebHistory } from 'vue-router'
import { routes } from './routes.js'
import { decode } from 'js-base64'
import { useAppStore } from '@/store/modules/app'

export const router = createRouter({
  history: createWebHistory(),
  routes: [...routes],
  scrollBehavior: () => ({ left: 0, top: 0 })
})

router.beforeEach((to, from, next) => {
  const appStore = useAppStore()
  document.title = (to.meta && to.meta.title) || ''
  // 设置面包屑
  const breadCrumbList = []
  to.matched.forEach(item => {
    breadCrumbList.push({ name: item.meta.title, path: item.path })
  })
  appStore.setBreadCrumb(breadCrumbList)
  // 直接跳转至/summary
  if (to.path === '/') {
    next( { name: 'BGPSituation' })
  } else {
    next()
  }
})

export function setupRouter(app) {
  app.use(router)
}
