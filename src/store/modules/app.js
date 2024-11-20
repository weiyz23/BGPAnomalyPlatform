import { defineStore } from 'pinia'
import { layoutMap } from '@/router/routes'

export const useAppStore = defineStore({
  id: 'app',
  state: () => ({
    counter: 0,
    breadCrumb: [],
    routerList: JSON.parse(JSON.stringify(layoutMap)),
  }),
  getters: {
    getBreadCrumb() {
      return this.breadCrumb
    },
    getRouterList() {
      return this.routerList
    }
  },
  actions: {
    setRouterList(routerList) {
      this.routerList = routerList
    },
    setBreadCrumb(breadCrumb) {
      this.breadCrumb = breadCrumb
    }
  }
})
