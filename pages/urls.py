from django.urls import path
from .views import HomePageView, AboutPageView



urlpatterns= [
     path("", HomePageView.as_view(), name='home'),
     path("drafts/", AboutPageView.as_view(), name='home'),
]