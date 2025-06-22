import uuid
from unittest.mock import mock_open

from django.contrib.auth.models import User
from django.db import models


class NFT(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    img = models.ImageField(upload_to="uploads/nft", null=False, blank=False)
    name = models.CharField('NFT Name', max_length=150, unique=True, null=False, blank=False)
    price = models.DecimalField('NFT Price', max_digits=10, decimal_places=2, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"NFT name: {self.name} | price: {self.price}"


class NFTCollection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('NFT Collection Name', max_length=150, unique=True, null=False, blank=False)
    nfts = models.ManyToManyField(NFT)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'NFT Collection: {self.name} | Author: {self.author}'


class NFTEventTags(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('NFT Event Tag Name', max_length=50, unique=True, null=False, blank=False)

    def __str__(self):
        return f'NFT Event Tag: {self.name}'

class NFTEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField('NFT Event Title', max_length=150, null=False, blank=False)
    description = models.TextField('NFT Event Description', max_length=5000, null=False, blank=False)
    timestamp = models.DateTimeField('NFT Event Timestamp', null=False, blank=False)
    tags = models.ManyToManyField(NFTEventTags)
    # detail - create hyperlink

    def __str__(self):
        return f'NFT Event Title: {self.title} | Time: {self.timestamp}'