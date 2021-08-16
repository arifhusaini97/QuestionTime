import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Question from '../views/Question.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    // with props: true, the slug parameter gets passed as a prop to the component
    path: '/question/:slug',
    name: 'Question',
    component: Question,
    props: true,
  },
];

// process.env.BASE_URL
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
