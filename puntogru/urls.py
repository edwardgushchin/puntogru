from django.conf.urls import url
from puntogru_kernel import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', views.MainPageView.as_view()),
    url(r'^portfolio/(?P<id>\w+)/$', views.PortfolioIdPageView.as_view()),
    url(r'^portfolio/$', views.PortfolioPageView.as_view()),
    url(r'^services/$', views.ServicesPageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^submit/$', views.SubmitPageView.as_view()),
    url(r'^email/$', views.EmailSend),
    url(r'^admin/', admin.site.urls),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico')),
]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)