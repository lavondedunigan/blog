from django.urls import path
from .views import HomePageView, AboutPageView
from .views import Index


urlpatterns= [
     path('register/', RegisterView.as_view(), name='register',)
     path("", HomePageView.as_view(), name='home'),
     path("", Index.as_view(), name='index'),
     path("drafts/", AboutPageView.as_view(), name='home'),
]