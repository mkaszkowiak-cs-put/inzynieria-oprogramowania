<script setup lang="ts">
import { onMounted, computed, inject } from 'vue';
import { RouterLink, RouterView } from 'vue-router'
import { useDataStore } from './stores/data';

const dataStore = useDataStore();
onMounted(() => {
  // dataStore.fetchData(); // mozna tak sobie z api pobrac na starcie
});

const $debug = inject('$debug');
</script>

<template>
  <header class="header">
    <RouterLink :to="{ name: 'home' }" class="header__logo">
      System kręglarski
    </RouterLink>
    <nav class="header__nav">

    </nav>
  </header>
  <main>
    <RouterView v-slot="{ Component }">
      <keep-alive>
        <component :is="Component" :key="$route.fullPath"></component>
      </keep-alive>
    </RouterView>
  </main>
</template>

<style scoped lang="scss">
.header {
  background: var(--hex-key);
  color: var(--hex-white);
  padding: 20px var(--px-container-padding);

  &__logo {
    font-weight: bold;
    text-decoration: none;
    color: var(--hex-white);
  }
}

main {
  padding: 20px var(--px-container-padding);
  flex: 1;
  display: flex;
  flex-direction: column;
}
</style>
