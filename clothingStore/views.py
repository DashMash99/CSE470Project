from django.shortcuts import redirect, render
from django.http import JsonResponse
import json
import datetime
from .models import *
from .utils import cookieCart, cartData, guestOrder
# from .forms import RegistrationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# Create your views here.

# def register(request):
#     if request.user.is_authenticated:
#         return HttpResponse('You are already registered and logged in')
#     else:
#         form = RegistrationForm()
#         if request.method == 'post' or request.method == 'POST':
#             form = RegistrationForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return HttpResponse('You are now registered and can log in')

#     context = {'form': form}
    
#     return render(request, 'clothingStore/register.html', context)

# def Customerlogin(request):
#     if request.user.is_authenticated:
#         return redirect('/dashboard')
#     else:
#         if request.method == 'POST' or request.method == 'post':
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             customer = authenticate(request, username=username, password=password)
#             if customer is not None:
#                 login(request, customer)
#                 return redirect('dashboard')
#             else:
#                 return redirect('/login')

#     return render(request, 'clothingStore/login.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        customer = authenticate(request, username=username, password=password)
        print('User:', customer)

        if customer is not None:
            login(request, customer)
            return redirect('/')
        else:
            return redirect('/dashboard')

    return render(request, 'clothingStore/login_Register.html')

def dashboard(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'clothingStore/dashboard.html', context)

def checkout(request):

    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
         
    return render(request, 'clothingStore/checkout.html', context)



def uploaditem(request):
    return render(request, 'clothingStore/uploadItem.html')

def viewproduct(request):
    return render(request, 'clothingStore/viewProduct.html')

def confirmorder(request):

    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'clothingStore/confirmOrder.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.days = (orderItem.days + 1)
    elif action == 'remove':
        orderItem.days = (orderItem.days - 1)
    
    orderItem.save()

    if orderItem.days <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        
    else:
        customer, order = guestOrder(request, data)


    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        area=data['shipping']['area'],
        zipcode=data['shipping']['zipcode'],
    )

    return JsonResponse('Payment was successful', safe=False)