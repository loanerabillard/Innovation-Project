import Vue from 'vue'
import Router from 'vue-router'
import Meta from 'vue-meta'

import NotFound from './views/not-found'
import Home from './views/home'
import SportsBetting from './views/SportsBetting.vue'
import LiveBetting from './views/LiveBetting.vue'
import Package from './views/package.vue'
import './style.css'

Vue.use(Router)
Vue.use(Meta)

export default new Router({
  mode: 'history',
  routes: [
    {
      name: 'Not-Found',
      path: '/not-found',
      component: NotFound,
    },
    {
      name: 'Home',
      path: '/',
      component: Home,
    },
    {
      name: 'sports-betting',
      path: '/sports-betting',
      component: SportsBetting,
    },
    {
      name: 'package',
      path: '/package/:packageType',
      component: Package,
    },
    {
      path: '*',
      component: NotFound,
    }
  ],
})
