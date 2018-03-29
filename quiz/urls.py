from django.urls import path

from . import views

app_name = 'quiz'
urlpatterns = [
    # ex: /quiz/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /quiz/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /pquiz/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /quiz/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
