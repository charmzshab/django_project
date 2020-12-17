from django.urls import path
from . views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView)
from . import views

urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),# -> looks for views with <app>/<model>_<viewtype>.html[blog/post_list.html]
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'), # since create & update will share the same view,
                                                                    #convention expects <app>/<model>_form.html
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),# convention -> <app>/<model>_confirm_delete.html
    path('about/', views.about, name='blog-about')
]