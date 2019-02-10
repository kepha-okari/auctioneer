from django.urls import include, path
# from django.conf.path.static import static
from . views import index

urlpatterns = [
    path('', index, name='index'),
    # path('auctionapp/', include('auctionapp.urls'))
]

