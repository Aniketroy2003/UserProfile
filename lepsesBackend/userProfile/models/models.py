from django.db import models
from django.contrib.auth.models import User
import uuid

genderChoice= (('male', 'Male'),
                ('female', 'Female'),
                ('others', 'Others'))

profileCategoryChoice= (('schoolStudent', 'School Student'),
                ('collegeStudent', 'College Student'),
                ('educators', 'Educators or Creators'))



board = (('CBSE','cbse'),('ICSE','icse'),('STATE','state'),('INTERNATIONAL','international'))

class ProfileCategory(models.Model):
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now_add=True)
    # category = models.CharField(blank=False, max_length=30)
    # user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    # def __str__(self):
    #     return self.category

# ----------------------------------------------Intrests--------------------------------------
class Interests(models.Model):
    interestId=models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True ,editable=False)
    interestItems = models.CharField(max_length=200)



# -----------------------------------------------Location-----------------------------------------------------
class Location(models.Model):
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=200)
    pincode = models.IntegerField()



# -------------------------------------------------School-------------------------------------------------------
class School(models.Model):
    schoolId = models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True ,editable=False)
    schoolName = models.CharField(max_length=200)
    schoolBoard = models.CharField(max_length=100, choices=board)


#------------------------------------------------------Class--------------------------------------------------
class Standard(models.Model):
    # classId = models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True ,editable=False)
    className = models.IntegerField()



# ------------------------------------Profile--------------------------------------------------------------

class Profile(models.Model):
    # category = models.ForeignKey(ProfileCategory, on_delete=models.CASCADE, related_name='ProfileUser')
    firstName = models.CharField(max_length=20, blank=True, null=True)
    lastName = models.CharField(max_length=20, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=profileCategoryChoice, blank=True, null=True)
    email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    mobile = models.IntegerField(null=True, blank=True, unique=True)
    gender = models.CharField(choices=genderChoice, max_length=10, blank=True, null=True)
    dateOfBirth = models.DateField(null=True,blank=True)
    age = models.CharField(max_length=10, null=True, blank=True)
    demographics = models.ForeignKey(Location,blank=True, null=True, on_delete=models.CASCADE)
    School = models.ForeignKey(School, blank=True, null=True, on_delete=models.CASCADE)
    # standardOfUser = models.ForeignKey(Standard, null=True, blank=True, on_delete=models.CASCADE)
    bioLink = models.URLField(null=True, blank=True)
    endorseCount =  models.IntegerField(default=0)
    followerCount = models.IntegerField(default=0)
    followingCount = models.IntegerField(default=0)
    networkCount = models.IntegerField(default=0)
    interest = models.ForeignKey(Interests, null=True, blank=True ,on_delete=models.CASCADE)

    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

    



