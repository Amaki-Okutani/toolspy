from django.urls import path
from . import views

urlpatterns = [
    path('tsn/productGroup/list/', views.product_group_list, name='group_list'),
    path('tsn/productGroup/regist/',views.regist_page,name='group_regist'),
    path('tsn/productGroup/check/',views.check_page,name='group_check'),

]
