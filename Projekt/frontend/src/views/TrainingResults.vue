<template>
  <div class="training-results">
    <h2>Wyniki Treningowe</h2>

    <ul>
      <li v-for="(result, index) in trainingResults" :key="index">
        {{ result.firstName }} {{ result.lastName }} - Data: {{ result.date }},
        Wynik: {{ result.result }}
      </li>
    </ul>

    <form @submit.prevent="addTrainingResult">
      <label for="firstName">Imię:</label>
      <input v-model="newResult.firstName" type="text" required />

      <label for="lastName">Nazwisko:</label>
      <input v-model="newResult.lastName" type="text" required />

      <label for="date">Data:</label>
      <input v-model="newResult.date" type="date" required />

      <label for="result">Wynik:</label>
      <input v-model="newResult.result" type="number" required />

      <button type="submit">Dodaj Wynik Treningowy</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";

const trainingResults = ref([
  { firstName: "John", lastName: "Doe", date: "2023-01-15", result: 80 },
  { firstName: "Alice", lastName: "Smith", date: "2023-02-20", result: 95 },
  { firstName: "Bob", lastName: "Johnson", date: "2023-03-10", result: 88 }
]);

const newResult = ref({
  firstName: "",
  lastName: "",
  date: "",
  result: null
});

const addTrainingResult = () => {
  trainingResults.value.push({ ...newResult.value });
  newResult.value = { firstName: "", lastName: "", date: "", result: null };
};
</script>

<style scoped>
.training-results {
  text-align: center;
  margin: 50px auto;
}

h2 {
  font-size: 2em;
  margin-bottom: 20px;
  color: #333;
}

ul {
  list-style-type: none;
  padding: 0;
  min-width: 450px;
}

li {
  margin: 10px 0;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f8f8f8;
}

li:hover {
  background-color: #e0e0e0;
}

form {
  margin-top: 100px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

label {
  margin-bottom: 5px;
  font-weight: bold;
}

input {
  margin-bottom: 10px;
}

button {
  padding: 10px;
  background-color: var(--hex-key);
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #093059;
}
</style>
