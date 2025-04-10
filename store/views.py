from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Book
from django.views.decorators.http import require_POST
from django.shortcuts import render
from .models import Book

# def cart_view(request):
#     cart = request.session.get('cart', [])
#     books_in_cart = Book.objects.filter(id__in=cart)
#     return render(request, 'store/cart.html', {'cart_books': books_in_cart})

@login_required
def cart_view(request):
    cart = request.session.get('cart', [])
    print("Cart content in session:", cart)  # 🔍 Debug
    books = Book.objects.filter(id__in=cart)
    print("Books fetched for cart:", books)  # 🔍 Debug
    return render(request, 'store/cart.html', {'books': books})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('book_list')
        else:
            return render(request, 'store/login.html', {'error': 'Invalid credentials'})
    return render(request, 'store/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'store/book_list.html', {'books': books})

# @login_required
# @require_POST
# def add_to_cart(request, book_id):
#     cart = request.session.get('cart', [])
#     if book_id not in cart:
#         cart.append(book_id)
#     request.session['cart'] = cart
#     return redirect('cart')

@login_required
@require_POST
def add_to_cart(request, book_id):
    cart = request.session.get('cart', [])
    print("Cart before adding:", cart)  # 🔍 Debug line

    book_id = int(book_id)
    if book_id not in cart:
        cart.append(book_id)
        print(f"Added book ID {book_id} to cart.")  # 🔍 Debug line
    else:
        print(f"Book ID {book_id} already in cart.")  # 🔍 Debug line

    request.session['cart'] = cart
    print("Cart after adding:", request.session['cart'])  # 🔍 Debug line

    return redirect('cart')
