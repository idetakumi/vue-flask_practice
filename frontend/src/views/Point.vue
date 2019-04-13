<template>
  <div class="point">
    <img src="@/assets/majang.jpg" style="width: 350px; height: 250px;">
    <h1>得点-点数換算アプリ</h1>
    <div>
      <label for="1st" class="majang-label" >一着 : </label>
      <input type="number" id="1st" v-model='first'>
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
      <button class="btn btn-primary" @click="computePoint">計算</button>
      <button class="btn btn-primary" style="margin-left: 20px;" @click="clearAll">CLEAR</button>
    </div>
    <br>
    <div v-if="results.length === 4">
      <h2>
        <i>1着 : </i>
        <i style="color: red;"> {{ results[3] }}</i>
      </h2>
      <h2>
        <i>2着 : </i>
        <i style="color: red;"> {{ results[2] }}</i>
      </h2>
      <h2>
        <i>3着 : </i>
        <i style="color: red;"> {{ results[1] }}</i>
      </h2>
      <h2>
        <i>4着 : </i>
        <i style="color: red;"> {{ results[0] }}</i>
      </h2>
    </div>
  </div>
</template>
<script>
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
export default {
  data () {
    return {
      first: 0,
      second: 0,
      third: 0,
      forth: 0,
      message: '',
      results: []
    }
  },
  methods: {
    computePoint () {
      this.message = ""
      this.results = []
      let pts = new Array
      this.computeRank(this.forth, pts, -30)
      this.computeRank(this.third, pts, -10)
      this.computeRank(this.second, pts, 10)
      let top = (pts[0] + pts[1] + pts[2]) * -1
      pts.push(top)

      // if ( pts[0] + pts[1] + pts[2] + top != 0) {
      //   this.message = "得点の入力に誤りがあります。合計が±0になりません！"
      //   return
      // }

      this.results = pts
    },
    computeRank (pt, pts, uma) {
      if (pt < 0) {
        pts.push(-60)
      } else {
        pts.push(Math.round((pt-300) / 10) + uma)
      }
    },
    clearAll () {
      this.first = 0
      this.second = 0
      this.third = 0
      this.forth = 0
      this.results = []
    }
  }
}
// # sourceURL=Point.js
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
