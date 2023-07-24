<template>
  <div>
    <!-- Post Begins -->
    <section

      class="card mt-4"
    >
      <div
        class="border p-2"
      >
        <!-- post header -->
        <div class="row m-0">
          <!--
          <div class="">
            <a
              class="text-decoration-none"
              href="#"
            >
              <img
                class=" rounded-circle"
                :src="post.user.photoURL"
                width="50"
                height="50"
                alt="..."
              >
            </a>
          </div>

          <div class="flex-grow-1 pl-2">
            <h2 class="text-capitalize h6 mb-0">
              @{{ post.user.displayName }}
            </h2>

            <p class="small text-secondary m-0 mt-1">
              <time-ago :datetime="post.create_time" />
            </p>
          </div>
          -->

          <!--
              <div class="dropdown">
                  <a class="" href="#" role="button" id="dropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                      <i class="fas fa-chevron-down"></i>
                  </a>

                  <div class="dropdown-menu" aria-labelledby="dropdownMenuLink">
                      <a class="dropdown-item text-primary" href="#">Edit</a>
                      <a class="dropdown-item text-primary" href="#">Delete</a>
                  </div>
              </div>
              -->
        </div>
        <!-- post body -->

        <div class="">
          <a
            :href="post.url"
            target="_blank"
          >
            <b-card

              :title="post.title"
              :img-src="post.image"
              img-bottom
              tag="article"
              style="max-width: 20rem;"
              class="mb-2"
            >
              <b-card-text>
                <p class="text-secondary">
                  {{ post.domain }}
                </p>
                {{ post.description }}
              </b-card-text>
            </b-card>
          </a>
        </div>

        <hr class="my-1">
        <!-- post footer begins -->
        <footer
          class=""
        >
          <!-- post actions -->
          <div class="">
            <ul class="list-group list-group-horizontal">
              <li class="list-group-item flex-fill text-center p-0 px-lg-2 border border-0">
                <a
                  class="small text-decoration-none"
                  href="#"
                >

                  <font-awesome-icon icon="thumbs-up" />
                  0 Like
                </a>
              </li>
              <li class="list-group-item flex-fill text-center p-0 px-lg-2 border border-right-0 border-top-0 border-bottom-0">
                <a
                  v-b-toggle.collapseExample
                  class="small text-decoration-none"
                  data-toggle="collapse"
                  :href="'#collapseComment' + post.id"
                  role="button"
                >

                  <font-awesome-icon icon="comment" />

                  {{ post.comments.length }} Comment
                </a>
              </li>
              <li class="list-group-item flex-fill text-center p-0 px-lg-2 border border-right-0 border-top-0 border-bottom-0">
                <a
                  class="small text-decoration-none"
                  href="#"
                >
                  <font-awesome-icon icon="share-alt" />
                  0 Share
                </a>
              </li>
            </ul>
          </div>

          <PostCardComment :post="post" />
        </footer>
        <!-- post footer ends -->
      </div>
    </section>
    <!-- Post Ends -->
  </div>
</template>

<script>

import PostCardComment from '@/components/PostCardComment.vue'

export default {
  components: {
    PostCardComment
  },
  props: ['post'],
  data: function () {
    return {
      new_comment: '',
      comments: this.post.comments
    }
  },
  methods: {

  }
}
</script>
