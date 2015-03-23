
def split_files(file, chunkSize):
    bytes = len(file)
    noOfChunks= bytes/chunkSize
    if(bytes%chunkSize):
        noOfChunks += 1
    blocks = {}
    for i in range(0, bytes+1, chunkSize):
        file_chunk = { "b_%s" % i: file[i:i + chunkSize] }
        blocks.update(file_chunk)

    return blocks

