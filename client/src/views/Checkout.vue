<template>
  <div>
    <h1>Checkout</h1>
    <tr class="ui basic padded table">
      <thead>
        <tr>
          <th class="single line">Name</th>
          <th>Description</th>
          <th>Price</th>
          <th>discount</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="cartitems in cart.cartitems" :key="cartitems.id">
          <td>
            <h3 class="ui center aligned header">{{cartitems.product.name}}</h3>
          </td>
          <td class="single line">{{cartitems.product.description}}</td>
          <td class="single line">₹ {{cartitems.product.price}}</td>
          <td class="right aligned">{{cartitems.product.discount}}%</td>
        </tr>
      </tbody>
      <tfoot>
        <tr>
          <th colspan="5">
            <div
              class="ui right floated small primary labeled icon button"
              @click="onCheckoutCLicked"
            >
              <i class="cart arrow down icon"></i>
              ₹ {{cart.total_price}}
            </div>
          </th>
        </tr>
      </tfoot>
    </tr>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import { Action, State } from 'vuex-class';

@Component
export default class Checkout extends Vue {
  @State cart;
  @Action checkout;

  create() {
    this.$router.replace('/');
  }

  onCheckoutCLicked() {
    this.checkout();
    this.$router.replace('/');
  }
}
</script>