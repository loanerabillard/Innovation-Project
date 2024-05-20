import Vue from 'vue'
import Router from 'vue-router'
import Meta from 'vue-meta'

import NotFound1, { NotFound } from './views/not-found'
import Home from './views/home'
import SportBettingPage from  './views/sportsbettingpage'
import './style.css'

Vue.use(Router)
Vue.use(Meta)
export default new Router({
  mode: 'history',
  routes: [
    {
      name: 'Not-Found',
      path: '/not-found',
      component: NotFound1,
    },
    {
      name: 'Home',
      path: '/',
      component: Home,
    },
    {
      name: 'Sports Betting',
      path: '/sports-betting',
      component: SportBettingPage
    },
    {
      name: '404 - Not Found',
      path: '**',
      component: NotFound,
      fallback: true,
    },
  ],
})
