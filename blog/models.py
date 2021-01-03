from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(u"栄養素",upload_to='images',null=True, blank=True)
    title = models.CharField(u"レシピタイトル",max_length=30)
    material = models.TextField(u"材料",default='')
    text = models.TextField(u"作り方")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    time = models.CharField(u"調理時間",max_length=3,default='')
    process = models.CharField(u"調理工程数",max_length=2,default='')
    motion = models.CharField(u"調理動作数",max_length=2,default='')
    ingredients = models.CharField(u"食材数",max_length=2,default='')
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title
