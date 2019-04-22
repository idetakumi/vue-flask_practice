<template>
  <div id="app">
    <div style="width: 350px; margin: auto;">
      <button type="button" id="addbtn" class="btn btn-primary" style="margin: auto;" @click="openForm">TODO追加</button>
      <br>
      <br>
      <Form v-if="isOpenForm" @closeForm='onCloseForm' @addCard='onAddCard'></Form>
    </div>
    <div class="panel panel-default">
      <Place :list="list"></Place>
    </div>
  </div>
</template>
<script>
import Form from '@/components/Form'
import Place from '@/components/Place'
import axios from 'axios'

export default {
  name: 'home',
  components: {
    Form,
    Place
  },
  data () {
    return {
      list: [],
      isOpenForm: false
    }
  },
  methods: {
    onAddCard ({ task }) {
      this.list.unshift(task)
      this.onCloseForm()
    },
    openForm () {
      this.isOpenForm = true
    },
    onCloseForm () {
      this.isOpenForm = false
    }
  },
  created: function () {
    const path = '/api/get'
    axios.get(path)
      .then(response => {
        this.list = response.data
      })
      .catch(error => {
        console.log(error)
      })
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
