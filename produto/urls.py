from django.urls import path
from django.views.generic.edit import CreateView

from .views import (
    ProductCreateView, ProductDeleteView, 
    ProductDetail, ProductListView, ProductUpdateView,
    CustomLoginView, LoginView, RegisterPage, produtos
)
from django.contrib.auth.views import LogoutView


app_name = 'product'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='product:login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    
    #path('', produtos, name='all-products'),
    path('novos-produtos/', produtos, name='novos-produtos'),
    path('', ProductListView.as_view(), name='all-products'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('product-create/', ProductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product-delete')
]