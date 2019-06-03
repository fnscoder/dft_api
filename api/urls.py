from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token

from .views import ShoeView, SingleShoeView, FileUploadView


urlpatterns = [
    path("auth/token/", obtain_jwt_token, name="api-jwt-auth"),
    path("shoes/", ShoeView.as_view()),
    path("shoes/<int:pk>/", SingleShoeView.as_view()),
    path("shoes/csv_import/", FileUploadView.as_view()),
]
