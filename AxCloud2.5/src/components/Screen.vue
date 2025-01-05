<template>
  <div id="screen">
    <slot></slot>
  </div>
</template>

<style scoped>
#screen{
  width: 100%; height: 100%;
  display: flex;
  /* border: 1px solid red; box-sizing: border-box; */
  overflow: hidden;
}
</style>