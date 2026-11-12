from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializer import BookSerializer


@api_view(['GET'])
def book_list_view(request):
    books = Book.objects.all()

    title = request.query_params.get("title")
    
    if title:
        posts = posts.filter(title__icontains=title)
    

    return Response(BookSerializer(books, many=True).data)


@api_view(['POST'])
def book_create_view(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def book_detail_view(request, id):
    book = get_object_or_404(Book, id=id, owner=request.user)
    return Response(BookSerializer(book).data)


@api_view(['PUT', 'PATCH'])
def book_update_view(request, id):
    book = get_object_or_404(Book, id=id, owner=request.user)
    serializer = BookSerializer(book, data=request.data, partial=request.method == 'PATCH')
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def book_delete_view(request, id):
    book = get_object_or_404(Book, id=id, owner=request.user)
    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
