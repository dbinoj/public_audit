
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

