from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token

from .views import ShoeView, SingleShoeView


urlpatterns = [
    path("shoes/", ShoeView.as_view()),
    path("shoes/<int:pk>/", SingleShoeView.as_view()),
    path("auth/token/", obtain_jwt_token, name="api-jwt-auth"),
]
