"""axi-blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include # url
from blog.views import (
    blog_post_create_view,
)
from . import views

#login-logout
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views


from searches.views import search_view
from .views import (
    home_page,

    contact_page,

    not_logged_in,
    login_view,
    logout_view,
    bokeh_view,
)


urlpatterns = [
    path('', home_page),

    path('blog-new/', blog_post_create_view),
    path('blog/', include('blog.urls')),
    path('search/', search_view),
    # re_path(r'^blog/(?P<slug>\w+)/$', blog_post_detail_view),



    path('contact/', contact_page),
    path('admin/', admin.site.urls),

    path('tasks/', include('tasks.urls')),

    path('register/', views.UserFormView.as_view(), name='register'),
    path('not_logged_in/', not_logged_in),
    path('login/', login_view),
    #path('logout/', auth_views.LogoutView.as_view(template_name='logout_template.html')),
    path('logout/', auth_views.LogoutView.as_view(next_page=home_page)),
    #path("logout/", auth_views.logout, {'next_page': '/'} ,name="logout"),
    #path('logout/', logout_view),

    path('bokeh/', bokeh_view, name='bokeh'),

]

if settings.DEBUG:
    # test mode
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






