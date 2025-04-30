from django.contrib import admin
from django.urls import path
from hello.views import say_hello

print(">>>>> USING UPDATED URLS.PY <<<<<")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', say_hello),
]

