#! coding: utf-8

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from puntogru_kernel import models 
from puntogru_kernel import forms 
from django.conf import settings
from datetime import datetime
import simplejson as json
from django.core.mail import send_mail
from django.http import HttpResponse, Http404

class MainTemplate(TemplateView):
	template_name = 'main_template.html'

	def get_context_data(self, **kwards):
		context = super(MainTemplate, self).get_context_data(**kwards)
		return context

class MainPageView(MainTemplate):
	template_name = 'main_page.html'

	def get_context_data(self, **kwards):
		context = super(MainPageView, self).get_context_data(**kwards)
		context['title'] = "Puntog.ru - Студия дизайна интерьеров"
		context['current'] = 1
		context['header_title'] = "P U N T O G"
		context['header_descript'] = "Студия дизайна интерьеров"
		context['settings'] = models.Settings.objects.filter(active=True).last()
		return context

class PortfolioPageView(MainTemplate):
	template_name = 'portfolio_page.html'

	def get_context_data(self, **kwards):
		context = super(PortfolioPageView, self).get_context_data(**kwards)
		context['title'] = "Puntog.ru - Наши работы"
		context['current'] = 2
		context['header_title'] = "Наши работы"
		context['header_descript'] = "Студия дизайна интерьеров Puntog"
		context['settings'] = models.Settings.objects.filter(active=True).last()
		context['works'] = models.Portfolio.objects.all()
		return context

class PortfolioIdPageView(MainTemplate):
	template_name = 'portfolio_id_page.html'

	def get_context_data(self, **kwards):
		context = super(PortfolioIdPageView, self).get_context_data(**kwards)
		id=self.kwargs['id']
		portfolio = models.Portfolio.objects.get(id=id)
		context['title'] = "Puntog.ru - " + portfolio.title
		context['header_title'] = "Наши работы"
		context['current'] = 2
		context['header_descript'] = portfolio.title
		context['settings'] = models.Settings.objects.filter(active=True).last()
		portfolio = models.Portfolio.objects.get(id=id)
		photo_list = portfolio.photo_list()
		context['photo_list'] = photo_list
		return context

class ServicesPageView(MainTemplate):
	template_name = 'services_page.html'

	def get_context_data(self, **kwards):
		context = super(ServicesPageView, self).get_context_data(**kwards)
		context['title'] = "Puntog.ru - Наши услуги"
		context['current'] = 3
		context['header_title'] = "Наши услуги"
		context['header_descript'] = "Студия дизайна интерьеров Puntog"
		context['settings'] = models.Settings.objects.filter(active=True).last()
		context['services'] = models.Services.objects.all()
		return context

class AboutPageView(MainTemplate):
	template_name = 'about_page.html'

	def get_context_data(self, **kwards):
		context = super(AboutPageView, self).get_context_data(**kwards)
		settings = models.Settings.objects.filter(active=True).last()
		context['title'] = "Puntog.ru - О нас"
		context['current'] = 4
		context['header_title'] = "О нас"
		context['header_descript'] = "Студия дизайна интерьеров Puntog"
		context['settings'] = settings
		context['year'] = datetime.now().year - settings.year_of_foundation
		context['projects'] = len(models.Portfolio.objects.all())
		context['reviews'] = models.Reviews.objects.all()
		context['howworks'] = models.HowWeWork.objects.all()
		return context

class SubmitPageView(MainTemplate):
	template_name = 'submit_page.html'

	def get_context_data(self, **kwards):
		context = super(SubmitPageView, self).get_context_data(**kwards)
		context['title'] = "Puntog.ru - Оставьте заявку"
		context['current'] = 5
		context['header_title'] = "Свяжитесь с нами"
		context['header_descript'] = "Дизайн вашей мечты начинается прямо сейчас"
		context['settings'] = models.Settings.objects.filter(active=True).last()
		return context

def EmailSend(request):
	form = forms.ContactForm(request.POST)
	if form.is_valid():
		name = form.cleaned_data['name']
		email = form.cleaned_data['email']
		phone = form.cleaned_data['phone']
		text = form.cleaned_data['text']

		message = text + '\n\r' + u'Email: ' + email + u' Phone: ' + phone
		send_mail(name, message, 'apps@puntog.ru', ['info@puntog.ru'], fail_silently=False)

		return HttpResponse(json.dumps({'result': 'success'}))
	else:
		raise Http404