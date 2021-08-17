<template>
  <div class="single-question mt-2">
    <div class="container">
      <h1>{{ question.content }}</h1>
      <app-question-actions v-if="isQuestionAuthor" :slug="question.slug" />
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
        :requestUser="requestUser"
        @delete-answer="deleteAnswer"
      />
      <div class="my-4">
        <p v-show="loadingAnswers">...loading...</p>
        <button
          v-show="next"
          @click="getQuestionAnswers"
          class="btn btn-sm btn-outline-success"
        >
          Load More
        </button>
      </div>
    </div>
  </div>
</template>

<script>
// INFO: @ symbol start from src file
import apiService from '@/common/api.service';
import AppAnswer from '@//components/Answer.vue';
import AppQuestionActions from '@//components/QuestionActions.vue';

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
    AppQuestionActions,
  },
  data() {
    return {
      question: {},
      answers: [],
      newAnswerBody: null,
      error: null,
      userHasAnswered: false,
      showForm: false,
      next: null,
      loadingAnswers: false,
      requestUser: null,
    };
  },
  computed: {
    isQuestionAuthor() {
      return this.question.author === this.requestUser;
    },
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
    setRequestUser() {
      this.requestUser = window.localStorage.getItem('username');
    },
    getQuestionAnswers() {
      let endpoint = `/api/questions/${this.slug}/answers/`;
      this.loadingAnswers = true;
      if (this.next) {
        endpoint = this.next;
      }
      apiService(endpoint).then((data) => {
        this.answers.push(...data.results);
        this.loadingAnswers = false;
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }

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
    async deleteAnswer(answer) {
      const endpoint = `/api/answers/${answer.id}/`;
      try {
        await apiService(endpoint, 'DELETE');
        // INFO: async-await allow the system wait for the rseult
        // INFO: before excute other code. So doesn't need to use then.
        // this.$delete(this.answers, this.answers.indexOf(answer));
        this.answers.splice(this.answers.indexOf(answer), 1);
        this.userHasAnswered = false;
      } catch (err) {
        console.log(err);
      }
    },
  },
  created() {
    this.getQuestionData();
    this.getQuestionAnswers();
    this.setRequestUser();
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
