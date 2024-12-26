<script setup>
// 묶어지는지 확인
defineProps({
  name: {
    type: String,
    required: false,
  },
  size: {
    type: String,
    required: false,
  },
  format: {
    type: String,
    required: false,
  },
  date: {
    type: String,
    required: false,
  },
})

</script>

<template>
  <!-- <div id="block">{{ msg }}</div> -->

  <div id="block">
    
    <div id="info_first" class="infos">
      <div>[-]</div>
      <div>{{ name }}</div>
    </div>
    <!-- ========================== -->
    <div id="info_last" class="infos">
      <div>{{ size }}</div>
      <div>{{ format }}</div>
      <div>{{ date }}</div>
      <div id="download">⇧</div>
      <div>:</div>
    </div>

  </div>

</template>

<style scoped>

#block{
  padding: 0.5rem;
  width: 100%; height: 2.5rem;
  border-bottom: 0.01rem solid rgba(255, 255, 255, 0.5);
  box-sizing: border-box;
  display: flex; align-items: center; justify-content: space-between;
  opacity: 0.7;
}
#block:hover{
  opacity: 1;
  background-color: rgba(0, 0, 0, 0.2);
  /* transition: all 0.25s; */
  /* transform: scale(1.025); */
  /* border: 1px solid white; */
}
#download{
  /* display: none; */
  opacity: 0;
  transform: scaleY(-1);
  width: 1rem; height: 1rem;
  text-align: center;
  border-radius: 0.25rem;
}

#block:hover > #info_last > #download{
  opacity: 1;
}
.infos{
  display: flex;
  /* align-items: end; */
  justify-content: start;
  gap: 0.5rem;
}
</style>