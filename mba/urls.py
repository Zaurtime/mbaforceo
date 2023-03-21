from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post_detail/<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('add_product/', views.add_product, name='add_product'),
    path('product-delete/<str:slug>/', views.delete_product, name='product_delete'),
    path('product-update/<str:slug>/', views.update_product, name='product_update'),
    path('post/', views.Post, name='post'),
]