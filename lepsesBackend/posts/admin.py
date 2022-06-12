from django.contrib import admin
from .models.models import PostImage,PostText,PostDocument, Interests, InterestsCategories

# Register your models here.
admin.site.register(PostImage)
admin.site.register(PostText)
admin.site.register(PostDocument)
admin.site.register(Interests)
admin.site.register(InterestsCategories)
# admin.site.register(Like)