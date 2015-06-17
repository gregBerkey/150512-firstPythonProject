__coding__      = 'utf-8'
__author__      = 'greg.berkey'
__credits__     = ['greg.berkey', 'scott.halepaska']
__license__     = 'GPL'
__created__     = '2015.0512'
__modified__    = '2015.0528'
__version__     = '.0.0.5'
__maintainer__  = 'greg.berkey'
__email__       = 'greg.berkey@dish.com'
__status__      = 'Development'

# This script reads a file and displays its size and checksum
def get_custom_checksum(input_file_name):
    from datetime import datetime

    starttime = datetime.now()
    # START: Actual checksum calculation
    from hashlib import md5, sha256
    chunk_size = 1048576  # 1024 B * 1024 B = 1048576 B = 1 MB
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
        #print('File could not be opened: %s' % (input_file_name))
        stoptime = datetime.now()
        processtime = str(stoptime - starttime)

        custom_checksum_profile = {
            'jobid': gv_runid,
            'fullpath': os.path.abspath(p),
            'starttime': starttime,
            'byte_size': 0,
            'file_read_iterations': 0,
            'last_chunk_size': 0,
            'md5_checksum': 0,
            'sha256_checksum': 0,
            'stoptime': stoptime,
            'processtime': processtime,
            'statuscode': 99,
        }

        # Get a connection to MSSQL ODBC DSN via pypyodbc, and assign it to conn
        conn = pypyodbc.connect('DSN=ENCASESQL')

        # Give me a cursor so I can operate the database with the cursor
        cur = conn.cursor()

        # Insert a row to the stageEsiInventory table
        cur.execute('''
        INSERT INTO  eDiscovery_metadata.dbo.stageEsiInventory_150528
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
        )
        VALUES
        (?,?,?,?,?,?,?,?,?,?,?
        );
        ''',
        (
            custom_checksum_profile['jobid'] #-- run_id - decimal
            ,custom_checksum_profile['fullpath'] #-- file_location - nvarchar(1024)
            ,custom_checksum_profile['starttime'] # -- 'YYYY-MM-DD hh:mm:ss[.nnn]'#-- start_time - datetime
            ,custom_checksum_profile['byte_size'] #175543059 #-- file_size - bigint
            ,custom_checksum_profile['file_read_iterations'] #169 #-- file_read_iterations - int
            ,custom_checksum_profile['last_chunk_size'] #430867 #-- last_chunk_size - int
            ,custom_checksum_profile['md5_checksum'] #'b67117ebacf6f0b2179814c49b53d02d' #-- hash_md5 - char(16)
            ,custom_checksum_profile['sha256_checksum'] #'67b8d5f80a97c743bb8ea1f989bd9829014c058db9f95f68ae9562f7d8577b09' #-- hash_sha256 - char(64)
            ,custom_checksum_profile['stoptime'] #GETDATE() -- 'YYYY-MM-DD hh:mm:ss[.nnn]'#-- stop_time - datetime
            ,custom_checksum_profile['processtime'] #'0:00:01.613161' #-- processing_time - varchar(16)
            ,custom_checksum_profile['statuscode'] #1 #-- job_status_code - int
        ))

        cur.commit()

        # I have done all the things, you can leave me and serve others!
        cur.close()
        conn.close()

        #exit()
        return custom_checksum_profile
    except:
        raise
    # END: Actual checksum calculation
    # For storage purposes, 1024 bytes = 1 kilobyte
    # For data transfer purposes, 1000 bits = 1 kilobit
    last_chunk_size = len(previous_byte)
    stoptime = datetime.now()
    processtime = str(stoptime - starttime)

    custom_checksum_profile = {
        'jobid': gv_runid,
        'fullpath': os.path.abspath(p),
        'starttime': starttime,
        'byte_size': byte_size,
        'file_read_iterations': file_read_iterations,
        'last_chunk_size': last_chunk_size,
        'md5_checksum': file_md5_checksum.hexdigest(),
        'sha256_checksum': file_sha256_checksum.hexdigest(),
        'stoptime': stoptime,
        'processtime': processtime,
        'statuscode': 1,
    }
    #print(custom_checksum_profile)
    #print(custom_checksum_profile['processtime'])

    # Get a connection to MSSQL ODBC DSN via pypyodbc, and assign it to conn
    conn = pypyodbc.connect('DSN=ENCASESQL')

    # Give me a cursor so I can operate the database with the cursor
    cur = conn.cursor()

    # Insert a row to the stageEsiInventory table
    cur.execute('''
    INSERT INTO  eDiscovery_metadata.dbo.stageEsiInventory_150528
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
    )
    VALUES
    (?,?,?,?,?,?,?,?,?,?,?
    );
    ''',
    (
        custom_checksum_profile['jobid'] #-- run_id - decimal
        ,custom_checksum_profile['fullpath'] #-- file_location - nvarchar(1024)
        ,custom_checksum_profile['starttime'] # -- 'YYYY-MM-DD hh:mm:ss[.nnn]'#-- start_time - datetime
        ,custom_checksum_profile['byte_size'] #175543059 #-- file_size - bigint
        ,custom_checksum_profile['file_read_iterations'] #169 #-- file_read_iterations - int
        ,custom_checksum_profile['last_chunk_size'] #430867 #-- last_chunk_size - int
        ,custom_checksum_profile['md5_checksum'] #'b67117ebacf6f0b2179814c49b53d02d' #-- hash_md5 - char(16)
        ,custom_checksum_profile['sha256_checksum'] #'67b8d5f80a97c743bb8ea1f989bd9829014c058db9f95f68ae9562f7d8577b09' #-- hash_sha256 - char(64)
        ,custom_checksum_profile['stoptime'] #GETDATE() -- 'YYYY-MM-DD hh:mm:ss[.nnn]'#-- stop_time - datetime
        ,custom_checksum_profile['processtime'] #'0:00:01.613161' #-- processing_time - varchar(16)
        ,custom_checksum_profile['statuscode'] #1 #-- job_status_code - int
    ))

    cur.commit()

    # I have done all the things, you can leave me and serve others!
    cur.close()
    conn.close()

    return custom_checksum_profile

def print_custom_checksum(input_file_name):
    custom_checksum_profile = get_custom_checksum(input_file_name)
    try:
        print ('Full Path             :', custom_checksum_profile['fullpath'])
        print ('Start Time            :', custom_checksum_profile['starttime'])
        print ('File Size (bytes)     :', custom_checksum_profile['byte_size'])
        print ('File Read Iterations  :', custom_checksum_profile['file_read_iterations'])
        print ('Last Chunk (bytes)    :', custom_checksum_profile['last_chunk_size'])
        print ('MD5                   :', custom_checksum_profile['md5_checksum'])
        print ('SHA256                :', custom_checksum_profile['sha256_checksum'])
        print ('Stop Time             :', custom_checksum_profile['stoptime'])
        print ('Processing Time       :', custom_checksum_profile['processtime'])
        print ('Status Code           :', custom_checksum_profile['statuscode'])
    except TypeError: #  'NoneType' object is unable to subscribe
        #raise
        #pass
        exit()
    # csv output

import os
import pypyodbc
from datetime import datetime

gv_runid = datetime.now().strftime('%y%m%d.%H%M')

#\\ednas1\Legal
#\\chy-fsjrnlp1\Journal_Exports
#\\chy-fsjrnlp1\Legal
#\\chy-fsjrnlp1\PMNAS2
#\\chy-fsjrnlp1\Temp-Legal

for root, dirs, files in os.walk(r'\\chy-fsjrnlp1\Temp-Legal'):
    for file in files:
        p = os.path.join(root, file)

        #get_custom_checksum(p)
        print_custom_checksum(p)

        print()