__coding__      = 'utf-8'
__author__      = 'greg.berkey'
__credits__     = ['greg.berkey', '...']
__license__     = 'GPL'
__created__     = '2015.0512'
__modified__    = '2015.0529'
__version__     = '.0.0.5'
__maintainer__  = 'greg.berkey'
__email__       = 'greg.berkey@dish.com'
__status__      = 'Development'

# This function reads a file and displays its size and checksum
def get_custom_checksum(input_file_name):
    from datetime import datetime

    start_time = datetime.now()
    # START: Actual checksum calculation
    from hashlib import md5, sha256
    chunk_size = 1048576
    file_md5_checksum = md5()
    file_sha256_checksum = sha256()
    try:
        with open(input_file_name, "rb") as f:
            byte = f.read(chunk_size)
            previous_byte = byte
            byte_size = len(byte)
            file_read_iterations = 1
            while byte:
                file_md5_checksum.update(byte)
                file_sha256_checksum.update(byte)
                previous_byte = byte
                byte = f.read(chunk_size)
                byte_size += len(byte)
                file_read_iterations += 1
    except IOError:
        stop_time = datetime.now()
        process_time = str(stop_time - start_time)

        custom_checksum_profile = {
            'job_id': gv_runid,
            'full_path': os.path.abspath(p),
            'start_time': start_time,
            'byte_size': 0,
            'file_read_iterations': 0,
            'last_chunk_size': 0,
            'md5_checksum': 0,
            'sha256_checksum': 0,
            'stop_time': stop_time,
            'process_time': process_time,
            'status_code': 99,
        }
        exit()
        return custom_checksum_profile
    except:
        raise
    # END: Actual checksum calculation

    last_chunk_size = len(previous_byte)
    stop_time = datetime.now()
    process_time = str(stop_time - start_time)

    custom_checksum_profile = {
        'job_id': gv_runid,
        'full_path': os.path.abspath(p),
        'start_time': start_time,
        'byte_size': byte_size,
        'file_read_iterations': file_read_iterations,
        'last_chunk_size': last_chunk_size,
        'md5_checksum': file_md5_checksum.hexdigest(),
        'sha256_checksum': file_sha256_checksum.hexdigest(),
        'stop_time': stop_time,
        'process_time': process_time,
        'status_code': 1,
    }

    return custom_checksum_profile

def print_custom_checksum(input_file_name):
    custom_checksum_profile = get_custom_checksum(input_file_name)
    try:
        print ('Full Path             :', custom_checksum_profile['full_path'])
        print ('Start Time            :', custom_checksum_profile['start_time'])
        print ('File Size (bytes)     :', custom_checksum_profile['byte_size'])
        print ('File Read Iterations  :', custom_checksum_profile['file_read_iterations'])
        print ('Last Chunk (bytes)    :', custom_checksum_profile['last_chunk_size'])
        print ('MD5                   :', custom_checksum_profile['md5_checksum'])
        print ('SHA256                :', custom_checksum_profile['sha256_checksum'])
        print ('Stop Time             :', custom_checksum_profile['stop_time'])
        print ('Processing Time       :', custom_checksum_profile['process_time'])
        print ('Status Code           :', custom_checksum_profile['status_code'])
    except TypeError: #  'NoneType' object is unable to subscribe
        #raise
        #pass
        exit()

# This function reads a file and provides specific attributes
def get_custom_fileAttributes(input_file_name):
    import time

    accTime2 = time.gmtime(os.stat(input_file_name).st_atime)
    accTime2_hr = time.strftime('%y%m%d.%H%M', accTime2)

    modTime2 = time.gmtime(os.stat(input_file_name).st_mtime)
    modTime2_hr = time.strftime('%y%m%d.%H%M', modTime2)

    chgTime2 = time.gmtime(os.stat(input_file_name).st_ctime)
    chgTime2_hr = time.strftime('%y%m%d.%H%M', chgTime2)

    fileSizeBytes = os.stat(input_file_name).st_size

    (fileShortName, fileExtension) = os.path.splitext(input_file_name)
    formatFileExtension = fileExtension.replace(".", "").lower()

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

def crud_fileInfo(input_file_name):
    custom_fileAttributes_profile = get_custom_fileAttributes(input_file_name)
    custom_checksum_profile = get_custom_checksum(input_file_name)

    # Get a connection to MSSQL ODBC DSN via pypyodbc, and assign it to conn
    conn = pypyodbc.connect('DSN=ENCASESQL')

    # Give me a cursor so I can operate the database with the cursor
    cur = conn.cursor()

    # Insert a row to the table
    cur.execute('''
    INSERT INTO  eDiscovery_metadata.dbo.stageEsiInventory_150529
    (
      job_id
     ,file_location
     ,start_time
     ,file_size
     ,file_read_iterations
     ,last_chunk_size
     ,hash_md5
     ,hash_sha256
     ,stop_time
     ,processing_time
     ,job_status_code
     ,file_created
     ,file_modified
     ,file_changed
     ,file_extension
    )
    VALUES
    (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
    );
    ''',
    (
        custom_checksum_profile['job_id'] #-- run_id - decimal
        ,custom_checksum_profile['full_path'] #-- file_location - nvarchar(1024)
        ,custom_checksum_profile['start_time'] # -- 'YYYY-MM-DD hh:mm:ss[.nnn]'#-- start_time - datetime
        ,custom_checksum_profile['byte_size'] #175543059 #-- file_size - bigint
        ,custom_checksum_profile['file_read_iterations'] #169 #-- file_read_iterations - int
        ,custom_checksum_profile['last_chunk_size'] #430867 #-- last_chunk_size - int
        ,custom_checksum_profile['md5_checksum'] #'b67117ebacf6f0b2179814c49b53d02d' #-- hash_md5 - char(16)
        ,custom_checksum_profile['sha256_checksum'] #'67b8d5f80a97c743bb8ea1f989bd9829014c058db9f95f68ae9562f7d8577b09' #-- hash_sha256 - char(64)
        ,custom_checksum_profile['stop_time'] #GETDATE() -- 'YYYY-MM-DD hh:mm:ss[.nnn]'#-- stop_time - datetime
        ,custom_checksum_profile['process_time'] #'0:00:01.613161' #-- processing_time - varchar(16)
        ,custom_checksum_profile['status_code'] #1 #-- job_status_code - int
        ,custom_fileAttributes_profile['file_accessed_time']
        ,custom_fileAttributes_profile['file_modified_time']
        ,custom_fileAttributes_profile['file_changed_time']
        ,custom_fileAttributes_profile['file_extension']
    ))

    cur.commit()

    # I have done all the things, you can leave me and serve others!
    cur.close()
    conn.close()

import os
import pypyodbc
from datetime import datetime

gv_runid = datetime.now().strftime('%y%m%d.%H%M')

for root, dirs, files in os.walk(r'\\ednas1\STAGE\eDiscovery-testing\150529 - file extensions'):
    for file in files:
        p = os.path.join(root, file)

        crud_fileInfo(p)

        #print_custom_checksum(p)
        #print_custom_fileAttributes(p)
        #print()