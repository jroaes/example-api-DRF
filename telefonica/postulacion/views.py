from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from postulacion.models import Persona
from postulacion.serializers import PersonaSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def persona_list(request):
    if request.method == 'GET':
        person = Persona.objects.all()
        serializer = PersonaSerializer(person, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SerieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def persona_detail(request, pk):
    try:
        person = Persona.objects.get(pk=pk)
    except Persona.DoesNotExist:
	return HttpResponse(status=404)

    if request.method == 'GET':
	serializer = SerieSerializer(person)
	return JSONResponse(serializer.data)

    elif request.method == 'PUT':
	data = JSONParser().parse(request)
	serializer = SerieSerializer(person, data=data)
	if serializer.is_valid():
	    serializer.save()
	    return JSONResponse(serializer.data)
	return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
	person.delete()
	return HttpResponse(status=204)
