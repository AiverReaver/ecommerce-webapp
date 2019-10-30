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
              <input type="text" placeholder="username" v-model="userdata.user.name" />
            </div>
          </div>
          <div class="field">
            <div class="ui left icon input">
              <i class="user icon"></i>
              <input type="text" placeholder="email" v-model="userdata.user.email" />
            </div>
          </div>
          <div class="field">
            <div class="ui left icon input">
              <i class="lock icon"></i>
              <input type="password" placeholder="Password" v-model="userdata.user.password" />
            </div>
          </div>
          <div class="field">
            <div class="ui left icon input">
              <i class="lock icon"></i>
              <input
                type="password"
                placeholder="Confirm password"
                v-model="userdata.user.confirmPassword"
              />
            </div>
          </div>
          <div v-if="isSeller" class="field">
            <div class="ui left icon input">
              <input type="text" placeholder="Company Name" v-model="userdata.company_name" />
            </div>
          </div>
          <div v-if="!isSeller" class="field">
            <div class="ui left icon input">
              <input type="text" placeholder="address" v-model="userdata.address" />
            </div>
          </div>
          <div v-if="!isSeller" class="field">
            <div class="ui left icon input">
              <input type="text" placeholder="city" v-model="userdata.city" />
            </div>
          </div>
          <div v-if="!isSeller" class="field">
            <div class="ui left icon input">
              <input type="text" placeholder="country" v-model="userdata.country" />
            </div>
          </div>
          <input type="submit" value="Register" class="ui fluid large teal submit button" />
          <div class="ui horizontal divider">OR</div>
          <a
            class="ui fluid primary basic button"
            v-if="isSeller"
            @click.prevent="isSeller = false"
          >Register as User</a>
          <a
            class="ui fluid primary basic button"
            v-else
            @click.prevent="isSeller = true"
          >Register as Seller</a>
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
    ...mapActions(['registerUser', 'registerSeller']),
  },
})
export default class Register extends Vue {
  userdata = { user: {} };
  isSeller = false;

  onRegisterClicked() {
    if (this.isSeller) {
      this.registerSeller(this.userdata)
        .then((_) => {
          this.$router.push('/login');
        })
        .catch((error) => {
          // TODO: Handle error
        });
    } else {
      this.registerUser(this.userdata)
        .then((_) => {
          this.$router.push('/login');
        })
        .catch((error) => {
          // TODO: Handle error
        });
    }
  }
}
</script>