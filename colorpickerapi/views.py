from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets, permissions, views
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FileUploadParser
from PIL import Image
from rest_framework.response import Response
import extcolors


def index(request):
    return render(request, 'index.html')


class imageapi(views.APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [MultiPartParser]

    def post(self, request):
        print(request.data)
        try:
            colors = processimg(request.data.getlist('image')[0])
        except:
            return Response({'error': 'no file found, make sure id/key is set to "image"'})

        return Response({'colors': colors})


def processimg(fp):
    im = Image.open(fp)
    colors, pixel_count = extcolors.extract_from_image(im)
    return (colors[0][0], colors[1][0])
