from django.urls import path
from . import views

app_name = 'donghu'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('sendcode/', views.sendcode, name='sendcode'),
    path('sendcode/code', views.identifycode, name="identifycode"),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('category/<slug:category_name_slug>/', views.category, name='category'),
    path('category/<slug:category_name_slug>/page=<int:page>/', 
        views.category, name='category'),
    path('add_article', views.add_article, name='addarticle'),
    path('category/<slug:category_name_slug>/<slug:username>/<int:aid>',
        views.detail, name='detail'),
    path('category/delete/<int:aid>/<slug:category_name_slug>/', 
        views.delete_article, name="delete"),
    path('comment/', views.submit_comment, name='comment'),
    path('delete/<slug:category_name_slug>/<int:aid>/<int:cid>/', views.delete_comment, name='delete_com'),
]