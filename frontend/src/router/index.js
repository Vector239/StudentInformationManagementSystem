import { createRouter, createWebHistory } from "vue-router";
import StudentManager from "@/components/StudentManager.vue";
import Login from "@/components/Login.vue";

const routes = [
  { path: "/", component: StudentManager },
  { path: "/login", component: Login },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;