from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,authenticate,login,logout
from user.models import user_details
User = get_user_model()

def login_page(request):
    context = {"invalid":False}
    if request.user.is_authenticated:
        return redirect(home_page)
    else:
        if request.method =='POST':
            email = request.POST['email']
            password = request.POST['password']
            try:
                username = User.objects.get(email=email).username
            except:
                return render(request,"login.html",{"invalid":True})
            user = authenticate(username=username,password=password)
            if not user==None:
                login(request,user)
                return redirect(home_page)
            else:
                return render(request,"login.html",{"invalid":True})
        return render(request,"login.html",context)

def home_page(request):
    context={}
    return render(request,"index.html",context)

def register_page(request):
    context={'username_taken':False,'email_exist':False,'phone_exist':False}
    if request.user.is_authenticated:
        return redirect(home_page)
    else:
        if request.method =='POST':
            username = request.POST['username']
            password = request.POST['password']
            first_name = request.POST['fname']
            last_name = request.POST['lname']
            phone = request.POST['phone']
            email = request.POST['email']
            dob = request.POST['dob']
            try:
                user_exist = User.objects.filter(username=username)
                phone_exist = user_details.objects.filter(phone=phone)
                email_exist = user_details.objects.filter(email=email)
                if user_exist:
                    return render(request,"signup.html",{'username_taken':True,'email_exist':False,'phone_exist':False})
                elif email_exist:
                    return render(request,"signup.html",{'username_taken':False,'email_exist':True,'phone_exist':False})
                elif phone_exist:
                    return render(request,"signup.html",{'username_taken':False,'email_exist':False,'phone_exist':True})
            except:
                pass

            try:
                new_user = User.objects.create_user(username,email,password)
                new_user.first_name = first_name
                new_user.last_name = last_name
                new_user.save()
                user_details.objects.create(username=username,first_name=first_name,last_name=last_name,phone=phone,email=email,dob=dob)
                return redirect(login_page)
            except Exception as ex:
                print(ex)
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
    if request.user.is_authenticated:
        try:
            user_phone = user_details.objects.get(username = request.user.username).phone
            context = {'user_phone':user_phone}
            print(context)
        except Exception as ex:
            print(ex)

        return render(request,"account.html",context)
    else:
        return redirect(login_page)

def logout_page(request):
    logout(request)
    return redirect(home_page)
