from django.urls import path
from .views import CommentAPIView, CommentUpdateDeleteAPIView


urlpatterns = [
    path('<slug:slug>/comments/', CommentAPIView.as_view(), name='comments'),
    path('<slug:slug>/comments/<str:id>/', CommentUpdateDeleteAPIView.as_view(), name='comment'),
]