from django.contrib import admin
from django.urls import path, include
from certificates.views import home_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('hlulhv1409/', admin.site.urls),
    path('certificates/', include('certificates.urls')),
    path('commerce/', include('commerce.urls')),
    path('', home_view, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
