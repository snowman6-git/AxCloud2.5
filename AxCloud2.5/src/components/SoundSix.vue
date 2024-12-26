<script setup>
  import DataBlock from './DataBlock.vue'
</script>

<template>
  <div id="screen">
    <div class="sections">
      <div id="album"></div>
      
    </div>
    
    <div class="sections">

    </div>
    
  </div>
</template>

<style scoped>
#screen{
  padding: 0.5rem;
  width: 100%; height: 100%;  
  display: flex;
  align-items: start;
  justify-content: center;
  flex-direction: row;
  border: 1px solid red;
  box-sizing: border-box;
}
.sections{
  width: 50%; height: 100%;
  border: 1px solid yellow;
}
#playbar{
  width: 100%; height: 20rem;
  border: 1px solid green;

}
</style>