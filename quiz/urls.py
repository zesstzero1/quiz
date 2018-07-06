from django.urls import path

from . import views

app_name = 'quiz'
urlpatterns = [
    path('', views.home_page, name='home'),
    # ex: /5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    
]
