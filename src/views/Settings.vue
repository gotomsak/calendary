<template>
    <div>
    <v-toolbar tabs>
        <v-tabs
          v-model="tabs"
          fixed-tabs
          color="transparent"
        >
          <!--<v-tabs-slider></v-tabs-slider>-->
          <v-tab v-for="tabIcon in tabsIcon" :key="tabIcon" href="#mobile-tabs-5-1" class="primary--text">
            <v-icon>{{tabIcon.tabIcon}}</v-icon>
          </v-tab>

          <!--<v-tab href="#mobile-tabs-5-2" class="primary&#45;&#45;text">-->
            <!--<v-icon>favorite</v-icon>-->
          <!--</v-tab>-->

          <!--<v-tab href="#mobile-tabs-5-3" class="primary&#45;&#45;text">-->
            <!--<v-icon>account_box</v-icon>-->
          <!--</v-tab>-->
        </v-tabs>

    </v-toolbar>

    <v-tabs-items v-model="tabs" class="white elevation-1">
      <v-tab-item
        v-for="i in 3"
        :key="i"
        :value="'mobile-tabs-5-' + i"
      >
        <!--<v-card>-->
          <!--<v-card-text>{{ text }}</v-card-text>-->
        <!--</v-card>-->
          <UserInfoCard></UserInfoCard>
      </v-tab-item>
    </v-tabs-items>
        </div>
</template>

<script>
    import UserInfoCard from "../components/UserInfoCard";
    export default {
        name: "Settings",
        components: {UserInfoCard},
        data() {
            return {
                tabs: null,
                text: 'Lorem ',
                tabsIcon:[
                    {tabIcon: 'account_box'},
                ],
                userInfo:[
                    {}
                ]

            }
        }
    }
</script>

<style scoped>

</style>