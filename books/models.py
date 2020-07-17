from django.db import models
# Create your models here.

#书籍大分类

class Category(models.Model):
    name = models.CharField('书籍系列', max_length=100)
    index = models.IntegerField(default=999, verbose_name='系列排序')
    
    class Meta:
        verbose_name = '书籍系列'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 书籍分小类
class Zcategory(models.Model):
    name = models.CharField('书籍分类', max_length=100)
    index = models.IntegerField(default=999, verbose_name='分类排序')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='书籍系列', blank=True, null=True)
    class Meta:
        verbose_name = '书籍分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 推荐
class Tui(models.Model):
    name = models.CharField('推荐位', max_length=100)

    class Meta:
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 书籍
class Book(models.Model):
    name = models.CharField('书名', max_length=70)
    autor = models.CharField('作者', max_length=70)
    category = models.ForeignKey(Zcategory, on_delete=models.DO_NOTHING, verbose_name='分类', blank=True, null=True)
    img = models.ImageField(upload_to='article_img/%Y/%m/%d/', verbose_name='书籍封面', blank=True, null=True)
    views = models.PositiveIntegerField('阅读量', default=0)
    tui = models.ForeignKey(Tui, on_delete=models.DO_NOTHING, verbose_name='推荐位', blank=True, null=True)

    created_time = models.DateTimeField('发布时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    download = models.URLField('下载地址', max_length=100)
    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = '书籍'

    def __str__(self):
        return self.name

class Link(models.Model):
    name = models.CharField('链接名称', max_length=20)
    linkurl = models.URLField('网址',max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'


class Banner(models.Model):
    text_info = models.CharField('标题', max_length=50, default='')
    img = models.ImageField('轮番图', upload_to='banner/')
    link_url = models.URLField('图片链接', max_length=100, blank=True, null=True)
    is_active = models.BooleanField('是否是active', default=False)

    def __str__(self):
        return self.text_info
    
    class Meta:
        verbose_name = '轮番图'
        verbose_name_plural = '轮番图'