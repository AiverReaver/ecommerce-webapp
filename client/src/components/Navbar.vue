<template>
  <div class="ui secondary menu">
    <router-link class="item" exact-active-class="active" to="/">Home</router-link>
    <div class="right menu">
      <a class="item" @click="logout">Logout</a>
      <router-link class="item" exact-active-class="active" to="/login">Login</router-link>
      <div class="item">
        <router-link class="ui primary button" exact-active-class="active" to="/register">SignUp</router-link>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";


export default class Navbar extends Vue {
  logout() {
    
  }
}
</script>


