from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views


# app_name = 'auctionapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('post/artifact/', views.post_artifact, name='post_artifact'),
    path('post/<int:artifact_id>/', views.view_artifact, name='view_artifact'),
    path('category/<int:category_id>/', views.list_by_category, name='list_by_category'),
    re_path(r'^search/', views.search_results, name='search_results'),
    path('comment/<int:artifact_id>/', views.comment, name='comment'),
    re_path(r'^place/bid/(\d+)', views.place_bid, name='place_bid'),
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^login/$',views.user_login,name='login'),

]
