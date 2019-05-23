<template>
    <v-app id="inspire">

        <v-navigation-drawer v-model="drawer" clipped fixed app>

            <v-list dense>
                <v-toolbar flat class="transparent">
                    <v-list>
                        <v-list-tile>
                            <v-list-tile-avatar :tile="tile">
                                <!--<img src="./assets/img/user/icon/nero.jpg" alt="avatar">-->
                                <img v-bind:src='image' alt="avatar">
                            </v-list-tile-avatar>
                            <v-list-tile-content>
                                <v-list-tile-title>{{ username }}</v-list-tile-title>
                            </v-list-tile-content>
                        </v-list-tile>
                    </v-list>
                </v-toolbar>

                <v-divider></v-divider>

                <a v-for="item in items" v-bind:key="item.title">
                    <router-link :to="item.path" class="link">
                        <v-list-tile>
                            <v-list-tile-action>
                                <v-icon>{{item.icon}}</v-icon>
                            </v-list-tile-action>
                            <v-list-tile-content>
                                <v-list-tile-title>{{item.title}}</v-list-tile-title>
                            </v-list-tile-content>
                        </v-list-tile>
                    </router-link>
                </a>

            </v-list>
        </v-navigation-drawer>

        <v-content>
            <v-layout justify-center>
                <router-view></router-view>
            </v-layout>
        </v-content>

        <v-toolbar app fixed clipped-left>
            <v-toolbar-side-icon @click.stop="stopDrawer"></v-toolbar-side-icon>
            <v-toolbar-title id="title">Calendary</v-toolbar-title>
        </v-toolbar>

    </v-app>

</template>
<script>
    import router from "./router"
    import store from "./store"
    router.afterEach((to) => {
        if (to.meta && to.meta.title) {
            document.getElementById("title").innerHTML = to.meta.title
        }
    })
    export default {
        components: {},
        methods: {
            stopDrawer: function () {
                this.drawer = !this.drawer
                //console.log(this.$router.name)
                console.log(this.username)
                this.username = store.state.username
            },

        },
        data() {

            return {
                drawer: true,
                // viewTitle: this.$router.name,
                tile: true,
                username: store.state.username,
                image: store.state.image,

                items: [
                    {title: 'Home', icon: 'mdi-home', path: '/'},
                    // { title: 'Account', icon: 'account_circle', path: '/account'},
                    {title: 'Create', icon: 'mdi-pencil', path: '/create'},
                    {title: 'Evaluation', icon: 'mdi-thumbs-up-down', path: '/evaluation'},
                    {title: 'History', icon: 'mdi-history', path: '/history'},
                    {title: 'Login', icon: 'mdi-login', path: '/login'},
                    {title: 'Signup', icon: 'mdi-account-plus', path: '/signup'},
                    {title: 'Settings', icon: 'mdi-settings', path:'/settings'}
                ],
                // mini: true,
                // right: null
            }
        }
    }

</script>
<style>
    .link {
        text-decoration: none;
        color: #000000;
    }
</style>
