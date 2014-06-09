from django.conf.urls import url, patterns
from django.views.generic import TemplateView

urlpatterns = patterns('',
                       url(r'^$', 'demo.views.main', name='main'),
                       url(r'^results', 'demo.views.get_results', name='results'),
)