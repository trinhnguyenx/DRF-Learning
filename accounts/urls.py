from django.urls import path
from .views import register_user, logout_user, login_user, get_user, update_user, delete_user, get_me




urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('users/', get_user, name='getUser'),
    path('users/<int:user_id>/update/', update_user, name="updateUser"),
    path('users/<int:user_id>/delete/', delete_user, name="deleteUser"),
    path('me/', get_me, name='getMe'),

]