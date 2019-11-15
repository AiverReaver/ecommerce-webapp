<template>
  <div>
    <h1>Create Product</h1>
    <form class="ui form">
      <div class="field">
        <label>Product Name</label>
        <input
          type="text"
          name="product-name"
          placeholder="Product Name"
          v-model="product.name"
          required
        />
      </div>
      <div class="field">
        <label>Description</label>
        <input
          type="text"
          name="description"
          placeholder="Description"
          v-model="product.description"
          required
        />
      </div>
      <div class="field">
        <label>Price</label>
        <input type="number" name="price" placeholder="Price" v-model="product.price" required />
      </div>
      <div class="field">
        <label>Units</label>
        <input type="number" name="units" placeholder="Units" v-model="product.units" required />
      </div>
      <div class="field">
        <label>Category</label>
        <select class="ui fluid dropdown" v-model="categoryId">
          <option value="0">Selct category</option>
          <option
            v-for="category in  categories"
            :key="category.id"
            :value="category.id"
          >{{category.name}}</option>
        </select>
      </div>
      <button class="ui button" @click.prevent="onCreate" type="submit">Create</button>
    </form>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import { State, Action, Getter } from 'vuex-class';

@Component
export default class CreateProduct extends Vue {
  @State categories;

  @Getter role;
  @Getter isLoggedIn;

  @Action fetchProductCategories;
  @Action createProduct;

  product = { name: '', description: '', price: 0, units: 0, in_stock: true };

  categoryId = 0;

  created() {
    if (!this.isLoggedIn) {
      this.$router.replace('/login');
    } else if (this.role !== 'seller') {
      this.$router.replace('/');
    }
    this.fetchProductCategories();
  }

  onCreate() {
    this.createProduct({
      categoryId: this.categoryId,
      product: this.product,
    });
    this.$router.replace('/');
  }
}
</script>