from django.shortcuts import render, get_object_or_404, redirect
from storage.models import ClientFile
# Create your views here.
def index(request):
    file_list = ClientFile.objects.all()
    context = {'file_list': file_list}
    return render(request, 'storage/index.html', context)

def file_metadata_send(request, file_id):
	file_metadata = get_object_or_404(ClientFile, pk=file_id)
	return redirect('storage:index')
