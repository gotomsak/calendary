<template>
    <v-flex xs4 class="grey lighten-4">

        <v-card flat>
          <v-card-title primary-title>
            <h4>Signup</h4>
          </v-card-title>
          <v-form>
            <a v-for="text in texts" v-bind:key="text.name">
              <v-text-field :prepend-icon="text.icon" :name="text.name" :label="text.label" :v-model="text.model"/>
            </a>
          <v-card-actions>
            <v-btn v-on:click="signup" primary large block>signup</v-btn>
          </v-card-actions>
          </v-form>
        </v-card>
      <!--<UserCard></UserCard>-->

    </v-flex>
</template>

<script>
  // import UserCard from "../components/UserCard"
  import axios from 'axios'
  import store from '../store'
    export default {
      name: "Signup",
      // components: {UserCard},
      //components: {TextField},
      data() {
        return {
          username: '',
          email: '',
          password: '',
          texts: [
            {icon: 'person', name: 'Username', label: 'Username', model: 'Username'},
            {icon: 'email', name: 'Email', label: 'Email', model: 'email'},
            {icon: 'lock', name: 'Password', label: 'Password', model: 'password'}
          ]

        }
      },
      methods:{
        signup: function () {
         console.log(this.email)
         console.log(this.password)
         axios.post('http://127.0.0.1:8000/api/user/signup/', {
           params: {
             username: this.username,
             email: this.email,
             password: this.password
           }
         })
           .then(function (response) {
             store.commit('login',response.data.token)
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
      comments:{

      }

    }
</script>

<style scoped>

</style>