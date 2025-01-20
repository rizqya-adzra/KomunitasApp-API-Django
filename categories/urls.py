from django.urls import path
from .views import get_categories, create_category, category_detail

urlpatterns = [
    path('categories/', get_categories, name='get_categories'),
    path('categories/create', create_category, name='create_category'),
    path('images/icon/', get_categories, name='get_categories'),
    path('categories/<int:pk>', category_detail, name='get_categories'),
]
