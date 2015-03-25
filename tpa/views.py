from django.shortcuts import render, get_object_or_404, redirect
from tpa.models import AuditRequest

# Create your views here.
def index(request):
    file_list = AuditRequest.objects.all()
    context = {'file_list': file_list}
    return render(request, 'tpa/index.html',context)


def file_requestto_server(request, file_id):
    file_request = get_object_or_404(AuditRequest, pk=file_id)
    return redirect('tpa:index')


def verify(request, file_id):
    file_request = get_object_or_404(AuditRequest, pk=file_id)
    return redirect('tpa:index')
