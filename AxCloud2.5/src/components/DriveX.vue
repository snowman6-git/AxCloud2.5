<script setup>
  import DataBlock from './DataBlock.vue'
</script>

<template>
  <div id="screen">
    <DataBlock name="ax.7z" size="7.92MB" format="7z" date="2024/12/12"/>
    <DataBlock name="이승호얼굴.jpg" size="2.15MB" format="jpg" date="2024/12/13"/>
    <DataBlock name="example.exe" size="8.12MB" format="exe" date="2024/12/11"/>
    <DataBlock name="정모2일차.mp4" size="114MB" format="mp4" date="2024/12/2"/>
    <!-- <slot></slot> -->
  </div>
</template>

<style scoped>
#screen{
  /* padding: 0.5rem; */
  /* width: 100%; height: 100%;   */
  /* display: flex;
  align-items: start;
  justify-content: center;
  flex-direction: column; */
}
</style>