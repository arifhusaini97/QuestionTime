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
  props: {
    slug: {
      type: String,
      required: false,
    },
  },
  methods: {
    onSubmit() {
      if (!this.question_body) {
        this.error = "You can't send an empty question!";
      } else if (this.question_body.length > 240) {
        this.error = 'Ensure this field has no more than 240 characters!';
      } else {
        let endpoint = '/api/questions/';
        let method = 'POST';
        if (this.slug === undefined) {
          endpoint += `${this.slug}/`;
          method = 'PUT';
        }
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
  async beforeRouteEnter(to, from, next) {
    if (to.params.slug !== undefined) {
      const endpoint = `/api/questions/${to.params.slug}/`;
      const data = await apiService(endpoint);
      return next((vm) => {
        const vmTemp = vm;
        vmTemp.question_body = data.content;
      });
    }
    return next();
  },
  created: () => {
    document.title = 'Editor - QuestionTime';
  },
};
</script>

<style></style>
