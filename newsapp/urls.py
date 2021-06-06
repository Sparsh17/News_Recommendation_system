from . import views
from django.urls import path

urlpatterns = [
    path('',views.home, name='home'),
    path('<int:id>', views.content, name='content'),
    path('getRating', views.getRating, name='getRating'),
    path('recommend', views.recommend, name='recommend')
]