<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">

          <div class="modal-header h3">
            <h5>
              テキストを確認・編集<br>できます！
            </h5>
          </div>
          <div>
            <h5 style='color: red;'>
              {{ message }}
            </h5>
          </div>

          <div class="modal-body">
            <h5 class="header" style="margin:10px"> TITLE </h5>
            <input type="text" v-model="prop.title">
            <h5 class="header" style="margin:10px"> MEMO </h5>
            <textarea class="input-card" type="text" maxlength="100" 
              placeholder="空白可" cols="40" row="2" v-model="prop.text"></textarea>
            <h5 class="header">PRIORITY</h5>
            <select class="selectpicker" v-model='prop.priority'>
              <option value="normal">ふつう</option>
              <option value="urgent">いそぎ</option>
              0<option value="relax">のんびり</option>
            </select>
            <!-- <h5 class="header">DUE</h5>
            <Datepicker v-model='prop.date' name='date' style="margin: auto;" format="yyyy/MM/dd"></Datepicker>
            <br> -->
          </div>

          <div class="modal-footer">
            <button class="btn btn-secondary" style="margin: 5px;" @click.stop="prop.isopen = false">
              CANCEL
            </button>
            <button class="btn btn-primary" style="margin: 5px;" @click.stop="updateCard">
              OK
            </button>
          </div>

        </div>
      </div>
    </div>
  </transition>
</template>
<script>
export default {
  props: ['prop'],
  data () {
    return {
      message: '',
      // modal: {
      //   modalTitle: this.prop.title,
      //   modalText: this.prop.text
      // }
    }
  },
  methods: {
    updateCard () {
      if (!this.prop.title) {
        this.message = 'タイトルに空白は登録できません。'
        return
      }
      this.$emit('updateCard', {updatedCard: {id: this.prop.id, title: this.prop.title, text: this.prop.text, priority: this.prop.priority, index: this.prop.index}})
      this.prop.isopen = false
    }
  }
}
// # sourceURL=modal_edit.js
</script>
<style>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, .5);
  display: table;
  transition: opacity .3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 300px;
  margin: 0px auto;
  padding: 30px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, .33);
  transition: all .3s ease;
  font-family: Helvetica, Arial, sans-serif;
  box-sizing: border-box
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>
