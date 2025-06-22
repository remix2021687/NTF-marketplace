from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from nft.models import NFT
from api.nft.serializer import NFTSerializerList


class NFTViewSet(viewsets.ModelViewSet):
    queryset = NFT.objects.all()
    serializer_class = NFTSerializerList
    permission_classes = [IsAuthenticatedOrReadOnly]
