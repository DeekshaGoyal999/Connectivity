from django.urls import path
from django.conf import settings

from accounts.views import (
    login_view,
    logout_view,
    register_view,
    profile_view
    )


urlpatterns = [
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    path('profile/', profile_view),
]

