import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Create from './views/Create.vue'
import Evaluation from "./views/Evaluation";
import Account from "./views/Account";
import History from "./views/History";

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      meta: { title: 'Home' }


    },
    {
      path: '/create',
      name: 'create',
      component: Create,
      meta: { title: 'Create' }
    },
    {
      path: '/account',
      name: 'account',
      component: Account,
      meta: { title: 'Account' }
    },
    {
      path: '/evaluation',
      name: 'evaluation',
      component: Evaluation,
      meta: { title: 'Evaluation' }
    },
    {
      path: '/history',
      name: 'history',
      component: History,
      meta: { title: 'History' }
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    }
  ]
})
