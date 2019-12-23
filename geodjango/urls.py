from django.contrib.gis import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import TemplateView
from django.views import defaults as default_views

#корневые пути всего проекта
urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path(
        "users/",
        include("users.urls", namespace="users"),
    ),
    #path('users/', admin.site.urls),
    #path('profiles/', admin.site.urls),
    #path('gp_projects/', admin.site.urls),
]


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
