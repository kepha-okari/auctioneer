from django.urls import include, path
# from django.conf.path.static import static
from . import views

urlpatterns = [
    path('index/', views.index, name='main-view'),
    # path('', include('auctionapp.urls'))
]

