# Use include() to add paths from the catalog application
from django.urls import include, urlpatterns
from django.views.generic import RedirectView
from django.urls import path
from . import views
urlpatterns += [
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
