from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ApplicationSerializer
from .models import EmailList
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

# Create your views here.
@api_view(['POST'])
def submit_application(request):
    json = JSONRenderer().render(request.data)
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = ApplicationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(" application submitted")
    else:
        print("sa serializer: ", serializer.data)
        return Response('did not create')

@api_view(['POST'])
def subscribe(request):
    new = request.data['email']
    new = EmailList.objects.create(email=new)    
    new.save()
    return Response("added email " + new.email)