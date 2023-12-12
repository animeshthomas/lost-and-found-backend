from . import views
from django.urls import path
urlpatterns = [
    path('addLostFound', views.addLostFound,name='addLostFound'),
    path('getLostFound', views.getLostFound,name='getLostFound'),
    path('searchLostFound', views.searchLostFound,name='searchLostFound'),
    path('deleteLostFound', views.deleteLostFound,name='deleteLostFound'),
]