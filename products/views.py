from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from.models import Books
from .serializers import BookSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class BookList(APIView):
    def get(self, request):
        books = Books.objects.all()
        serializer = BookSerializer(books, many=True)
        rpns = {
            'data': serializer.data,
            'status': status.HTTP_200_OK,
            "message": 'Book List'
        }
        return Response(rpns)


class BookCreate(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            rpns = {
                'data': serializer.data,
                'status': status.HTTP_201_CREATED,
                "message": 'Book Created'
            }
            return Response(rpns)
        else:
            rpns = {
                'data': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST,
                "message": 'Invalid Data'
            }
            return Response(rpns)
    
    
    
class BookUpdate(APIView):
    def put(self, request, pk, *args, **kwargs):
        book = Books.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            rpns = {
                'data': serializer.data,
                'status': status.HTTP_200_OK,
                "message": 'Book Updated'
            }
            
        else:
            rpns = {
                'data': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST,
                "message": 'Invalid Data'
            }
        return Response(rpns)
    
    def patch(self, request, pk, *args, **kwargs):
        book = Books.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            rpns = {
                'data': serializer.data,
                'status': status.HTTP_200_OK,
                "message": 'Book Updated'
            }
            
        else:
            rpns = {
                'data': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST,
                "message": 'Invalid Data'
            }
        return Response(rpns)
    
    
# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = 'pk'

# class BookList(ListAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer


# class BookCreate(CreateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer


# class BookDelete(DestroyAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = 'pk'


# class BookUpdate(UpdateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = 'pk'


# class BookListCreate(ListCreateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer
    
    
# class BookRetrieveDestroy(RetrieveUpdateDestroyAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = 'pk'
    








