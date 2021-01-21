from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import URLValidator

class Category(models.Model):
    name = models.CharField('難易度', max_length=50)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(u"レシピタイトル",max_length=30)
    link = models.CharField(u"URL",max_length=100)
    category = models.ForeignKey(
                    Category, verbose_name='カテゴリー',
                    on_delete=models.PROTECT
               )
    image1 = models.ImageField(u"栄養素1",upload_to='images',null=True, blank=True)
    image2 = models.ImageField(u"栄養素2",upload_to='images',null=True, blank=True)
    image3 = models.ImageField(u"栄養素3",upload_to='images',null=True, blank=True)
    image4 = models.ImageField(u"栄養素4",upload_to='images',null=True, blank=True)
    calorie = models.CharField(u"カロリー",max_length=4,default='')
    carbohydrate = models.FloatField(u"炭水化物",max_length=3,default='')
    protein = models.FloatField(u"たんぱく質",max_length=3,default='')
    lipid = models.FloatField(u"脂質",max_length=3,default='')
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
