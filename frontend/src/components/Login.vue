<template>
<div>
<button type="button"
:class="{LoggedIn:isLoggedIn}"
@click="isLoggedIn = !isLoggedIn"
style="position: absolute; 
top: 20px;
right: 20px;">

{{isLoggedIn ? 'Logout' : 'Login'}}</button>

<img src="../assets/qrcode.png" 
style="height: 20em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;"
class="logo vue" alt="Vue logo" v-if="isLoggedIn"/> 

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