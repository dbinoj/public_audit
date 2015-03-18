from django.shortcuts import render

# Create your views here.
def index(request):
    #file_id = FileMeta.objects.order_by('ts')
    #context = {'file_list': file_list}
    return render(request, 'tpa/index.html')
