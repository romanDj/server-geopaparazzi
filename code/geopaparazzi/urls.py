from django.contrib.gis import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views import defaults as default_views
from geopaparazzi.api.views import verify_token, user_info, roles, users, admin_role

#корневые пути всего проекта
urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    path('admin/', admin.site.urls),
    path("account/", include("allauth.urls")),
    path(
        "users/",
        include("users.urls", namespace="users"),
    ),
    path('gp_projects/', include('gp_projects.urls')),
    path('profiles/', include('profiles.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    #Api views
    path('api/o/v4/tokeninfo', 
        verify_token, name='tokeninfo'),
    path('api/o/v4/userinfo',
        user_info, name='userinfo'),
    path('api/roles', roles, name='roles'),
    path('api/adminRole', admin_role, name='adminRole'),
    path('api/users', users, name='usersapi'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
