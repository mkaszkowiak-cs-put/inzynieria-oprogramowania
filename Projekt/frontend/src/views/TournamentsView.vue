<template>
  <div class="tournaments-list">
    <h2>Lista Turniejów</h2>
    <ul>
      <li v-for="tournament in tournaments" :key="tournament.id">
        <div>
          <strong>{{ tournament.name }}</strong>
        </div>
        <div>Data rozpoczęcia: {{ tournament.date_start }}</div>
        <div>Data zakończenia: {{ tournament.date_end }}</div>
        <div>Zakończony: {{ tournament.finished ? "Tak" : "Nie" }}</div>
      </li>
    </ul>
    <form @submit.prevent="addTournament">
      <label for="name">Nazwa turnieju:</label>
      <input v-model="newTournament.name" type="text" required />

      <label for="date_start">Data rozpoczęcia:</label>
      <input v-model="newTournament.date_start" type="date" required />

      <label for="date_end">Data zakończenia:</label>
      <input v-model="newTournament.date_end" type="date" required />

      <label for="finished">Zakończony:</label>
      <input v-model="newTournament.finished" type="checkbox" />

      <button type="submit">Dodaj Turniej</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";

const tournaments = ref([
  {
    id: 1,
    name: "Mistrzostwa Polski Juniorów 2024",
    date_start: "2024-01-20",
    date_end: "2024-01-28",
    finished: false,
    bowling_alley_id: 5
  },
  {
    id: 2,
    name: "4. Memoriał Ryszarda Bonka",
    date_start: "2023-01-01",
    date_end: "2023-01-03",
    finished: true,
    bowling_alley_id: 4
  },
  {
    id: 3,
    name: "8. Puchar Starosty w Sierakowie",
    date_start: "2023-06-11",
    date_end: "2023-06-15",
    finished: true,
    bowling_alley_id: 3
  }
]);

const newTournament = ref({
  name: "",
  date_start: "",
  date_end: "",
  finished: false
});

const addTournament = () => {
  tournaments.value.push({
    ...newTournament.value,
    id: tournaments.value.length + 1
  });
  newTournament.value = {
    name: "",
    date_start: "",
    date_end: "",
    finished: false
  };
};
</script>

<style scoped>
.tournaments-list {
  text-align: center;
  margin: 50px auto;
  min-width: 600px;
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
  margin: 20px 0;
  padding: 20px;
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
