from django.urls import path
from tm import views

# define the urls
urlpatterns = [
    path('tms/', views.tms),
    path('tms/<int:pk>/', views.tm_detail),    
]