from django.contrib import admin
from django.urls import path
from . import views
app_name = 'books'

urlpatterns = [
    #path('',views.index,name = 'index'),
    #path('<int:book_id>' + '/',views.detail,name = 'detail')
    path('',views.Indexview.as_view(),name = 'index'),
    path('<int:pk>' + '/',views.Detailview.as_view(),name = 'detail'),
    path('books/add/',views.bookcreate.as_view(), name='book_add'),
]
