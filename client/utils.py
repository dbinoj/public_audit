import os, random, struct
from Crypto.Cipher import AES


def split_files(file, chunkSize):
    bytes = len(file)
    noOfChunks= bytes/chunkSize
    if(bytes%chunkSize):
        noOfChunks += 1
    blocks = {}
    b_count = 1
    for i in range(0, bytes+1, chunkSize):
        file_chunk = { "b_%s" % b_count: file[i:i + chunkSize] }
	b_count += 1
        blocks.update(file_chunk)

    return blocks

def encrypt_file(key, in_file, out_filename, chunksize=64*1024):
    iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = len(in_file)

    with in_file:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = in_file.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))

def decrypt_file(key, in_filename, out_filename, chunksize=24*1024):
    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)
