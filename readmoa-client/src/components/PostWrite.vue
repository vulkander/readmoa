<template>
  <div class="container-fluid my-1">
    <div class="row">
      <div class="col-12">
        <!--- Post Form Begins -->
        <BlockUI
          v-if="blockShow"
          :message="msg"
          :html="html"
        />
        <section class="card">
          <div class="card-header">
            <ul
              id="myTab"
              class="nav nav-tabs card-header-tabs"
              role="tablist"
            >
              <li class="nav-item">
                <a
                  id="posts-tab"
                  class="nav-link active"
                  data-toggle="tab"
                  href="#posts"
                  role="tab"
                  aria-controls="posts"
                  aria-selected="true"
                >글쓰기</a>
              </li>
            </ul>
          </div>

          <div class="card-body">
            <div
              id="myTabContent"
              class="tab-content"
            >
              <div
                id="posts"
                class="tab-pane fade show active"
                role="tabpanel"
                aria-labelledby="posts-tab"
              >
                <div class="form-group">
                  <label
                    class="sr-only"
                    for="message"
                  >post</label>
                  <input
                    v-model="url"
                    class="form-control"
                    placeholder="URL을 입력하세요."
                    @keyup="onUrlChange($event)"
                  >

                  <div>
                    <b-card
                      :title="title"
                      :img-src="image"
                      img-bottom
                      tag="article"
                      style="max-width: 20rem;"
                      class="mb-2"
                    >
                      <b-card-text>
                        <p class="text-secondary">
                          {{ domain }}
                        </p>
                        {{ description }}
                      </b-card-text>
                    </b-card>
                  </div>

                  <textarea
                    id="comment"
                    v-model="comment"
                    class="form-control"
                    rows="3"
                    placeholder="어떻게 생각하세요?"
                  />
                </div>
              </div>
            </div>

            <div class="text-right">
              <button
                type="submit"
                class="btn btn-primary"
                @click="writeGul"
              >
                등록
              </button>
            </div>
          </div>
        </section>
        <!--- Post Form Ends -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import firebase from 'firebase'

export default {
  name: 'PostWrite',

  data () {
    return {
      url: '',
      comment: '',
      title: '',
      domain: '',
      link: '',
      description: '',
      image: '',

      blockShow: false,
      msg: 'Loading site info..',
      html: '<i class="fa fa-cog fa-spin fa-3x fa-fw"></i>' // this line demostrate how to use fontawesome animation icon
    }
  },
  mounted () {
    console.log('mounted')
    const user = firebase.auth().currentUser
    if (!user) {
      // alert('로그인한 사용자만 글쓰기가 가능합니다.')
      this.$router.push('/login')
    }
  },
  methods: {
    writeGul (event) {
      if (this.url === '') {
        alert('정확한 URL을 입력하세요')
        return
      }

      if (this.comment === '') {
        alert('코멘트를 입력하세요')
        return
      }
      const router = this.$router
      const path = this.$hostname + '/write'
      const param = {
        url: this.url, // varEmail is a variable which holds the email
        comment: this.comment,
        title: this.title,
        domain: this.domain,
        link: this.link,
        description: this.description,
        image: this.image,
        user: firebase.auth().currentUser
      }

      firebase.auth().currentUser.getIdToken().then(function (token) {
        axios.post(path, param,
          {
            headers: {
              Authorization: 'Bearer ' + token
            }
          }).then((res) => {
          console.log(res.data)
          if (res.data.success) {
            router.push('/')
          } else {
            alert(res.data.message)
          }
        })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          })
      })
    },
    // url 입력시 이벤트
    onUrlChange (event) {
      if (this.isValidUrl(event.target.value)) {
        this.domain = this.getDomain(event.target.value)
        // parse url
        console.log(this.url)
        const path = this.$hostname + '/parse_url?url=' + encodeURIComponent(this.url)
        this.blockShow = true
        axios.get(path)
          .then((res) => {
            console.log(res.data)
            this.title = (res.data.og.title == null ? res.data.page.title : res.data.og.title)
            this.domain = (res.data.og.url == null ? res.data._internal.url : res.data.og.url)
            this.link = (res.data.page.canonical == null ? res.data._internal.url : res.data.page.canonical)
            this.description = (res.data.og.description == null ? res.data.meta.description : res.data.og.description)
            this.image = (res.data.og.image == null ? res.data.meta.image : res.data.og.image)
            this.blockShow = false
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
            this.blockShow = false
          })
      } else {
        // 정확한 URL을 입력하세요.
      }
    },
    // URL이 정확한지 체크
    isValidUrl (url) {
      var pattern = new RegExp('^(https?:\\/\\/)?' + // protocol
    '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|' + // domain name
    '((\\d{1,3}\\.){3}\\d{1,3}))' + // OR ip (v4) address
    '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*' + // port and path
    '(\\?[;&a-z\\d%_.~+=-]*)?' + // query string
    '(\\#[-a-z\\d_]*)?$', 'i') // fragment locator
      return !!pattern.test(url)
    },
    // url에서 도메인 얻기s
    getDomain (url, subdomain) {
      subdomain = subdomain || false

      url = url.replace(/(https?:\/\/)?(www.)?/i, '')

      if (!subdomain) {
        url = url.split('.')

        url = url.slice(url.length - 2).join('.')
      }

      if (url.indexOf('/') !== -1) {
        return url.split('/')[0]
      }

      return url
    }

  }
}
</script>
