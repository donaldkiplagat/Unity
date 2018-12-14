from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^games',views.games, name='games'),
    url(r'^trailers',views.trailers, name='trailers'),
    url(r'^news',views.news, name='news'),
    url(r'^view/article/(\d+)',views.article,name='article'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
