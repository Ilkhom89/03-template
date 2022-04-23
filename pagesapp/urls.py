from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView,PlatPageView, PractPageView



urlpatterns = [
    path('',HomePageView.as_view(),name = 'home'),
    path('about/',AboutPageView.as_view(),name = 'about'),
    path('contact/',ContactPageView.as_view(),name = 'contact'),
    path('platforma/',PlatPageView.as_view(),name = 'platforma'),
    path('practikum/',PractPageView.as_view(),name = 'practikum')

]
