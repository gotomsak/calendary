<template>
    <v-btn
            :loading="loading"
            :disabled="loading"
            color="blue-grey"
            class="white--text"
            @click="loader = 'loading'"
    >
        Upload
        <v-icon right dark>cloud_upload</v-icon>
    </v-btn>
</template>

<script>
    export default {
        name: "ImageUpload",
        data() {
            return {
                loader: null,
                loading: false,
            }
        },
        watch: {
            loader() {
                const l = this.loader
                this[l] = !this[l]

                setTimeout(() => (this[l] = false), 3000)

                this.loader = null
            }
        }
    }
</script>

<style scoped>

</style>