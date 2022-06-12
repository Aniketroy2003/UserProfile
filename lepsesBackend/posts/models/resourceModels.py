from django.db import models
import uuid
from django.contrib.auth.models import User
# from .models import PostDocument




class BasePost(models.Model):
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True ,editable=False)

    class Meta:
        abstract = True

class Interests(BasePost):
    value = models.CharField(max_length=50, default=None, null=True)
    
    def __str__(self):
        return self.value

class InterestsCategories(BasePost):
    interest = models.ForeignKey(Interests, on_delete=models.CASCADE)
    values = models.CharField(max_length=100, null=False, blank=False, default=None)

    def __str__(self):
        return f"{self.interest}.{self.values}"

