from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, Http404
from .models import Article, Category



#----------------------------------------------------------------
class ArticleList(ListView):
    queryset = Article.objects.published()
    paginate_by = 6


#----------------------------------------------------------------
class ArticleDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(), slug=slug)


# ----------------------------------------------------------------
# def category(request,slug, page=1):
#     category =  get_object_or_404(Category, slug=slug, status=True)
#     articles_list = category.articles.published()
#     paginator = Paginator(articles_list, 4)
#     articles = paginator.get_page(page)
#     context = {
#        "category": category ,
#        "articles": articles ,
# }

#     return render(request, "blog/category.html", context)

class CategoryList(ListView):
    paginate_by = 5
    template_name = "blog/category_list.html"

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context