from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import time
from django.http import HttpResponse





@login_required(login_url='login')
def home(request):
    front_obj= Front.objects.all()
    params={
        "front_obj":front_obj
    }
    return render(request,'index.html',params)

def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password1')
        user1 = authenticate(username = username , password = pass1)
        if user1 is not None:
            login(request,user1)
            messages.success(request, f'Successfully {username} Logged in ')
            return redirect('home')
        else:
            messages.warning(request, f'Login Unsuccessful for {username}')
            return redirect('home')
    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1!= password2:
           messages.warning(request, f'Passwords did not match for {username}') 
           return redirect('register')
        else:
            user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password1)
            user.save()
            print(username,email,password1)
            messages.success(request, f'User created successfully for {username}')
            return render(request,'login.html')
    return render(request,"register.html")

def log(request):
    logout(request)
    messages.success(request , 'User Logout Successful')
    return redirect('home')

def contact(request):
    return render(request,"contact.html")

def t_c(request):
    return render(request,"t_c.html")

def aboutus(request):
    return render(request,"aboutus.html")



def cart(request,id):
    front_obj= Front.objects.get(id = id)
    params={
        "front_obj":front_obj
    }

    return render(request,"cart.html",params)

def buy(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zip=request.POST.get('zip')
        cardName=request.POST.get('cardName')
        cardNum=request.POST.get('cardNum')
        purchase_obj=Purchase.objects.create(name=name, email=email, address=address, city=city, state=state, zip=zip, cardName=cardName, cardNum=cardNum)
        purchase_obj.save()
        return redirect("aboutus")
    
    return render(request,"buy.html")

def product(request):
	product=Product.objects.all()
	context={
		'product':product
	}
	return render(request,"products.html",context)



def rosescart(request):
    return render(request,"rosescart.html")

def somethingcart(request):
    return render(request,"somethingcart.html")

def gepiccart(request):
    return render(request,"gepiccart.html")

def wnmecart(request):
    return render(request,"wnmecart.html")

def rosesbuy(request):
    if request.method=='POST':
        accountname=POST.get('accountname')
        bname=POST.get('bname')
        cvv=POST.get('cvv')
        Branch=POST.get('Branch')
        Email=POST.get('Email')
        buy_obj=Buy.objects.create(accountname=accountname, cvv=cvv, bname=bname, Branch=Branch, Email=Email)
        buy_obj.save()
        return render(request,"index.html")

    response = HttpResponse("Redirecting to the Payment Gateway....")
    # time.sleep(3)
    return render(request,"rosesbuy.html")

# *************************************************************************************************************
# admin site:
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password1')
        user1 = authenticate(username = username , password = pass1)
        if user1 is not None:
            admin = authenticate(username = 'admin', password = '123')
            print(admin)
            if user1 == admin:
                login(request,admin)
                messages.success(request, f'Successfully {username} Logged in ')
                return redirect('admin_homepg')
            else :
                messages.warning(request, f'Login Unsuccessful for Admin :- {username} ')
                return redirect('home')
    return render(request,"admin_login.html")

@login_required(login_url='admin_login')
def admin_homepg(request):
    dm_obj=Front.objects.all()
    params={"dm_obj":dm_obj}
    return render(request,"admin_homepg.html",params)

def delete_book(request,id):
    del_book = Front.objects.get(id = id)
    del_book.delete()
    return redirect("admin_homepg")

def update_book(request,id):
    update_obj = Front.objects.get(id= id)

    if request.method == 'POST':
        n_bookname = request.POST['bookname']
        n_book_price = request.POST['book_price']
        n_book_desc = request.POST['book_desc']
      
        
        update_obj.bookname = n_bookname
        update_obj.book_price = n_book_price
        update_obj.book_desc = n_book_desc
        update_obj.image = update_obj.image
        
        update_obj.save()
        return redirect('admin_homepg')

    upd=Front.objects.get(id = id)
    context = {
        "update_obj":update_obj,
        "upd":upd,
        }

    return render(request,"update_book.html",context)

def user_pg(request):
    book_obj=Purchase.objects.all()
    params={"book_obj":book_obj}
    return render(request,"user_pg.html",params)

def delete_user(request,id):
    del_user = Purchase.objects.get(id = id)
    del_user.delete()
    return redirect("user_pg")

def update_user(request,id):
    update_obj = Purchase.objects.get(id= id)

    if request.method == 'POST':
        n_name = request.POST['name']
        n_email = request.POST['email']
        n_address = request.POST['address']
        n_city = request.POST['city']
        n_state = request.POST['state']
        n_zip = request.POST['zip']
      
        
        update_obj.name = n_name
        update_obj.email = n_email
        update_obj.address = n_address
        update_obj.city = update_obj.city
        update_obj.state = update_obj.state
        update_obj.zip = update_obj.zip
        
        update_obj.save()
        return redirect('user_pg')

    upd=Purchase.objects.get(id = id)
    context = {
        "update_obj":update_obj,
        "upd":upd,
        }
    return render(request,"update_user.html",context)


def add_book(request):
    if request.method == 'POST':
        bookname = request.POST['bookname']
        book_price = request.POST['amount']
        book_desc = request.POST['desc']
        bookimage = request.POST['image']
        if len(book_price)>=1 and len(bookname)>=1:
            add_obj = Front.objects.create(bookname=bookname, book_price=book_price, book_desc=book_desc, bookimage=bookimage)
            add_obj.save()
            return redirect('admin_homepg')
        else:
            return redirect('add_book')

    return render(request,"add_book.html")
