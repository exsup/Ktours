
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('booking_terms', views.booking_terms, name='booking_terms'),
    path('travelinfo/<int:package_id>', views.travelinfo, name='travelinfo'),
    path('popularinfo/<int:package_id>', views.popularinfo, name='popularinfo')
]

