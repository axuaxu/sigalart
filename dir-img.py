#http://pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/
#http://www.bogotobogo.com/python/python_traversing_directory_tree_recursively_os_walk.php
# Import the os module, for the os.walk function
import os
 
# Set the directory you want to start from

print('first check')
rootDir = '.\images'


def flist():
  #t="dir,name,twi,extra\n"
  t=""
  for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
     
    for fname in fileList:
        print('\t%s' % fname)
        t=t+dirName+'\\'+fname+'\n'
  return t

# writing csv
 
ft = flist()  
with open('flist-01.csv', 'wb') as f:
      f.write(ft)

 