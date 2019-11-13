<template>
  <div class="card">
    <div class="content">
      <div class="header">{{ product.name }}</div>
      <div class="meta" v-if="!product.in_stock">Out of Stock</div>
      <div class="description">{{ product.description }}</div>
    </div>
    <div
      class="ui bottom attached button"
      :class="{'red disabled':!product.in_stock, 'green': product.in_stock }"
      @click="onAddToCartCliked"
    >
      <i class="add icon"></i>
      Add to cart
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator';
import { Action, State } from 'vuex-class';

@Component
export default class ProductItem extends Vue {
  @Prop() product;

  @State cart;
  @Action addToCart;
  @Action getCart;

  onAddToCartCliked() {
    const cartToSend = { id: this.cart.id, productId: this.product.id };
    this.addToCart(cartToSend);
    this.getCart();
  }
}
</script>