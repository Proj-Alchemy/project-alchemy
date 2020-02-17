from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from main.api import router as main_router


schema_view = get_schema_view(
    openapi.Info(
        title="Project Alchemy",
        default_version="v1",
        description="",
        terms_of_service="",
        contact=openapi.Contact(email="dev@dev.com"),
        license=openapi.License(name="GPLv3"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    url(r"^", include(main_router.urls)),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    url(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    url(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    url(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    path("admin/", admin.site.urls),
]
