from django.urls import path
from . import views

urlpatterns = [
    path('tsn/', views.product_group_list, name='tsn_list'),
]
