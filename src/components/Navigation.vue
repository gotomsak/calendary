<template>

    <v-navigation-drawer
            v-model="drawer"
            clipped
            fixed
            app
    >
        <!--<v-list dense>-->

        <!--<v-list-tile>-->
        <!--<v-list-tile-avatar>-->
        <!--<img src="https://randomuser.me/api/portraits/men/85.jpg">-->
        <!--</v-list-tile-avatar>-->

        <!--<v-list-tile-content>-->
        <!--<v-list-tile-title>John Leider</v-list-tile-title>-->
        <!--</v-list-tile-content>-->
        <!--</v-list-tile>-->
        <!--<router-link class="link" to="/create">-->
        <!--<v-list-tile-->
        <!--v-for="item in items"-->
        <!--:key="item.title"-->
        <!--@click=""-->
        <!--&gt;-->

        <!--<v-list-tile-action>-->
        <!--<v-icon>{{ item.icon }}</v-icon>-->
        <!--</v-list-tile-action>-->

        <!--<v-list-tile-content>-->
        <!--<v-list-tile-title>{{ item.title }}</v-list-tile-title>-->
        <!--</v-list-tile-content>-->

        <!--</v-list-tile>-->
        <!--</router-link>-->
        <!--</v-list>-->

        <v-list dense>
            <v-toolbar flat class="transparent">
                <v-list>
                    <v-list-tile>
                        <v-list-tile-avatar>
                            <img src="https://randomuser.me/api/portraits/men/85.jpg">
                        </v-list-tile-avatar>

                        <v-list-tile-content>
                            <v-list-tile-title>John Leider</v-list-tile-title>
                        </v-list-tile-content>
                    </v-list-tile>
                </v-list>
            </v-toolbar>

            <v-divider></v-divider>

            <router-link class="link" to="/">
                <v-list-tile>
                    <v-list-tile-action>
                        <v-icon>home</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-content>
                        <v-list-tile-title>Home</v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
            </router-link>

            <router-link class="link" to="/create">
                <v-list-tile>
                    <v-list-tile-action>
                        <v-icon>create</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-content>
                        <v-list-tile-title>Create</v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
            </router-link>

            <router-link class="link" to="/evaluation">
                <v-list-tile>
                    <v-list-tile-action>
                        <v-icon>thumbs_up_down</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-content>
                        <v-list-tile-title>Evaluation</v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
            </router-link>

            <router-link class="link hist" to="/history">
                <v-list-tile>
                    <v-list-tile-action>
                        <v-icon>history</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-content>
                        <v-list-tile-title>History</v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
            </router-link>


        </v-list>

    </v-navigation-drawer>





</template>

<script>
    export default {
        name: "Navigation",
        data() {
            return{
                title: "Home"
            }

        }
    }
</script>

<style scoped>

</style>
