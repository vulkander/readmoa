
import Vue from 'vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import App from './App.vue'
import router from './router'

// bootstarp
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// font awesome
import { library } from '@fortawesome/fontawesome-svg-core'
import { faComment, faThumbsUp, faShareAlt } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import BlockUI from 'vue-blockui'

// material icons
import { MdIcon } from 'vue-material/dist/components'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

// components
import BottomNav from './components/BottomNav'
import TopNav from './components/TopNav'
import PostWrite from './components/PostWrite'
import PostList from './components/PostList'
import Loginform from './components/LoginForm'

// firebase
import firebase from 'firebase'

// my style css
import './assets/css/main.css'

Vue.use(BlockUI)

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
library.add(faComment, faThumbsUp, faShareAlt)
Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.use(MdIcon)
Vue.component('TopNav', TopNav)
Vue.component('BottomNav', BottomNav)
Vue.component('PostWrite', PostWrite)
Vue.component('PostList', PostList)
Vue.component('LoginForm', Loginform)

Vue.config.productionTip = false

Vue.prototype.$hostname = 'http://127.0.0.1:5000'
// Vue.prototype.$hostname = 'http://testsocial.tk:5000'

// Initialize Firebase
let app = ''

firebase.initializeApp({
  apiKey: 'AIzaSyD5QZ1NRWxA3rr2VxVPFOLXmRLY_1EK1R0',
  authDomain: 'read-moa.firebaseapp.com',
  databaseURL: 'https://read-moa.firebaseio.com',
  projectId: 'read-moa',
  storageBucket: 'read-moa.appspot.com',
  messagingSenderId: '440773081280',
  appId: '1:440773081280:web:bb616368dcd13410ba5525'

})

firebase.auth().onAuthStateChanged(() => {
  if (!app) {
    app = new Vue({
      router,
      render: h => h(App)
    }).$mount('#app')
  }
})
