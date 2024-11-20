import Layout from '@/layout/index.vue'
import RouteView from '@/components/Tool/RouteView.vue'
const layoutMap = [
  // {
  //   path: 'home',
  //   name: 'Home',
  //   component: () => import('@/view/home/index.vue'),
  //   meta: { title: 'BGP安全态势感知', icon: 'HomeFilled' }
  // },
  {
    path: 'situation',
    name: 'BGPSituation',
    component: RouteView,
    meta: { title: 'BGP安全态势感知', icon: 'Setting' },
    redirect: { name: 'Summary' },
    children: [
      {
        path: 'summary',
        name: 'Summary',
        meta: { title: '安全态势概览', icon: 'User' },
        component: () => import('@/view/situation/summary/index.vue'),
      },
      {
        path: 'details-prefix',
        name: 'DetailsPrefix',
        meta: { title: '前缀详情', icon: 'User' },
        component: () => import('@/view/situation/details-prefix/index.vue')
      },
      {
        path: 'details-asn',
        name: 'DetailsAsn',
        meta: { title: 'AS详情', icon: 'Stamp' },
        component: () => import('@/view/situation/details-asn/index.vue')
      },
      {
        path: 'as-topology',
        name: 'ASTopology',
        meta: { title: 'AS拓扑关系', icon: 'Menu' },
        component: () => import('@/view/situation/as-topology/index.vue')
      },
    ]
  }
]

const routes = [
  {
    path: '/',
    name: 'Layout',
    meta: { title: '主页' },
    redirect: { name: 'BGPSituation' },
    component: Layout,
    children: [...layoutMap]
  },
]

export { routes, layoutMap }
