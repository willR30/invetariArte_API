#por defencto rest framework nos permite crear las rutas por defecto
from rest_framework import routers
from .api import ProductsViewSet

router=routers.DefaultRouter()

router.register('products',ProductsViewSet, 'Products')

urlpatterns=router.urls