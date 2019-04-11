<template>
  <v-app id="inspire">

    <v-navigation-drawer v-model="drawer" clipped fixed app>

      <v-list dense>
        <v-toolbar flat class="transparent">
          <v-list>
            <v-list-tile>
              <v-list-tile-avatar>
                <img src="image">
              </v-list-tile-avatar>

              <v-list-tile-content>
                <v-list-tile-title>John Leider</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
        </v-toolbar>

        <v-divider></v-divider>

        <router-link to="/" class="link">
          <v-list-tile>
            <v-list-tile-action>
              <v-icon>home</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>Home</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </router-link>

        <router-link to="/create" class="link">
          <v-list-tile>
            <v-list-tile-action>
              <v-icon>create</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>Create</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </router-link>

        <router-link to="/evaluation" class="link">
          <v-list-tile>
            <v-list-tile-action>
              <v-icon>thumbs_up_down</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>Evaluation</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </router-link>

        <router-link to="/history" class="link">
          <v-list-tile>
            <v-list-tile-action>
              <v-icon>history</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>History</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </router-link>

        <router-link to="/login" class="link">
          <v-list-tile >
            <v-list-tile-action>
              <v-icon>login</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>Login</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </router-link>

      </v-list>

    </v-navigation-drawer>

    <v-content>
        <v-layout justify-center>
          <router-view></router-view>
        </v-layout>
    </v-content>

    <v-toolbar app fixed clipped-left >
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title id="title">Home</v-toolbar-title>
    </v-toolbar>

  </v-app>

</template>
<script>
  import router from "./router"
  // router.afterEach((to) => {
  //   if (to.meta && to.meta.title) {
  //     document.getElementById("title").innerHTML = to.meta.title
  //   }
  // })
  export default {
    components: { },
    methods:{
    },
    data () {

      return {
        drawer: true,
        // items: [
        //   { title: 'Home', icon: 'home'},
        //   { title: 'Account', icon: 'account_circle'},
        //   { title: 'Create', icon: 'create'},
        //   { title: 'Evaluation', icon: 'thumbs_up_down'},
        //   { title: 'History', icon: 'history'}
        // ],
        // mini: true,
        // right: null
      }
    }
  }

</script>
<style>
   .link {
     text-decoration:none;
     color: #000000;
  }
</style>
