from . import views
from django.urls import path
from mba.views import addProduct

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('add_product', views.AddProduct.as_view(), name='add_product'),
    path('post/', views.Post, name='post'),
]