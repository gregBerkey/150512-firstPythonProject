__author__ = 'greg.berkey'
__credits__ = ['greg.berkey', 'scott.halepaska']
__license__ = 'GPL'
__date__ = '2015.0512'
__version__ = '.0.0.1'
__maintainer__ = 'greg.berkey'
__email__ = 'greg.berkey@dish.com'
__status__ = 'Development'

'''
   https://docs.python.org/3/library/stat.html
'''

# Import the os module, for the os.walk function
import os, time, datetime

'''
# Set the directory you want to start from
rootDir = '../'
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        print(rootDir.lower())
        print('\t%s' % fname)
print('~~~~')
print()
'''

print('\nData:')

for root, dirs, files in os.walk('../../'):
    for file in files:
        p = os.path.join(root, file)
        # print(p)
        print(os.path.abspath(p))

        info = os.stat(p)
        print(info.st_size)
        info = os.stat(p)
        print(time.ctime(info.st_mtime))

        print()

'''
for root, dirs, files in os.walk(r'\\chy-fsjrnlp1\Journal_Exports'):
    for file in files:
        p = os.path.join(root, file)
        #print(p)
        print(os.path.abspath(p))
        print

        info = os.stat(p)
        print(info.st_size)
        info = os.stat(p)
        print(time.ctime(info.st_mtime))

        print()

'''