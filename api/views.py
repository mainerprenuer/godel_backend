from .models import Popularmodel,Recommendedmodel,usermodel,cartmodel,favmodel
from .serializers import PopularSerializer,RecommendedSerializer,UserSerializer,cartSerializer,favSerializer
from django.http import HttpResponse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import render
import base64


@csrf_exempt
def popularview(request):
    if request.method == 'GET':
        queryset=Popularmodel.objects.all()[:4]
        serializer=PopularSerializer(queryset,many=True)
        food=serializer.data
        
        for x in food:
         print(x)
         if x == 'peanut':
           continue
         print(x)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PopularSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"response": {"data": "success"}}, status=200)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def popularlistview(request):
    if request.method == 'GET':
        queryset=Popularmodel.objects.all()
        serializer=PopularSerializer(queryset,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PopularSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"response": {"data": "success"}}, status=200)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def recommendedview(request):
    if request.method == 'GET':
        queryset=Recommendedmodel.objects.all()[:4]
        serializer=RecommendedSerializer(queryset,many=True)
        food=serializer.data
        
        for x in food:
         print(x)
         if x == 'banana':
           continue
         print(x)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RecommendedSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"response": {"data": "success"}}, status=200)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def recommendedlistview(request):
    if request.method == 'GET':
        queryset=Recommendedmodel.objects.all()
        serializer=RecommendedSerializer(queryset,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RecommendedSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"response": {"data": "success"}}, status=200)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def addcart(request):
    if request.method == 'GET':
        queryset=cartmodel.objects.all()
        serializer=cartSerializer(queryset,many=True)
        return JsonResponse({"response": {"data": serializer.data,"error":'null'}}, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = cartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"response": {"data": "success"}}, status=200)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def fetchcart(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            queryset=cartmodel.objects.filter(userid=data['userid'])
            serializer=cartSerializer(queryset,many=True)
            if len(serializer.data)==0:
                return JsonResponse({"response": {"data": 'null',"error":'no_items_found'}}, status=400)
            return JsonResponse({"response": {"data": serializer.data,"error":'null'}}, safe=False)
        except:
            return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def deletecart(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            queryset=cartmodel.objects.get(id=data['id'])
        except:
            return JsonResponse({"response": {"data": 'null',"error":'item_not_found'}}, status=400)
        if queryset is None:
            return JsonResponse(serializer.errors, status=400)
        queryset.delete()
        return JsonResponse({"response": {"data": 'success',"error":'null'}}, safe=False)
       
       

# this view is used to create and fetch the user data
@csrf_exempt
def adduser(request):
    if request.method == 'GET':
        queryset=usermodel.objects.all()
        serializer=UserSerializer(queryset,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        queryset=usermodel.objects.filter(username=data['username'])
        checkserializer=UserSerializer(queryset,many=True)
        if len(checkserializer.data)==0:
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"response": {"data": "success","error":"null"}}, status=200)
            return JsonResponse({"response": {"data": "null","error":serializer.errors}}, status=400)
        return JsonResponse({"response": {"data": "null","error":"email_already_exists"}}, status=400)



@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            queryset=usermodel.objects.filter(username=data['username'])
            serializer=UserSerializer(queryset,many=True)
            if len(serializer.data)==0:
                return JsonResponse({"response": {"data": 'null',"error":'user_not_found'}}, status=400)
            if serializer.data[0]['password']==data['password']:
                return JsonResponse({"response": {"data": serializer.data,"error":'null'}}, safe=False)
            return JsonResponse({"response": {"data": 'null',"error":'Wrong_password'}}, status=400)
        except:
            return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def addfav(request):
    if request.method == 'GET':
        queryset=favmodel.objects.all()
        serializer=favSerializer(queryset,many=True)
        return JsonResponse({"response": {"data": serializer.data,"error":'null'}}, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        queryset=usermodel.objects.filter(userid=data['userid'])
        serializer1=UserSerializer(queryset,many=True)
        if len(serializer1.data)==0:
            return JsonResponse({"response": {"data": 'null',"error":'user_not_found'}}, status=400)

        queryset1=favmodel.objects.filter(productid=data['productid'])
        serializer2=favSerializer(queryset1,many=True)
        if data['isfav']=='false':
            if len(serializer2.data)==0:
                return JsonResponse({"response": {"data": 'null',"error":'product_not_found_on_your_fav'}}, status=400)
            queryset1.delete()
        elif data['isfav']=='true':
            serializer = favSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"response": {"data": "success"}}, status=200)
            return JsonResponse(serializer.errors, status=400)
        return JsonResponse({"response": {"data": 'null',"error":'something_went_wrong'}}, status=400)

# dummy if you want delete items(food) use this one
@csrf_exempt
def fetchpopular(request,id):
    try:
        snippet = Popularmodel.objects.get(id=id)
    except: 
        return HttpResponse(status=400)   
    if request.method == 'GET':
        serializer = PopularSerializer(snippet)
        return JsonResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PopularSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


@csrf_exempt
def fetchrecommended(request,id):
    try:
        snippet = Recommendedmodel.objects.get(id=id)
    except: 
        return HttpResponse(status=400)   
    if request.method == 'GET':
        serializer = RecommendedSerializer(snippet)
        return JsonResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RecommendedSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

        
# image fetch url set
@csrf_exempt
def imgsnd(request):
    return 'assets/food0.png'



# 

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import PopularSerializer, RecommendedSerializer
# from .models import Popular,Recommended

# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         {
#             'Endpoint':'/food',
#             'method': 'GET',
#             'body': None,
#             'description': 'Returns an array of food'
#         },
#         {
#             'Endpoint':'/food/popular',
#             'method': 'GET',
#             'body': None,
#             'description': 'Returns an array of food'
#         },
#         {
#             'Endpoint':'/food/recommended',
#             'method': 'GET',
#             'body': None,
#             'description': 'Returns an array of food'
#         },
#         {
#             'Endpoint':'/food/recommended/id',
#             'method': 'GET',
#             'body': None,
#             'description': 'Returns an single food object'
#         },
#         {
#             'Endpoint':'/food/recommended/create',
#             'method': 'POST',
#             'body': {'body': ""},
#             'description': 'Creates new food with data sent in post request'
#         },
#         {
#             'Endpoint':'/food/recommended/id/update',
#             'method': 'GET',
#             'body': None,
#             'description': 'Returns an array of food'
#         },
#         {
#             'Endpoint':'/food/recommended/id/delete',
#             'method': 'DELETE',
#             'body': None,
#             'description': 'Deletes and existing food'
#         },    
#         {
#             'Endpoint':'/food/popular/id',
#             'method': 'GET',
#             'body': None,
#             'description': 'Returns an single food object'
#         },
#         {
#             'Endpoint':'/food/popular/create',
#             'method': 'POST',
#             'body': {'body': ""},
#             'description': 'Creates new food with data sent in post request'
#         },
#         {
#             'Endpoint':'/food/popular/id/update',
#             'method': 'GET',
#             'body': None,
#             'description': 'Returns an array of food'
#         },
#         {
#             'Endpoint':'/food/popular/id/delete',
#             'method': 'DELETE',
#             'body': None,
#             'description': 'Deletes and existing food'
#         }, 
#     ]
#     return Response(routes)

# @api_view(['GET'])
# def getPopular(request):
#     popular = Popular.objects.all()
#     serializer = PopularSerializer(popular, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getPopular(request, pk):
#     popular = Popular.objects.get(id=pk)
#     serializer = PopularSerializer(popular, many=False)
#     return Response(serializer.data)


# @api_view(['GET'])
# def getRecommended(request):
#     recommended = Recommended.objects.all()
#     serializer = RecommendedSerializer(recommended, many=True)
#     return Response(serializer.data)