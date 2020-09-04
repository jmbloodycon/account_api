from rest_framework.routers import DefaultRouter

from .views import TopUpBalanceView, SubstractBalanceView

router = DefaultRouter()

router.register('add', TopUpBalanceView)
router.register('substract', SubstractBalanceView)

urlpatterns = router.urls
