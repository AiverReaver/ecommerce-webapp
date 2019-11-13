<template>
  <div>
    <CategoryMenu :categories="categories" />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { State, Action } from 'vuex-class';
import CategoryMenu from '../components/CategoryMenu.vue';

@Component({
  components: {
    CategoryMenu,
  },
})
export default class Home extends Vue {
  @State categories;
  @Action fetchProductCategories;

  created() {
    this.fetchProductCategories();
  }
}
</script>
