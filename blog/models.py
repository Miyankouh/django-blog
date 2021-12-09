from django.db import models
from django.utils.html import format_html
from django.utils import timezone
from extensions.utils import jalali_converter




# my managers = Article
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status="p")
 


# my managers = Caregory
class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)

#-----------------------------------------------
#  CategoryModel

class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='children', verbose_name='زیر دسته')
    title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی ')
    slug = models.SlugField(max_length=100, unique=True,verbose_name=' ادرس دسته بندی')
    status = models.BooleanField(default=True, verbose_name='ایا نمایش داده شود؟')
    position = models.IntegerField(verbose_name='پوزیشن')
   
    # setting for Category model
    class Meta():
        verbose_name = 'دسته بندی '
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['parent__id' ,'position']

    def __str__(self):
        return self.title

    objects = CategoryManager()


#-----------------------------------------------
# Article Model

class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش نویس  '),
        ('p', 'منتشر شده '),
    )

    title = models.CharField(max_length=60, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=60, unique=True,verbose_name='ادرس مقاله')
    # ManyToMany
    category = models.ManyToManyField(Category, verbose_name='دسته بندی', related_name='articles')
    description = models.TextField(verbose_name='محتوا')
    thumbnail = models.ImageField(upload_to="images/", verbose_name='تصویر مقاله')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')



     # setting for Article model 
    class Meta():
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['-publish']    

    # show title in admin page  
    def __str__(self):
        return self.title

    # jpublish means jalali publish
    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = "زمان انتشار"

    # Fix a category bug when we disable it
    def category_published(self):
        return self.category.filter(status=True)

    # thumbnail 
    def thumbnail_tag(self):
        return format_html("<img width=100 height=75 style='border-radius:7px;' src='{}'".format(self.thumbnail.url))
    thumbnail_tag.short_description = " عکس"

   # Replacing  ArticleManager with the original Objects
    objects = ArticleManager()