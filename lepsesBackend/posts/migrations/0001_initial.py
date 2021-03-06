# Generated by Django 4.0.5 on 2022-06-12 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('value', models.CharField(default=None, max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InterestsCategories',
            fields=[
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('values', models.CharField(default=None, max_length=100)),
                ('interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.interests')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostText',
            fields=[
                ('postId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('postURL', models.CharField(max_length=200, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('isBookMarked', models.BooleanField(default=False)),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('descOfPost', models.TextField(blank=True, max_length=1000, null=True)),
                ('interestChoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.interests')),
                ('interestTags', models.ManyToManyField(default=None, max_length=50, related_name='textCategories', to='posts.interestscategories')),
                ('liked', models.ManyToManyField(blank=True, default=None, related_name='textLike', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('postId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('postURL', models.CharField(max_length=200, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('isBookMarked', models.BooleanField(default=False)),
                ('descOfImage', models.TextField(blank=True, max_length=1000, null=True)),
                ('uploadImage', models.ImageField(upload_to='postImage')),
                ('interestChoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.interests')),
                ('interestTags', models.ManyToManyField(default=None, max_length=50, related_name='imageCategories', to='posts.interestscategories')),
                ('liked', models.ManyToManyField(blank=True, default=None, related_name='imageLike', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostDocument',
            fields=[
                ('postId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('postURL', models.CharField(max_length=200, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('isBookMarked', models.BooleanField(default=False)),
                ('docTitle', models.CharField(max_length=100)),
                ('descOfDocuments', models.TextField(blank=True, max_length=1000, null=True)),
                ('uploadDocuments', models.FileField(blank=True, null=True, upload_to='postDoc')),
                ('numberOfDownloads', models.IntegerField(default=0)),
                ('thumbnailImage', models.ImageField(upload_to='postDocTB')),
                ('whoIsThisDocForChoices', models.CharField(choices=[('SCHOOLSTUDENT', 'schoolStudent'), ('COLLEGESTUDENT', 'collegeStudent'), ('EVERYONE', 'everyone')], default='Everyone', max_length=20)),
                ('selectClassChoices', models.CharField(choices=[('EIGHT', 8), ('NINE', 9), ('TEN', 10), ('ELEVEN', 11), ('TWELVE', 12)], default='10', max_length=20)),
                ('fileLanguageChoices', models.CharField(choices=[('HINDI', 'hindi'), ('ENGLISH', 'english'), ('TELUGU', 'telugu'), ('TAMIL', 'tamil')], default='English', max_length=20)),
                ('subjectOfFileSchoolChoices', models.CharField(choices=[('PHYSICS', 'physics'), ('CHEMISTRY', 'chemistry'), ('MATHS', 'maths'), ('HINDI', 'hindi'), ('ENGLISH', 'english'), ('SOCIALSCIENCE', 'socialScience'), ('SANSKRIT', 'sanskrit'), ('BIOLOGY', 'biology'), ('COMPUTERSCIENCE', 'computerscience')], default='English', max_length=20)),
                ('streamOfSubjectSchoolChoices', models.CharField(choices=[('SCIENCE', 'science'), ('COMMERCE', 'commerce'), ('ARTS', 'arts')], default='Science', max_length=20)),
                ('interestChoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.interests')),
                ('interestTags', models.ManyToManyField(default=None, max_length=50, related_name='docCategories', to='posts.interestscategories')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
