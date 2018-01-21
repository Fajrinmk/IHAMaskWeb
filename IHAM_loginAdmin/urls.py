from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import *
urlpatterns = [
    url(r'^$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^adminIHA/', logged_in, name = 'logged_in'),
    url(r'^add_promo_code/', add_promo_code, name = 'add_promo_code'),
    url(r'^delete_code/(?P<code_id>[0-9]+)/$', delete_code, name='delete_code'),
    url(r'^paidSlideTrue/(?P<paidTrue_id>[0-9]+)/$', paidSlideTrue, name='paidSlideTrue'),
    url(r'^paidSlideFalse/(?P<paidFalse_id>[0-9]+)/$', paidSlideFalse, name='paidSlideFalse'),
    url(r'^deliveredSlideFalse/(?P<deliveredFalse_id>[0-9]+)/$', deliveredSlideFalse, name='deliveredSlideFalse'),
    url(r'^deliveredSlideTrue/(?P<deliveredTrue_id>[0-9]+)/$', deliveredSlideTrue, name='deliveredSlideTrue'),
]