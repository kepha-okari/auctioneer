from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/artifact', views.post_artifact, name='post_image'),
    # path('post/<int:pk>/', views.view_artifact, name='view_artifact'),
    re_path(r'^post/(\d+)', views.view_artifact, name='view_artifact'),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
