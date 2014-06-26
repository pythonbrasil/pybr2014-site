# coding: utf-8

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

from . import serializers


class PromoCodeView(generics.GenericAPIView):
    '''
    API endpoint that checks if the user is associated, is so, send a e-mail
    with discount code
    '''
    serializer_class = serializers.PromoCodeSerializer

    def post(self, request):
        ser = self.get_serializer(data=request.DATA)

        if ser.is_valid():
            pc = ser.save()
            pc.send_email()
            return Response(ser.data)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
