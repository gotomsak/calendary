<template>
    <!--<v-container fluid grid-list-md>-->
    <!--<v-slide-y-transition mode="out-in">-->
    <!--<v-layout row wrap align-center>-->
    <!--<v-flex>-->
    <!--<v-card flat>-->
    <!--<v-card-title primary-title>-->
    <!--<h4>Signup</h4>-->
    <!--</v-card-title>-->
    <!--<v-form>-->
    <!--<TextField v-bind:name="texts"/>-->
    <!--<v-card-actions>-->
    <!--<v-btn v-on:click="signup" primary large block>signup</v-btn>-->
    <!--</v-card-actions>-->
    <!--</v-form>-->
    <!--</v-card>-->
    <!--</v-flex>-->
    <!--</v-layout>-->
    <!--</v-slide-y-transition>-->
    <!--</v-container>-->
    <!--<a v-if="texts">-->
    <!--<user-info-card v-bind:name="texts" v-bind:class="signup"></user-info-card>-->
    <!--</a>-->
    <UserInfoCard v-on:userInfoEvent="signup" v-bind:name="texts" v-bind:title="title"></UserInfoCard>
</template>

<script>
    // import UserCard from "../components/UserCard"
    import axios from 'axios'
    // import store from '../store'
    //import TextField from '../components/TextField'
    import UserInfoCard from "../components/UserInfoCard";

    export default {
        name: "Signup",
        // components: {UserCard},
        components: {
            UserInfoCard,
            //TextField
        },
        data() {
            return {
                title: 'Signup',
                texts: [
                    {icon: 'person', name: 'Username', label: 'Username', model: '', type: 'name'},
                    {icon: 'email', name: 'Email', label: 'Email', model: '', type: 'email'},
                    {icon: 'lock', name: 'Password', label: 'Password', model: '', type: 'password'}
                ]

            }
        },
        methods: {
            signup: function () {

                axios.post('http://127.0.0.1:8000/api/user/signup/', {
                    params: {
                        username: this.texts[0].model,
                        email: this.texts[1].model,
                        password: this.texts[2].model
                    }
                })
                    .then(function (response) {
                        console.log('Signupしました')
                        // store.commit('login', response.data.token)
                        //console.log(response.data);
                    })
                    .catch(function (error) {
                        console.log(error);
                    })
                    .then(function () {
                        // always executed
                    });
            }
        },
        comments: {}

    }
</script>

<style scoped>

</style>