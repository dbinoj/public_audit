from django.shortcuts import render, get_object_or_404, redirect
from client.models import FileMeta, FileAudit
from storage.models import ClientFile, FileBlock, AuditResponse
from tpa.models import AuditRequest

import hashlib
# Create your views here.
def index(request):
    file_list = ClientFile.objects.all()
    context = {'file_list': file_list}
    return render(request, 'storage/index.html', context)

def file_metadata_send(request, file_id):
    clientfile = get_object_or_404(ClientFile, pk=file_id)
    auditrequest, created = AuditRequest.objects.get_or_create(
        storage_file_id = file_id,
    )
    
    blocks = clientfile.fileblock_set.order_by('path')
    enc_md5 = hashlib.new('md5')
    enc_sha1 = hashlib.new('sha1')
    for block in blocks:
        encrypted_block = open(block.path, 'r')
        block_contents = encrypted_block.read()
        encrypted_block.close()
        enc_md5.update(block_contents)
        enc_sha1.update(block_contents)
    server_message = enc_md5.hexdigest() + '$' + enc_sha1.hexdigest() + '$' + str(file_id) + '$' + clientfile.signature
    auditrequest.server_message = server_message
    auditrequest.result = "Verification Message sent to TPA"
    auditrequest.save()
    auditresponse, created = AuditResponse.objects.get_or_create(
        file_id = file_id,
    )
    auditresponse.result = "Verification Message sent to TPA"
    auditresponse.save()
    return redirect('storage:index')
