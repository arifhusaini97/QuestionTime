<template>
  <div class="single-question mt-2">
    <div class="container">
      <h1>{{ question.content }}</h1>
      <p class="mb-0">
        Posted by:
        <span class="question-author-name">{{ question.author }}</span>
      </p>
      <p>{{ question.created_at }}</p>
    </div>
    <hr />
    <div class="container">
      <AppAnswer
        v-for="(answer, index) in answers"
        :key="index"
        :answer="answer"
      />
    </div>
  </div>
</template>

<script>
import apiService from '@/common/api.service';
// INFO: @ symbol start from src file
import AppAnswer from '@//components/Answer.vue';

export default {
  name: 'question',
  props: {
    slug: {
      type: String,
      required: true,
    },
  },
  components: {
    AppAnswer,
  },
  data() {
    return {
      question: {},
      answers: [],
    };
  },
  methods: {
    setPageTitle(title) {
      document.title = title;
    },
    getQuestionData() {
      const endpoint = `/api/questions/${this.slug}/`;
      apiService(endpoint).then((data) => {
        this.question = data;
        this.setPageTitle(data.content);
      });
    },
    getQuestionAnswers() {
      const endpoint = `/api/questions/${this.slug}/answers/`;
      apiService(endpoint).then((data) => {
        this.answers = data.results;
        this.setPageTitle('Answers');
      });
    },
  },
  created() {
    this.getQuestionData();
    this.getQuestionAnswers();
  },
};
</script>

<style scoped>
.question-author-name {
  font-weight: bold;
  color: #dc3545;
}
</style>
