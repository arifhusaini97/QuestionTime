<template>
  <div class="container mt-2">
    <h1 class="mb-3">Edit Your Answer</h1>
    <form @submit.prevent="onSubmit">
      <textarea v-model="answerBody" class="form-control" rows="10"></textarea>
      <hr />
      <button class="btn btn-success" type="submit">Publish your asnwer</button>
    </form>
    <p v-if="error" class="muted mt-2">
      {{ error }}
    </p>
  </div>
</template>

<script>
import apiService from '@/common/api.service';

export default {
  name: 'AnswerEditor',
  props: {
    id: {
      type: Number,
      required: true,
    },
    // previousAnswer: {
    //   type: String,
    //   required: true,
    // },
    // questionSlug: {
    //   type: String,
    //   required: true,
    // },
  },
  data() {
    return {
      questionSlug: null,
      answerBody: null,
      // answerBody: this.previousAnswer,
      error: null,
    };
  },
  methods: {
    onSubmit() {
      if (this.answerBody) {
        const endpoint = `/api/answers/${this.id}/`;
        apiService(endpoint, 'PUT', { body: this.answerBody }).then(() => {
          this.$router.push({
            name: 'question',
            params: { slug: this.questionSlug },
          });
        });
      } else {
        this.error = "You can't submit an empty answer!";
      }
    },
  },
  async beforeRouteEnter(to, from, next) {
    const toTemp = to;
    const endpoint = `/api/answers/${toTemp.params.id}/`;
    const data = await apiService(endpoint);
    // toTemp.params.previousAnswer = data.body;
    // toTemp.params.questionSlug = data.question_slug;
    // INFO: to access props by other alternative
    return next((vm) => {
      const vmTemp = vm;
      vmTemp.answerBody = data.body;
      vmTemp.questionSlug = data.question_slug;
    });
  },
};
</script>

<style></style>
