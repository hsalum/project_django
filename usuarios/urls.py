from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import UserRegisterView, CustomLoginView, CustomlogoutView, profileView, AvatarUpdateView,ProfileUpdateView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomlogoutView.as_view(), name='logout'),
    path('profile/', login_required(profileView.as_view()), name='profile'),
    path("profile-edit/", ProfileUpdateView.as_view(), name="edit_profile"),
    path('update-avatar/', AvatarUpdateView.as_view(), name='avatar_update'),
    

]