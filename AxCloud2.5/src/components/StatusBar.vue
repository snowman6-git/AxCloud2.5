<script setup>
defineProps({
  msg: {
    type: String,
    required: true,
  },
})
</script>

<template>
  <div id="status">
    <!-- <table border="0">
      <tr>
        <td colspan="1" style="opacity: 0.5; font-size: 0.5rem;">NowRunning</td>
      </tr>
      <tr>
        <td rowspan="2">
          <img id="appicon" src="/logo.svg" alt="">
        </td>
        <td>Storage X</td>
      </tr>
      <tr>
        <td style="opacity: 0.5; font-size: 0.6rem;">Network Storage</td>
      </tr>
    </table> -->

  </div>
</template>

<style scoped>
#appicon{
  width: 2rem; height: 2rem;
  margin-right: 0.25rem;
  right: 0;
}
#status{
  padding: 0.25rem;
  display: flex; 
  width: 100%;
  align-items: center;
  justify-content: space-between;
  border: 0.1rem solid white;
  box-sizing: border-box;
}
</style>
