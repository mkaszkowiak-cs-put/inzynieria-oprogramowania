import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import LoginView from "@/views/LoginView.vue";
import BowlingAlleysView from "@/views/BowlingAlleysView.vue";
import CompetitorsView from "@/views/CompetitorsView.vue";
import ResultsView from "@/views/ResultsView.vue";
import TournamentsView from "@/views/TournamentsView.vue";
import TrainingResults from "@/views/TrainingResults.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "login1",
      component: LoginView
    },
    {
      path: "/home/",
      name: "home",
      component: HomeView
    },
    {
      path: "/about/",
      name: "about",
      component: HomeView
    },
    {
      path: "/login/",
      name: "login",
      component: LoginView
    },
    {
      path: "/bowling-alleys/",
      name: "bowling-alleys",
      component: BowlingAlleysView
    },
    {
      path: "/competitors/",
      name: "competitors",
      component: CompetitorsView
    },
    {
      path: "/results/",
      name: "results",
      component: ResultsView
    },
    {
      path: "/tournaments/",
      name: "tournaments",
      component: TournamentsView
    },
    {
      path: "/training-results/",
      name: "training-results",
      component: TrainingResults
    }
  ]
});

export default router;
