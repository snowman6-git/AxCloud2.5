
<script setup>
import StatusBar from './StatusBar.vue'
defineProps({
  msg: {
    type: String,
    required: true,
  },
})
</script>

<template>
  <div id="head">
      <div id="title">
        <img class="hicon" src="/logo.svg" alt="">
        <h1>AxCloud2.5</h1>
      </div>
      <div id="center">
        <StatusBar/>
        <!-- <div>검색</div> -->
      </div>
      <div id="endmenu">
      </div>
  </div>
</template>

<style scoped>
#head{
  box-sizing: border-box;
  padding: 0.25rem;
  display: flex; 
  width: 100%;
  align-items: center;
  justify-content: space-between;
  /* border-left: 0.25rem solid white; */
  border: 1px solid red;
}

#center, #endmenu{
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: row;
}

#title{
  display: flex; align-items: center;
}
#profile{
  border-radius: 50%;
  border: 0.1rem solid white;
  padding: 0.25rem;
}
.hicon{
  height: 2rem; width: auto;
  margin-right: 0.5rem;
}
h1 {
  font-weight: 500;
  font-size: 1.5rem;
}
</style>
