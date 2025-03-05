<script setup>
    import { RouterLink } from 'vue-router'
    import Logo from '/Images/Logo.png'

</script>

<template>
    <header class="flex justify-between w-full h-[100px] items-center">
        
            <RouterLink to="/">
            <div class="left text-2xl cursor-pointer flex gap-5 items-center">
            <img :src="Logo" alt="Logo" class="size-16 object-cover">
            <h3>LineNodes</h3>
            </div>
            </RouterLink>
        <div class="right flex gap-5 text-2xl items-center ">
            <RouterLink to="/">Home</RouterLink>
            <RouterLink to="/partners">Partners</RouterLink>
            <RouterLink to="/plans">Plans</RouterLink>
            <RouterLink class="BtnStyle" to="/register">Register </RouterLink>

        </div>
    </header>
</template>

<script>
</script>