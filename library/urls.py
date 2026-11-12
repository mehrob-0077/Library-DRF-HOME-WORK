from django.urls import path
from .views import book_detail_view,book_create_view,book_list_view,book_update_view,book_delete_view

urlpatterns = [
    path('list/',book_list_view,name="list"),
    path('create/',book_create_view,name='create'),
    path('detail/<int:id>/',book_detail_view,name='details'),
    path('update/<int:id>/',book_update_view,name='update'),
    path('delete/<int:id>/',book_delete_view,name='delete')
]


