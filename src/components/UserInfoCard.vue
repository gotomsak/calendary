<template>
     <v-container fluid grid-list-md>
        <v-slide-y-transition mode="out-in">
            <v-layout row wrap align-center>
                <v-flex>
                    <v-card flat>
                        <v-card-title primary-title>
                            <h4>{{ title }}</h4>
                        </v-card-title>
                        <v-form>
                            <a v-for="text in name" v-bind:key="text.icon">

                                <v-text-field
                                        :prepend-icon="text.icon"
                                        :name="text.name"
                                        :label="text.label"
                                        :type="text.type"
                                        v-model="text.model"
                                />
                            </a>
                            <v-card-actions>
                                <v-btn @click="$emit('userInfoEvent')" primary large block>send</v-btn>
                            </v-card-actions>
                        </v-form>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-slide-y-transition>
    </v-container>
</template>

<script>


    export default {

        name: "UserInfoCard",
        props: ['name', 'title'],
        data(){
            return{
            }
        },
        component:{

        },
        methods:{
            userInfoEvent: function(){
                this.$emit('user-info-event')
            }
        }

    }
</script>

<style scoped>

</style>