<script setup>
import { RouterLink } from 'vue-router'
import Logo from '/Images/Logo.png'
import Telegram from '/Images/telegram.png'
import Discord from '/Images/discord.png'
import Youtube from '/Images/youtube.png'
</script>

<template>
  <div class="flex flex-col ">
    <footer class=" text-white ">
      <div class="flex justify-between gap-4  w-full  max-w-7xl mx-auto p-6 border  border-indigo-600 ">
        <div class="">
          <div class="text-1xl cursor-pointer flex gap-4 items-center space-y-2">
            <img :src="Logo" alt="Logo" class="size-8 object-cover" />
            <h3>LineNodes</h3>
          </div>
          <div class="w-60 text-gray-500">
            <p>Профессиональный игровой хостинг 24/7 для серверов майнкрафт</p>
          </div>
        </div>
        <div class="flex flex-col space-y-2">
          <h3>Юридический раздел</h3>
          <router-link class="text-gray-500 cursor-pointer" to="/faq">Правила использования</router-link>
          <router-link class="text-gray-500 cursor-pointer" to="/support">Техническая поддержка</router-link>
        </div>
        <div class="flex flex-col space-y-2">
          <h3>Сервисы</h3>
          <router-link class="text-gray-500 cursor-pointer" to="/#">Панель управления</router-link>
          <router-link class="text-gray-500 cursor-pointer" to="/#">Клиент панель</router-link>
        </div>
        <div class="flex flex-col space-y-2">
          <h3>Страницы</h3>
          <router-link class="text-gray-500 cursor-pointer" to="/">Главная</router-link>
          <router-link class="text-gray-500 cursor-pointer" to="/partners">Партнерство</router-link>
          <router-link class="text-gray-500 cursor-pointer" to="/creators">Создатели</router-link>
        </div>
      </div>

      <div class="p-6 w-full max-w-7xl mx-auto flex justify-between text-gray-500">
        <p>2021 - 2022 LineNodes. Мы не связаны ни с одним брендом.</p>
        <div class="flex justify-between gap-3">
            <a href=""><img :src="Youtube" alt=""></a>
            <a href=""><img :src="Discord" alt=""></a>
            <a href=""><img :src="Telegram" alt=""></a>
        </div>
      </div>
    </footer>
  </div>
</template>


<style>
</style>