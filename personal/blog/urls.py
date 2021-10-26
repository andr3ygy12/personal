from django.core import paginator
from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='blog_home'),
    # path('<slug:slug>/',views.PostDetails.as_view(), name='post_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail')
]