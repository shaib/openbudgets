from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from openbudget.commons.views import OBudgetSitemap, OBudgetSearchView
admin.autodiscover()


sitemaps = {
    'site': OBudgetSitemap,
}


urlpatterns = patterns('',
    url(r'^admin/',
        include(admin.site.urls)
    ),
    url(r'^accounts/',
        include('openbudget.apps.accounts.urls.ui')
    ),
    url(r'^entities/',
        include('openbudget.apps.entities.urls.ui')
    ),
    url(r'^sheets/',
        include('openbudget.apps.sheets.urls.ui')
    ),
    url(r'^interactions/',
        include('openbudget.apps.interactions.urls')
    ),
    url(r'^tools/',
        include('openbudget.apps.projects.urls.ui'),
    ),
    url(r'^taxonomies/',
        include('openbudget.apps.taxonomies.urls')
    ),
    url(r'^transport/',
        include('openbudget.apps.transport.urls')
    ),
    url(r'^sources/',
        include('openbudget.apps.sources.urls')
    ),
    url(r'^search/',
        OBudgetSearchView(),
        name='search'
    ),
    url(r'^comments/',
        include('django.contrib.comments.urls')
    ),
    url(r'^robots\.txt',
        TemplateView.as_view(template_name='robots.txt')
    ),
    url(r'^sitemap\.xml$',
        'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}
    ),
    url(r'^grappelli/',
        include('grappelli.urls')
    ),
    url(r'^social_auth/', 
        include('social_auth.urls')
    ),
    url(r'^',
        include('openbudget.apps.pages.urls')
    ),
)
