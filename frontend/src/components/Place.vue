<template>
<div class="card">
  <div class="card-default">
  <EditModal v-if='modalProp.isopen' :prop="modalProp" @updateCard="onUpdateCard"></EditModal>
  <div>
    <ul>
      <li v-for='(card, index) in list' v-bind:key='index' class='card-list'>
        <Card :card="card" :index="index" @deleteCard='onDeleteCard' @openEditModal='onOpenEditModal'></Card>
      </li>
    </ul>
  </div>
  </div>
</div>
</template>
<script>
import Card from '@/components/Card'
import EditModal from '@/components/Modal_edit'
import axios from 'axios'

export default {
  props: ['list'],
  data () {
    return {
      modalProp: {
        id: '',
        title: '',
        text: '',
        index: '',
        isopen: false
      }
    }
  },
  methods: {
    onDeleteCard (index,id) {
      const path = '/api/delete'
      let params = new URLSearchParams()
      params.append('id', id)
      this.list.splice(index, 1)
      axios.post(path, params)
        .then(response => {
          console.log(response)
        })
        .catch(error => {
          console.log(error)
        })
    },
    onOpenEditModal ({ card }, { index }) {
      this.modalProp.id = card.id
      this.modalProp.title = card.title
      this.modalProp.text = card.text
      this.modalProp.index = index
      this.modalProp.isopen = true
    },
    onUpdateCard ({ updatedCard }) {
      const path = '/api/update'
      let params = new URLSearchParams()
      params.append('id', updatedCard.id)
      params.append('title', updatedCard.title)
      params.append('text', updatedCard.text)
      axios.post(path, params)
        .then(response => {
          console.log(response)
        })
        .catch(error => {
          console.log(error)
        })
      this.list[updatedCard.index].title = updatedCard.title
      this.list[updatedCard.index].text = updatedCard.text
    }
  },
  components: {
    Card,
    EditModal
  }
}
// # sourceURL=place.js
</script>
<style>
  .content {
    text-align: center;
  }
  .card-list {
    position: relative;
    margin: auto;
    list-style-type: none;
  }
  ul {
    list-style: none;
    padding-inline-start: 0px;
  }
</style>
