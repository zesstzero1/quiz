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

    path('add_question', views.add_question, name='add_question'),
    
    path('<int:question_id>/add_choice/', views.add_choice, name='add_choice'),

    path('<int:question_id>/del_question/', views.del_question, name='del_question'),

]
