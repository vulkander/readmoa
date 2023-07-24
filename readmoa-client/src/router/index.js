import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Write from '../views/Write.vue'
import Login from '../views/Login.vue'
import Setting from '../views/Setting.vue'
import Privacy from '../views/Privacy.vue'
import Terms from '../views/Terms.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: Home,
    name: 'Home'
  },
  {
    path: '/login',
    component: Login,
    name: '로그인'
  },
  {
    path: '/write',
    component: Write,
    name: '글쓰기'

  },
  {
    path: '/setting',
    component: Setting,
    name: '설정'
  },
  {
    path: '/privacy',
    component: Privacy
  },
  {
    path: '/terms',
    component: Terms
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
