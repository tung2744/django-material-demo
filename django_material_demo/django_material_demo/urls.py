"""django_material_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from cms.polls import views as cms_views
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import include, path
from material.frontend import urls as frontend_urls
from polls.forms import EmailLoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    # Override login page from Frontend
    path('accounts/login/', LoginView.as_view(
        authentication_form=EmailLoginForm),
        name="login"
    ),
    path('', include(frontend_urls)),
    path('polls/', include('polls.urls')),
    path('cms/setting/', cms_views.SettingsView.as_view(), name='settings'),
]
