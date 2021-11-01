from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, reverse

import util.views
from util.forms import SetPasswordFormNew

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', util.views.home, name='home'),

    # Authentication
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Redirects to settings.LOGIN_REDIRECT_URL
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Redirects to settings.LOGOUT_REDIRECT_URL
    path('register/', util.views.register, name='register'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(form_class=SetPasswordFormNew), name='password_reset_confirm'),
    path('password-reset-confirm/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    # Account settings
    path('account', util.views.account, name='account'),
    path('change-password', auth_views.PasswordChangeView.as_view(
        template_name='account/password_change_form.html',
        form_class=SetPasswordFormNew
    ), name='password_change'),
    path('change-password/done', auth_views.PasswordChangeDoneView.as_view(
        template_name='account/password_change_done.html'
    ), name='password_change_done'),

]
