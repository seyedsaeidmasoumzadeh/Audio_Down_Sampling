from rest_framework.serializers import Serializer, FileField

# Serializers define the API representation.
class UploadSerializer(Serializer):
    file_uploaded = FileField()
    class Meta:
        fields = ['file_uploaded']

class DownloadSerializer(Serializer):
    class Meta:
        fileds = ['downloaded_file']
