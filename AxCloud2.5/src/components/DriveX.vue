<template>

  <div id="panel">
    <div id="screen">
      <div
      class="dropzone"
      @dragover.prevent
      @drop.prevent="handleDrop"
      @dragleave="handleDragLeave"
      :class="{ 'is-dragover': isDragOver }"
    >
      <p>파일을 드래그 앤 드롭하세요!</p>
      <input type="file" @change="check()" multiple />
    </div>
    
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
const chunkSize = 10 * 1024 * 1024;

function check(){
  const files = event.target.files;
  for (let i = 0; i < files.length; i++) {
    console.log(files[i])
    upload(files[i])
  }  
  // flist.forEach(function(target) {
  // })
}

const upload = async (file) => {
  const totalChunks = Math.ceil(file.size / chunkSize);
  let offset = 0;
  for (let i = 0; i < totalChunks; i++) {
    const chunk = file.slice(offset, offset + chunkSize);
    const formData = new FormData();
    formData.append('filename', file.name); // 파일 이름 추가
    formData.append('chunk', chunk); // 청크 추가
    formData.append('chunk_now', i+1); // 청크 추가
    formData.append('chunk_max', totalChunks); // 청크 추가
    formData.append('size', file.size); // 청크 추가
    try {
        const response = await fetch('http://localhost:3160/upload', {
            method: 'POST',
            body: formData,
            credentials: "include"
        });
        console.log(response.status);
        if (response.status != 200){
          window.location.href = "#/login"
          break
        }
      } catch (error) {
      console.error('Error uploading chunk:', error);
      break; // 에러 발생 시 루프 종료
    }
    offset += chunkSize; // 다음 청크로 오프셋 이동
  }
}


//보류
// async function upload(file) {

//   let offset = 0;
//   const chunkSize = 50 * 1024 * 1024;

//   while (offset < file.size) {
//     const fileslice = file.slice(offset, offset + chunkSize);
    
//     console.log(offset, fileslice)
    
//     axios.post('http://localhost:3160/upload', {
//       headers: {
//         'Content-Type': 'multipart/form-data'
//       },
//       filename: "ax25",
//       chunk: fileslice
//     }).then(function (response) {
//       offset += fileslice;
//       // if (response.data != "200"){
//       //   return false;
//       // }
//       // else{
//       // }
//     })
//   }
// }
// ==================











const close = () => {
  document.querySelector("#side").classList.remove("active")
}

import { ref } from 'vue';
import DataBlock from './DataBlock.vue';
// components 배열을 ref로 정의
const components = ref([]);
components.value.push({ filename: "Aaa", filesize:"7.92MB", fileformat: "7z", filedate: "date"});


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