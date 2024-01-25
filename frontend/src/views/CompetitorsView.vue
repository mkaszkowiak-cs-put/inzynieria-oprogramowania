<template>
  <div class="competitors-list">
    <h2>Lista Zawodników</h2>
    <ul>
      <li v-for="competitor in competitors" :key="competitor.id">
        {{ competitor.firstName }} {{ competitor.lastName }} (Wiek:
        {{ competitor.age }}, Ranking: {{ competitor.ranking }})
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const generateRandomCompetitor = () => {
  const firstNames = ["John", "Alice", "Bob", "Emma", "Michael"];
  const lastNames = ["Smith", "Johnson", "Williams", "Jones", "Brown"];

  return {
    id: Math.floor(Math.random() * 1000),
    firstName: firstNames[Math.floor(Math.random() * firstNames.length)],
    lastName: lastNames[Math.floor(Math.random() * lastNames.length)],
    age: Math.floor(Math.random() * 10) + 20,
    ranking: Math.floor(Math.random() * 100) + 1
  };
};

const competitors = ref([]);

onMounted(() => {
  for (let i = 0; i < 10; i++) {
    competitors.value.push(generateRandomCompetitor());
  }
});
</script>

<style scoped>
.competitors-list {
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
</style>
