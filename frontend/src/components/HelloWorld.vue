<script setup>
import {ref} from 'vue'

const count = ref(0)
</script>

<template>
  <h1>{{ msg }}</h1>

  <div class="card">
    <button type="button" @click="count++">count is {{ count }}</button>
    <p>
      Edit
      <code>components/HelloWorld.vue</code> to test HMR
    </p>
    <button type="button" @click="getHelloWorld">count is {{ message }}</button>

  </div>

  <p>
    Check out
    <a href="https://vuejs.org/guide/quick-start.html#local" target="_blank"
    >create-vue</a
    >, the official Vue + Vite starter
  </p>
  <p>
    Install
    <a href="https://github.com/vuejs/language-tools" target="_blank">Volar</a>
    in your IDE for a better DX
  </p>
  <p class="read-the-docs">Click on the Vite and Vue logos to learn more</p>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>

<script>
import axios from 'axios';
export default {
  name: 'HelloWorld',
  props: {
    msg: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      message: '',
    };
  },
  methods: {
    getHelloWorld() {
    // make a get request to localhost:8000 and set the response to message
      axios.get('http://localhost:8000',{
          withCredentials: true,
      }).then((response) => {
        this.message = response.data;
      });
    },
  }
};
</script>
