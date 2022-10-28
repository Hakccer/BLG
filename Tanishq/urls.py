from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

admin.site.site_header = "The Tech Hood"
admin.site.site_title = "Welcome Back"
admin.site.index_title = "Welcome Boi's"

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('-$5P+3Q9}62w4!N*k437&35T5;Y8"XJ3/', admin.site.urls),
    path('', include('Vick.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root':       settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,
            {'document_root': settings.STATIC_ROOT}),
]
