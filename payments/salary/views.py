from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from .models import Salary, paid
from .serilaizers import PaidSerilizer, SalarySerilizer, UserSerilizer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User


class A(ModelViewSet):
    def get_serializer(self, *args, **kwargs):
        return super().get_serializer(*args, **kwargs)


def all_sallry(req):
    data = Salary.objects.all().values('date', 'salaryAmount')
    rsponce = {'salaries': list(data)}
    return JsonResponse(rsponce, safe=False)


@api_view(['GET', 'POST'])
def FBV_List(request):
    if (request.method == 'GET'):
        Salaries = Salary.objects.prefetch_related('paids')
        ser = SalarySerilizer(Salaries, many=True)
        return Response(ser.data)
    else:
        if (request.method == 'POST'):
            ser = SalarySerilizer(data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data, status=status.HTTP_201_CREATED)
            return Response(ser.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def FBV_Id(request, id):
    try:
        Salaries = Salary.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if (request.method == 'GET'):
        ser = SalarySerilizer(Salaries)
        return Response(ser.data)
    else:
        if (request.method == 'PUT'):
            ser = SalarySerilizer(data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data, status=status.HTTP_202_ACCEPTED)
            return Response(ser.data, status=status.HTTP_400_BAD_REQUEST)
        else:
            if (request.method == 'DELETE'):
                Salaries.delete()
                return Response(ser.data)


@api_view(['GET', 'POST'])
def PAIDS_List(request):
    if (request.method == 'GET'):
        Salaries = paid.objects.all()
        ser = PaidSerilizer(Salaries, many=True)
        return Response(ser.data)
    else:
        if (request.method == 'POST'):

            salary = Salary.objects.get(
                id=request. data['salary'])
            salary.currsalaryAmount -= request.data['paidAmount']
            salary.save()

            ser = PaidSerilizer(data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data, status=status.HTTP_201_CREATED)
            return Response(ser.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def PAID_Id(request, id):
    try:
        Salaries = paid.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if (request.method == 'GET'):
        ser = PaidSerilizer(Salaries)
        return Response(ser.data)
    else:
        if (request.method == 'PUT'):
            ser = PaidSerilizer(data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data, status=status.HTTP_202_ACCEPTED)
            return Response(ser.data, status=status.HTTP_400_BAD_REQUEST)
        else:
            if (request.method == 'DELETE'):
                Salaries.delete()
                return Response(ser.data)


class UserVeiwSet(ModelViewSet):
    serializer_class = UserSerilizer
    queryset = User.objects.all()
