<template>
  <v-container fluid grid-list-md>
    <v-slide-y-transition mode="out-in">
      <v-layout row wrap align-center>
        <v-flex v-for="entry in entryList" v-bind:key="entry.title">
          <v-card>

            <v-img :src="entry.img" aspect-ratio="2.75">
            </v-img>
            <v-card-title>
              <span class="headline">{{ entry.title }}</span>
            </v-card-title>
            <v-card-text>
              <blockquote>
                {{ entry.content }}
                <footer>
                  <small>
                    <em>&mdash;{{ entry.date }}</em>
                  </small>
                </footer>
              </blockquote>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-slide-y-transition>
  </v-container>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
import axios from 'axios'

export default {
  data () {
    return {
      entryList: []
    }
  },
  mounted: function () {
    console.log('mounted')
    // APIを叩く。
    // 開発サーバで動作中はちゃんとDjangoの8000番ポートを叩いてくれます。
    axios.get('/api/entries/')
      .then((response) => {
        this.entryList = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods:{
    image_show: function (i) {
      return require(i.img)
    }
  }
}
</script>