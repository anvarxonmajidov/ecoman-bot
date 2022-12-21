from django.shortcuts import render
from django.http.response import JsonResponse
import json
from .models import Foydalanuvchi, Post,get_ecoin

def first_api(request):
    return JsonResponse({"status":request.META['REMOTE_ADDR']})

def create_user(request):
    if request.method=="POST":
        data=json.loads(request.body)
        user=Foydalanuvchi.objects.get_or_create(telegram_id=data['telegram_id'])
    return JsonResponse({"holati":"no" if user[1] else "yes","qadam":user[0].res_step})

def set_phone(request,id):
    if request.method=="POST":
        data=json.loads(request.body)
        user=Foydalanuvchi.objects.get(telegram_id=id)
        user.phone=data['phone']
        user.ism=data['ism']
        user.res_step+=1
        user.save()
    return JsonResponse({"qadam":user.res_step})

def get_balans(request,id):
    return JsonResponse({"ecoin":get_ecoin(id)})

def get_posts(request,id):
    foydalanuvchi=Foydalanuvchi.objects.get(telegram_id=id)
    posts=foydalanuvchi.post.all()
    data=[]
    for post in posts:
        data.append({
            'link':post.image,
            'tasdiq':post.tasdiq,
            'date':post.added_date
            })
    return JsonResponse(data,safe=False)

def get_step(request,id):
    user=Foydalanuvchi.objects.get(telegram_id=id)
    return JsonResponse({"qadam":user.res_step})


def increment_step(request,id):
    user=Foydalanuvchi.objects.get(telegram_id=id)
    user.res_step+=1
    if request.method=="POST":
        data=json.loads(request.body)
        print(data['city'])
        user.city=data['city']
    user.save()
    return JsonResponse({"qadam":user.res_step})

def get_add(request,id):
    user=Foydalanuvchi.objects.get(telegram_id=id)
    return JsonResponse({"qadam":user.res_step})

def increment_add(request,id):
    user=Foydalanuvchi.objects.get(telegram_id=id)
    user.add+=1
    user.save()
    return JsonResponse({"qadam":user.res_step})

def decrement_add(request,id):
    # TODO image url

    user=Foydalanuvchi.objects.get(telegram_id=id)
    if request.method=="POST":
        data=json.loads(request.body)
        post=Post.objects.create(foydalanuvchi=user,image=data['image'])
    user.add-=1
    user.save()
    return JsonResponse({"qadam":user.res_step})

