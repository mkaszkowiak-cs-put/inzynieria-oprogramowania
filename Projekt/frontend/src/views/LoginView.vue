<template>
  <div class="login-container">
    <h1>Logowanie</h1>
    <form @submit.prevent="login" class="login-form">
      <label for="username">Login:</label>
      <input
        type="text"
        id="username"
        v-model="username"
        required
        class="input-field"
      />
      <br />
      <label for="password">Hasło:</label>
      <input
        type="password"
        id="password"
        v-model="password"
        required
        class="input-field"
      />
      <br />
      <button type="submit">Zaloguj</button>
    </form>
  </div>
</template>

<style scoped>
.login-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 70vh;
}

h1 {
  margin-bottom: 20px;
}
.login-form {
  width: 60%;
  max-width: 300px;
  margin: 0 auto;
}

.input-field {
  width: 100%;
  box-sizing: border-box;
  margin-bottom: 10px;
}
</style>

<script setup>
import { useRouter } from "vue-router";
import { ref } from "vue";

const $router = useRouter();

const login = async () => {
  try {
    $router.push({ name: "home" });
  } catch (error) {
    console.error("Login failed:", error);
  }
};
</script>
