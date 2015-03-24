from django.shortcuts import render, get_object_or_404, redirect

from django.conf import settings

from client.models import FileMeta
from storage.models import ClientFile, FileBlock

from client.forms import FileUploadForm
from client.utils import split_files, encrypt_file

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 
from Crypto.Hash import SHA256

from rsa.bigfile import *
from functools import partial

import os, tempfile
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
        md5 = hashlib.new('md5')
        sha1 = hashlib.new('sha1')
        sha256 = SHA256.new()
        for chunk in iter(partial(file.read, 8192), ''):
            md5.update(chunk)
            sha1.update(chunk)
            sha256.update(chunk)
        
        # The above with block sends the file pointer to the end of the file
        file.seek(0, 0)

        RSAkey = RSA.generate(1024)
        AESkey = rsa.randnum.read_random_bits(128)
        file_md5 = md5.hexdigest()
        file_sha1 = sha1.hexdigest()
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
            hash_sha1=file_sha1, 
            hash_md5=file_md5, 
            signature=signature_b64
        )

        blocks = split_files(file.read(), STORAGE_BLOCK_SIZE)
        blocks_enc = {}
        for key, value in blocks.iteritems() :
                plain_value = tempfile.NamedTemporaryFile()
                plain_value.write(value)
                block_path = os.path.join(
                                    getattr(settings, 'BASE_DIR'),
                                    'storage',
                                    'client_files', 
                                    str(key)
                )
                
                encrypt_file(AESkey, plain_value.name, block_path)
                if plain_value.closed == False:
                    plain_value.close()
                exit()

    file_list = FileMeta.objects.order_by('ts')
    context = {'file_list': file_list, "form": form}
    return render(request, 'client/index.html', context)

def file_detail(request, file_id):
    file_meta = get_object_or_404(FileMeta, pk=file_id)
    return render(request, 'client/file_detail.html', {'file_meta': file_meta})


def file_request_audit(request, file_id):
    file_meta = get_object_or_404(FileMeta, pk=file_id)
    return redirect('client:index')
