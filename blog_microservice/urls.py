from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.contrib.auth import views

schema_view = get_schema_view(
    openapi.Info(
        title="Blog Microapi",
        default_version='v1',
        description="A Web API for creating and editing blog posts"
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', include('blog.urls')),
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('schema/', schema_view),
    #path('', schema_view),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)