<template>
  <div class="about">
    <img src="@/assets/majang.jpg" style="width: 350px; height: 250px;">
    <h1>オーラス点数計算アプリ</h1>
    <div>
      <label for="mine">自分の点数 : </label>
      <input type="number" id="mine" v-model="mine">
      <i>00点</i>

      <input type="checkbox" id="parent" v-model="isParent" class="checkbox">
      <label for="parent">親</label>
    </div>
    <br>
    <div>
      <label for="other">他家の点数 : </label>
      <input type="number" id="other" v-model="other">
      <i>00点</i>

      <input type="checkbox" id="parent-other" v-model="isParent_other" class="checkbox">
      <label for="parent">親</label>
    </div>
    <br>
    <div>
      <label for="kyoutaku">供託 : </label>
      <input type="number" min="0" id="kyoutaku" v-model="kyotaku" readonly="readonly">
      <i>本</i>
      <button class="btn btn-primary" style="margin: 5px;" @click="incrementKyotaku">+</button>
      <button class="btn btn-primary" style="margin: 5px;" @click="decrementKyotaku">-</button>
    </div>
    <br>
    <div>
      <label for="honba"></label>
      <input type="number" min="0" id="honba" v-model="honba" readonly="readonly">
      <i>本場</i>
      <button class="btn btn-primary" style="margin: 5px;" @click="incrementHonba">+</button>
      <button class="btn btn-primary" style="margin: 5px;" @click="decrementHonba">-</button>
    </div>
    <br>
    <div>
      <button class="btn btn-primary" @click='computeResult'>計算</button>
      <button class="btn btn-primary" @click="clearAll" style="margin-left: 20px;">CLEAR</button>
    </div>
    <div id="result">
      <h2>
        {{ message }}
      </h2>
      <h2 v-if="ronResult">
        <i>直撃 : 逆転には</i>
        <i style="color: red;">{{ ronResult }}</i>
        <i>が必要です</i>
      </h2>
      <h2 v-if="ronResult">
        <i>ツモ : 逆転には</i>
        <i style="color: red;">{{ tsumoResult }}</i>
        <i>が必要です</i>
      </h2>
    </div>
  </div>
</template>
<script>
import ron_child from '@/assets/ron_child.json'
import ron_parent from '@/assets/ron_parent.json'
import tsumo_child_child from '@/assets/tsumo_child_child.json'
import tsumo_child_parent from '@/assets/tsumo_child_parent.json'
import tsumo_parent_child from '@/assets/tsumo_parent_child.json'

export default {
  data () {
    return {
      mine: 0,
      other: 0,
      isParent: true,
      isParent_other: false,
      message: "",
      kyotaku: 0,
      honba: 0,
      ronResult: "",
      tsumoResult: ""
    }
  },
  computed: {
  },
  methods: {
    computeResult () {
      this.message = ""
      this.ronResult = ""
      this.tsumoResult = ""
      if (isNaN(Number(this.mine)) || isNaN(Number(this.other))) {
        this.message = "数値を入力してください！"
        return
      }
      if (this.isParent && this.isParent_other) {
        this.message = "親は複数設定できません！"
        return
      }
      let difference = Math.abs(this.mine - this.other) * 100
      let ronDifference = difference - (this.kyotaku * 1000 + this.honba * 600)
      let tsumoDifference = difference - (this.kyotaku * 1000 + this.honba * 400)
      let ronMap
      switch(this.isParent) {
        case "親":
          ronMap = ron_parent.data
          break
        case "子":
          ronMap = ron_child.data
          break
        default:
          ronMap = ron_parent.data
          break
      }
      let tsumoMap
      if (this.isParent == "親") {
        tsumoMap = tsumo_parent_child.data
      } else if (this.isParent_other == "親") {
        tsumoMap = tsumo_child_parent.data
      } else {
        tsumoMap = tsumo_child_child.data
      }
      let i = 0
      while (i < ronMap.length) {
        let differ = ronMap[i].differ
        if (ronDifference < differ) {
          this.ronResult = ronMap[i].huhan.join('もしくは')
          break
        }
        i++
      }
      i = 0
      while (i < tsumoMap.length) {
        let differ = tsumoMap[i].differ
        if (tsumoDifference < differ) {
          this.tsumoResult = tsumoMap[i].huhan.join('もしくは')
          break
        }
        i++
      }
    },
    clearAll () {
      this.mine = 0
      this.other = 0
      this.isParent = '親'
      this.isParent_other = '子'
      this.message = ''
      this.kyotaku = 0
      this.honba = 0
      this.ronResult = ''
    },
    incrementKyotaku () {
      this.kyotaku += 1
    },
    decrementKyotaku () {
      if (this.kyotaku == 0) {
        return
      }
      this.kyotaku -= 1
    },
    incrementHonba () {
      this.honba += 1
    },
    decrementHonba () {
      if (this.honba == 0) {
        return
      }
      this.honba -= 1
    }
  }
}
// # sourceURL=About.js
</script>
<style>
  .about {
    background: #ededed;
    font-family: 'Open Sans', sans-serif;
    font-weight: bold;
  }
  .kyotaku_button {
    display: inline-block;
    width: 30px;
    height: 30px;
    background: #9ec34b;
    color: #FFF;
    font-weight: bold;
    margin: 10px;
    border-radius: 5px;
    position: relative;
  }
  .checkbox {
    height: 25px;
    margin: 10px;
  }
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
input[type=text], input[type=number] {
  width: 100px;
}
input[type=checkbox] {
	width:			24px;
	height:			24px;
	-moz-transform:		scale(1.4);
	-webkit-transform:	scale(1.4);
	transform:		scale(1.4);
}
</style>


