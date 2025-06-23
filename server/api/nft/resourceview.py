from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from nft.models import NFT, NFTCollection, NFTEvent
from api.nft.serializer import NFTSerializerList, NFTCollectionListSerializer, NFTCollectionOneSerializer, \
    NFTEventListSerializer, NFTEventOneSerializer


class NFTViewSet(viewsets.ModelViewSet):
    queryset = NFT.objects.all()
    serializer_class = NFTSerializerList
    permission_classes = [IsAuthenticatedOrReadOnly]


class NFTCollectionViewSet(viewsets.ModelViewSet):
    queryset = NFTCollection.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return NFTCollectionListSerializer
        else:
            return NFTCollectionOneSerializer


class NFTEventViewSet(viewsets.ModelViewSet):
    queryset = NFTEvent.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return NFTEventListSerializer
        else:
            return NFTEventOneSerializer
