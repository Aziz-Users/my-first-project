<script setup>
import { RouterLink } from 'vue-router';
import Govno from '/Images/govno.png';
import Mine from '/Images/mine.png'
import Python from '/Images/python.png'
import Js from '/Images/js.png'
</script>

<template>
    <div class="min-h-[1000px]">
        <div class="flex justify-center items-center min-h-[1000px]">
            <div class="flex flex-col items-center text-center">
                <h1 class="text-[70px] mb-4 w-[60%]">
                    Надежный бесплатный хостинг игровых серверов
                </h1>
                <p class="text-gray-500 text-[20px] mb-6">
                    С большой скоростью сети и легкой панелью управления
                </p>
                <RouterLink class="BtnStyle mb-8" to="/register">Зарегестрируйся</RouterLink>
                <img :src="Govno" alt="" class="animate-fadeIn">
            </div>
        </div>
    </div>

<!-- //----------------------------------------------------------------------------------------------------------- -->

    <div class="my-20">
        <div class="relative ">            
            <h2 class="text-5xl absolute bottom-[-70px] ">Почему мы?</h2>
        </div>
        <div class="grid grid-cols-3 gap-10 ">            
            <div>
                <div class="border border-gray-600 rounded-sm p-9 mt-[150px] h-[290px] space-y-3">
                    <h3 class="text-4xl">Удобно</h3>
                    <p class="text-2xl/7 text-gray-500">Наши профессиональные панели управления, позволяет пользоваться нашим сервисом в любое время и за любым устройством.</p>
                </div>
            </div>
            <div>
                <div class="border border-gray-600 rounded-sm p-9 mt-[100px] h-[290px] space-y-3">
                    <h3 class="text-4xl">Стабильно</h3>
                    <p class="text-2xl/7 text-gray-500">Наше оборудование имеет безпрерывную поддержку , низкий пинг и отсутствие лагов. А скорость работы позволит установить сервер за 25 секунд.</p>
                </div>
            </div>
            <div>
                <div class="border border-gray-600 rounded-sm p-9 mt-[50px] h-[279px] space-y-3">
                    <h3 class="text-4xl">Безопасно</h3>
                    <p class="text-2xl/7 text-gray-500">У нас установлен сертификат безопасности, все данные передаются в зашифрованном виде.</p>
                </div>
            </div>
           
        </div>
    </div>

    <!-- //----------------------------------------------------------------------------------------------------------- -->

    <div class="my-40">
        <div class="flex">


            <div class="w-[45%] space-y-3 flex flex-col items-center">
                <h2 class="text-5xl">Поддерживаемые сервисы</h2>
                <p class="text-3xl text-gray-500">В будущем мы планируем пополнить этот список</p>
            </div>

<div class="w-[100%]">               
<div class="grid grid-cols-2 gap-10">
    <div class="flex p-[29px] border border-gray-600 space-y-2 rounded-xl">
        <div class="mr-4">
            <img :src="Js" alt="">
        </div>
        <div class="space-y-2">
            <h2 class="text-2xl">Node.js</h2>
            <p class="text-gray-600">Дискорд боты
                Телеграм
            </p>
        </div>
    </div>

    <div class="flex p-[29px] border border-gray-600 space-y-2 rounded-xl">
        <div class="mr-5">
            <img :src="Mine" alt="">
        </div>
        <div class="space-y-2">
            <h2 class="text-2xl">minecraft</h2>
            <p class="text-gray-600">Vanilla Sponge
                Spigot Forge
            </p>
        </div>
    </div>

    <div></div> <!-- Пустой div для пропуска -->

    <div class="flex p-[29px] border border-gray-600 space-y-2 rounded-xl">
        <div class="mr-4">
            <img :src="Python" alt="">
        </div>
        <div class="space-y-2">
            <h2 class="text-2xl">Python</h2>
            <p class="text-gray-600">Дискорд боты
                Сервера
            </p>
        </div>
    </div>
</div>

            </div>
        </div>
    </div>
</template>

<style>
@keyframes fadeIn {
    0% {
        opacity: 0;
        transform: translateY(20px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

.animate-fadeIn {
    animation: fadeIn 1s ease-out;
}
</style>