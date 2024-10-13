from django.urls import path
from base.views import about, addBook, addBookView, addRecord, addRecordView, addUser, addUserView, book, books, deleteBook, deleteRecord, deleteUser, home, login, records, user, users

urlpatterns = [
    path('', home, name='home'),
    path('ulanyjylar', users, name='users'),
    path('books', books, name='books'),
    path('records', records, name='records'),
    path('addUser', addUserView, name='add_user'),
    path('adduserObject', addUser, name='add_user_object'),
    path('addBook', addBookView, name='add_book'),
    path('addBookObject', addBook, name='add_book_object'),
    path('addRecord', addRecordView, name='add_record'),
    path('addRecordObject', addRecord, name='add_record_object'),
    path('user/<int:pk>', user, name='user'),
    path('user', user, name='user'),
    path('book/<int:pk>', book),
    path('delete/<int:pk>', deleteRecord, name='delete_record'),
    path('about', about, name='about'),
    path('deletebook/<int:pk>', deleteBook, name='delete_book'),
    path('deleteuser/<int:pk>', deleteUser, name='delete_user'),
    path('login', login, name='login'),
]
