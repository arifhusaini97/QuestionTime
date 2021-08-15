from app_questions.api.permissions import IsAuthorOrReadOnly
from app_questions.api.serializers import QuestionSerializer
from app_questions.models import Question
from rest_framework import viewsets
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
