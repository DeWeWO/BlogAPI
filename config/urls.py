from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("api.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Refresh token
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1MjkxMTk3NiwiaWF0IjoxNzUyODI1NTc2LCJqdGkiOiJiMTkzMGYyYzcxZGM0N2I1OTFjYWFiNmFmMWM4YTcyMiIsInVzZXJfaWQiOjJ9.fSVm8lZtopBkEah5jNZ3X7hH3eoYd5WBBMTuebcvGjU