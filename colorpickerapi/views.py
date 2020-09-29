from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets, permissions, views
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FileUploadParser
from PIL import Image
import requests
from io import BytesIO
from rest_framework.response import Response
import extcolors


def index(request):
    return render(request, 'index.html')


class imageapi(views.APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [MultiPartParser]

    def post(self, request):

        try:
            colors = processimg(fp=request.data.getlist('image')[0])
        except:
            return Response({'error': 'no file found, make sure id/key is set to "image"'})

        return Response({
                        'logo_border': colors[1],
                        'dominant_color': colors[0]
                        })

    def get(self, request):
        img_url = request.query_params.get('src')
        colors = processimg(url=img_url)
        return Response({
                        'logo_border': colors[1],
                        'dominant_color': colors[0]
                        })


def processimg(fp=None, url=None):
    if url:
        response = requests.get(url)
        im = Image.open(BytesIO(response.content))
    else:
        im = Image.open(fp)
    colors, pixel_count = extcolors.extract_from_image(im)

    return ('#%02x%02x%02x' % colors[0][0], '#%02x%02x%02x' % colors[1][0])
