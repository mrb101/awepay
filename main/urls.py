"""app URL Configuration

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
from django.conf.urls import url

from .views import (
    Home,
    Services,
    Merchant,
    DebitCard,
    Partner,
    About,
    News,
    Contact
)

urlpatterns = [
    url(r'^services/$', Services.as_view(), name="services"),
    url(r'^merchant/$', Merchant.as_view(), name="merchant"),
    url(r'^debit/$', DebitCard.as_view(), name="debit"),
    url(r'^partner/$', Partner.as_view(), name="partner"),
    url(r'^about/$', About.as_view(), name="about"),
    url(r'^news/$', News.as_view(), name="news"),
    url(r'^contact/$', Contact.as_view(), name="contact"),
    url(r'^', Home.as_view(), name="home"),
]
