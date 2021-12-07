from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from accounts.models import CustomUser
from .forms import CustomUserCreationForm



class HomePageView(TemplateView):
    template_name = "index.html"

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
