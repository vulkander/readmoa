<template>
  <!-- collapsed comments begins -->
  <b-collapse
    :id="'collapseComment' + post.id"
    class="collapse"
  >
    <div
      class="card border border-right-0 border-left-0 border-bottom-0 mt-1"
    >
      <!-- new comment form -->
      <section class="mt-3">
        <form action="">
          <div class="input-group input-group">
            <input
              v-model="new_comment"
              type="text"
              class="form-control"
              placeholder="댓글쓰기"
            >
            <div class="input-group-append">
              <a
                class="text-decoration-none text-white btn btn-primary"
                role="button"
                @click="writeComment"
              >댓글쓰기</a>
            </div>
          </div>
        </form>
      </section>
      <!-- comment card bgins -->
      <section
        v-for="comment in post.comments.slice().reverse()"
        :key="comment.create_time"
      >
        <div
          class="card p-2 mt-3"
        >
          <!-- comment header -->
          <div class="d-flex">
            <div class="">
              <a
                class="text-decoration-none"
                href="#"
              >
                <img
                  class=" rounded-circle"
                  :src="comment.user.photoURL"
                  width="40"
                  height="40"
                >
              </a>
            </div>
            <div class="flex-grow-1 pl-2">
              <a
                class="text-decoration-none text-capitalize h6 m-0"
                href="#"
              >@{{ comment.user.displayName }}</a>
              <p class="small m-0 text-muted">
                <time-ago :datetime="comment.create_time" />
              </p>
            </div>
            <!--
                                                        <div>
                                                            <div class="dropdown">
                                                                <a class="" href="#" role="button" id="dropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                                                    <i class="fas fa-chevron-down"></i>
                                                                </a>

                                                                <div class="dropdown-menu" aria-labelledby="dropdownMenuLink">
                                                                    <a class="dropdown-item text-primary" href="#">Edit</a>
                                                                    <a class="dropdown-item text-primary" href="#">Delete</a>
                                                                </div>
                                                            </div>
                                                        </div>
                                                        -->
          </div>
          <!-- comment header -->
          <!-- comment body -->
          <div class="card-body p-0">
            <p class="card-text h7 mb-1">
              {{ comment.comment }}
            </p>
          </div>
        </div>
      </section>
      <!-- comment card ends -->
    </div>
  </b-collapse>
  <!-- collapsed comments ends -->
</template>

<script>
import TimeAgo from 'vue2-timeago'
import axios from 'axios'
import firebase from 'firebase'
export default {
  components: {
    TimeAgo
  },
  props: ['post'],
  data: function () {
    return {
      new_comment: ''
    }
  },
  methods: {
    writeComment (event) {
      if (this.new_comment === '') {
        alert('댓글을 입력하십시오.')
        return
      }
      const user = firebase.auth().currentUser
      if (!user) {
        alert('로그인한 사용자만 댓글쓰기가  가능합니다.')
        this.$router.push('/Login')
        return
      }

      const path = this.$hostname + '/writeComment'
      const param = {
        id: this.post.id,
        comment: this.new_comment,
        user: firebase.auth().currentUser
      }

      const currentPost = this.post
      firebase.auth().currentUser.getIdToken().then(function (token) {
        axios.post(path, param,
          {
            headers: {
              Authorization: 'Bearera ' + token
            }
          }).then((res) => {
          console.log(res.data)
          if (res.data.success) {
            console.log(currentPost)
            currentPost.comments.push(res.data.result)
          }
        })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          })
      })
    }
  }
}
</script>
