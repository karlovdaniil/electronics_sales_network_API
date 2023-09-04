from rest_framework import routers

from goods.views import RetailNetworkViewSet

router = routers.SimpleRouter()
router.register('retail_network', RetailNetworkViewSet)

urlpatterns = []
urlpatterns += router.urls
