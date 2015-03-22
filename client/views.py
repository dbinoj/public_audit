from django.shortcuts import render, get_object_or_404

from client.models import FileMeta
from django.conf import settings

from .forms import FileUploadForm


STORAGE_BLOCK_SIZE = getattr(settings, 'STORAGE_BLOCK_SIZE', 10240)

# Create your views here.


def index(request):
    form = FileUploadForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        file = request.FILES['file_field']
        file_size = len(file)
        file_name = file.name
    file_list = FileMeta.objects.order_by('ts')
    context = {'file_list': file_list, "form": form}
    return render(request, 'client/index.html', context)

def file_detail(request, file_id):
    file_meta = get_object_or_404(FileMeta, pk=file_id)
    return render(request, 'client/file_detail.html', {'file_meta', file_meta})
