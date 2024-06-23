import { createRouter, createWebHistory } from "vue-router";

import WanNianLi from "@/views/exercise/WanNianLi.vue";
import TriangleView from "@/views/exercise/TriangleView.vue";
import ComputerSale from "@/views/exercise/ComputerSale.vue";
import SalesCommission from "@/views/exercise/SalesCommission.vue";
import TelecomCharge from "@/views/exercise/TelecomCharge.vue"
import  TeamUnit  from "@/views/unit/TeamUnit.vue"
import TrackUnit from "@/views/unit/TrackUnit.vue"
import NoteUnit from "@/views/unit/NoteUnit.vue"
import AttractionUnit from "@/views/unit/AttractionUnit.vue"
import UserUnit from "@/views/unit/UserUnit.vue"
import  TeamIntegrate  from "@/views/integrate/TeamIntegrate.vue"
import TrackIntegrate from "@/views/integrate/TrackIntegrate.vue"
import NoteIntegrate from "@/views/integrate/NoteIntegrate.vue"
import AttractionIntegrate from "@/views/integrate/AttractionIntegrate.vue"
import UserIntegrate from "@/views/integrate/UserIntegrate.vue"
import  TeamSystem  from "@/views/system/TeamSystem.vue"
import TrackSystem  from "@/views/system/TrackSystem.vue"
import NoteSystem  from "@/views/system/NoteSystem.vue"
import AttractionSystem  from "@/views/system/AttractionSystem.vue"
import UserSystem  from "@/views/system/UserSystem.vue"

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
      path: '/teamunit',
      component: TeamUnit,
    },
    {
      path: '/trackunit',
      component: TrackUnit,
    },
    {
      path: '/noteunit',
      component: NoteUnit,
    },
    {
      path: '/userunit',
      component: UserUnit,
    },
    {
      path: '/attractionunit',
      component: AttractionUnit,
    },
    {
      path: '/teamintegrate',
      component: TeamIntegrate,
    },
    {
      path: '/trackintegrate',
      component: TrackIntegrate,
    },
    {
      path: '/noteintegrate',
      component: NoteIntegrate,
    },
    {
      path: '/userintegrate',
      component: UserIntegrate,
    },
    {
      path: '/attractionintegrate',
      component: AttractionIntegrate,
    },
    {
      path: '/teamsystem',
      component: TeamSystem,
    },
    {
      path: '/tracksystem',
      component: TrackSystem,
    },
    {
      path: '/notesystem',
      component: NoteSystem,
    },
    {
      path: '/usersystem',
      component: UserSystem,
    },
    {
      path: '/attractionsystem',
      component: AttractionSystem,
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