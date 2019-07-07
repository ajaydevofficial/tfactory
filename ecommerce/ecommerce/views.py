from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.template.loader import get_template
from django.template import Context, Template,RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,authenticate,login,logout
from user.models import user_details
import datetime
import hashlib
from random import randint
from paywix.payu import PAYU
from payu.gateway import get_hash
from uuid import uuid4

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


def web_order_page(request):
    context={}
    return render(request,"weborder.html",context)

def terms_page(request):
    context={}
    return render(request,"terms_conditions.html",context)

def success_page(request):
    context={}
    return render(request,"success.html",context)

def failure_page(request):
    context={}
    return render(request,"failure.html",context)

def account_page(request):
    user_phone = user_details.objects.get(username = request.user.username).phone
    context={'valid':False,'invalid':False,'user_phone':user_phone,'user_email':request.user.email,'user_first_name':request.user.first_name,'user_last_name':request.user.last_name}
    if request.user.is_authenticated:
        try:
            if request.method =='POST':
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                phone = request.POST['phone']
                email = request.POST['email']
                try:
                    user_details.objects.update(first_name=first_name,last_name=last_name,phone=phone,email=email)
                    user_object = User.objects.filter(username= request.user.username)
                    user_object.update(first_name=first_name,last_name=last_name,email=email)
                    context = {'valid':True,'user_phone':phone,'user_email':email,'user_first_name':first_name,'user_last_name':last_name}
                    return render(request,"account.html",context)
                except Exception as ex:
                    context = {'invalid':True,'user_phone':user_phone,'user_email':request.user.email,'user_first_name':request.user.first_name,'user_last_name':request.user.last_name}
                    return render(request,"account.html",context)
                    print(ex)
        except Exception as ex:
            print(ex)

        return render(request,"account.html",context)
    else:
        return redirect(login_page)

def kurta_store_page(request):
    context={}
    #payu = PAYU()
    #hash_object = hashlib.sha256(b'randint(0,20)')
    #txnid = hash_object.hexdigest()[0:20]
    #payment_data = {}
    posted = {}
    MERCHANT_KEY = 'E9jUqX8v'
    key = 'E9jUqX8v'
    SALT = 'vLnHGFL0jo'
    action = "https://sandboxsecure.payu.in/_payment"
    S_URL = 'http://127.0.0.1:8000/success/'
    F_URL = 'http://127.0.0.1:8000/failure/'
    if request.method=='POST':
    	for i in request.POST:
    		posted[i]=request.POST[i]

    	hash_object = hashlib.sha256(b'randint(0,20)')
    	txnid = hash_object.hexdigest()[0:20]
    	hashh = ''
    	posted['txnid']=txnid
    	hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
    	posted['key']= key
    	posted['productinfo'] = 'kurta'
    	hash_string=''
    	posted['surl'] = S_URL
    	posted['furl'] = F_URL
    	hashVarsSeq=hashSequence.split('|')
    	for i in hashVarsSeq:
    		try:
    			hash_string+=str(posted[i])
    		except Exception:
    			hash_string+=''
    		hash_string+='|'
    	hash_string+=SALT
    	hashh= hashlib.sha512(hash_string.encode('utf-8')).hexdigest().lower()
    	print(hash_string)
    	print(posted)
    	request.session['context'] = {'posted':posted,'action':action,"hashh":hashh,"MERCHANT_KEY":MERCHANT_KEY,"txnid":txnid,"hash_string":hash_string,}
    	print(context)
    	return redirect(kurta_checkout_page)
    return render(request,"kurtastore.html",context)

def logout_page(request):
    logout(request)
    return redirect(home_page)

def kurta_checkout_page(request):

    if request.session['context'] == None:
        context={}
    else:
        context = request.session['context']
        print(context)
    return render(request,'kurta_checkout_page.html',context)


#payment_data = {
#		'txnid': txnid,
#		'amount': request.POST['ordertotal'],
#		'firstname': request.POST['firstname'] ,
#		'email': request.POST['email'],
#		'phone': request.POST['phone'],
#		'productinfo': 'kurta',
#		'address1': request.POST['address1'],
#		'address2': request.POST['address2'],
#		'city': request.POST['city'],
#		'state': request.POST['state'],
#		'zipcode': request.POST['pincode'],
#        'udf1': request.POST['small'],
#		'udf2': request.POST['medium'],
#		'udf3': request.POST['large'],
#		'udf4': request.POST['xlarge'],
#		'udf5': request.POST['xxlarge'],
#        'color': request.POST['color']
#}
#payu_data = payu.initate_transaction(payment_data)
#payu_data['action'] = 'https://test.payu.in/_payment'
#request.session['payu_data'] = payu_data
#return redirect(kurta_checkout_page)
