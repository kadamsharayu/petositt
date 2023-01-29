from django.shortcuts import render,HttpResponse,HttpResponseRedirect,reverse,get_object_or_404

# Razorpay Imports
from razorpay import Client
# Models Import
from .models import Pets,PetWalking,PetBoarding,PetGrooming
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def pet_grooming(request):
    if request.method == "POST":
        name = request.POST.get('pet_name')
        age = request.POST.get('pet_age')
        breed_name = request.POST.get('breed_name')
        weight = request.POST.get('weight')
        type = request.POST.get('pet_type')
        service = request.POST.get('service')
        get_user = get_object_or_404(User,pk=request.user.pk)
        new_pet = Pets(user=get_user,pet_type=type,pet_age=age,pet_name=name,breed_name=breed_name,pet_weight=weight)
        new_pet.save()
        new_pet_groom = PetGrooming(pet_detail=new_pet,pet_service_type=service)
        new_pet_groom.save()
        return HttpResponse("Saved!!!!")
    return render(request,'pet_detail.html')

def pet_boarding(request):
    if request.method == "POST":
        name = request.POST.get('pet_name')
        age = request.POST.get('pet_age')
        breed_name = request.POST.get('breed_name')
        weight = request.POST.get('weight')
        type = request.POST.get('pet_type')
        time = request.POST.get('time')
        meal = request.POST.get('meal')
        special_care = request.POST.get('special_care')
        get_user = get_object_or_404(User, pk=request.user.pk)
        new_pet = Pets(user=get_user, pet_type=type, pet_age=age, pet_name=name, breed_name=breed_name,
                       pet_weight=weight)
        new_pet.save()
        new_boarding = PetBoarding(pet_detail=new_pet,time=time,meal=meal,special_care=special_care)
        new_boarding.save()

        return HttpResponse("Saved!!!!!!")
    return render(request,'pet_boarding.html')

@csrf_exempt
def pet_walking(request):
    if request.method == "POST":
        name = request.POST.get('pet_name')
        age = request.POST.get('pet_age')
        breed_name = request.POST.get('breed_name')
        weight = request.POST.get('weight')
        type = request.POST.get('pet_type')
        get_user = get_object_or_404(User, pk=request.user.pk)
        new_pet = Pets(user=get_user, pet_type=type, pet_age=age, pet_name=name, breed_name=breed_name,
                       pet_weight=weight)
        new_pet.save()
        walking_obj = PetWalking(user=get_user,pet_detail=new_pet)
        walking_obj.save()

        return HttpResponse("Saved!!!!!!")
    razorpay_order_id = Client(auth=('rzp_test_5oavlxNIw3XN70','3CYNikEOYjwXPlcHdAdIj4iV'))
    razorpay_order_id = razorpay_order_id.order.create({'amount':'1000','currency':'INR','payment_capture':'1'})
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = 'rzp_test_5oavlxNIw3XN70'
    context['razorpay_amount'] = '5000'
    context['currency'] = 'INR'

    return render(request, 'pet_walking.html')

def home(request):
    razorpay_order_id = Client(auth=('rzp_test_5oavlxNIw3XN70', '3CYNikEOYjwXPlcHdAdIj4iV'))
    razorpay_order_id = razorpay_order_id.order.create({'amount': '1000', 'currency': 'INR', 'payment_capture': '1'})
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = 'rzp_test_5oavlxNIw3XN70'
    context['razorpay_amount'] = '5000'
    context['currency'] = 'INR'

    return render(request,'index.html',context=context)

def gallery(request):
    razorpay_order_id = Client(auth=('rzp_test_5oavlxNIw3XN70', '3CYNikEOYjwXPlcHdAdIj4iV'))
    razorpay_order_id = razorpay_order_id.order.create({'amount': '1000', 'currency': 'INR', 'payment_capture': '1'})
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = 'rzp_test_5oavlxNIw3XN70'
    context['razorpay_amount'] = '5000'
    context['currency'] = 'INR'
    return render(request,'Gallery.html',context=context)

def aboutus(request):
    razorpay_order_id = Client(auth=('rzp_test_5oavlxNIw3XN70', '3CYNikEOYjwXPlcHdAdIj4iV'))
    razorpay_order_id = razorpay_order_id.order.create({'amount': '1000', 'currency': 'INR', 'payment_capture': '1'})
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = 'rzp_test_5oavlxNIw3XN70'
    context['razorpay_amount'] = '5000'
    context['currency'] = 'INR'
    return render(request,'ABOUT US.html',context=context)

def faqs(request):
    razorpay_order_id = Client(auth=('rzp_test_5oavlxNIw3XN70', '3CYNikEOYjwXPlcHdAdIj4iV'))
    razorpay_order_id = razorpay_order_id.order.create({'amount': '1000', 'currency': 'INR', 'payment_capture': '1'})
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = 'rzp_test_5oavlxNIw3XN70'
    context['razorpay_amount'] = '5000'
    context['currency'] = 'INR'
    return render(request,'FAQs.html',context=context)

def services(request):
    razorpay_order_id = Client(auth=('rzp_test_5oavlxNIw3XN70', '3CYNikEOYjwXPlcHdAdIj4iV'))
    razorpay_order_id = razorpay_order_id.order.create({'amount': '50000', 'currency': 'INR', 'payment_capture': '1'})
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = 'rzp_test_5oavlxNIw3XN70'
    context['razorpay_amount'] = '5000'
    context['currency'] = 'INR'
    return render(request,'Services.html',context=context)

