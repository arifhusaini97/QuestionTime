from django.urls import include, path
from rest_framework.routers import DefaultRouter
from app_questions.api import views as aqv

router = DefaultRouter()

router.register(r"questions", aqv.QuestionViewSet)

# ! The url is trailing backslash sensitive.
urlpatterns = [
    path("", include(router.urls)),
    path(
        "questions/<slug:slug>/answers/",
        aqv.AnswerListAPIView.as_view(),
        name='answer-list'
    ),
    path(
        "questions/<slug:slug>/answer/",
        aqv.AnswerCreateAPIView.as_view(),
        name='answer-create'
    ),
    path(
        "answers/<int:pk>/",
        aqv.AnswerRetrieveUpdateDestroyAPIView.as_view(),
        name='answer-detail'
    ),
    path(
        "answers/<int:pk>/like/",
        aqv.AnswerLikeAPIView.as_view(),
        name='answer-like'
    )
]
