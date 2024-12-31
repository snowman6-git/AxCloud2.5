<template>

  <div id="panel">

    <div id="side" class="active">
      <table border="0" id="profile">
      <tr>
        <td rowspan="2">
          <img id="profile_img" src="/profile.jpeg" alt="">
        </td>
        <td style="font-size: 1.25rem;">snowman6</td>
      </tr>
      <tr>
        <td style="opacity: 1; font-size: 0.8rem;">
          <progress value="50" max="100"></progress>
          <div>FreeSpace 11.9GB/25GB</div>
        </td>
      </tr>
    </table>
    
    <div class="side_menu">
      <input type="radio" id="drivex" name="interest" value="interest" checked>
      <label for="drivex">DriveX</label>
    </div>

    <div class="side_menu">
      <input type="radio" id="ytcat" name="interest" value="interest">
      <label for="ytcat">Yt.Cat</label>
    </div>

    <div class="side_menu">
      <input type="radio" id="soundsix" name="interest" value="interest">
      <label for="soundsix">SoundSix</label>
    </div>

    <div class="side_menu">
      <input type="radio" id="usync" name="interest" value="interest">
      <label for="usync">Usync</label>
    </div>
    
    <div class="side_menu">
      <input type="radio" id="setting" name="interest" value="interest">
      <label for="setting">Setting</label>
    </div>

    
    
    <!-- <div id="DriveX" class="side_menu">DriveX</div>
    <div class="side_menu">Yt.Cat</div>
    <div class="side_menu">SoundSix</div>
    <div class="side_menu">Usync</div>
    <div class="side_menu">Setting</div> -->
      
      

    </div>


    <div id="screen">
      <!-- <button @click="addComponent">Add Component</button> -->
      <!-- <button @click="close">close side</button> -->
      <div style="width: 100%;" v-for="(component, index) in components" :key="index">
        <DataBlock :name="component.filename" :size="component.filesize" :format="component.fileformat" :date="component.filedate"/>
        <!-- 컴포넌트에서 수신하는 props값="밑에서 추가하는 컴포넌트.키와값" -->
        <!-- :name="component.msg" -->
        <!-- <DataBlock name="ax.7z" size="7.92MB" format="7z" date="2024/12/12"/> -->
      </div>
    </div>
  
  </div>

</template>

<script setup>
import axios from 'axios';
axios.defaults.withCredentials = true; 

const close = () => {
  document.querySelector("#side").classList.remove("active")
}

import { ref } from 'vue';
import DataBlock from './DataBlock.vue';
// components 배열을 ref로 정의
const components = ref([]);
axios.post('http://localhost:3160/files', {
}).then(function (response) {
  response["data"].forEach(function(DataBlock) {
    let infos = JSON.parse(DataBlock[0])
    console.log(infos)
    components.value.push({ filename: infos["filename"], filesize:"7.92MB", fileformat: "7z", filedate: infos["date"]});
  })
})
</script>
<style scoped>

[type="radio"] {
  display: none;
}
/* 1면 2도 */
[type="radio"]:checked + label{
  opacity: 1;
  background-color: black;
}
label{
  position: relative;
  /* transition: 0.25s all; */
  opacity: 0.5;
  padding: 0.5rem;
  width: 100%;
  display: inline-block;
  background-color: transparent;
  box-sizing: border-box;
}

#panel{
  width: 100%; height: 100%;
  display: flex; 
  /* gap: 0.5rem; */
}
#side{
  height: 100%; width: 0px;
  border: 1px solid green;
  box-sizing: border-box;

  display: flex;
  align-items: start;
  justify-content: start;
  flex-direction: column;
  transition: 0.5s all;

}
#side > *{
  opacity: 0;
}
#side.active{
  width: 20rem
}
#side.active > *{
  opacity: 1;
}

.side_menu{
  display: flex; align-items: center; justify-content: center;
  /* background-color: black; */
  width: 100%;
  transition: all 0.55s;
  margin-bottom: 0.25rem;
}

.side_menu:hover{
  opacity: 1;
}
#profile{
  text-align: center;
  padding: 0.5rem;
  width: 100%;
  border-bottom: 0.1rem solid white;
}
#profile_img{
  border-radius: 0.25rem;
  width: 4rem; height: 4rem;
  /* padding: 0.5rem; */
  /* border: 0.1rem solid white; */
}

#screen {
  /* padding: 0.5rem; */
  width: 100%; height: 100%;
  display: flex;
  align-items: start;
  justify-content: start;
  flex-direction: column;
  border: 1px solid yellow;
  box-sizing: border-box;
  overflow-y: scroll;
}
</style>