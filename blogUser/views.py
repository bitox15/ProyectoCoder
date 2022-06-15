from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User


class SignUp(SuccessMessageMixin, CreateView):
  template_name = 'blogUser/blogUser_crear_acc.html'
  success_url = reverse_lazy('blog_login')
  form_class = UserCreationForm
  success_message = "Perfil Satisfactorio"

class BlogUserProfile(DetailView):

    model = User
    template_name = "blogUser/blogUser_detail.html"


class BlogUserUpdate(LoginRequiredMixin, UpdateView):

    model = User
    template_name = "blogUser/user_form.html"
    fields = ["username", "email", "first_name", "last_name"]

    def get_success_url(self):
      return reverse_lazy("blogUser_profile", kwargs={"pk": self.request.user.id})