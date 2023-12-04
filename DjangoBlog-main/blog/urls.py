from django.urls import path
from .import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post-detail/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post-create/', views.PostCreateView.as_view(), name='post-create'),
    path('post-update/<int:pk>/', views.PostUpdateView.as_view(), name='post-update'),
    path('post-delete/<int:pk>/', views.PostDeleteView.as_view(), name='post-delete'),
    path('posts/user/<str:username>/', views.UserPosts.as_view(), name='user-posts'),

]