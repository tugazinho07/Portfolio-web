from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.home_view, name = 'home'),
    path('home', views.home_view, name='home'), 
    path('about', views.about_view, name='about'),
    path('projects', views.projects_view, name='projects'),
    path('web', views.web_view, name='web'),
    path('blog', views.blog_view, name='blog'),
    path('blog_new/', views.new_tarefa_view, name='blog_new'),
    path('blog_edit/<int:portfolio_id>', views.edit_tarefa_view, name='blog_edit'),
    path('delete/<int:portfolio_id>', views.delete_tarefa_view, name='delete'),
    path('contacts', views.contacts_view, name='contacts'),
    path('quizz', views.quizz, name='quizz'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout')
]