<template>

  <div id="panel">

    <div id="side" class="active">
      <progress value="50" max="100"></progress>
      <div>FreeSpace 11.9GB/25GB</div>
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
  align-items: center;
  justify-content: end;
  flex-direction: column;
  transition: 0.5s all;
  padding: 0.5rem;
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