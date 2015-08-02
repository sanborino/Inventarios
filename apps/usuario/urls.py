from django.conf.urls import include, url
from .views import editar_perfil, perfil

urlpatterns = [
    url(r'^actualizado/$', perfil.as_view()),
    url(r'^perfil/$', editar_perfil),
    # url(r'^user/password/reset/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/user/password/reset/done/'}, name="password_reset"),
    # url(r'^user/password/reset/done/$','django.contrib.auth.views.password_reset_done'),
    # url(r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'post_reset_redirect' : '/user/password/done/'},),
    # url(r'^user/password/done/$', 'django.contrib.auth.views.password_reset_complete'),
    url(r'^password/$', 'django.contrib.auth.views.password_change', {'post_change_redirect' : '/actualizado/','template_name': 'usuarios/password.html'},),
]