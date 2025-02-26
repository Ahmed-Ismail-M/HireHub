<script setup lang="ts"></script>
<template>
  <app-header />
  <router-view />
  <toast />
</template>

<script setup lang="ts">
import AppHeader from './components/AppHeader.vue'
import Toast from './components/Toast.vue'
</script>

<style>
@import 'bootstrap/dist/css/bootstrap.min.css';
</style>
