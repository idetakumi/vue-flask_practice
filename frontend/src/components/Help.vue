<template>
  <div>
    <br>
    <h4>HELP</h4>
    <p> TODO管理アプリの使い方 </p>
    <div class="card help-card">
      <h4 style="color: #71ff71; background-color: forestgreen;">基本説明</h4>
      <div class="card-body" style="background-color: lightgrey; color: black;">
        <div class="card-text">
          <li>
            <span class="text">TITLEエリアにタイトルを入力し、</span>
            <span class="text">保存ボタンを押下するとTODOメモが</span>
            <span class="text">保存されます。</span>
          </li>
          <li>
            <span class="text">一つのTODOメモには、</span>
            <span class="text">タスクひとつを想定しています。</span>
          </li>
          <li>
            <span class="text">MEMOエリアは空白で保存可能です。</span>
            <span class="text">備考や詳細としてご記入ください。</span>
          </li>
          <li>
            <span class="text">PRIORITYは、そのTODOメモの優先度</span>
            <span class="text">または緊急度を示すものです。</span>
            <span class="text">「いそぎ」は<i style="color: #ff6347;">赤色</i>で、</span>
            <span class ="text">「ふつう」は<i style="color: #71ff71;">緑色</i>で、</span>
            <span class="text"> 「のんびり」は<i style="color: #6495ed;">青色</i>で表示されます</span>
          </li>

        </div>
      </div>
        
    </div>
  </div>
</template>
<style>
  .help-card {
    border: solid;
    width: 350px;
    margin: auto;
  }
  .text {
    display: inline-block;
  }
</style>
