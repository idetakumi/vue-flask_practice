<template>
  <div id="app">
    <Form @addCard="onAddCard"></Form>
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
      list: []
    }
  },
  methods: {
    onAddCard ({ task }) {
      this.list.unshift(task)
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
