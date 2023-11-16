from django.shortcuts import render
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from student.serializer import StudentSerializer
from student.models import StudentModel
# Create your views here.

@csrf_exempt
def add(request):
     if request.method=="POST":
        recieved_data=json.loads(request.body)
        print(recieved_data)
         
        serializer_check=StudentSerializer(data=recieved_data)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"added successfully"}))
        else:
            return HttpResponse(json.dumps({"status":"failed"}))

@csrf_exempt
def viewAll(request):
    if request.method=="POST":
        studentList=StudentModel.objects.all()
        serialize_data=StudentSerializer(studentList,many=True)
        return HttpResponse(json.dumps(serialize_data.data))