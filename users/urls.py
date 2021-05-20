from django.contrib.auth import views as auth_views
from django.urls import path
from .views import account_page_view, login_page_view, logout_view, register_page_view

app_name = 'account'

urlpatterns = [
    path('<int:user_id>/', account_page_view, name='view'),

    path('login/', login_page_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_page_view, name='register'),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='password_reset/password_change_done.html'), name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='password_reset/password_change.html'), name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset/password_reset_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset/password_reset_complete.html'), name='password_reset_complete'),
]
