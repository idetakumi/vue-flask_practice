<template>  
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container" style="padding: 5px;">
          <div>
            {{ message }}
          </div>
          <div class="modal-body" style="padding: 0px;">

            <h5 class="header"> TITLE </h5>
            <input type="text" v-model='card.title' maxlength="20">
            <br>
            <br>
            <h5 class="header"> MEMO </h5>
            <textarea class="input-card" cols="40" rows="2" v-model='card.text' 
              maxlength="100" placeholder="空白可"></textarea>
            <br>
            <br>
            <h5 class="header">PRIORITY</h5>
            <select class="selectpicker" v-model='card.priority'>
              <option value="normal">ふつう</option>
              <option value="urgent">いそぎ</option>
              <option value="relax">のんびり</option>
            </select>
            <br>
            <br>
            <!-- <h5 class="header">DUE</h5>
            <Datepicker v-model='card.date' name='date' style="margin: auto;" format="yyyy/MM/dd"></Datepicker>
            <br> -->

            <button class="btn btn-primary" style="margin: 5px;" v-on:click='saveText'>保存</button>
            <button class="btn btn-primary" style="margin: 5px;" v-on:click='clearText'>クリア</button>
          </div>
          <div class="modal-footer">
            <button class="btn btn-secondary" style="margin: 5px;" v-on:click='closeForm'>CANCEL</button>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import axios from 'axios'
// import Datepicker from 'vuejs-datepicker'
export default {
  // name: 'Form',
  // components: {
  //   Datepicker
  // },
  data () {
    return {
      card: {
        title: '',
        text: '',
        priority: 'normal',
        // date: ''
      },
      message: '',
    }
  },
  methods: {
    clearText () {
      this.card.title = ''
      this.card.text = ''
      this.card.priority = 'normal'
      // this.card.date = ''
      this.message = ''
    },
    saveText () {
      if (!this.card.title) {
        this.message = 'タイトルが空欄です！'
        return
      }
      const path = '/api/add'
      let params = new URLSearchParams()
      var titleValue = this.card.title
      var textValue = this.card.text
      var priority = this.card.priority
      // var date = this.card.date
      params.append('title', titleValue)
      params.append('text', textValue)
      params.append('priority', priority)
      // params.append('date', date)
      let task
      axios.post(path, params)
        .then(response => {
          let id = response.data
          task = {'id': id, 'text': textValue, 'title': titleValue, 'priority': priority}
          this.clearText()
          this.addCard(task)
        }).catch(error => {
          console.log(error)
        })
    },
    closeForm () {
      this.$emit('closeForm')
    },
    addCard (task) {
      this.$emit('addCard', {task: task})
    }
  }
}
// # sourceURL=form.js
</script>
<style>
  .input-card {
    width:200px;
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

.vdp-datepicker {
  width: 100% !important;
  text-align: center !important;
}
</style>
