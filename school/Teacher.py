from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import yearclass,teacherdetail,teachpaymonths,months
from .serializers import yearsSerializer,teacherdetailSerializer,t_paymentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.generics import ListAPIView
from rest_framework import generics
from rest_framework.filters import SearchFilter

@api_view(['GET','POST','DELETE'])
def teacheroverall(request):
    if request.method == 'GET':
        allstudents = teacherdetail.objects.all()
        
        # title = request.query_params.get('s_name', None)
        # if title is not None:
        #     allstudents = allstudents.filter(title__icontains=title)
        
        allstudents_serializer = teacherdetailSerializer(allstudents, many=True)
        return JsonResponse(allstudents_serializer.data,safe = False)
    elif request.method == 'POST':
        teacherpostdata = JSONParser().parse(request)
        postserializer = teacherdetailSerializer(data=teacherpostdata)
        if postserializer.is_valid():
            postserializer.save()
            return JsonResponse(postserializer.data,status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'message': 'invalid entry'},status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':      
                teacherdetail.objects.all().delete()  
            
    return JsonResponse({'message':'all students data deleted'},status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
def teacherdelete(request,pk):
    if request.method == 'DELETE':
        teacherdetail.objects.get(pk=pk).delete()
        return JsonResponse({'message':'student data deleted'})


@api_view(['GET'])
def teacherpaymentview(request,pk):
    if request.method == 'GET':
        monthss = teachpaymonths.objects.filter(teacher__pk=pk)
    
        month_serializer = t_paymentSerializer(monthss ,many=True)
        return JsonResponse(month_serializer.data, safe=False)

@api_view(['POST'])
def updateteacherpayments(request,tyear,pk,monthh):
    if request.method == 'POST':
        tmonthss = teacherdetail.objects.get(pk=pk)
        yearr = yearclass.objects.get(year=tyear)
        month = months.objects.get(monthname=monthh)
        data_month = JSONParser().parse(request)
        try:
            monthss = teachpaymonths.objects.get(teacher__pk=pk,years__year=tyear,months__monthname=monthh)
            tmonth_serializer = t_paymentSerializer(monthss, data=data_month, partial=True)
            if tmonth_serializer.is_valid():
                tmonth_serializer.save()
                return JsonResponse(tmonth_serializer.data,status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(month_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except teachpaymonths.DoesNotExist:
            ins = teachpaymonths(teacher=tmonthss,years=yearr,months=month)
            ins.save()
            monthss = teachpaymonths.objects.get(teacher__pk=pk,years__year=tyear,months__monthname=monthh)
            tmonth_serializer = t_paymentSerializer(monthss,data=data_month, partial=True)
            if tmonth_serializer.is_valid():
                tmonth_serializer.save()
                return JsonResponse(tmonth_serializer.data,status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(tmonth_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
