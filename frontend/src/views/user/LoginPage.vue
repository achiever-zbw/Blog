<script setup>
    import { ref, watch  } from 'vue'
    import { useUserStore } from '@/stores'
    import { login_api } from '@/api/login'
    

    const login_form_data = ref({
        username: '',
        password: ''
    })
    const login_form = ref('')

    const login = async () => {
        if (!check_login())
            return
        else{
            const res = await login_api(login_form_data.value)
            console.log(res)
        }
    } 

    const check_login = () => {
        if (login_form_data.value.username == ''){
            return false
        }
        if (login_form_data.value.password == ''){
            return false
        }
        return true
    }

    

</script>

<template>
    <div class="container"></div>
     <div class="animation">
        <div class="item" style="--i:0;"></div>
        <div class="item" style="--i:1;"></div>
        <div class="item" style="--i:2;"></div>
        <div class="item" style="--i:3;"></div>
        <div class="item" style="--i:4;"></div>
        <div class="item" style="--i:5;"></div>
        <div class="item" style="--i:6;"></div>
        <div class="item" style="--i:7;"></div>
        <div class="item" style="--i:8;"></div>
        <div class="item" style="--i:9;"></div>
        <div class="item" style="--i:10;"></div>
        <div class="item" style="--i:11;"></div>
        <div class="item" style="--i:12;"></div>
        <div class="item" style="--i:13;"></div>
        <div class="item" style="--i:14;"></div>
        <div class="item" style="--i:15;"></div>
        <div class="item" style="--i:16;"></div>
        <div class="item" style="--i:17;"></div>
        <div class="item" style="--i:18;"></div>
        <div class="item" style="--i:19;"></div>
        <div class="item" style="--i:20;"></div>
      </div>
    <div class="wrapper">
          <div class="card-switch">
              <label class="switch">
                 <input type="checkbox" class="toggle">
                 <span class="slider"></span>
                 <span class="card-side"></span>
                 <div class="flip-card__inner">
                    <div class="flip-card__front">
                       <div class="title">登录</div>
                       <form class="flip-card__form" action=""  ref = "login_form" @submit.prevent="login()">
                          <input class="flip-card__input" name="name" v-model="login_form_data.username" placeholder="用户名" type="name">
                          <input class="flip-card__input" name="password" v-model="login_form_data.password" placeholder="密码" type="password">
                          <button class="flip-card__btn">确定</button>
                       </form>
                    </div>
                    <div class="flip-card__back">
                       <div class="title">注册</div>
                       <form class="flip-card__form" action="">
                          <input class="flip-card__input" placeholder="用户名" type="name">
                          <input class="flip-card__input" name="password" placeholder="密码" type="password">
                          <button class="flip-card__btn" @click="register()">提交</button>
                       </form>
                    </div>
                 </div>
              </label>
          </div>   
    </div>
</template>

<style scoped>
    .animation {
    position: absolute;
    top: 50vh;
    left: 50vw;
    transform: translate(-50%, -50%);
    height: 90%;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .item {
    position: absolute;
    background-color: transparent;
    width: calc(var(--i) * 7.5vmin);
    aspect-ratio: 1;
    border-radius: 50%;
    border: .9vmin solid rgb(0, 200, 255) ;
    transform-style: preserve-3d;
    transform: rotateX(70deg) translateZ(50px) translateY(80vmin);
    animation: my-move 5s ease-in-out calc(var(--i) * 0.08s) infinite;
    box-shadow: 0px 0px 15px rgb(124, 124, 124),
      inset 0px 0px 15px rgb(124, 124, 124);
  }

  @keyframes my-move {
    0%,
    100% {
      transform: rotateX(70deg) translateZ(50px) translateY(80vmin);
      filter: hue-rotate(0deg);
    }

    50% {
      transform: rotateX(70deg) translateZ(50px) translateY(-50vmin);
      filter: hue-rotate(180deg);
    }
  }
    .container {
        width: 100vw;
        height: 100vh;
        position: fixed;
        left: 0;
        top: 0;
        background: radial-gradient(
        125% 125% at -2% 101%,
        rgba(245, 87, 2, 1) 10.5%,
        rgba(245, 120, 2, 1) 16%,
        rgba(245, 140, 2, 1) 17.5%,
        rgba(245, 170, 100, 1) 25%,
        rgba(238, 174, 202, 1) 40%,
        rgba(202, 179, 214, 1) 65%,
        rgba(148, 201, 233, 1) 100%
        );
    }

  .wrapper {
    --input-focus: #2d8cf0;
    --font-color: #323232;
    --font-color-sub: #666;
    --bg-color: #fff;
    --bg-color-alt: #666;
    --main-color: #323232;
    position: fixed;
    left: 50vw;
    top: 50vh;
    transform: translate(-50%, -50%);
    
  }
  /* switch card */
  .switch {
    transform: translateY(-200px);
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 30px;
    width: 50px;
    height: 20px;
  }

  .card-side::before {
    position: absolute;
    content: '登录';
    left: -70px;
    top: 0;
    width: 100px;
    text-decoration: underline;
    color: var(--font-color);
    font-weight: 600;
  }

  .card-side::after {
    position: absolute;
    content: '注册';
    left: 70px;
    top: 0;
    width: 100px;
    text-decoration: none;
    color: var(--font-color);
    font-weight: 600;
  }

  .toggle {
    opacity: 0;
    width: 0;
    height: 0;
  }

  .slider {
    box-sizing: border-box;
    border-radius: 5px;
    border: 2px solid var(--main-color);
    box-shadow: 4px 4px var(--main-color);
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: var(--bg-colorcolor);
    transition: 0.3s;
  }

  .slider:before {
    box-sizing: border-box;
    position: absolute;
    content: "";
    height: 20px;
    width: 20px;
    border: 2px solid var(--main-color);
    border-radius: 5px;
    left: -2px;
    bottom: 2px;
    background-color: var(--bg-color);
    box-shadow: 0 3px 0 var(--main-color);
    transition: 0.3s;
  }

  .toggle:checked + .slider {
    background-color: var(--input-focus);
  }

  .toggle:checked + .slider:before {
    transform: translateX(30px);
  }

  .toggle:checked ~ .card-side:before {
    text-decoration: none;
  }

  .toggle:checked ~ .card-side:after {
    text-decoration: underline;
  }

  /* card */ 

  .flip-card__inner {
    width: 300px;
    height: 350px;
    position: relative;
    background-color: transparent;
    perspective: 1000px;
      /* width: 100%;
      height: 100%; */
    text-align: center;
    transition: transform 0.8s;
    transform-style: preserve-3d;
  }

  .toggle:checked ~ .flip-card__inner {
    transform: rotateY(180deg);
  }

  .toggle:checked ~ .flip-card__front {
    box-shadow: none;
  }

  .flip-card__front, .flip-card__back {
    padding: 20px;
    position: absolute;
    display: flex;
    flex-direction: column;
    justify-content: center;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    background: rgba(33, 80, 84, 0.4);
    gap: 20px;
    border-radius: 5px;
    border: 2px solid var(--main-color);
    box-shadow: 4px 4px var(--main-color);
  }

  .flip-card__back {
    width: 100%;
    transform: rotateY(180deg);
  }

  .flip-card__form {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
  }

  .title {
    margin: 20px 0 20px 0;
    font-size: 25px;
    font-weight: 900;
    text-align: center;
    color: var(--main-color);
  }

  .flip-card__input {
    width: 250px;
    height: 40px;
    border-radius: 5px;
    border: 2px solid var(--main-color);
    background-color: var(--bg-color);
    box-shadow: 4px 4px var(--main-color);
    font-size: 15px;
    font-weight: 600;
    color: var(--font-color);
    padding: 5px 10px;
    outline: none;
  }

  .flip-card__input::placeholder {
    color: var(--font-color-sub);
    opacity: 0.8;
  }

  .flip-card__input:focus {
    border: 2px solid var(--input-focus);
  }

  .flip-card__btn:active, .button-confirm:active {
    box-shadow: 0px 0px var(--main-color);
    transform: translate(3px, 3px);
  }

  .flip-card__btn {
    margin: 20px 0 20px 0;
    width: 120px;
    height: 40px;
    border-radius: 5px;
    border: 2px solid var(--main-color);
    background-color: var(--bg-color);
    box-shadow: 4px 4px var(--main-color);
    font-size: 17px;
    font-weight: 600;
    color: var(--font-color);
    cursor: pointer;
  }
</style>
