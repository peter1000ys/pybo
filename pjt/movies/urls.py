from django.urls import path
from . import views


app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/delete/', views.delete, name='delete'),
    path('<int:movie_pk>/update/', views.update, name='update'),
    path('<int:pk>/reviews/', views.reviews_create, name='reviews_create'),
        path(
        '<int:movie_pk>/reviews/<int:review_pk>/delete/',
        views.reviews_delete,
        name='reviews_delete',
    ),
]