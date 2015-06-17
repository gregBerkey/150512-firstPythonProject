__coding__ = 'utf-8'
__author__ = 'greg.berkey'
__credits__ = ['greg.berkey', 'scott.halepaska']
__license__ = 'GPL'
__date__ = '2015.0513'
__version__ = '.0.0.1'
__maintainer__ = 'greg.berkey'
__email__ = 'greg.berkey@dish.com'
__status__ = 'Development'


# We use the Python 2.x & 3.x compatible print function.

# Let Python load it's ODBC connecting tool pypyodbc
import pypyodbc

# Let Python load it's datetime functions
import datetime

# Get a connection to MSSQL ODBC DSN via pypyodbc, and assign it to conn
conn = pypyodbc.connect('DSN=ENCASESQL')

# Give me a cursor so I can operate the database with the cursor
cur = conn.cursor()

# Give me a cursor so I can operate the database with the cursor
cur = conn.cursor()


# Create a sellout table in SQLServer
cur.execute('''
CREATE TABLE eDiscovery_metadata.dbo.sellout (
  ID integer PRIMARY KEY IDENTITY,
  customer_name nvarchar(25),
  product_name nvarchar(25),
  price float,
  volume int,
  sell_time datetime
);
''')

cur.commit()


# Insert a row to the sellout table
cur.execute('''
INSERT INTO eDiscovery_metadata.dbo.sellout (customer_name
, product_name
, price
, volume
, sell_time)
  VALUES ('江文' -- customer_name - varchar(25)
  ,'Huawei Ascend mate' -- product_name - varchar(25)
  , 5000.5 -- price - float
  , 2 -- volume - int
  , GETDATE() -- 'YYYY-MM-DD hh:mm:ss[.nnn]'-- sell_time - datetime
  );
''')

cur.commit()


# Insert a row to the sellout table
cur.execute('''
INSERT INTO eDiscovery_metadata.dbo.sellout (customer_name
, product_name
, price
, volume
, sell_time)
  VALUES (?,?,?,?,?
  );
''', (u'杨天真', 'Apple IPhone 5', 5500.1, 1, '2012-1-21'))

cur.commit()


# Insert a batch rows of data to the sellout table using a same query
a_batch_rows = [(u'杨天真', 'Apple IPhone 5', 5500.1, 1, '2012-1-21'),
                (u'郑现实', 'Huawei Ascend D2', 5100.5, 2, '2012-1-22'),
                (u'莫小闵', 'Lenovo P780', 2000.5, 3, '2012-1-22'),
                (u'顾小白', 'Huawei Ascend Mate', 3000.4, 2, '2012-1-22')]

# Insert a row to the sellout table
cur.executemany('''
INSERT INTO eDiscovery_metadata.dbo.sellout (customer_name
, product_name
, price
, volume
, sell_time)
  VALUES (?,?,?,?,?
  );
''', a_batch_rows)

cur.commit()

# Insert a row to the stageEsiInventory table
cur.execute('''
INSERT INTO  eDiscovery_metadata.dbo.stageEsiInventory
(
  run_id
 ,file_location
 ,start_time
 ,file_size
 ,file_read_iterations
 ,last_chunk_size
 ,hash_md5
 ,hash_sha256
 ,stop_time
 ,processing_time
)
VALUES
(
  150513.1225 -- run_id - decimal
 ,'C:\\Users\\greg.berkey\\Downloads\\testSmall\\mID3202.zipx' -- file_location - nvarchar(1024)
 ,GETDATE() -- 'YYYY-MM-DD hh:mm:ss[.nnn]'-- start_time - datetime
 ,175543059 -- file_size - bigint
 ,169 -- file_read_iterations - int
 ,430867 -- last_chunk_size - int
 ,'b67117ebacf6f0b2179814c49b53d02d' -- hash_md5 - char(16)
 ,'67b8d5f80a97c743bb8ea1f989bd9829014c058db9f95f68ae9562f7d8577b09' -- hash_sha256 - char(64)
 ,GETDATE() -- 'YYYY-MM-DD hh:mm:ss[.nnn]'-- stop_time - datetime
 ,'0:00:01.613161' -- processing_time - varchar(16)
);
''')

cur.commit()


# Select those records about "Huawei" products
cur.execute('''
SELECT * FROM eDiscovery_metadata.dbo.sellout WHERE product_name LIKE '%Huawei%';
''')

# Print the table headers (column descriptions)
for d in cur.description:
    print(d[0], end=" ")

# Start a new line
print('')

# Print the table, one row per line
for row in cur.fetchall():
    for field in row:
        print(field, end=" ")
    print('')

# I have done all the things, you can leave me and serve for others!

cur.close()
conn.close()

print('end of code')
