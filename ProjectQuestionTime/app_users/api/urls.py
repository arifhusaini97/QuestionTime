from django.urls import path
from app_users.api.views import CurrentUserAPIView

urlpatterns =[
    path("user/", CurrentUserAPIView.as_view(), name="current-user")
]