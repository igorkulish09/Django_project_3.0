from django.urls import path
from . import views

app_name = 'magazine'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('model1/', views.model1_list, name='model1_list'),
    path('model1/<int:model1_id>/', views.model1_detail, name='model1_detail'),
    path('model2/', views.model2_list, name='model2_list'),
    path('model2/<int:model2_id>/', views.model2_detail, name='model2_detail'),
]

