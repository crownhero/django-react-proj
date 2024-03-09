from django.contrib import admin
from django.views import debug
from django.urls import path
from core.views import json_test_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', json_test_view),
    path('django/', debug.default_urlconf),
]
