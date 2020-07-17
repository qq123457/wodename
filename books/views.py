from django.shortcuts import render
from django.http import HttpResponse

from .models import Book, Category, Zcategory, Banner
# Create your views here.

def global_variable(request):
    cates = {}
    cp = Category.objects.all()
    for c in cp:
        q = Zcategory.objects.filter(category=c)
        cates[c] = q
    banner = Banner.objects.all()[0:3]
    
    return locals()

def index(request):
    
    cates = {}
    cp = Category.objects.all()
    for c in cp:
        q = Zcategory.objects.filter(category=c)
        cates[c] = q
    tui = Book.objects.filter(tui__id=1)[:10]

    #把两个变量封装到上下文里
    
    #把上下文传递到模板里
    return render(request,'index.html',locals())
    

# 搜索页
def search(request):
    
    ss=request.GET.get('search')
    if not ss:
        list = []
    else:
        list = Book.objects.filter(name__contains=ss)

    
    return render(request, 'search.html', locals())

#分类下的小分类

def clist(request, lid):
    

    clist = Book.objects.filter(category_id=lid)
    cname = Zcategory.objects.get(id=lid)
    return render(request, 'clist.html', locals())



    
