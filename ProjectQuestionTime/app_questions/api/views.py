from app_questions.api.permissions import IsAuthorOrReadOnly
from app_questions.api.serializers import AnswerSerializer, QuestionSerializer
from app_questions.models import Answer, Question
from rest_framework import generics, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    lookup_field = "slug"
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            created_by=self.request.user,
            updated_by=self.request.user
        )


class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwargs_slug = self.kwargs.get("slug")
        question = get_object_or_404(Question, slug=kwargs_slug)

        if question.answers_question.filter(author=request_user).exists():
            raise ValidationError("You have already answered this question!")

        serializer.save(
            author=request_user,
            created_by=request_user,
            updated_by=request_user,
            question=question
        )


class AnswerListAPIView(generics.ListAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwargs_slug = self.kwargs.get("slug")
        return Answer.objects.filter(
            question__slug=kwargs_slug
        ).order_by("-created_at")
