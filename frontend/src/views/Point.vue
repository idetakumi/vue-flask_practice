<template>
  <div class="point">
    <img src="@/assets/majang.jpg" style="width: 350px; height: 250px;">
    <h1>得点-点数換算アプリ</h1>
    <div>
      <label for="1st" class="majang-label" >一着 : </label>
      <input type="number" id="1st" v-model='first' @onchange="checkDigit(first)">
      00
    </div>
    <br>
    <div>
      <label for="2nd" class="majang-label">二着 : </label>
      <input type="number" id="2nd" v-model='second'>
      00
    </div>
    <br>
    <div>
      <label for="3nd" class="majang-label">三着 : </label>
      <input type="number" id="3nd" v-model='third'>
      00
    </div>
    <br>
    <div>
      <label for="4th" class="majang-label">四着 : </label>
      <input type="number" id="4th" v-model="forth">
      00
    </div>
    <br>
    <div>
      <h2>{{ message }}</h2>
    </div>
    <div>
      <button class="majang_button">計算</button>
      <button class="majang_button" style="margin-left: 20px;">CLEAR</button>
    </div>
  <div>
  </div>
  </div>  
</template>
<script>
export default {
  data () {
    return {
      first: 0,
      second: 0,
      third: 0,
      forth: 0,
      message: ''
    }
  },
  methods: {
    checkDigit (newVal) {
      this.first = newVal
    }
  }
}
</script>
<style>
  .majang_button {
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
  .majang-label {
    font-weight: bold;
  }
  .btn-icon:before {
    font-family: "FontAwesome";
    content: "\f105";
    position: absolute;
    left: 16px;
    top: 50%;
    margin-top: -8px;
  }
  .btn-icon:hover {
    opacity: 0.8;
  }
</style>
