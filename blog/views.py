from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, Http404
from .models import Article, Category



#----------------------------------------------------------------

def home(request):
    articles_list = Article.objects.published()
    paginator = Paginator(articles_list, 5)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    context = {
       "articles": articles,
      
}
    return render(request, "blog/home.html", context)

#----------------------------------------------------------------
# detail article

def detail(request, slug):
        context = {
                # give object for article
            "article": get_object_or_404(Article.objects.published(), slug=slug),
           

        }          
        return render(request, "blog/detail.html", context)

# ----------------------------------------------------------------
def category(request,slug):
    context = {
       "category": get_object_or_404(Category, slug=slug, status=True),
}

    return render(request, "blog/category.html", context)