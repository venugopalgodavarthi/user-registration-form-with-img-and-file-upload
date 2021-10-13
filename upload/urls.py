from django.urls import path
from upload import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path("reg/",views.viewregister,name="viewregister"),
    path("details/",views.details,name="details"),
    path("login/",views.loginview,name="login"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)