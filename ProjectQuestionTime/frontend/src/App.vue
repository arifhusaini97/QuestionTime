<template>
  <div id="nav">
    <app-nav-bar></app-nav-bar>
  </div>
  <router-view />
</template>
<script>
import AppNavBar from './components/NavBar.vue';
// INFO: @ symbol start from src file
import apiService from '@/common/api.service';

export default {
  name: 'App',
  components: {
    AppNavBar,
  },
  methods: {
    async setUserInfo() {
      const data = await apiService('/api/user/');
      const requestUser = data.username;
      window.localStorage.setItem('username', requestUser);
    },
  },
  created() {
    this.setUserInfo();
  },
};
</script>

<style>
/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
} */

html,
body {
  height: 100%;
  font-family: 'Playfair Display', serif;
}

.btn:focus {
  box-shadow: none !important;
}
</style>
