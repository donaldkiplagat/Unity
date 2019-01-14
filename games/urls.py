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
    url(r'^download/(\d+)',views.game_download,name='game_download'),
    url(r'^profile/(?P<username>\w{0,50})',views.profile,name='profile'),

    url(r'^api/countries/$',views.countriesList.as_view()),
    url(r'^api/categories/$',views.categoriesList.as_view()),
    url(r'^api/platforms/$',views.platformsList.as_view()),
    url(r'^api/games/$',views.GamesList.as_view()),
    url(r'^api/profiles/$',views.ProfileList.as_view()),
    url(r'^api/news/$',views.NewsList.as_view()),
    url(r'^api/comments/$',views.CommentList.as_view()),
    url(r'^api/users/$',views.UsersList.as_view()),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
