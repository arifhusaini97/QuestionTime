import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/views/Home.vue';
import Question from '@/views/Question.vue';
import QuestionEditor from '@/views/QuestionEditor.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    // with props: true, the slug parameter gets passed as a prop to the component
    path: '/question/:slug',
    name: 'question',
    component: Question,
    props: true,
  },
  {
    path: '/ask',
    name: 'question-editor',
    component: QuestionEditor,
  },
];

// process.env.BASE_URL
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
