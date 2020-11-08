from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # app/model_viewtype.html (template format for detail view)
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    # model_form.html (template format for create view)
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # model_confirm_delete.html file to be created
    path('about/', views.about, name='blog-about'),
]

# pk = primery key
# int for id of post ex:1,2,3
