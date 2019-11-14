<template>
  <div class="ui secondary menu">
    <router-link class="item" exact-active-class="active" to="/">Home</router-link>
    <div class="right menu">
      <div class="item">
        <router-link
          exact-active-class="active"
          to="/orders"
          class="ui labeled button"
          v-if="isLoggedIn"
        >
          <i class="shopping bag icon"></i>My Orders
        </router-link>
      </div>
      <router-link exact-active-class="active" to="/checkout" class="item" v-if="isLoggedIn">
        <i class="shopping cart icon"></i>
        <div class="ui teal left pointing label">{{ CartItemsCount }}</div>
      </router-link>
      <a class="item" v-if="isLoggedIn" @click="logout">Logout</a>
      <router-link v-if="!isLoggedIn" class="item" exact-active-class="active" to="/login">Login</router-link>
      <div class="item" v-if="!isLoggedIn">
        <router-link class="ui primary button" exact-active-class="active" to="/register">SignUp</router-link>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import { Getter, Action } from 'vuex-class';

@Component
export default class Navbar extends Vue {
  @Getter isLoggedIn;
  @Getter CartItemsCount;
  @Action logoutUser;
  @Action getCart;
  @Action decodeUserToken;

  mounted() {
    if (this.isLoggedIn) {
      this.getCart();
    }
  }
  public logout() {
    this.logoutUser();
    this.decodeUserToken();
  }
}
</script>
