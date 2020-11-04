from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('applogic/', include('applogic.urls')),
    path('admin/', admin.site.urls),
]
