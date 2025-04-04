from django.urls import path
from .views import BookList, BookCreate,  BookUpdate#, BookListCreate, BookRetrieveDestroy, BookDelete

urlpatterns = [
    path('', BookList.as_view(), name='book_list'),
    path('create/', BookCreate.as_view(), name='create_book'),
    # path('delete/<int:pk>/', BookDelete.as_view(), name='delete_book'),
    path('update/<int:pk>/', BookUpdate.as_view(), name='update_book'),
    # path('lstcrt/', BookListCreate.as_view()),
    # path('dstdltupt/<int:pk>/', BookRetrieveDestroy.as_view()),
]




# from .views import BookViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'books', BookViewSet, basename='book')
# urlpatterns = router.urls