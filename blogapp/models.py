from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

status_choices=[
    ('0','0'),
    ('1','1')
]
class UserProfile(User):
    profile_pic = models.ImageField(upload_to='profile_pic')
    bio = models.CharField(max_length=144,blank=True, null=True)
    
    def __str__(self):
        return self.first_name + " "+self.last_name
    

class Blog(models.Model):

    title = models.CharField(max_length=50)
    content =  RichTextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    publication_date = models.DateField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.CharField(max_length=1,choices=status_choices,default=1)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title
    
    

class BlogComments(models.Model):
    blog_fk = models.ForeignKey(Blog,on_delete=models.CASCADE)
    blog_comment = models.TextField()
    blog_commented_user_fk = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.CharField(max_length=1,choices=status_choices,default=1)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Blog Comment'
        verbose_name_plural = 'Blog Comments'

    def __str__(self):
        return self.blog_fk.title

class CategoryMaster(models.Model):
    category = models.CharField(max_length=50) 
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.CharField(max_length=1,choices=status_choices,default=1)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category

class BlogCategory(models.Model):
    blog_fk = models.ForeignKey(Blog,on_delete=models.CASCADE)
    blog_category_fk = models.ForeignKey(CategoryMaster,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.CharField(max_length=1,choices=status_choices,default=1)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Categories'

    def __str__(self):
        return self.blog_category_fk.category