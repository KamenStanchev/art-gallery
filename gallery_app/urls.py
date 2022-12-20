from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/<str:pk>', views.picture_details, name='picture-details'),
    path('categories/', views.categories_page, name='categories_page'),
    path('categories/<str:pk>', views.view_by_category, name='view-by-category'),
    path('about-us/', views.about_us, name='about-us'),
    path('contact-us/', views.contact_us, name='contact-us')

]