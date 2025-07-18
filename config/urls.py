from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1',
      description="Read our Blog API's documentation!",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="dewel000per@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("api.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Refresh token
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1MjkxMTk3NiwiaWF0IjoxNzUyODI1NTc2LCJqdGkiOiJiMTkzMGYyYzcxZGM0N2I1OTFjYWFiNmFmMWM4YTcyMiIsInVzZXJfaWQiOjJ9.fSVm8lZtopBkEah5jNZ3X7hH3eoYd5WBBMTuebcvGjU