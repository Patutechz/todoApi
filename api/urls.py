from django.urls import path
from .views import ItemList, ItemDetail, TodoList, TodoDetail

urlpatterns = [
    path('item/', ItemList.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view()),
    path('todo/', TodoList.as_view()),
    path('todo/<int:pk>/', TodoDetail.as_view()),
]