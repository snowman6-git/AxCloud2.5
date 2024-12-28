<template>

  <div id="panel">

  </div>

</template>

<script setup>
const close = () => {
  document.querySelector("#side").classList.remove("active")

}

import { ref } from 'vue';
import DataBlock from './DataBlock.vue';

// components 배열을 ref로 정의
const components = ref([]);

components.value.push({ filename: `Filename ${components.value.length + 1}`, filesize:"7.92MB", fileformat: "7z", filedate: "1/11"});

// 컴포넌트를 추가하는 메서드
const addComponent = () => {
  components.value.push({ filename: `Filename ${components.value.length + 1}`, filesize:"7.92MB", fileformat: "7z", filedate: "1/11"});
};
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