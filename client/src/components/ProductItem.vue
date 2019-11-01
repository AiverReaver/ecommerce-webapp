<template>
  <div class="card">
    <div class="content">
      <div class="header">{{ product.name }}</div>
      <div class="meta" v-if="!product.in_stock">Out of Stock</div>
      <div class="description">{{ product.description }}</div>
    </div>
    <div class="ui bottom attached button" @click="onAddToCartCliked">
      <i class="add icon"></i>
      Add to cart
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator';
import { Action } from 'vuex-class';

@Component
export default class ProductItem extends Vue {
  @Prop() product;

  @Action addToCart;

  onAddToCartCliked() {
    this.addToCart(this.product.id);
  }
}
</script>