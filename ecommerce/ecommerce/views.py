from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,authenticate,login,logout

def login_page(request):
    context = {"invalid":False}
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if not request.POST.get('remember_me', None):
            request.session.set_expiry(0)
        if not user==None:
            login(request,user)
            return redirect(home_page)
        else:
            print("Login Failed")
            return render(request,"login.html",{"invalid":True})
    return render(request,"login.html",context)

def home_page(request):
    context={}
    return render(request,"index.html",context)

def register_page(request):
    context={}
    return render(request,"signup.html",context)

def soon_page(request):
    context={}
    return render(request,"soon.html",context)

def talent_page(request):
    context={}
    return render(request,"talent.html",context)


def technical_page(request):
    context={}
    return render(request,"technical.html",context)

def clothes_page(request):
    context={}
    return render(request,"clothes.html",context)

def design_order_page(request):
    context={}
    return render(request,"designorder.html",context)

def privacy_page(request):
    context={}
    return render(request,"privacy.html",context)

def return_page(request):
    context={}
    return render(request,"return.html",context)

def project_order_page(request):
    context={}
    return render(request,"projectorder.html",context)

def portrait_order_page(request):
    context={}
    return render(request,"portraitorder.html",context)

def kurta_store_page(request):
    context={}
    return render(request,"kurtastore.html",context)

def web_order_page(request):
    context={}
    return render(request,"weborder.html",context)

def terms_page(request):
    context={}
    return render(request,"terms_conditions.html",context)

def account_page(request):
    context={}
    return render(request,"account.html",context)
