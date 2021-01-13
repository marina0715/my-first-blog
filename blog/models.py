from django.conf import settings
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField('難易度', max_length=50)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(u"レシピタイトル",max_length=30)
    
    calorie = models.CharField(u"カロリー",max_length=4,default='')
    time = models.CharField(u"調理時間",max_length=3,default='')
    process = models.CharField(u"調理工程数",max_length=2,default='')
    motion = models.CharField(u"調理動作数",max_length=2,default='')
    ingredients = models.CharField(u"食材数",max_length=2,default='')
    material = models.TextField(u"材料",default='')
    text = models.TextField(u"作り方")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

    class Meta:      #追加
        verbose_name= 'レシピ'
        verbose_name_plural = 'レシピ'
