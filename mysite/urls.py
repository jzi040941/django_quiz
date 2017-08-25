"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', auth_views.login, name='login'),
    url(r'^admin/', admin.site.urls),
    url(r'^teacher/', include('teacher.urls')),
    url(r'^student/', include('student.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'login_success/$', views.login_success, name='login_success'),
    url(r'logoutuser/$', views.logoutuser, name='logoutuser'),
    url(r'^logout', auth_views.logout, {'next_page': settings.LOGOUT_REDIRECT_URL},name='logout'),
    url(r'^thank_you', views.thank_you, name='thank_you'),
    url(r'^back_home', views.back_home, name='back_home')
    #url(r'^management/logout/$', 'django.contrib.auth.views.logout')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
