from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from guess.models import *
import json

# Create your views here.
@csrf_exempt
def add_guess_subject(request):
	subject = GuessSubject()
	subject.content = request.POST.get('content')
	subject.choiceA = request.POST.get('choiceA')
	subject.choiceB = request.POST.get('choiceB')
	subject.stepsA = 0
	subject.stepsB = 0
	subject.save()
	return HttpResponse("success")


@csrf_exempt
def get_guess_subject(request):
	subjects = []
	for dbitem in GuessSubject.objects.all():
		item = {
			'id':dbitem.id,
			'content':dbitem.content,
			'choiceA':dbitem.choiceA,
			'choiceB':dbitem.choiceB,
			'stepsA':dbitem.stepsA,
			'stepsB':dbitem.stepsB
		}
		subjects.append(item)
	return HttpResponse(json.dumps(subjects))



