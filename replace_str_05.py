#http://pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/
#http://www.bogotobogo.com/python/python_traversing_directory_tree_recursively_os_walk.php
# Import the os module, for the os.walk function
import os
import re 
# Set the directory you want to start from
def title_name(before,after,extra,instr):
    pattern = '('+before+')'+'(.*)'+'('+after+')'
    gfind = re.findall(pattern,instr)
    for desc in gfind:
        rep_desc = desc[1].replace(extra,'')
        rep_desc = rep_desc.replace('-',' ')
        rep_desc = desc[0]+rep_desc.title()+desc[2]
        org_desc = desc[0]+desc[1]+desc[2]
        instr = instr.replace(org_desc,rep_desc) 
    return instr

 
def rep_name(indexF,name):
	f = open(indexF,'r')
	fstr = f.read()
	f.close
	fstr = fstr.replace('>img</a></h1>','>ArtList.org</a></h1>')
	#painter name
	painter = name.replace('-',' ')
	painter = painter.title()
	fstr = fstr.replace(name,painter)
	before = '<figcaption itemprop="caption description">'
	after = '</figcaption>'
	extra = '.jpg'
	fstr = title_name(before,after,extra,fstr)	 
	f = open(indexF,'w')
	f.write(fstr)
	f.close
    	      
def rep_index001(indexname):
    f = open(indexname,'r')
    fstr = f.read()
    f.close
    fstr = fstr.replace('>img</a></h1>','>ArtList.org</a></h1>')
    before = '<span class="album_title">'
    after = '</span>'
    extra = ''
    fstr = title_name(before,after,extra,fstr)
    f = open(indexF,'w')
    f.write(fstr)
    f.close
inFile = "index-list.csv"
#fout = codecs.open(out,"w",encoding="utf-8")
inlist = open(inFile,'r',encoding="utf-8")
count = 200
##cdir = '.\\status-art'
#srcDown = '.\\status-down-art'
#maxid = 9999999999999999999
i = 0
indexArr = []
for findex in inlist:
     indexArr.append(findex)

for indexF in indexArr:
	indexF = indexF.replace('\n','')
	indexF = indexF.replace('\r','')
	#print (indexF)
	nameArr = indexF.split('\\')
	if len(nameArr) >3:
	   print (nameArr[2])
	   rep_name(indexF,nameArr[2])
	else:
          print (nameArr[2])
          rep_index001(indexF)
