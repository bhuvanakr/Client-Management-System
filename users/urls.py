from django.conf.urls import url
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, re_path

from . import views
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # url(r'^password_change/$', views.password_change, name='password_change'),
    re_path(r'^password_change/$',
            PasswordChangeView.as_view(template_name='registration/my_password_change.html'),
            name='my_password_change'),
    re_path(r'^password_change/done/$',
            PasswordChangeDoneView.as_view(template_name='registration/password_change_success.html'),
            name='password_change_success'),
    re_path(r'^password_reset/$',
            PasswordResetView.as_view(template_name='registration/password_reset.html'),
            name='password_reset'),
    re_path(r'^password_reset/done/$',
            PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
            name='password_reset_done'),
    re_path(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
            PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirmation.html'),
            name='password_reset_confirmation'),
    re_path(r'^password/reset/complete/$',
            PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
            name='password_reset_complete')
]
