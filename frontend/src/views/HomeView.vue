<script setup lang="ts">
import { changeTitle } from '@/helpers/metatags';
changeTitle('System kręglarski');
</script>

<template>
  <section class="homepage">
    <h1>Witaj na stronie głównej wariat</h1>
    <RouterLink :to="{ name: 'about', params: {} }">
      O aplikacji
    </RouterLink>
  </section>
</template>

<style  scoped lang="scss"></style>