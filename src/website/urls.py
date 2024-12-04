from django.urls import path
from . views import (
    HomeView, AboutView, ServicesView, WorksView, ContactView, ProjectDetailView
)

app_name = 'website'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('services/', ServicesView.as_view(), name='services'),
    path('works/', WorksView.as_view(), name='works'),
    path('works/<int:pk>/', ProjectDetailView.as_view(), name='works_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
]