from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views


# app_name = 'auctionapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('post/artifact/', views.post_artifact, name='post_image'),
    path('place/bid/', views.place_bid, name='place_bid'),
    # re_path(r'^place/bid/(\d+)', views.place_bid, name='view_artifact'),
    # path('post/<int:pk>/', views.view_artifact, name='view_artifact'),
    re_path(r'^post/(\d+)', views.view_artifact, name='view_artifact'),
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^login/$',views.user_login,name='user_login'),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




    
    # re_path(r'^signup/$', views.signup, name='signup'),
    # re_path(r'^user_login/$',views.user_login,name='user_login'),
    # re_path(r'^accounts/', include('registration.backends.simple.urls')),