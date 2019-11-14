<template>
  <div>
    <h2>Past orders</h2>
    <OrderList :orders="getOrders" />
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import { Action, Getter } from 'vuex-class';
import OrderList from '../components/OrderList.vue';

@Component({
  components: {
    OrderList,
  },
})
export default class Order extends Vue {
  @Action fetchOrders;
  @Getter isLoggedIn;
  @Getter getOrders;

  mounted() {
    this.fetchOrders();
  }
}
</script>
