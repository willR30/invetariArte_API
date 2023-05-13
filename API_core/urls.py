#por defencto rest framework nos permite crear las rutas por defecto
from rest_framework import routers
from .api import *

router=routers.DefaultRouter()


router.register('equipmentCategory', EquipmentCategoryViewSet, 'EquipmentCategory')
router.register('equipment',EquipmentViewSet,'Equipment')
router.register('category', CategoryViewSet, 'Category' )
router.register('products',ProductsViewSet, 'Products')
router.register('billState', BillStateViewSet,'BillState')
router.register('month', MonthViewSet,'Month')
router.register('year', YearViewSet,'Year')
router.register('bill', BillViewSet,'Bill')
router.register('sale',SaleViewSet,'Sale')

#Registrar demas urls

urlpatterns=router.urls