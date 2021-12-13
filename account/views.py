from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import User
from .forms import ProfileForm
from .mixins import (
    FieldsMixin,
    FormValidMixin,
    AuthorAccessMixin,
    SuperUserAccessMixin,
    )
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView, 
    DeleteView,
    )

from blog.models import Article
# Create your views here.




class ArticleList(LoginRequiredMixin, ListView):
    template_name = 'registration/home.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)

#----------------------------------------------------------------

class ArticleCreate(LoginRequiredMixin, FormValidMixin ,  FieldsMixin ,  CreateView):
    model = Article
    template_name = 'registration/article-create-update.html'


# ----------------------------------------------------------------
#Updated
class ArticleUpdate(AuthorAccessMixin, FormValidMixin ,  FieldsMixin ,  UpdateView):
    model = Article
    template_name = 'registration/article-create-update.html'



# ------------------------------
#delet
class ArticleDelete(SuperUserAccessMixin,DeleteView):
    model = Article
    success_url = reverse_lazy('account:home')
    template_name = "registration/article_confirm_delete.html"


# ---------------------------------------------------------------------
#profile
class Profile(UpdateView):
    model = User
    template_name = "registration/profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy('account:profile')
    

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)