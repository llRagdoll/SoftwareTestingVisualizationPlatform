import { createRouter, createWebHistory } from "vue-router";

import WanNianLi from "@/views/WanNianLi.vue";
import TriangleView from "@/views/TriangleView.vue";
import ComputerSale from "@/views/ComputerSale.vue";
import SalesCommission from "@/views/SalesCommission.vue";
import TelecomCharge from "@/views/TelecomCharge.vue"

const routes = [
    {
    path: '/wannianli',
    component: WanNianLi,
    },
    {
    path: '/triangle',
    component: TriangleView,
    },
    {
    path: '/computersale',
    component: ComputerSale,
    },
    {
    path: '/salesCommission',
    component: SalesCommission,
    },
    {
    path: '/telecom',
    component: TelecomCharge,
    },
    {
    path: '/',
    redirect: '/triangle'
    }
]
const router = createRouter({
    history: createWebHistory(),
    routes
  });

export default router;