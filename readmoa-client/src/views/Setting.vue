<template>
  <div>
    <TopNav />
    <UserInfo />
    <BottomNav />
  </div>
</template>

<script>
import firebase from 'firebase'
import UserInfo from '@/components/UserInfo.vue'

export default {
  name: 'Setting',
  components: {
    UserInfo
  },
  data: function () {
    return {
      user: firebase.auth().currentUser
    }
  },
  mounted () {
    console.log(firebase.auth().currentUser)
  }
}
</script>
