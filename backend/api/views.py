from django.http import JsonResponse
from products.serializers import ProductSerializer
from products.models import *
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view(["POST"])
def api_home(request,*args, **kwargs):
   
    # instance = Product.objects.all().order_by('?').first()
    serializer = ProductSerializer(data= request.data)
    
    if serializer.is_valid():
        print(serializer.data)
        data = serializer.data
    # if instance: 
    #    data = ProductSerializer(instance).data
        return Response(data)