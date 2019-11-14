<template>
  <div id="app">
    <Navbar />
    <div class="ui container">
      <router-view />
    </div>
  </div>
</template>

<script>
import { Component, Vue } from 'vue-property-decorator';
import { Action } from 'vuex-class';
import Navbar from '@/components/Navbar.vue';

@Component({
  components: {
    Navbar,
  },
})
export default class App extends Vue {
  @Action decodeUserToken;

  created() {
    this.decodeUserToken();
  }
}
</script>

<style>
body > .grid {
  height: 100%;
}
.column {
  max-width: 450px;
}
</style>
