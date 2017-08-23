from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^basketball/', include('basketball.urls')),
    url(r'^admin/', admin.site.urls),
]