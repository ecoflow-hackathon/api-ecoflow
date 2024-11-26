from rest_framework.routers import DefaultRouter
from .views import ProdutorViewSet, LoteViewSet, InformacaoProducaoViewSet

router = DefaultRouter()
router.register(r'produtores', ProdutorViewSet)
router.register(r'lotes', LoteViewSet)
router.register(r'informacoes', InformacaoProducaoViewSet)

urlpatterns = router.urls
