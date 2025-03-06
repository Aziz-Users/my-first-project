<script setup>
    import { RouterLink } from 'vue-router';
    import Govno from '/Images/govno.png'
</script>


<template>
    <div>

        <div class="flex justify-center items-center ">
            <div class="h-[100vh] ">

            <h1 class="text-[70px]">
                Надежный бесплатный хостинг игровых серверов
            </h1>
            <p class="text-gray-500 text-[20px]">
                С большой скоростью сети и легкой панелью управления
            </p>
            <RouterLink class="BtnStyle" to="/register">Зарегестрируйся</RouterLink>
            <img :src="Govno" alt="">
            </div>
        </div>


    </div>
</template>

<style>
</style>