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
      <div v-if="userHasAnswered">
        <p class="answer-added">You've written an answer</p>
      </div>
      <div v-else-if="showForm">
        <form class="card" @submit.prevent="onSubmit">
          <div class="card-header px-3">Answer the Question</div>
          <div class="card-block">
            <textarea
              rows="5"
              class="form-control"
              placeholder="Share your knowledge!"
              v-model="newAnswerBody"
            ></textarea>
          </div>
          <div class="card-footer px-3">
            <button type="submit" class="btn btn-sm btn-success">
              Submit Your Answer
            </button>
          </div>
        </form>
        <p v-if="error" class="error mt-2">{{ error }}</p>
      </div>
      <div v-else class="btn btn-sm btn-success" @click="showForm = true">
        Answer the Question
      </div>
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
      newAnswerBody: null,
      error: null,
      userHasAnswered: false,
      showForm: false,
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
        this.userHasAnswered = data.user_has_answered;
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
    onSubmit() {
      if (this.newAnswerBody) {
        const endpoint = `/api/questions/${this.slug}/answer/`;
        apiService(endpoint, 'POST', { body: this.newAnswerBody }).then(
          (data) => {
            this.answers.unshift(data);
          },
        );
        this.newAnswerBody = null;
        this.showForm = false;
        this.userHasAnswered = true;
        if (this.error) {
          this.error = null;
        }
      } else {
        this.error = "You can't send an empty answer!";
      }
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
.answer-added {
  font-weight: bold;
  color: green;
}
.error {
  font-weight: bold;
  color: red;
}
</style>
