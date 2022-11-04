from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.http import FileResponse
from .serializers import UploadSerializer, DownloadSerializer
from datetime import datetime
from resampling.resampler import wave_down_sampling, mp3_down_sampling
from scipy.io import wavfile
import tempfile


from django.http import HttpResponse
from django.shortcuts import render


from io import BytesIO

# ViewSets define the view behavior.
class UploadViewSetAPI(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        
        if ".wav" in file_uploaded.name:
            new_signal = wave_down_sampling(BytesIO(file_uploaded.read()))

        elif ".mp3" in file_uploaded.name:
            new_signal = mp3_down_sampling(file_uploaded)    

        else:
            Response({'message':'file must be wav or mp3','error':True,'code':500})    

        with tempfile.SpooledTemporaryFile(max_size = 1024 * 1024 * 500, mode="wb+") as out_f:
            wavfile.write(out_f, 32000, new_signal)
            return FileResponse(BytesIO(out_f.read()))   
          
