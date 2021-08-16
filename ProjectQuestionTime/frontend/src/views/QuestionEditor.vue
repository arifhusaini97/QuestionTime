<template>
  <div class="container mt-2">
    <h1 class="mb-3">Ask a Question</h1>
    <form @submit.prevent="onSubmit">
      <textarea
        v-model="question_body"
        class="form-control"
        placeholder="What do you want to ask?"
        cols="30"
        rows="10"
      ></textarea>
      <hr />
      <button class="btn btn-success" type="submit">Publish</button>
    </form>
    <p v-if="error" class="muted mt-2">
      {{ error }}
    </p>
  </div>
</template>

<script>
import apiService from '@/common/api.service';

export default {
  name: 'QuestionEditor',
  data() {
    return {
      question_body: null,
      error: null,
    };
  },
  methods: {
    onSubmit() {
      if (!this.question_body) {
        this.error = "You can't send an empty question!";
      } else if (this.question_body.length > 240) {
        this.error = 'Ensure this field has no more than 240 characters!';
      } else {
        const endpoint = '/api/questions/';
        const method = 'POST';
        apiService(endpoint, method, { content: this.question_body }).then(
          (response) => {
            this.$router.push({
              name: 'question',
              params: { slug: response.slug },
            });
          },
        );
      }
    },
  },
  created: () => {
    document.title = 'Editor - QuestionTime';
  },
};
</script>

<style></style>
