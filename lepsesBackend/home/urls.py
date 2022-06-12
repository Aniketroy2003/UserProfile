from django.urls import path,include
from home.views import views
urlpatterns = [
    path('', views.index),
    path('profile/',views.profile),
    path('setting/', views.setting),
    path('signup/', views.signup),
    path('signin/', views.signin),

]
