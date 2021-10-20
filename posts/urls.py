from django.urls import path

from posts.views import PostListView, PostDetailView, CommentCreateView

app_name = 'posts'

urlpatterns = [
    path('<int:pk>', PostDetailView.as_view(), name='detail'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment'),
    path('', PostListView.as_view(), name='list')
]