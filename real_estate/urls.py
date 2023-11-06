from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [
    path("supersecret/", admin.site.urls),
]

admin.site.site_header = "Real Estate Admin"
admin.site.site_title = "Real estate Admin Portal"
admin.site.index_title = "Welcome to the Real Estate Portal"