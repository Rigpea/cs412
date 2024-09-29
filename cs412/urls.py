from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('quotes.urls')),  # Map root URL to the quotes app
    path('', include('restaurant.urls') )
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)