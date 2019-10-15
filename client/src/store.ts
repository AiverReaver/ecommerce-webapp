import Vue from 'vue';
import Vuex from 'vuex';

import ecom from './api';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    token: localStorage.getItem('token'),
    refreshToken: localStorage.getItem('refresh_token'),
  },
  mutations: {
    setToken(state, token) {
      state.token = token;
    },

    setRefreshToken(state, token) {
      state.refreshToken = token;
    },
  },
  actions: {
    loginUser(context, user) {
      return ecom.post('/token/', user);
    },
    setTokens({ commit }, data) {
      ecom.defaults.headers.Authorization = `Bearer ${data.access_token}`;

      commit('setToken', data.access);
      commit('setRefreshToken', data.refresh);

      localStorage.setItem('token', data.access);
      localStorage.setItem('refresh_token', data.refresh);
    },
  },
});
