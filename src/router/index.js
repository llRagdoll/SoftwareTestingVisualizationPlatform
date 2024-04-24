import { createRouter, createWebHistory } from "vue-router";

import WanNianLi from "@/views/WanNianLi.vue";

const routes = [{
    path: '/wannianli',
    component: WanNianLi,
}]
const router = createRouter({
    history: createWebHistory(),
    routes
  });

export default router;