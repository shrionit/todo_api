from django.urls import include, path
from .views import *
urlpatterns = [
	path('', TodoItemListCreateView.as_view()),
    path('<int:pk>/', TodoItemDetailView.as_view())
]
