from django.shortcuts import render, get_object_or_404, redirect

from django.conf import settings

from client.models import FileMeta, FileAudit
from storage.models import ClientFile, FileBlock, AuditResponse
from tpa.models import AuditRequest

from client.forms import FileUploadForm
from client.utils import split_files, encrypt_file

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 
from Crypto.Hash import SHA256

from rsa.bigfile import *
from functools import partial
from django.core.context_processors import csrf

import os, tempfile, collections
import base64
import cStringIO
import hashlib
import rsa.randnum
import storage

import pprint

STORAGE_BLOCK_SIZE = getattr(settings, 'STORAGE_BLOCK_SIZE', 10240)

# Create your views here.

def index(request):
    form = FileUploadForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        file = request.FILES['file_field']
        file_size = file.size
        file_name = file.name
        #md5 = hashlib.new('md5')
        #sha1 = hashlib.new('sha1')
        sha256 = SHA256.new()
        for chunk in iter(partial(file.read, 8192), ''):
            #md5.update(chunk)
            #sha1.update(chunk)
            sha256.update(chunk)
        
        # The above with block sends the file pointer to the end of the file
        file.seek(0)

        RSAkey = RSA.generate(1024)
        AESkey = rsa.randnum.read_random_bits(128)
        #file_md5 = md5.hexdigest()
        #file_sha1 = sha1.hexdigest()
        signer = PKCS1_v1_5.new(RSAkey)
        signature = signer.sign(sha256)
        signature_b64 = base64.b64encode(signature)
        
        # verifyer = PKCS1_v1_5.new(RSAkey.publickey())
        # if verifyer.verify(sha256, base64.b64decode(signature_b64)):
        #     print "Verified"
        # else:
        #     print "Not Verified"

        filemeta = FileMeta.objects.create(
            name=file_name, 
            size=file_size, 
            private_key=RSAkey.exportKey(), 
            aes_key=AESkey, 
            hash_sha1='', 
            hash_md5='', 
            signature=signature_b64
        )

        clientfile = ClientFile.objects.create(
            name=file_name,
            size=file_size,
            signature=signature_b64
        )

        blocks = split_files(file.read(), STORAGE_BLOCK_SIZE)
        blocks_count = len(blocks)
        # Python Dicts are not sorted. Sorting using collections.OrderedDict
        # Must sort so that we get same hash everytime.
        blocks = collections.OrderedDict(sorted(blocks.items()))
        clientfile.blocks = blocks_count
        clientfile.save()
        enc_md5 = hashlib.new('md5')
        enc_sha1 = hashlib.new('sha1')
        blocks_enc = {}
        for key, value in blocks.iteritems():
            plain_value = tempfile.NamedTemporaryFile()
            plain_value.write(value)
            block_path = os.path.join(
                                getattr(settings, 'BASE_DIR'),
                                'storage',
                                'client_files', 
                                str(key)
            )
            
            encrypt_file(AESkey, plain_value.name, block_path)
            encrypted_block = open(block_path, 'r')
            block_contents = encrypted_block.read()
            encrypted_block.close()
            block_md5 = hashlib.md5(block_contents).hexdigest()
            block_sha1 = hashlib.sha1(block_contents).hexdigest()
            enc_md5.update(block_contents)
            enc_sha1.update(block_contents)
            block_sha256 = SHA256.new(block_contents)
            block_signature = signer.sign(block_sha256)
            block_signature_b64 = base64.b64encode(block_signature)
            fileblock = FileBlock.objects.create(
                file_id=clientfile,
                path=block_path,
                hash_sha1=block_sha1,
                hash_md5=block_md5,
                block_size=os.path.getsize(block_path),
                signature=block_signature_b64
            )
            if plain_value.closed == False:
                plain_value.close()
        enc_file_md5 = enc_md5.hexdigest()
        enc_file_sha1 = enc_sha1.hexdigest()
        filemeta.storage_file_id = clientfile.id
        filemeta.hash_md5 = enc_file_md5
        filemeta.hash_sha1 = enc_file_sha1
        filemeta.save()

    file_list = FileMeta.objects.order_by('ts')
    context = {'file_list': file_list, "form": form}
    return render(request, 'client/index.html', context)

def file_detail(request, file_id):
    file_meta = get_object_or_404(FileMeta, pk=file_id)
    return render(request, 'client/file_detail.html', {'file_meta': file_meta})


def file_request_audit(request, file_id):
    file_meta = get_object_or_404(FileMeta, pk=file_id)
    auditrequest, created = AuditRequest.objects.get_or_create(
        storage_file_id = file_meta.storage_file_id,
    )
    client_message = file_meta.hash_md5 + '$' + file_meta.hash_sha1 + '$' + str(file_meta.storage_file_id) + '$' + file_meta.signature
    auditrequest.client_message = client_message
    auditrequest.name = file_meta.name
    auditrequest.result = "Audit Request Recieved from Client"
    auditrequest.save()


    fileaudit, created = FileAudit.objects.get_or_create(
        file_id = file_meta,
    )
    fileaudit.result = "Audit Request sent to TPA"
    fileaudit.save()

    auditresponse, created = AuditResponse.objects.get_or_create(
        file_id = ClientFile.objects.get(pk=file_meta.storage_file_id),
    )
    auditresponse.result = "Waiting for TPA to request Verification Data."
    auditresponse.save()

    return redirect('client:index')


def login(request):
    c={}
    c.update(csrf(request))
    return render( 'login.html', c)

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            return HttpResponseRedirct('client:index')
        else:
            return HttpResponseRediect('client:login')
