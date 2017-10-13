incsv = "img-01.csv"
fin = open(incsv,'r')

outhtml = "img-html-01.html"
fout = open(outhtml,'w')

thtml = "0-01.html"
fhtml = open(thtml,'r')
htmlstr = fhtml.read()
mark = htmlstr.find('<body>')
instr = ""
#read  template file
i = 0
for line in fin:
  if i<100:
	#print line
	i = i+1
	narr = line.split('\\')
	#print len(narr)
	if  len(narr)>2:
         painter = narr[2]
         name = painter.split('-')
         lastname = name[-1]
         fullname = painter.replace('-','')
         pic = narr[3]
         pic=  pic.split('.')[0]
         painter = painter.replace('-',' ')
         pic = pic.replace('-',' ')
         #print (painter)
         #print (pic)
         status =  painter+'\n'+pic
         status = status.title()
        #hashstr = '\n#art '+'#painting '+'#'+fullname+' '+'#'+lastname
         status = status
         desc = painter+' '+pic
         desc = desc.title()
         imgsrc = narr[2]+'/'+narr[3]
         imgsrc = imgsrc.replace('\n','')
         print imgsrc
         imgstr = '<img alt="'+desc+'" src="images/'+imgsrc+'" data-image="images/' +imgsrc+'" data-description="'+desc+'">'
         instr = instr+imgstr+"\n"
         #print imgstr
         #<img alt="Image 2 Title" 
	     #     src="thumbs/greece.jpg"
		 #     data-image="images/greece.jpg"
	     #     data-description="Image 2 Description">
	     #print status
outstr = '"<div id="gallery" style="display:none;">'+instr+'</div>'
outstr = htmlstr[:mark]+outstr+htmlstr[mark:]
fout.write(outstr)
