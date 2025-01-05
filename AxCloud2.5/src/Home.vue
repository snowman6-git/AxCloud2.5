<script setup>
import axios from 'axios';
axios.defaults.withCredentials = true; //해야 쿠키랑 같이 리퀘스트 보냄

import Head from './components/Head.vue'
import Screen from './components/Screen.vue'
import DriveX from './components/DriveX.vue'
import Loding from './components/Loading.vue'
import SoundSix from './components/SoundSix.vue'
import SideBar from './components/SideBar.vue';

document.addEventListener("DOMContentLoaded", function() {
  const loading = document.querySelector("#loading")
});

axios.post('http://localhost:3160/verify', {
})
.then(function (response) {
  console.log(response.data)
  if (response.data == 200){
    setTimeout(function() {
      loading.classList.add("ok")
    }, 500)
    //인증성공시 원래 동작 넣기, 목록불러오기나 ㅇㅇ 아마 컴포넌트 별로 계속 인증 하고 있으면 가고 이런식 해야할듯
  }
  else{
    window.location.href = "#/login"
  }
})
.catch(function (error) {
  console.error('Error:', error);
});


//나중에 도입
// const routes = {
//   '/DriveX': DriveX,
// }
// const currentPath = ref(window.location.hash)
// window.addEventListener('hashchange', () => {
//   currentPath.value = window.location.hash
// })
// const currentView = computed(() => {
//   return routes[currentPath.value.slice(1) || '/'] || NotFound //없는 경로면 알아서 절로감, 미친 개끌 nginx같은느낌.
// })
</script>

<template>
  <Loding id="loading"/>
  <Head/>
  <Screen>
    <SideBar/>
    <DriveX/>
  </Screen>
</template>

<style scoped>
#loading{
  width: 100vw; height: 100vh;
  position: fixed;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 99;
  background-color: #2f2f2f;
  border: 0.1rem solid white; box-sizing: border-box;
  overflow: hidden;
}
#loading.ok{
  transition: all 0.5s;
  transform: scale(2);
  opacity: 0;
  display: none;
  /* transform: translateY(-100vh); */
}
</style>


