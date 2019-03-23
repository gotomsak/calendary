import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Create from './views/Create.vue'
import Evaluation from "./views/Evaluation";
import Account from "./views/Account";
import History from "./views/History";
import test from "./views/test";
import store from "./store";
import Login from "./views/Login";


Vue.use(Router)


const router = new Router({

  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      meta: { title: 'Home', meta: { requiresAuth: true }}

    },
    {
      path: '/create',
      name: 'create',
      component: Create,
      meta: { title: 'Create', meta: { requiresAuth: true }}
    },
    {
      path: '/account',
      name: 'account',
      component: Account,
      meta: { title: 'Account', meta: { requiresAuth: true }}
    },
    {
      path: '/evaluation',
      name: 'evaluation',
      component: Evaluation,
      meta: { title: 'Evaluation', meta: { requiresAuth: true }}
    },
    {
      path: '/history',
      name: 'history',
      component: test,
      meta: { title: 'History', meta: { requiresAuth: true }}
    },
    {
      path: '/login',
      name: 'login',
      component: Login,

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

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.getters.loggedIn) {
      next({
        path: '/login',
        query: {
          redirect: to.fullPath,
          message: true
        }
      })
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router