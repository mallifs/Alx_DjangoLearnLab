from django.urls import path
from .views import BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'book', BookViewSet)


urlpatterns =[
    
    path('', BookViewSet.as_view('Book'), name = 'book_list',)
]