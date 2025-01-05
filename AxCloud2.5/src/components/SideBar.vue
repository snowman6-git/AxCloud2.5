<template>
  <div id="side" class="active">
    <table border="0" id="profile">
    <tr>
      <td rowspan="2">
        <img id="profile_img" src="/profile.jpeg" alt="">
      </td>
      <td style="font-size: 1.25rem;">snowman6</td>
    </tr>
    <tr>
        <td style="opacity: 1; font-size: 0.8rem;">
          <div>50% Used</div>
          <progress value="50" max="100"></progress>
        <div>FreeSpace 11.9GB/25GB</div>
      </td>
    </tr>
  </table>
  
  <div class="side_menu">
    <input type="radio" id="drivex" name="interest" value="interest" checked>
    <label for="drivex">DriveX</label>
  </div>

  <div class="side_menu">
    <input type="radio" id="ytcat" name="interest" value="interest">
    <label for="ytcat">Yt.Cat</label>
  </div>

  <div class="side_menu">
    <input type="radio" id="soundsix" name="interest" value="interest">
    <label for="soundsix">SoundSix</label>
  </div>

  <div class="side_menu">
    <input type="radio" id="usync" name="interest" value="interest">
    <label for="usync">Usync</label>
  </div>
  
  <div class="side_menu">
    <input type="radio" id="setting" name="interest" value="interest">
    <label for="setting">Setting</label>
  </div>
</div>
</template>

<script setup>
</script>
<style scoped>

[type="radio"] {
  display: none;
}
/* 1면 2도 */
[type="radio"]:checked + label{
  opacity: 1;
  background-color: black;
}
progress {
  -webkit-appearance: none; /* 기본 스타일 제거 (WebKit 브라우저) */
  appearance: none; /* 기본 스타일 제거 */
  border: none;
  border-left: 0.2rem solid white;
  border-right: 0.2rem solid white;
  height: 0.25rem; /* 프로그레스 바의 높이 설정 */
  background-color: transparent;
}
/* 프로그레스 바의 진행 상태 스타일 */
progress::-webkit-progress-bar {
  background-color: transparent; /* 남은 부분의 색상 */
}
progress::-webkit-progress-value {
  background-color: white; /* 채워진 부분의 색상 */
}
progress::-moz-progress-bar {
  background-color: green; /* Firefox에서 채워진 부분의 색상 */
}

label{
  position: relative;
  opacity: 0.5;
  padding: 0.5rem;
  width: 100%;
  display: inline-block;
  background-color: transparent;
  box-sizing: border-box;
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
</style>