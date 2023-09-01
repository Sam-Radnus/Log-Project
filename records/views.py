from django.shortcuts import render
import json
from .models import Log
from django.utils import timezone 
from django.http import JsonResponse
# Create your views here.
def createLog(request):
    try:
        info=json.loads(request.body)
        name=info["name"]
        
        new_log_entry=Log(
            project_name=name,
            time=timezone.now()
        )
        new_log_entry.save()
        return JsonResponse({"success":"true"})
    except:
        return JsonResponse({"success":"false"})

def showLogs(request):
    logs=Log.objects.all()
    return render(request,'records/index.html',{"logs":logs})