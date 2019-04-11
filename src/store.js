import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    //userId: ''
    token: localStorage.getItem('token'),
  },
  getters: {
    loggedIn: state => {
      return Boolean(state.userId.trim())
    }
  },
  mutations: {
    setUserId(state, userId) {
      state.userId = userId
    }
  },
  actions: {
    // login({commit}, user){
    // return new Promise((resolve, reject) => {
    //   commit('auth_request')
    //   axios({url: 'http://localhost:8000/api/user/login', data: user, method: 'POST' })
    //   .then(resp => {
    //     const token = resp.data.token
    //     const user = resp.data.user
    //     localStorage.setItem('token', token)
    //     axios.defaults.headers.common['Authorization'] = token
    //     commit('auth_success', token, user)
    //     resolve(resp)
    //   })
    //   .catch(err => {
    //     commit('auth_error')
    //     localStorage.removeItem('token')
    //     reject(err)
    //   })
    //   })
    // },

  }
})
