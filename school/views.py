from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import studentsdetail,yearclass,months,teacherdetail,teachpaymonths,fees,enroll_student,schoolclasses
from .serializers import studentsdetailSerializer,yearsSerializer,monthsSerializer,teacherdetailSerializer,feesSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.generics import ListAPIView
from rest_framework import generics
# from rest_framework.filters import SearchFilter
from rest_framework.filters import SearchFilter





@api_view(['GET', 'POST', 'DELETE'])
def studentslist(request):
    if request.method == 'GET':
        allstudents = studentsdetail.objects.all()
        
        title = request.query_params.get('s_name', None)
        if title is not None:
            allstudents = allstudents.filter(title__icontains=title)
        
        allstudents_serializer = studentsdetailSerializer(allstudents, many=True)
        return JsonResponse(allstudents_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        students_data = JSONParser().parse(request)
        allstudents_serializer = studentsdetailSerializer(data=students_data)
        if allstudents_serializer.is_valid():
            allstudents_serializer.save()
            return JsonResponse(allstudents_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(allstudents_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    elif request.method == 'DELETE':      
                studentsdetail.objects.all().delete()  
            
    return JsonResponse({'message':'all students data deleted'},status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST','DELETE'])    
def studentdetail(request, pk) :    
        try:
            student=studentsdetail.objects.filter(pk=pk)
        except studentsdetail.DoesNotExist: 
            return JsonResponse({'message': 'The Student does not exist'}, status=status.HTTP_404_NOT_FOUND)
     
     
        if request.method == 'DELETE':
            student.delete()
            return JsonResponse({'message':'this row is deleted successfully'},status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'GET':
            student=studentsdetail.objects.get(pk=pk)
            student_serializer=studentsdetailSerializer(student)
        return JsonResponse(student_serializer.data)


@api_view(['GET', 'POST', 'DELETE'])
def yearview(request):
    if request.method == 'GET':
        yearr = yearclass.objects.all()
        years_serializer = yearsSerializer(yearr, many=True)
        return JsonResponse(years_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        year_data = JSONParser().parse(request)
        years_serializer = yearsSerializer(data=year_data)
        if years_serializer.is_valid():
            years_serializer.save()
            return JsonResponse(years_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(years_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    elif request.method == 'DELETE':      
                yearclass.objects.all().delete()  
            
    return JsonResponse({'message':'all years cleared'},status=status.HTTP_204_NO_CONTENT)
    


@api_view(['GET'])
def monthsview(request,roll):
    if request.method == 'GET':
        monthss = months.objects.filter(student__rollnbr=roll)
        month_serializer = monthsSerializer(monthss, many=True)
        
        return JsonResponse(month_serializer.data, safe=False)
        # 'safe=False' for objects serialization

@api_view(['GET', 'POST', 'DELETE'])
def feesget(request):
    if request.method == 'GET':
        allstudents = fees.objects.all()
        allstudents_serializer = feesSerializer(allstudents, many=True)
        return JsonResponse(allstudents_serializer.data, safe=False)

@api_view(['POST'])
def feespost(request,roll,yerr,month,standardd):
    if request.method == 'POST':
        data_month = JSONParser().parse(request)
        try:
            insyear = yearclass.objects.get(year=yerr)
            try:
                insenroll = enroll_student.objects.get(student=roll,years=yerr,standard__standardname=standardd)
            except enroll_student.DoesNotExist:
                inststudent = studentsdetail.objects.get(rollnbr=roll)
                insstandard = schoolclasses.objects.get(standardname=standardd)
                insenroll = enroll_student(student=inststudent,years=insyear,standard=insstandard)
                insenroll.save()
            # insstandard = standard.objects.get(standardname=standardd)
            print(insenroll)
            insmonths = months.objects.get(monthname=month)
            insfees = fees(enrollstudent=insenroll,months=insmonths)
            print(insfees)
            fees_serialized = feesSerializer(insfees, data=data_month, partial=True)
            if fees_serialized.is_valid():
                fees_serialized.save()
                return JsonResponse(fees_serialized.data,status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(fees_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        except fees.DoesNotExist:
            insfees.save()
            insfees = fees(enroll_student=insenroll,year=insyear,months=insmonths)
            fees_serialized = feesSerializer(insfees,data=data_month, partial=True)
            if fees_serialized.is_valid():
                fees_serialized.save()
                return JsonResponse(fees_serialized.data,status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(fees_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def updateview(request,roll,yerr):
#     if request.method == 'POST':
#         monthss = studentsdetail.objects.get(rollnbr=roll)
#         yearr = yearclass.objects.get(year=yerr)
#         data_month = JSONParser().parse(request)
#         try:
#             monthss = months.objects.get(student__rollnbr=roll,years__year=yerr)
#             month_serializer = monthsSerializer(monthss, data=data_month, partial=True)
#             if month_serializer.is_valid():
#                 month_serializer.save()
#                 return JsonResponse(month_serializer.data,status=status.HTTP_201_CREATED)
#             else:
#                 return JsonResponse(month_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except months.DoesNotExist:
#             ins = months(student=monthss,years=yearr)
#             ins.save()
#             monthss = months.objects.get(student__rollnbr=roll,years__year=yerr)
#             month_serializer = monthsSerializer(monthss,data=data_month, partial=True)
#             if month_serializer.is_valid():
#                 month_serializer.save()
#                 return JsonResponse(month_serializer.data,status=status.HTTP_201_CREATED)
#             else:
#                 return JsonResponse(month_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


