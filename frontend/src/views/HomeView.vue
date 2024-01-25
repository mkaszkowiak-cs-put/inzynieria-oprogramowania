<template>
  <section class="homepage">
    <div class="homepage-container">
      <h1>Witaj na stronie głównej, wariacie!</h1>
      <p class="intro-text">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed cursus
        augue vel tristique tincidunt. Quisque vitae eros a mi ullamcorper
        ullamcorper. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Sed cursus augue vel tristique tincidunt. Quisque vitae eros a mi
        ullamcorper ullamcorper. Lorem ipsum dolor sit amet, consectetur
        adipiscing elit. Sed cursus augue vel tristique tincidunt. Quisque vitae
        eros a mi ullamcorper ullamcorper. Lorem ipsum dolor sit amet,
        consectetur adipiscing elit. Sed cursus augue vel tristique tincidunt.
        Quisque vitae eros a mi ullamcorper ullamcorper.
      </p>
      <RouterLink :to="{ name: 'about', params: {} }" class="about-link">
        O aplikacji
      </RouterLink>
    </div>
  </section>
</template>

<script setup lang="ts">
import { changeTitle } from "@/helpers/metatags";
changeTitle("System kręglarski");
</script>

<style scoped lang="scss">
.homepage {
  text-align: center;
  padding: 50px 0;
  color: #333;
  font-family: "Arial", sans-serif;

  .homepage-container {
    max-width: 800px;
    margin: 0 auto;
  }

  h1 {
    font-size: 2.5em;
    margin-bottom: 20px;
    color: blac;
  }

  .intro-text {
    font-size: 1.2em;
    margin-bottom: 30px;
    color: #555;
  }

  .about-link {
    display: inline-block;
    padding: 10px 20px;
    background-color: var(--hex-key);
    color: #fff;
    text-decoration: none;
    border-radius: 5px;
    transition: background-color 0.3s ease;

    &:hover {
      background-color: #093059;
    }
  }
}
</style>
