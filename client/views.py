from django.shortcuts import render, get_object_or_404

from client.models import FileMeta

from .forms import FileUploadForm
# Create your views here.


def index(request):
    form = FileUploadForm()
    file_list = FileMeta.objects.order_by('ts')
    context = {'file_list': file_list, "form": form}
    return render(request, 'client/index.html', context)

def file_detail(request, file_id):
    file_meta = get_object_or_404(FileMeta, pk=file_id)
    return render(request, 'client/file_detail.html', {'file_meta', file_meta})
