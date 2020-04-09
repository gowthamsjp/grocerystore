from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
# from .forms import UserRegisterForm
from .models import User, Product, ProductImage
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import Http404

# def home(request):
#     return render(request, 'html/home.html', {'title': 'Home Page'})
#  main page 
#  @login_required
def homeMain(request):
    product = Product.objects.all()
    context = {'product': product,
               'title': 'Home Page'}
    template = 'html/homeMain.html'
    return render(request, template, context)

def search(request): 
    try:
        search = request.GET.get('search')
    except: 
        search = None
    if search: 
        product = Product.objects.filter(title__icontains = search)
        context = {'query': search, 'product': product}
        template = 'html/search.html'
    else: 
        context = {}
        template = 'html/homeMain.html'
    return render(request, template, context)

@login_required
def about(request):
    # u = User.objects.get(username=request.user.username)

    return render(request, 'html/about.html', {'title': 'About'})

#  sign in function
def signin(request):
    request.session.set_expiry(120000)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('about')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('signin')
    else:
        return render(request, 'html/signin.html', {'title': 'Sign in'})


# Logout function
# should set name function is different than logout unless the recusion problem happens.
def logout_views(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('homeMain')


# register function
def register(request):
    request.session.set_expiry(120000)
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                password=password, email=email)
                user.save()
                messages.success(request, f'Account created {user.username}!')
                return redirect('signin')
        else:
            messages.error(request, 'Does not match password')
    # else:
    #     form = UserCreationForm()
    return render(request, 'html/register.html')

# for a specific product
# @login_required
def UniqueProduct(request,slug):
    try:
        product = Product.objects.get(slug=slug)
        # print(products.title)
        # images = ProductImage.productimage_set.all()
        images = ProductImage.objects.filter(product=product)
        context = {'product': product,'images': images, 
                   'title': 'Home Page'}
        template = 'html/product.html'
        return render(request, template, context) 
    except product.DoesNotExist:
        raise Http404("Does not exist")