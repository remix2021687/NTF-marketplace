from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.nft.resourceview import NFTViewSet, NFTCollectionViewSet, NFTEventViewSet

router = routers.DefaultRouter()
router.register('nfts', NFTViewSet)
router.register('collections', NFTCollectionViewSet)
router.register('events', NFTEventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]