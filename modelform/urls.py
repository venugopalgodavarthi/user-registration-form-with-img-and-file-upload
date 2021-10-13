from django.urls import path
from modelform import views
urlpatterns = [
    path("",views.registerview,name="register"),
    ]