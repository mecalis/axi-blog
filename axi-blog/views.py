from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template

#Loginform importjai
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from .forms import UserFrorm
# Dont Repeat Yourself = DRY

from .forms import ContactForm
from blog.models import BlogPost
from tasks.models import Task3, TaskListModel3


def home_page(request):
    my_title = "Helló, helló!"
    qs = BlogPost.objects.all()[:8]

    form = UserFrorm
    context = {"title": "Üdv itt. Minden tesztelés alatt!", 'blog_list': qs, "form": form}
    if request.user.is_authenticated:

        user = request.user
        tasks = Task3.objects.filter(tasklist__owner=user)[:5]
        context['tasks'] = tasks
    return render(request, "home.html", context)




def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": "Contact us", 
        "form": form
    }
    return render(request, "form.html", context)

class UserFormView(View):
    form_class = UserFrorm
    template_name = 'registration_form.html'

    #kap az ember egy üres formot
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form} )
    #miután megnyomta a gombot
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)

            # adat tisztítás
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                return redirect(home_page)
        return render(request, self.template_name, {'form': form})

def login_view(request):
    print(request)
    #username = request.POST['username']
    #password = request.POST['password']
    username = request.POST.get('username')
    password = request.POST.get('password')
    #print(request)
    user = authenticate(request, username=username, password=password)
    #print(username, password)
    if user is not None:
        login(request, user)
        return redirect(home_page)
    else:
        return render(request, 'not_logged_in.html', {})

def logout_view(request):
    logout(request)
    return redirect(logout_view)

def not_logged_in(request):
    return render(request, 'not_logged_in.html', {})

def bokeh_view(request):
    return render(request, 'bokeh_template.html', {})


