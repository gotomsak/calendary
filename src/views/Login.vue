<template>
  <!--<v-container>-->
    <!--<v-layout row class="text-xs-center">-->
      <!--<v-flex xs3 style="background-image: url('http://cdn.wallpapersafari.com/7/86/gqiGH7.jpg')">-->
        <!--<v-card height="500px"></v-card>-->
      <!--</v-flex>-->
      <v-flex xs4 class="grey lighten-4">
        <!--<v-container style="position: relative;top: 13%;" class="text-xs-center">-->
          <v-card flat>
            <v-card-title primary-title>
              <h4>Login</h4>
            </v-card-title>
            <v-form>
            <v-text-field prepend-icon="person" name="Email" label="Email" v-model="email"></v-text-field>
            <v-text-field prepend-icon="lock" name="Password" label="Password" type="password" v-model="password"></v-text-field>
            <v-card-actions>
              <v-btn v-on:click="login" primary large block>Login</v-btn>
            </v-card-actions>
            </v-form>
          </v-card>
        <!--</v-container>-->
      </v-flex>
    <!--</v-layout>-->
  <!--</v-container>-->
</template>

<script>
    import axios from 'axios'
    //import state from '../store'
    export default {
      name: "Login",
      data() {
        return {
          email: '',
          password: '',
          token: ''
        }
      },
      methods: {
       login: function () {
         console.log(this.email)
         console.log(this.password)
         axios.get('http://127.0.0.1:8000/api/user/login/', {
           params: {
             email: this.email,
             password: this.password
           }
         })
           .then(function (response) {
              console.log(response);
            })
            .catch(function (error) {
              console.log(error);
            })
            .then(function () {
              // always executed
            });
       }
      }
    }
</script>

<style scoped>

</style>