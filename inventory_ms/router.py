from rest_framework import routers
from inventory_app.viewsets import ItemViewSet

router = routers.DefaultRouter()
router.register('item', ItemViewSet)