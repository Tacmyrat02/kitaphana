import random
from django.shortcuts import get_object_or_404, redirect, render
from base.forms import BookForm, CardForm, RecordForm

from base.models import Book, Card, Record

# Create your views here.


def home(request):
    users = Card.objects.all()
    context = {'users': users}
    return render(request, 'index.html', context=context)


def users(request):
    if request.session['auth']:
        users = Card.objects.all()
        context = {'users': users}
        return render(request, 'ulanyjylar.html', context=context)
    return redirect('home')


def books(request):
    if request.session['auth']:
        books = Book.objects.all()
        for book in books:
            setattr(book, 'currentNumber', int(
                book.allNumber) - int(book.recordsBook.count()))
        context = {'books': books}
        return render(request, 'kitaplar.html', context=context)
    return redirect('home')


def records(request):
    if request.session['auth']:
        users = Card.objects.all()
        context = {'users': users}
        return render(request, 'kitapcalar.html', context=context)
    return redirect('home')


def user(request, pk=None):
    if request.session['auth']:
        if not pk:
            pk = request.GET.get('id')
        user_ = get_object_or_404(Card, id=pk)
        context = {'user': user_}
        return render(request, 'user.html', context=context)
    return redirect('home')


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    request.session['auth'] = False
    if username == 'admin' and password == 'admin':
        request.session['auth'] = True
        return redirect('books')
    request.session['auth'] = False
    return render(request, 'login.html')


def book(request, pk):
    if request.session['auth']:
        book_ = get_object_or_404(Book, id=pk)
        context = {'book': book_}
        return render(request, 'book.html', context=context)
    return redirect('home')


def addUserView(request):
    return render(request, 'ulanyjygos.html')


def addBookView(request):
    return render(request, 'kitapgos.html')


def addRecordView(request):
    return render(request, 'kitapcagos.html')


def get_random_id(model):
    while True:
        id = random.randint(1111, 9999)
        try:
            obj = model.objects.get(id=id)
        except:
            return id


def addUser(request):
    temp = request.POST.copy()
    temp['id'] = get_random_id(Card)
    form = CardForm(temp or None)
    print(form.is_valid())
    print(form)
    # print(form)
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        return redirect('users')
    else:
        return redirect('add_user')


def addBook(request):
    temp = request.POST.copy()
    temp['id'] = get_random_id(Book)
    form = BookForm(temp or None, request.FILES or None)
    print(form.is_valid())
    print(form.errors)

    # print(form)
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        return redirect('users')
    else:
        return redirect('add_book')


def addRecord(request):
    try:
        user_ = Card.objects.get(id=request.POST.get('user'))
    except Card.DoesNotExist:
        user_ = None
    try:
        book_ = Book.objects.get(id=request.POST.get('book'))
    except Book.DoesNotExist:
        book_ = None

    data = {'user': user_, 'book': book_}

    form = RecordForm(data)
    print(form.is_valid())
    # print(form)
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        return redirect('users')
    else:
        return redirect('add_record')


def deleteRecord(request, pk):
    obj = Record.objects.get(pk=pk).delete()
    return redirect('records')


def deleteBook(request, pk):
    obj = Book.objects.get(id=pk).delete()
    return redirect('books')


def deleteUser(request, pk):
    obj = Card.objects.get(id=pk).delete()
    return redirect('users')


def about(request):
    return render(request, 'barada.html')
