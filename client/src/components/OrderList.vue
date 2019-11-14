<template>
  <div class="ui cards">
    <div class="card" v-for="order in orders" :key="order.order_number">
      <div class="content">
        <div class="header">
          Order no.
          <small>{{order.order_number}}</small>
        </div>
        <div class="meta">₹ {{order.cart.total_price}}</div>
        <div class="description">Ordered {{order.cart.cartitems.length}} items</div>
      </div>
      <div class="content">
        <h4 class="ui sub header">Items Ordered</h4>
        <div class="ui small feed">
          <div class="event" v-for="item in order.cart.cartitems" :key="item.id">
            <div class="content">
              <div class="summary">
                {{item.product.name}}
                <small>price</small>
                ₹ {{item.product.price}}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
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
export default class OrderList extends Vue {
  @Prop() orders;
}
</script>