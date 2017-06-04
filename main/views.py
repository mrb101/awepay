from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'main/home.html'


class Merchant(TemplateView):
    template_name = 'main/merchant.html'


class Services(TemplateView):
    template_name = 'main/services.html'


class DebitCard(TemplateView):
    template_name = 'main/debit.html'


class Partner(TemplateView):
    template_name = 'main/partner.html'


class About(TemplateView):
    template_name = 'main/about.html'


class News(TemplateView):
    template_name = 'main/news.html'


class Contact(TemplateView):
    template_name = 'main/contact.html'
