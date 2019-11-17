<template>
  <div class="ui celled list">
    <div class="item" v-for="order in orders" :key="order.id">
      <div class="content">
        <div class="header">{{order.user}}</div>
        <b>{{order.product_name}}</b>
        delivere to
        <b>{{order.address}}</b>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import { Getter, Action } from 'vuex-class';

@Component
export default class ProductOrders extends Vue {
  @Getter isLoggedIn;
  @Getter role;

  @Action fetchProductOrders;

  orders = [];

  async created() {
    if (!this.isLoggedIn) {
      this.$router.replace('/');
    }
    this.orders = await this.fetchProductOrders();
  }
}
</script>