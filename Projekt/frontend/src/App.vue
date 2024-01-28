<script setup lang="ts">
import { inject } from "vue";
import { RouterLink, RouterView } from "vue-router";
import { useDataStore } from "./stores/data";

const dataStore = useDataStore();
console.log(dataStore);
const $debug = inject("$debug");
</script>

<template>
  <header class="header">
    <RouterLink :to="{ name: 'home' }" class="header header__logo">
      System kręglarski
    </RouterLink>
    <nav class="header__nav" v-if="$route.fullPath !== '/'">
      <RouterLink :to="{ name: 'competitors' }" class="header header__nav">
        Zawodnicy
      </RouterLink>
      <RouterLink :to="{ name: 'bowling-alleys' }" class="header header__nav">
        Kręgielnie
      </RouterLink>
      <RouterLink :to="{ name: 'results' }" class="header header__nav">
        Wyniki
      </RouterLink>
      <RouterLink :to="{ name: 'tournaments' }" class="header header__nav">
        Zawody
      </RouterLink>
      <RouterLink :to="{ name: 'training-results' }" class="header header__nav">
        Treningi
      </RouterLink>
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
  padding: 15px var(--px-container-padding);
  display: flex;
  justify-content: space-between;

  &__logo {
    font-weight: bold;
    text-decoration: none;
    color: var(--hex-white);
    font-size: x-large;
  }

  &__nav {
    display: flex;
    margin-right: 50px;

    .header__nav {
      text-decoration: none;
      color: var(--hex-white);
      margin-right: 15px;

      &:hover {
        text-decoration: underline;
      }
    }
  }
}

main {
  padding: 20px var(--px-container-padding);
  flex: 1;
  display: flex;
  flex-direction: column;
}
</style>
