from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.shortcuts import render

from ..forms.register_form import RegisterForm
from ..repository.user_repository import create_new_user, filter_by


class RegisterFormView(FormView):
    template_name = "blog/register.html"
    form_class = RegisterForm
    success_url = "/"
    

    
    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        
        create_new_user(username=username, email=email, password=form.cleaned_data.get("password"))
        
        return super().form_valid(form)
    

    def form_invalid(self, form):
        return render(self.request, "blog/register.html", {"form": form})
    
            
        






