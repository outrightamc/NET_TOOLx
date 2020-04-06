
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from .views import home
from accounts.views import login_view, register_view, logout_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('home/', home),
    path('', include ('statool.urls')),
    path('accounts/login/', login_view),
    path('accounts/register/', register_view),
    path('accounts/logout/', logout_view),
]