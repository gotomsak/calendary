import Vue from 'vue'
import Vuex from 'vuex'
//import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        username: localStorage.getItem('username'),
        email: '',
        token: localStorage.getItem('token'),
        image: ''
    },
    getters: {
        loggedIn: state => {
            return Boolean(state.userId.trim())
        }
    },
    modules: {

    },
    mutations: {
        setUserId(state, userId) {
            state.userId = userId
        },
        // login(state, token){
        //   localStorage.setItem('token', token)
        //   const ch = localStorage.getItem('token')
        //   console.log(ch)
        // }
        // login(state, email, password) {
        //      console.log(email)
        //      console.log(password)
        //      axios.get('http://127.0.0.1:8000/api/user/login/', {
        //        params: {
        //          email: email,
        //          password: password
        //        }
        //      })
        //        .then(function (response) {
        //           console.log(response);
        //           //state.token = response.status
        //         })
        //         .catch(function (error) {
        //           console.log(error);
        //         })
        //         .then(function () {
        //           // always executed
        //         });
        //    }

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
