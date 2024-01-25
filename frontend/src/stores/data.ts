import { defineStore } from "pinia";
import api from "../api/api";

export const useDataStore = defineStore("user", {
  state: () => ({
    isLoggedIn: true
    /*
        points: [] as Point[],
        floors: [] as Floor[]
        */
  }),
  actions: {
    async fetchData() {
      // pobieranie danych z api
      /*
            try {
                const response = await api.getPoints();
                this.points = response.points;
                this.floors = response.floors;
            }
            catch (error) {
                alert(error)
                console.log(error)
            }
            */
    },
    login() {
      this.isLoggedIn = true;
    },
    logout() {
      this.isLoggedIn = false;
    }
  }
});
