from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('surveys/', include("surveys.urls")),
    path('admin/', admin.site.urls),
]
