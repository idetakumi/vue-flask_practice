<template>
  <div class="card">
    <div class="card-body">
    <div>
      {{ message }}
    </div>
    <div>
      <h4 class="header"> TITLE </h4>
      <input type="text" v-model='card.title' maxlength="20">
    </div>
    <br>
    <div>
      <h4 class="header"> TASK </h4>
      <textarea class="input-card" cols="40" rows="2" v-model='card.text' maxlength="100"></textarea>
    </div>
    <div>
      <button class="btn btn-primary" style="margin: 5px;" v-on:click='saveText'>保存</button>
      <button class="btn btn-primary" style="margin: 5px;" v-on:click='clearText'>クリア</button>
    </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      card: {
        title: '',
        text: ''
      },
      lists: [],
      message: ''
    }
  },
  methods: {
    clearText () {
      this.card.title = ''
      this.card.text = ''
      this.message = ''
    },
    saveText () {
      if (!this.card.title || !this.card.text) {
        this.message = 'タイトルもしくは内容が空欄です！'
        return
      }
      const path = 'http://localhost:5000/api/add'
      let params = new URLSearchParams()
      params.append('title', this.card.title)
      params.append('text', this.card.text)
      let task
      var titleValue = this.card.title
      var textValue = this.card.text
      axios.post(path, params)
        .then(response => {
          let id = response.data
          task = {'id': id, 'text': textValue, 'title': titleValue}
          this.clearText()
          this.$emit('addCard', { task: task })
        }).catch(error => {
          console.log(error)
        })
    }
  }
}
// # sourceURL=form.js
</script>
<style>
  .input-card {
    width:160px;
    height:50px;
  }

  .header {
    color: #42b983;
  }

  .form-button {
  display: inline-block;
  max-width: 180px;
  text-align: left;
  background-color: #9ec34b;
  font-size: 15px;
  color: #FFF;
  text-decoration: none;
  font-weight: bold;
  padding: 8px 16px 8px 16px;
  border-radius: 4px;
  position: relative;
  height: 40px;
}

.btn-icon:before {
  font-family: "FontAwesome";
  content: "\f105";/* 好きなフォントアイコンを　*/
  position: absolute;
  left: 16px;
  top: 50%;
  margin-top: -8px;
}

.btn-icon:hover {
  opacity: 0.8;
}
</style>
