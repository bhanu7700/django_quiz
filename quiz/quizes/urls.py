from django.urls import path
from django.urls.resolvers import URLPattern
from .views import (
    QuizListView,
    quiz_data_view, 
    quiz_view
)

app_name = 'quizes'

urlpatterns = [
    path('',QuizListView.as_view(),name='main_view'),
    path('<pk>/',quiz_view, name='quiz_view'),
    path('<pk>/data/',quiz_data_view,name='quiz_data_view'),
]