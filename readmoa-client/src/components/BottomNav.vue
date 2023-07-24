<template>
  <!-- Bottom Nav Bar -->
  <footer class="footer">
    <div
      id="buttonGroup"
      class="btn-group selectors"
      role="group"
      aria-label="Basic example"
    >
      <button
        id="home"
        type="button"
        :class="{'btn':true,'btn-secondary':true, 'button-inactive':(this.$route.path!='/'), 'button-active':(this.$route.path=='/')}"
        @click="$router.push('/')"
      >
        <div class="selector-holder">
          <i class="material-icons">home</i>
          <span>Home</span>
        </div>
      </button>

      <button
        id="write"
        type="button"
        :class="{'btn':true,'btn-secondary':true, 'button-inactive':(this.$route.path!='/Write'), 'button-active':(this.$route.path=='/Write')}"
        @click="$router.push('write')"
      >
        <div class="selector-holder">
          <i class="material-icons">create</i>
          <span>글쓰기</span>
        </div>
      </button>

      <button
        v-if="!user"
        id="login"
        type="button"
        :class="{'btn':true,'btn-secondary':true, 'button-inactive':(this.$route.path!='/Login'), 'button-active':(this.$route.path=='/Login')}"
        @click="$router.push('login')"
      >
        <div class="selector-holder">
          <i class="material-icons">login</i>
          <span>로그인</span>
        </div>
      </button>

      <button
        v-if="user"
        id="setting"
        type="button"
        :class="{'btn':true,'btn-secondary':true, 'button-inactive':(this.$route.path!='/Setting'), 'button-active':(this.$route.path=='/Setting')}"
        @click="$router.push('setting')"
      >
        <div class="selector-holder">
          <i class="material-icons">settings</i>
          <span>설정</span>
        </div>
      </button>
    </div>
  </footer>
</template>

<script>
import firebase from 'firebase'

export default {
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
