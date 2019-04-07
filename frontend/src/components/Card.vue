<template>
    <div class="card" @click='openEditModal'>
      <p class="cancel" @click.stop='deleteCard'>×</p>
      <div class="card-content">
        {{ card.title }}
      </div>
    </div>
</template>
<script>
export default {
  props: ['card', 'index'],
  methods: {
    deleteCard () {
      this.$emit('deleteCard', this.index, this.card.id)
    },
    openEditModal () {
      this.$emit('openEditModal', {card: this.card}, {index: this.index})
    }
  }
}
// # sourceURL=card.js
</script>
<style lang="scss" scoped>
  .card {
    margin: auto;
    margin-bottom: 5px;
    width: 200px;
    height: auto;
    min-height: 30px;
    background: #71ff71;
    border-radius: 5px;
    box-shadow: 0 2px 5px #111;
    padding: 5px;
    overflow-wrap: break-word;
    position: relative;
    cursor: pointer;
  }
  .card-footer-item {
    padding-top: 0px;
    padding-bottom: 0px;
  }
  .card-footer {
    position: relative;
  }
  .card-content {
    margin: 0;
    overflow-wrap: break-word;
  }
  .cancel {
    position: absolute;
    right: 5px;
    top: 0;
    margin:0;
    font-weight: 100;
    font-size: 15pt;
  }
</style>
