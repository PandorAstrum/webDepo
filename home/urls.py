from django.conf.urls import url
from .views import (
    homepage,
    gamesPage,
    portfolioPage,
    blogPage,
    AboutPage,
)


urlpatterns = [
    url(r'^$', homepage),
    url(r'^gamesall/$', gamesPage),
    url(r'^portfolio/$', portfolioPage),
    url(r'^blog/$', blogPage),
    url(r'^about/$', AboutPage),
]