#http://pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/
#http://www.bogotobogo.com/python/python_traversing_directory_tree_recursively_os_walk.php
# Import the os module, for the os.walk function
import os
import re 
# Set the directory you want to start from

def rep_name(indexF,name):
	f = open(indexF,'r')
	fstr = f.read()
	f.close
	fstr = fstr.replace('>img</a></h1>','>ArtList.org</a></h1>')
	#painter name
	painter = name.replace('-',' ')
	painter = painter.title()
	fstr = fstr.replace(name,painter)
	p2 = '(<figcaption itemprop="caption description">)(.*)(</figcaption>)'
	g2=re.findall(p2,fstr)
	for desc in g2:
		print(desc[1])
		rep_desc = desc[1].replace('.jpg','')
		rep_desc = rep_desc.replace('-',' ')
		rep_desc = rep_desc.title()
		org_desc = desc[0]+desc[1]+desc[2]
		#fstr = fstr.replace(org_desc,rep_desc)
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
