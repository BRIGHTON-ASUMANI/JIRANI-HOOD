from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^login/',views.login_user, name='login'),
    url('logout/',views.logout_user, name='logout'),
    url('register/',views.register_user, name='register'),
    url('edit_profile/',views.edit_profile, name='edit_profile'),
    url('edit/',views.edit, name='edit'),
    url('change_password/',views.change_password, name='change_password'),
    url(r'^post/$', views.new_project, name='new_project'),
    url(r'^comments/(\d+)', views.comment, name='comments'),
    url( r'^profile/$' , views.profile , name='profile' ),
    url( r'pro/(?P<pk>[0-9]+)/$' , views.dump, name='dump' ),
    url( r'project/(?P<pk>[0-9]+)/$' , views.AlbumUpdate.as_view( ) , name='album-update' ) ,
    url( r'prof/(?P<pk>[0-9]+)/$' , views.ProfileUpdate.as_view( ) , name='profile-update' ) ,
    url( r'project/(?P<pk>[0-9]+)/delete/$' , views.AlbumDelete.as_view( ) , name='album-delete' ) ,
    url( r'profile/(?P<pk>[0-9]+)/delete/$' , views.ProfileDelete.as_view( ) , name='profile-delete' ) ,
    url( r'^create/$' , views.create , name='create' ),
    url(r'^search/$',views.search , name='search'),
    # url(r'^rates/(\d+)$', views.rates, name='rates'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
