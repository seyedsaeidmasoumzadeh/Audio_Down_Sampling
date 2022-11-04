from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from django.http import FileResponse
from .serializers import UploadSerializer
from resampling.resampler import down_sampling
import os


from io import BytesIO

# ViewSets define the view behavior.
class UploadViewSetAPI(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        _, format = os.path.splitext(file_uploaded.name)
        if format not in ['.wav', '.mp3']:
            raise APIException('format must be wav or mp3')
        out_signal = down_sampling(file_uploaded)
        if out_signal:
            return FileResponse(BytesIO(out_signal))
        else:
            raise APIException('sampling rate must be larger than 32kHz')   

