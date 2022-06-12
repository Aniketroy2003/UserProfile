from django.db import models
from django.contrib.auth.models import User 
import uuid
from .resourceModels import Interests, InterestsCategories


# Create your models here.
postTypeChoices = [('IMAGE','image'),('ARTICLES','articles'),
                ('DOCUMENTS','documents'),('POLL','poll')]
interestChoices=(('ENGINEERING','Engineering'),('BUSINESS','Business'),('MEDICAL','Medical'),
                 ('AEROSPACE','Aerospace'),('DEFENCE','Defence'),('SCIENCE','Science'),
                 ('BOTANIC','Botanic'),('PLANTING','Planting'),('POLITICS','Politics'))
    

class BasePost(models.Model):
    postId=models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True ,editable=False)
    postURL=models.CharField(max_length=200,unique=True, null=False,blank=False)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now_add=True)
    isBookMarked=models.BooleanField(default=False)


    class Meta:
        abstract = True


class PostImage(BasePost):
    interestChoice=models.ForeignKey(Interests, on_delete=models.CASCADE)
    descOfImage=models.TextField(max_length=1000,null=True ,blank=True)
    uploadImage = models.ImageField(null=False,blank=False,upload_to='postImage')
    interestTags = models.ManyToManyField(InterestsCategories, max_length=50, default=None, related_name='imageCategories')
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='imageLike')


    def __str__(self):
        return self.descOfImage[:10]

    # @property
    # def getNumberOfLikes(self):
    #     return self.liked.all().count()

class PostText(BasePost):
    interestChoice=models.ForeignKey(Interests, on_delete=models.CASCADE)
    title=models.CharField(max_length=150, null=True, blank=True)
    descOfPost=models.TextField(max_length=1000,null=True, blank=True)
    interestTags = models.ManyToManyField(InterestsCategories, max_length=50, default=None, related_name='textCategories')
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='textLike')
    
    def __str__(self):
        return self.title

    # @property
    # def getNumberOfLikes(self):
    #     return self.liked.all().count()


whoIsThisDocFor=(('SCHOOLSTUDENT','schoolStudent'),('COLLEGESTUDENT','collegeStudent')
                     ,('EVERYONE','everyone'))
selectClass=(('EIGHT',8),('NINE',9),('TEN',10),('ELEVEN',11),('TWELVE',12))
fileLanguage=(('HINDI','hindi'),('ENGLISH','english'),('TELUGU','telugu'),
                  ('TAMIL','tamil'))
subjectOfFileSchool=(('PHYSICS','physics'),('CHEMISTRY','chemistry'),('MATHS','maths'),
                         ('HINDI','hindi'),('ENGLISH','english'),('SOCIALSCIENCE','socialScience')
                   ,     ('SANSKRIT','sanskrit'),('BIOLOGY','biology'),('COMPUTERSCIENCE',
                         'computerscience'))
streamOfSubjectSchool=(('SCIENCE','science'),('COMMERCE','commerce'),('ARTS','arts'))

class PostDocument(BasePost):
    interestChoice=models.ForeignKey(Interests, on_delete=models.CASCADE)
    docTitle=models.CharField(max_length=100,null=False,blank=False)
    descOfDocuments=models.TextField(max_length=1000,null=True ,blank= True)
    uploadDocuments = models.FileField(null=True, blank=True,upload_to='postDoc')
    numberOfDownloads= models.IntegerField(default=0)
    thumbnailImage=models.ImageField(null=False,blank=False,upload_to='postDocTB')
    whoIsThisDocForChoices=models.CharField(max_length=20,choices=whoIsThisDocFor,default='Everyone')
    selectClassChoices=models.CharField(max_length=20,choices=selectClass,default='10')
    fileLanguageChoices=models.CharField(max_length=20,choices=fileLanguage,default='English')
    subjectOfFileSchoolChoices=models.CharField(max_length=20,choices=subjectOfFileSchool,default='English')
    streamOfSubjectSchoolChoices=models.CharField(max_length=20,choices=streamOfSubjectSchool,default='Science')
    interestTags = models.ManyToManyField(InterestsCategories, max_length=50, default=None, related_name='docCategories')
    # liked = models.ManyToManyField(User, default=None, blank=True, related_name='docLike')


    def __str__(self):
        return self.docTitle
    
#     @property
#     def getNumberOfLikes(self):
#         return self.liked.all().count()

# LIKE_CHOICES = (('like', 'Like'),
#                 ('dislike', 'Dislike'))

# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
#     post = models.ForeignKey(PostDocument, on_delete=models.CASCADE)
#     value = models.CharField(max_length=10, default="Like",choices=LIKE_CHOICES)

#     def __str__(self):
#         return str(self.post)
    

    
    
    