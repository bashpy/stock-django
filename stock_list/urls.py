__author__ = 'jovin'
from django.conf.urls import patterns, include, url
from stock_list import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stock.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

        url(r'^$',views.list),
)