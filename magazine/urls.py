from django.urls import path

from . import views

app_name = "magazine"

urlpatterns = [
    path("", views.index, name="index"),
    path('magazine/', views.product_list, name='product_list'),
    path('magazine/<int:product_id>/', views.product_detail, name='product_detail'),
]
