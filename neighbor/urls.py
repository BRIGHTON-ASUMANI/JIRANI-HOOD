from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns=[
    url('^$',views.home,name='home'),
    url('login/',views.login_user, name='login'),
    url('logout/',views.logout_user, name='logout'),
    url('register/',views.register_user, name='register'),
    url('edit_profile/',views.edit_profile, name='edit_profile'),
    url('change_password/',views.change_password, name='change_password'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
