from django.shortcuts import render
from storage.models import ClientFile
# Create your views here.
def index(request):
    file_list = ClientFile.objects.order_by('ts')
    context = {'file_list': file_list}
    return render(request, 'storage/index.html', context)