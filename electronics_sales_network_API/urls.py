from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/goods/', include('goods.urls')),
    path('api/user/', include('users.urls')),
]
