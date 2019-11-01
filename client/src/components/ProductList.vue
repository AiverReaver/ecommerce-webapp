<template>
  <div class="ui cards">
    <ProductItem v-for="product in products" :key="product.id" :product="product" />
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator';
import ProductItem from './ProductItem.vue';

@Component({
  components: {
    ProductItem,
  },
})
export default class ProductList extends Vue {
  @Prop() products;
}
</script>