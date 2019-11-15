import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import Login from './views/Login.vue';
import Register from './views/Register.vue';
import Checkout from './views/Checkout.vue';
import Order from './views/Order.vue';
import CreateProduct from './views/CreateProduct.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
    {
      path: '/register',
      name: 'register',
      component: Register,
    },
    {
      path: '/checkout',
      name: 'checkout',
      component: Checkout,
    },
    {
      path: '/orders',
      name: 'orders',
      component: Order,
    },
    {
      path: '/create',
      name: 'create product',
      component: CreateProduct,
    },
  ],
});
