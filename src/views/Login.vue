<template>
    <!--<v-container fluid grid-list-md>-->
    <!--<v-slide-y-transition mode="out-in">-->
    <!--<v-layout row wrap align-center>-->
    <!--<v-flex>-->
    <!--<v-card flat>-->
    <!--<v-card-title primary-title>-->
    <!--<h4>Login</h4>-->
    <!--</v-card-title>-->
    <!--<v-form>-->
    <!--<TextField v-bind:name="texts"/>-->
    <!--<v-card-actions>-->
    <!--<v-btn v-on:click="login" primary large block>login</v-btn>-->
    <!--</v-card-actions>-->
    <!--</v-form>-->
    <!--</v-card>-->
    <!--</v-flex>-->
    <!--</v-layout>-->
    <!--</v-slide-y-transition>-->
    <!--</v-container>-->

    <UserInfoCard v-on:userInfoEvent="login" v-bind:name="texts" v-bind:title="title"></UserInfoCard>
</template>

<script>
    import axios from 'axios'
    // import store from '../store'
    //import TextField from '../components/TextField'
    import UserInfoCard from "../components/UserInfoCard";
    import store from "../store"

    export default {
        name: "Login",
        data() {
            return {
                title: 'Login',
                texts: [
                    {icon: 'email', name: 'Email', label: 'Email', model: '', type: 'email'},
                    {icon: 'lock', name: 'Password', label: 'Password', model: '', type: 'password'}
                ]

            }
        },
        components: {
            UserInfoCard,
            //TextField,
        },
        methods: {
            login: function () {
                // console.log(this.texts.password)
                axios.get('http://127.0.0.1:8000/api/user/login/', {
                    params: {
                        email: this.texts[0].model,
                        password: this.texts[1].model
                    }
                })
                    .then(function (response) {
                        // store.commit('login', response.data.token)
                        localStorage.setItem('token', response.data[1].key);
                        localStorage.setItem('username', response.data[0].username);
                        console.log(store.state.username);
                        console.log(store.state.token);
                        store.state.token = response.data[1].key;
                        store.state.username = response.data[0].username;
                        store.state.image = response.data[0].image;
                        //console.log(response.data);
                    })
                    .catch(function (error) {
                        console.log(error);
                    })
                    .then(function () {
                        // always executed
                    });
            },

        }

    }

</script>

<style scoped>

</style>