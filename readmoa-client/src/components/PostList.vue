<template>
  <div class="container-fluid my-1">
    <div class="row">
      <div
        class="col-12"
      >
        <div
          v-for="post in posts"
          :key="post.comment"
        >
          <PostCard :post="post" />
        </div>
        <infinite-loading @infinite="getPosts" />
      </div>
    </div>
  </div>
</template>

<script>
import firebase from 'firebase'
import axios from 'axios'
import PostCard from '@/components/PostCard.vue'
import InfiniteLoading from 'vue-infinite-loading'
export default {
  components: {
    PostCard, InfiniteLoading
  },
  data: function () {
    return {
      user: firebase.auth().currentUser,
      posts: [],
      last_id: ''

    }
  },
  computed: {

  },
  mounted () {

  },
  methods: {

    getPosts ($state) {
      const path = this.$hostname + '/list'

      console.log('last id:' + this.last_id)
      axios.get(path, {
        params: {
          last_id: this.last_id
        }
      })
        .then((res) => {
          if (res.data.length) {
            this.posts.push(...res.data)
            this.last_id = this.posts[this.posts.length - 1].id
            $state.loaded()
          } else {
            $state.complete()
          }
        })
    }
  }
}
</script>
