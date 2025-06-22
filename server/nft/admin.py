from django.contrib import admin
from .models import NFT, NFTEventTags, NFTEvent, NFTCollection

model_list = (NFT, NFTEventTags, NFTEvent, NFTCollection)

admin.site.register(model_list)
