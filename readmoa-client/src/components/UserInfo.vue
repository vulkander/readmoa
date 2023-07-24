<template>
  <div class="container-fluid my-1">
    <div class="row">
      <div class="col-12 ">
        <div class="card">
          <div class="card-body text-center">
            <img
              class="avatar rounded-circle"

              :src="user.photoURL"
              style="width: 100px;height:100px;"
            >
            <h4 class="card-title">
              {{ user.displayName }}
            </h4>
            <h6 class="card-subtitle mb-2 text-muted">
              {{ user.email }}
            </h6>
            <h6 class="card-subtitle mb-2 text-muted">
              APIKEY : {{ apiKey }}
            </h6>

            <p class="card-text">
              <ul>
                <li>lastLoginAt : {{ user.metadata.lastSignInTime }}</li>
                <!--
                <li>전체 글 등록 : 30 건</li>
                <li>전체 글 등록 : 30 건</li>
                -->
              </ul>
              <button
                type="button"
                class="btn btn-secondary"
                @click="logout"
              >
                로그아웃
              </button>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import firebase from 'firebase'

export default {
  data: function () {
    return {
      user: firebase.auth().currentUser,
      apiKey: ''

    }
  },
  mounted () {
    this.apiKey = firebase.auth().currentUser.uid
  },
  methods: {
    logout () {
      const router = this.$router
      firebase.auth().signOut().then(function () {
        // Sign-out successful.
        // alert('Logout')
        router.push('/Login')
      }).catch(function (error) {
        // An error happened.
        alert(error)
      })
    }
  }
}
</script>
