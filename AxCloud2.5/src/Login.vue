<script setup>
import axios from 'axios';

function sleep(ms) {return new Promise(resolve => setTimeout(resolve, ms))}
document.addEventListener("keydown", (event) => {if (event.key === "Enter") {event.preventDefault(); document.querySelector("#submit").click()}})


document.addEventListener("DOMContentLoaded", function() {
  const talk = document.querySelector("#talk")
  const nameplate = document.querySelector("#nameplate")
});

async function nameplate_return(ment){
  talk.textContent = ment
  setTimeout(function() {
    nameplate.classList.remove("send")
  }, 500)
  talk.classList.add("active")
  await sleep(3000)
  talk.classList.remove("active")
}
async function submit() {
  const id = document.querySelector("#id")
  const pw = document.querySelector("#pw")

  nameplate.classList.add("send")



  if (pw.value == "" || id.value == ""){
    nameplate_return("뭐라도 써서 주셔야죠.")
  }
  axios.post('http://localhost:8000/login', {
    id: id.value,
    pw: pw.value
  })
  .then(function (response) {
    if (response == 200){
      nameplate_return("인증 완료되었습니다.")
    }

    if (response != 200){
      nameplate_return()
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
  <div id="talk">
    O O O
  </div>

  <div id="panel">
    
    <!-- =============== -->
    <div id="nameplate">
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
#talk{
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
}

#panel{
  z-index: 1;

  width: 100%; height: 100%;
  display: flex; align-items: center; justify-content: center;
  flex-direction: column;
}

#info{
  width: 100%;
  display: flex; align-items: center; justify-content: center;
  flex-direction: column;
}
#id{
  font-size: 1.5rem;
}

#nameplate.send{
  transform: translateY(-80vh);
}
#nameplate{
  transition: 2s ease;
  /* background-color: ; */
  width: 18rem; height: 25rem;
  border: 0.01rem solid white;
  border-radius: 0.5rem;

  display: flex;
  align-items: center;

  justify-content: space-between;
  flex-direction: column;
  
  /* padding: 1rem; */
  /* transform: rotate(-10deg); */
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