<template>
  <div class="bowling-alley-list">
    <h2>Lista Kręgielni</h2>
    <ul>
      <li v-for="alley in bowlingAlleys" :key="alley.id">
        {{ alley.name }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import api from "../api/api";

const bowlingAlleys = [
  {
    id: 1,
    name: "Wronki"
  },
  {
    id: 2,
    name: "Leszno"
  },
  {
    id: 3,
    name: "Sieraków"
  },
  {
    id: 4,
    name: "Tarnowo Podgórne"
  },
  {
    id: 5,
    name: "Poznań"
  },
  {
    id: 6,
    name: "Łaziska Górne"
  },
  {
    id: 7,
    name: "Puck"
  },
  {
    id: 8,
    name: "Gostyń"
  }
];

onMounted(async () => {
  try {
    const response = await fetch(
      `${BACKEND_URL}/api/v1/bowling_alleys/?skip=0&limit=10`
    );

    const data = response.json();
    console.log(data);
    bowlingAlleys.value = data;
  } catch (error) {
    console.error("Błąd pobierania listy kregielni:", error);
  }
});
</script>

<style scoped>
.bowling-alley-list {
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
  transition: background-color 0.3s ease;
}

li:hover {
  background-color: #e0e0e0;
}

li-enter-active,
li-leave-active {
  transition: opacity 0.5s;
}
li-enter,
li-leave-to {
  opacity: 0;
}
</style>
