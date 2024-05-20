import { createRouter, createWebHistory } from "vue-router";

import WanNianLi from "@/views/WanNianLi.vue";
import TriangleView from "@/views/TriangleView.vue";
import ComputerSale from "@/views/ComputerSale.vue";

const routes = [{
    path: '/wannianli',
    component: WanNianLi,
},{
    path: '/triangle',
    component: TriangleView,
},{
    path: '/computersale',
    component: ComputerSale,
},{
    path: '/',
    redirect: '/triangle'
}]
const router = createRouter({
    history: createWebHistory(),
    routes
  });

export default router;