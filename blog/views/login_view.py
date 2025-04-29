from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.shortcuts import render

from ..forms.login_form import LoginForm


class LoginFormView(FormView):
    template_name = "blog/login.html"
    form_class = LoginForm
    success_url = "/"
    

    def form_valid(self, form):
        user = authenticate(
            request=self.request, 
            username=self.request.POST['username'], 
            password=self.request.POST['password']
        )

        if user:
            login(self.request, user=user)
            return super().form_valid(form)
        
        else:
            form.add_error(None, "Incorrect user or password")
            return self.form_invalid(form)
        
    def form_invalid(self, form):
        # return render(self.request, "blog/login.html", context={"form": form})
        return self.render_to_response(self.get_context_data(form=form))
    



