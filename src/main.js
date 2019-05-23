import Vue from 'vue'
//import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'
import '@mdi/font/css/materialdesignicons.css'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import axios from 'axios'
// import Axios from 'axios'
//
// Vue.prototype.$http = Axios;
// const token = localStorage.getItem('token')
// if (token) {
//   Vue.prototype.$http.defaults.headers.common['Authorization'] = token
// }
Vue.config.productionTip = false
Vue.use(Vuetify)
new Vue({

    router,
    store,
    render: h => h(App),
    created() {
        axios.get('http://127.0.0.1:8000/api/check_user/', {
            params: {
                token: store.state.token
            }
        })
            .then(function (response) {
                // store.commit('login', response.data.token)
                console.log(response.data[0])
                console.log(response.data[1])
                localStorage.setItem('token', response.data[1].key);
                localStorage.setItem('username', response.data[0].username);
                console.log(store.state.username);
                console.log(store.state.token);
                store.state.token = response.data[1].key;
                store.state.username = response.data[0].username;
                //console.log(response.data);
            })
            .catch(function (error) {
                console.log(error);
            })
            .then(function () {
                // always executed
            });
    }

}).$mount('#app')
