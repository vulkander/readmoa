<template>
  <nav class="navbar navbar-light bg-light">
    <span
      v-if="!user"
      class="navbar-brand mb-0 h1"
    >ReadMoa</span>
    <span
      v-if="user"
      class="navbar-brand mb-0 h1"
    ><img
      class="avatar rounded-circle"

      :src="user.photoURL"
      style="width: 30px;height:30px;"
    >{{ this.$router.currentRoute.name }}</span>
  </nav>
</template>

<script>
import firebase from 'firebase'

export default {
  name: 'TopNav',
  data: function () {
    return {
      user: firebase.auth().currentUser
    }
  }
}
</script>

<style>
@import '//fonts.googleapis.com/css?family=Roboto:400,500,700,400italic|Material+Icons';
</style>
