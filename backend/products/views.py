from rest_framework import generics, authentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from api.mixins import StaffEditorPermissionMixin
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    authentication_classes = [authentication.SessionAuthentication,authentication.TokenAuthentication]
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content = content)
        return super().perform_create(serializer)

class ProductDetailAPIView(StaffEditorPermissionMixin,
                           generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(StaffEditorPermissionMixin,
                           generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field ='pk'
    def perform_update(self, serializer):
        instance= serializer.save()
        if not instance.content :
            instance.content = instance.title


class ProductDestroyAPIView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field ='pk'
    

@api_view(['POST', 'GET'])
def product_alt_view(request,pk=None,*args, **kwargs):
    method = request.method


    if method == 'GET':
        if pk is not None:
            obj= get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj).data

            return Response(data)

        # get request
        qs = Product.objects.all()
        data = ProductSerializer(qs , many=True).data
        return Response(data)

    elif method == 'POST':
        serializer = ProductSerializer(data= request.data)
    
        if serializer.is_valid():
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content = content)
            return Response(serializer.data)
        return Response({"invaild":"no good data"}, status=404  )