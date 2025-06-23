from rest_framework import serializers

from nft.models import NFT, NFTCollection, NFTEvent, NFTEventTags


class NFTSerializerList(serializers.ModelSerializer):
    class Meta:
        model = NFT
        fields = ('id', 'img', 'name', 'price', 'author')


class NFTCollectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFTCollection
        fields = ('id', 'name', 'author')


class NFTCollectionOneSerializer(serializers.ModelSerializer):
    nfts = NFTSerializerList(many=True)

    class Meta:
        model = NFTCollection
        fields = ('id', 'name', 'nfts', 'author')


class NFTEventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFTEvent
        fields = ('id', 'name', 'timeset')


class NFTEventTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFTEventTags
        fields = ('id', 'name')


class NFTEventOneSerializer(serializers.ModelSerializer):
    tags = NFTEventTagsSerializer(many=True)
    
    class Meta:
        model = NFTEvent
        fields = ('id', 'name', 'description', 'tags', 'timeset', 'author')
