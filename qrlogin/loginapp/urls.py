from django.urls import path
from .views import qr_login, qr_login_callback

urlpatterns = [
    path('qr-login/', qr_login, name='qr_login'),
    path('qr-login-callback/', qr_login_callback, name='qr_login_callback'),
]
