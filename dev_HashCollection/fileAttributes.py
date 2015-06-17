__author__ = 'greg.berkey'

# This function reads a file and provides specific attributes
def get_custom_fileAttributes(input_file_name):
    import time

    #statinfo = os.lstat(input_file_name)
    #print(statinfo.st_atime)

    accTime2 = time.gmtime(os.stat(input_file_name).st_atime)
    #print(modTime2)
    #modTime2_hr = time.strftime("%m/%d/%Y %H:%M:%S", modTime2)
    accTime2_hr = time.strftime('%y%m%d.%H%M', accTime2)
    #print(accTime2_hr)

    modTime2 = time.gmtime(os.stat(input_file_name).st_mtime)
    #print(modTime2)
    #modTime2_hr = time.strftime("%m/%d/%Y %H:%M:%S", modTime2)
    modTime2_hr = time.strftime('%y%m%d.%H%M', modTime2)
    #print(modTime2_hr)

    chgTime2 = time.gmtime(os.stat(input_file_name).st_ctime)
    #print(modTime2)
    #modTime2_hr = time.strftime("%m/%d/%Y %H:%M:%S", modTime2)
    chgTime2_hr = time.strftime('%y%m%d.%H%M', chgTime2)
    #print(chgTime2_hr)

    fileSizeBytes = os.stat(input_file_name).st_size
    #print(fileSizeBytes)

    (fileShortName, fileExtension) = os.path.splitext(input_file_name)
    formatFileExtension = fileExtension.replace(".","").lower()

    #print(fileShortName + ' ' + formatFileExtension)


    custom_fileAttributes_profile = {
        'file_accessed_time': accTime2_hr,
        'file_modified_time': modTime2_hr,
        'file_changed_time': chgTime2_hr,
        'file_byte_size': fileSizeBytes,
        'file_extension': formatFileExtension,
    }

    return custom_fileAttributes_profile


def print_custom_fileAttributes(input_file_name):
    custom_fileAttributes_profile = get_custom_fileAttributes(input_file_name)
    try:
        print ('File Created          :', custom_fileAttributes_profile['file_accessed_time'])
        print ('File Modified         :', custom_fileAttributes_profile['file_modified_time'])
        print ('File Changed          :', custom_fileAttributes_profile['file_changed_time'])
        print ('File Size (B)         :', custom_fileAttributes_profile['file_byte_size'])
        print ('File Extension        :', custom_fileAttributes_profile['file_extension'])
    except TypeError: #  'NoneType' object is unable to subscribe
        #raise
        #pass
        exit()
    # csv output


import os

for root, dirs, files in os.walk(r'\\ednas1\STAGE\eDiscovery-testing\150529 - file extensions'):
    for file in files:
        p = os.path.join(root, file)

        #get_custom_fileAttributes(p)
        print_custom_fileAttributes(p)

        print()

"""

Description
The method lstat() is very similar to fstat() and returns the information about a file, but do not follow symbolic links.
This is an alias for fstat() on platforms that do not support symbolic links, such as Windows.

Here is the structure returned by lstat method:
st_dev:     ID of device containing file
st_ino:     inode number
st_mode:    protection
st_nlink:   number of hard links
st_uid:     user ID of owner
st_gid:     group ID of owner
st_rdev:    device ID (if special file)
st_blksize: blocksize for filesystem I/O
st_blocks:  number of blocks allocated

st_size:    total size, in bytes
st_atime:   time of last access
st_mtime:   time of last modification
st_ctime:   time of last status change

"""

