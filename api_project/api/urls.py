from api.urls import path
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include("api.urls")),
    path('admin/', admin.site.urls)
  
]

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns = [
    path('books/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]