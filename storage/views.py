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
    
    server_message = file_meta.hash_md5 + '$' + file_meta.hash_sha1 + '$' + str(file_meta.storage_file_id) + '$' + file_meta.signature
    auditrequest.client_message = client_message
    auditrequest.name = file_meta.name
    auditrequest.result = "Audit Request Recieved from Client"
    auditrequest.save()
    blocks = file_metadata.fileblock_set.order_by('path')
    enc_md5 = hashlib.new('md5')
    enc_sha1 = hashlib.new('sha1')
    for block in blocks:
        encrypted_block = open(block.path, 'r')
        block_contents = encrypted_block.read()
        encrypted_block.close()
        enc_md5.update(block_contents)
        enc_sha1.update(block_contents)
    return redirect('storage:index')
