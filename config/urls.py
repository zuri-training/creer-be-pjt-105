"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt import views as jwt_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Authentication Web Api",
        default_version='v1',
        description="This is the API for Creer",
        terms_of_service="https://mycreer/terms/",
        contact=openapi.Contact(email="bello4aus@gmail.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    # authentication_classes=[JWTAuthentication],
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    # path('api/token', jwt_views.TokenObtainPairView.as_view(),
    #      name='token_obtain_pair'),
    # path('api/token/refresh', jwt_views.TokenRefreshView.as_view(),
    #      name='token_refresh'),
    path('api/qanda/', include('QandAmodel.urls')),
    path('api/social_auth/', include('social_auth.urls')),
    path('docs', include_docs_urls(title="CreerAPI")),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger'),
    path('api/api.json/', schema_view.without_ui(cache_timeout=0),
         name="schema-swagger-ui"),
    path('redoc', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc')
]
