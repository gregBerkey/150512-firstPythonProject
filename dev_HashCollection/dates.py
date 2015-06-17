__coding__      = 'utf-8'
__author__      = 'greg.berkey'
__credits__     = ['greg.berkey', 'scott.halepaska']
__license__     = 'GPL'
__created__     = '2015.0512'
__modified__    = '2015.0513'
__version__     = '.0.0.3'
__maintainer__  = 'greg.berkey'
__email__       = 'greg.berkey@dish.com'
__status__      = 'Development'

# some new change
import datetime

print('\n~~~~~~~~~~~~~~~~~')
print ('Now    :', datetime.datetime.now())
print ('Today  :', datetime.datetime.today())
print ('UTC Now:', datetime.datetime.utcnow())


d = datetime.datetime.now()
year = getattr(d,'year')

print('\n~~~~~~~~~~~~~~~~~')
print(d)
print(year)

for attr in [ 'year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
    print (attr, ':', getattr(d, attr))

print('\n~~~~~~~~~~~~~~~~~')
#https://aralbalkan.com/1512/
import datetime
print (str(datetime.datetime.now()))

print('\n~~~~~~~~~~~~~~~~~')
#http://importpython.blogspot.com/2014/07/how-to-convert-date-formats-from.html
from datetime import datetime

oldformat = '20140716'
datetimeobject = datetime.strptime(oldformat,'%Y%m%d')

print(datetimeobject)

newformat = datetimeobject.strftime('%m-%d-%Y')
print (newformat)

newformat = datetimeobject.strftime('%yy%m%dd')
print (newformat)

print('\n~~~~~~~~~~~~~~~~~')
#http://www.cyberciti.biz/faq/howto-get-current-date-time-in-python/
from datetime import datetime

i = datetime.now()

print (str(i))
print (i.strftime('%Y/%m/%d %H:%M:%S'))
print (i.strftime('%y%m%d.%H%M'))

print('\n~~~~~~~~~~~~~~~~~')
print (datetime.now().strftime('%y%m%d.%H%M'))