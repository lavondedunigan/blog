from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserRegisterForm
from django.urls import reverse_lazy
from django.views import View


class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})
    
    def post(self, request):
        form = UserRegisterForm(request.POST)

class Index(View):
    def get(self, request):
        return render(request, 'blog/index.html')

class HomePageView(TemplateView):
    template_name = "pages/home.html"
    
class AboutPageView(TemplateView):
    template_name = "pages/about.html" 
    

class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")