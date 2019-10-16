<template>
  <div class="ui middle aligned centered aligned grid">
    <div class="column">
      <h2 class="ui image header">
        <div class="content">Register for new account</div>
      </h2>
      <form class="ui large form" @submit.prevent="onRegisterClicked">
        <div class="ui stacked segment">
          <div class="field">
            <div class="ui left icon input">
              <i class="user icon"></i>
              <input type="text" placeholder="Username" v-model="user.name" />
            </div>
          </div>
          <div class="field">
            <div class="ui left icon input">
              <i class="user icon"></i>
              <input type="text" placeholder="email" v-model="user.email" />
            </div>
          </div>
          <div class="field">
            <div class="ui left icon input">
              <i class="lock icon"></i>
              <input type="password" placeholder="Password" v-model="user.password" />
            </div>
          </div>
          <div class="field">
            <div class="ui left icon input">
              <i class="lock icon"></i>
              <input type="password" placeholder="Confirm password" v-model="user.confirmPassword" />
            </div>
          </div>
          <input type="submit" value="Register" class="ui fluid large teal submit button" />
        </div>
      </form>

      <div class="ui message">
        already have an account?
        <router-link to="/login">login</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { Vue, Component } from 'vue-property-decorator';
import { mapActions } from 'vuex';

@Component({
  methods: {
    ...mapActions(['registerUser']),
  },
})
export default class Register extends Vue {
  user = {};

  onRegisterClicked() {
    this.registerUser(this.user)
      .then((_) => {
        this.$router.push('/login');
      })
      .catch((error) => {
        // TODO: Handle error
      });
  }
}
</script>