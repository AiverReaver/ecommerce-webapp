import Vue from 'vue';
import Vuex from 'vuex';

import ecom from './api';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    categories: [],
    selectedCategory: { id: '' },
    cart: { cartitems: [] },
    token: localStorage.getItem('token'),
    refreshToken: localStorage.getItem('refresh_token'),
  },
  mutations: {
    setCategories(state, categories) {
      state.categories = categories;
    },

    setSelectedCategory(state, category) {
      state.selectedCategory = category;
    },
    setCart(state, cart) {
      state.cart = cart;
    },

    setToken(state, token) {
      state.token = token;
    },

    setRefreshToken(state, token) {
      state.refreshToken = token;
    },
  },
  actions: {
    async fetchProductCategories({ commit }) {
      const { data } = await ecom.get('/categories/');
      commit('setCategories', data);
      commit('setSelectedCategory', data[0]);
    },
    async getProducts({ state }) {
      const { data } = await ecom.get(
        `/categories/${state.selectedCategory.id}/products/`,
      );
      return data;
    },

    async addToCart({ commit }, cart) {
      const { data } = await ecom.post(`/cart/`, cart);

      commit('setCart', data);
    },

    async getCart({ commit }) {
      const { data } = await ecom.get('/cart/');
      commit('setCart', data);
    },

    deleteCart(context, id) {
      return ecom.delete(`/cart/${id}/`);
    },
    loginUser(context, user) {
      return ecom.post('/token/', user);
    },
    registerUser(context, user) {
      return ecom.post('/register/customer/', user);
    },
    registerSeller(context, user) {
      return ecom.post('/register/seller/', user);
    },
    setTokens({ commit }, data) {
      ecom.defaults.headers.Authorization = `Bearer ${data.access_token}`;

      commit('setToken', data.access);
      commit('setRefreshToken', data.refresh);

      localStorage.setItem('token', data.access);
      localStorage.setItem('refresh_token', data.refresh);
    },
    logoutUser({ commit, state }) {
      commit('setToken', null);
      commit('setRefreshToken', null);
      localStorage.removeItem('token');
      localStorage.removeItem('refresh_token');
    },
  },
  getters: {
    isLoggedIn(state) {
      return state.token !== null;
    },
    CartItemsCount(state) {
      return state.cart.cartitems.length;
    },
  },
});
