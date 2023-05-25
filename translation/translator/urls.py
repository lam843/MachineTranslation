from django.urls import path
from .views import TranslationView, home

urlpatterns = [
    path('', TranslationView.as_view(), name='translation'),
    path('home/', home, name='home'),
]

