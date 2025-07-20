from django.urls import path
from .views import UserRegisterView, CustomLoginView, CustomlogoutView, profileView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomlogoutView.as_view(), name='logout'),
    path( 'profile/', profileView.as_view(), name='profile'),
 

]