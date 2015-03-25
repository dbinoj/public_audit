from django.shortcuts import render, get_object_or_404, redirect
from client.models import FileMeta, FileAudit
from storage.models import ClientFile, FileBlock, AuditResponse
from tpa.models import AuditRequest

# Create your views here.
def index(request):
    file_list = AuditRequest.objects.all()
    context = {'file_list': file_list}
    return render(request, 'tpa/index.html',context)


def file_requestto_server(request, file_id):
    auditrequest = get_object_or_404(AuditRequest, pk=file_id)
    
    auditrequest.result = "Verification Message Requested from Server"
    auditrequest.save()


    auditresponse, created = AuditResponse.objects.get_or_create(
        file_id = ClientFile.objects.get(pk=auditrequest.storage_file_id),
    )
    auditresponse.result = "Verification Message Requested from Server"
    auditresponse.save()
    return redirect('tpa:index')


def verify(request, file_id):
    auditrequest = get_object_or_404(AuditRequest, pk=file_id)
    if auditrequest.client_message == auditrequest.server_message:
        message = "File Verification Success"
    else:
        message = "File Verification Failed"
    auditrequest.result = message
    auditrequest.save()


    auditresponse, created = AuditResponse.objects.get_or_create(
        file_id = ClientFile.objects.get(pk=auditrequest.storage_file_id),
    )
    auditresponse.result = message
    auditresponse.save()

    filemeta = FileMeta.objects.get(
        storage_file_id = auditrequest.storage_file_id,
    )
    fileaudit, created = FileAudit.objects.get_or_create(
        file_id = filemeta,
    )
    fileaudit.result = message
    fileaudit.save()
    return redirect('tpa:index')
