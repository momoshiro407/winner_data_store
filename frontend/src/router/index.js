import { createRouter, createWebHistory } from "vue-router";
import ScrapingPlatform from "@/views/ScrapingPlatform.vue";

const routes = [
  {
    path: "/",
    name: "ScrapingPlatform",
    component: ScrapingPlatform,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
