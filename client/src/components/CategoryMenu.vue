<template>
  <div class="ui grid">
    <div class="four wide column">
      <div class="ui secondary vertical pointing menu">
        <a
          v-for="category in categories"
          :key="category.id"
          @click.prevent="onCategorySelected(category)"
          :class="{'active': category.id == selectedCategory.id}"
          class="item"
        >{{category.name}}</a>
      </div>
    </div>
    <div class="twelve wide stretched column">
      <div class="ui segment">
        <ProductList :products="selectedCategory.products" />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator';
import { State, Mutation, Action } from 'vuex-class';

import ProductList from './ProductList.vue';

@Component({
  components: {
    ProductList,
  },
})
export default class CategoryMenu extends Vue {
  @Prop() categories;

  @State selectedCategory;
  @Action getProducts;
  @Mutation setSelectedCategory;

  async onCategorySelected(category) {
    this.setSelectedCategory(category);
  }
}
</script>