<template>
  <div class="ui cards">
    <div class="card" v-for="product in products" :key="product.id">
      <div class="content">
        <div class="header">{{ product.name }}</div>
        <div class="meta" v-if="!product.in_stock">Out of Stock</div>
        <div class="description">{{ product.description }}</div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator';

@Component
export default class ProductList extends Vue {
  @Prop() products;
}
</script>