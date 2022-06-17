from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from blog.models import BlogModel
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponseRedirect
from django.urls import reverse

class BlogList(ListView):

    model = BlogModel
    template_name = "blog/blog_list.html"


class BlogDetail(DetailView):

    model = BlogModel
    template_name = "blog/blog_detail.html"


class BlogCreate(LoginRequiredMixin, CreateView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")
    fields = ["titulo", "sub_titulo", "cuerpo",]
# Cargo el valor autor en funcion del usuario que esta registrdo
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class BlogUpdate(LoginRequiredMixin, UpdateView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")
    fields = ["titulo", "sub_titulo", "cuerpo",]


class BlogDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")
# verificacion de usuario sea el mismo que lo creo, importo UserPassesTestMixin
    def test_func(self):
     exist = BlogModel.objects.filter(autor=self.request.user.id, id=self.kwargs['pk'])
     return True if exist else False
# Si el usuario no esta autorizado lo derivo a que no es posible
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse("no_autorizado"))

class BlogLogin(LoginView):
    template_name = 'blog/blog_login.html'
    next_page = reverse_lazy("blog_list")


class BlogLogout(LogoutView):
    template_name = 'blog/blog_logout.html'

def no_autorizado(request):
    return render(request, 'blog/bog_no_autorizado.html', )
  