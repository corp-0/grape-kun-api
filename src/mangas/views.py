from rest_framework.generics import ListAPIView
from .models import MangaPreview
from .serializers import MangaPreviewSerializer

class MangaPreviewView(ListAPIView):
    queryset = MangaPreview.objects
    serializer_class = MangaPreviewSerializer
