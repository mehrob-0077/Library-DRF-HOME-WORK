from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','title','author','year','price','owner','created_at')
        read_only_fields = ('id','owner','created_at')

