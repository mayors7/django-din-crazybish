from django.urls import path ,include
from .views import SignUpView
urlpatterns = [
    path('', include('api.urls')),
    path("signup/", SignUpView.as_view(), name="signup"),
]
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="News API",
        default_version='v1',
        description="API документация для News App",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]