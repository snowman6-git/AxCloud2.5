<script setup>
// import { RouterLink, RouterView } from 'vue-router'
// import HelloWorld from './components/HelloWorld.vue'

import { ref, computed } from 'vue'

import Login from './Login.vue'
import Home from './Home.vue'
import NotFound from './NotFound.vue'
import Welcome from './Welcome.vue'

// 나중에 홈으로 옮기기
// import Head from './components/Head.vue'
// import Screen from './components/Screen.vue'
// import DriveX from './components/DriveX.vue'
// import SoundSix from './components/SoundSix.vue'

const routes = {
  '/': Welcome,
  '/login': Login,
  '/Home': Home
}
const currentPath = ref(window.location.hash)
window.addEventListener('hashchange', () => {
  currentPath.value = window.location.hash
})
const currentView = computed(() => {
  return routes[currentPath.value.slice(1) || '/'] || NotFound //없는 경로면 알아서 절로감, 미친 개끌 nginx같은느낌.
})
</script>

<template>

  <!-- 이게 있으면 computed에서 넣은거로 나옴 -->
  <component :is="currentView" />

  <!-- <a href="#/">Home</a> |
  <a href="#/about">About</a> |
  <a href="#/non-existent-path">잘못된 링크</a> -->
  
  <!-- <Head/> -->
  <!--  -->
  <!-- <Screen> -->

    <!-- <Login/> -->
    <!-- <DriveX/> -->
    <!-- <SoundSix/> -->

  <!-- </Screen> -->
</template>

<style scoped>
</style>