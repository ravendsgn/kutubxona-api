from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from.models import Books
from .serializers import BookSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

# 1. Register API
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 2. Profile API (foydalanuvchi ma'lumotlarini ko‘rish)
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'username': user.username,
            'email': user.email
        })

# 3. Profile update (foydalanuvchi ma'lumotlarini yangilash)
class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        serializer = ProfileUpdateSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Profile updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 4. Profile delete (foydalanuvchini o‘chirish)
class ProfileDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        user.delete()
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

# 5. Logout API (token invalidate qilish)
class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

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
    








