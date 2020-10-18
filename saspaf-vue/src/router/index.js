import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import GetInvolved from '../views/GetInvolved.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'GetInvolved',
    component: GetInvolved
  }
]

const router = new VueRouter({
  routes
})

export default router
