<template>
    <div>
        <!--<a v-for="item in texts" v-bind:key="item.name">-->
            <!--<v-text-field :prepend-icon="item.icon" :name="item.name" :label="item.label" :v-model="item.model"/>-->
        <!--</a>-->
        <a v-for="text in name" v-bind:key="text.icon">

            <v-text-field :prepend-icon="text.icon" :name="text.name" :label="text.label" :type="text.type" v-model="model.add"/>
        </a>
    </div>
</template>

<script>
    export default {
        name: "TextField",
        props: ['name'],
        data(){
            return {
                model: []
            }
        },

        methods: {

            inputModel: function () {
                this.$emit('inModel', this.name)
            },

        }


    }
</script>

<style scoped>

</style>