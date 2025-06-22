from rest_framework import serializers

from nft.models import NFT


class NFTSerializerList(serializers.ModelSerializer):
    class Meta:
        model = NFT
        fields = ('id', 'img', 'name', 'price', 'author')
