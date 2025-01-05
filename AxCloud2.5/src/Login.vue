<script setup>
import axios from 'axios';
axios.defaults.withCredentials = true;

function sleep(ms) {return new Promise(resolve => setTimeout(resolve, ms))}
document.addEventListener("keydown", (event) => {if (event.key === "Enter") {event.preventDefault(); document.querySelector("#submit").click()}})

async function fail() {
  nameplate.classList.add("fail")
  await sleep(2000)
  nameplate.className = '';
}
async function submit() {
  const id = document.querySelector("#id")
  const pw = document.querySelector("#pw")

  nameplate.classList.add("scan")
  scanner.classList.add("active")
  await sleep(1000)
  scanner.classList.remove("active")

  if (pw.value == "" || id.value == ""){
    fail()
  }
  axios.post('http://localhost:3160/login', {
    id: id.value,
    pw: pw.value
  })
  .then(function (response) {
    if (response.data["code"] == "OK"){
      setTimeout(function() {
        nameplate.classList.add("ok")
        window.location.href = "#/Home"
      }, 500)
    }
    else{
      fail()
    }
  })
  .catch(function (error) {
    console.error('Error:', error);
  });
  // const url = 'localhost:8000/login';
  // const formData = new FormData();
  // formData.append('id', id.value)
  // formData.append('pw', pw.value);
  // await fetch(url, {
  //   method: 'POST',
  //   body: formData,
  //   credentials: "include"
  // })
  // .then((response) => response.text())
  // .then((result) => {
  //   pw.value == ""
  //   if (result == 200){
  //     window.location.href = "#/Home"
  //   }
  //   else{relock()}
  // })
  
}
</script>

<template>
  <div id="panel">
    <!-- =============== -->
    <div id="nameplate">
      <div id="scanner"></div>
      <div id="login-title">
        
        <table border="0">
          <tr>
            <td rowspan="2">
              <img id="appicon" src="/logo.svg" alt="">
            </td>
            <td>AxCloud2.5</td>
          </tr>
          <tr>
            <td style="opacity: 0.5; font-size: 0.6rem;">Acquire of X tools</td>
          </tr>
        </table>
      </div>
      <div id="info">
        <img id="profile" src="/profile.jpeg" alt="">
        <input type="text" name="" id="id" placeholder="ID" class="idpw">
        <input type="password" name="" id="pw" placeholder="Password" class="idpw">
      </div>
      <div id="level">
        Unknown
      </div>
    <!-- =============== -->


      
    
    </div>

    <div id="submit" @click="submit" style="margin-top: 1rem;">submit</div>
  </div>
</template>

<style scoped>
/* #talk{
  opacity: 0;
  margin: 0 auto;
  margin-top: 1rem;
  display: flex; align-items: center; justify-content: center;
  width: 10rem; 
  height: 5rem;
  border: 0.1rem solid white;
  transition: 1s all;
  transform: translateY(-100vh);

}

#talk.active{
  opacity: 1;
  transform: translateY(0vh);
  width: 20rem; height: 5rem;
} */

#panel{
  width: 100%; height: 100%;
  display: flex; align-items: center; justify-content: center;
  flex-direction: column;
}
#scanner{
  opacity: 0;
  transform: translateY(-1rem);
  width: 20rem; height: 0.25rem;
  background-color: red;
}
#scanner.active{
  opacity: 1;
  animation: scanning 1.5s ease-in-out infinite alternate;
}
@keyframes scanning {
  0%{transform: translateY(-5rem)}
  100%{transform: translateY(30rem)}
}
#info{
  width: 100%;
  display: flex; align-items: center; justify-content: center;
  flex-direction: column;
}
#id{
  font-size: 1.5rem;
}
#nameplate{
  transition: 0.5s all;
  /* background-color: ; */
  width: 18rem; height: 25rem;
  border: 0.01rem solid white;
  border-radius: 0.5rem;

  display: flex;
  align-items: center;

  justify-content: space-between;
  flex-direction: column;
  /* box-sizing: border-box; */
  
  /* position: fixed; */
  
  /* padding: 1rem; */
  /* transform: rotate(-10deg); */
}
#nameplate.scan{
  transform: scale(0.95);
  opacity: 0.5;
}
#nameplate.ok{
  opacity: 1;
  /* transform: rotate(-90deg); */
  width: 100vw; height: 100vh;
  /* border: 0.01rem solid green; */
}
#nameplate.ok > *{
  opacity: 0;
}
#nameplate.fail{
  opacity: 1;
  border: 0.01rem solid red;
}

#login-title{
  margin-top: 1rem;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;

}

#level{
  border-top: 0.01rem solid white;
  width: 100%; height: 3rem;
  box-sizing: border-box;
  /* padding: 1rem; */
  display: flex; align-items: center; justify-content: center;
}

#profile{
  width: 6rem; height: 6rem;
  margin-bottom: 0.5rem;
  border-radius: 0.25rem;
  /* border: 0.15rem solid white; */
}
#appicon{
  width: 2rem; height: 2rem;
  margin-right: 0.25rem;
  right: 0;
}
</style>