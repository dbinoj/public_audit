from django.shortcuts import render, get_object_or_404

from client.models import FileMeta

# Create your views here.


def index(request):
    file_list = FileMeta.objects.order_by('ts')
    context = {'file_list': file_list}
    return render(request, 'client/index.html', context)

def file_detail(request, file_id):
    file_meta = get_object_or_404(FileMeta, pk=file_id)
    return render(request, 'client/file_detail.html', {'file_meta', file_meta})
