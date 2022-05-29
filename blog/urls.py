from django.urls import path
from . import views

urlpatterns = [
    path('feeds/', views.FeedView.as_view(), name="feeds"),
    path('banner/', views.BannerView.as_view(), name="banner"),
]
