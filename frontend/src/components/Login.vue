<template>
<div>
  <button type="button" @click="Login">Login {{ message }}</button>
</div>
</template>

<style></style>

<script>
export default {
    data() {
        return {
            isLoggedIn: false
        }
    },
    methods: {
        changeLogin() {
            return false
        }
    }
}
</script>