#https://stackoverflow.com/questions/31748444/how-to-update-twitter-status-with-image-using-image-url-in-tweepy
import requests
import os
import shutil
from time import sleep
import sys
import codecs
import json
import urllib

reload(sys)
sys.setdefaultencoding('utf-8')

# Access and authorize our Twitter credentials from credentials.py


#4502
def downPics(fname,imgD,videoD):
# define image file name = userid t[0] + twit_id t[1]
  ft = codecs.open(fname,"r",encoding="utf-8")
  darr = fname.split("\\")
  dd = darr[2]
  farr = dd.split("-")
  userid = farr[0]
  print userid
  for line in ft:
       # print line.encode('utf-8')
    #line = line.replace('\r\n','')
   if len(line) >0:
    t = line.split('||')
    if len(t) > 3:
       #print t[0]
       #userid = t[0].replace('\n','')
       twit_id = t[1]
       url = t[5]
       if '.jpg' in t[5]:
             #print userid
             narr = t[5].split('/')
             img = narr[-1]
             iname = imgD+userid+'-'+twit_id+'-'+img
             urllib.urlretrieve(t[5],iname)
             print iname
       if ('.mp4' in t[6]) or ('.m3u8' in t[6]):
             varr = t[6].split('/')
             video = varr[-1].replace('\n','')
             vname = videoD + userid + '-' + twit_id + '-'+video
             urllib.urlretrieve(t[6],vname)
             print vname
    	      #varr = t[4].split('/')
            #video = varr[-1].replace('\n','')
          #video = varr[-1].replace('\n','')
          #vname = videoD + userid + '-' + twit_id + '-'+video
    	    #video = varr[-1].replace('\n','')
          #urllib.urlretrieve(t[4],vname)
          #vname =  '.\\videos\\amazingnature33\\'+video
          #vname = videoD + userid+'-'+twit_id+'-'+video
          #urllib.urlretrieve(t[4],vname)
          #print vname


source = os.listdir(".\\status-art\\")
destination = ".\\status-down-art\\"
srcdir = ".\\status-art\\"
imgD = ".\\pics-art\\"
videoD = ".\\videos\\"
count = 3
i = 0
for files in source:
  if i < count :
    if files.endswith(".txt"):
      f = srcdir + files
      fd = destination + files
      downPics(f,imgD,videoD)
      shutil.move(f,fd)
    i = i + 1
#print ("source status %s \nimages %s \nvideos %s \ndown status %s",source,imgD,videoD,destination)
print ("source status:",srcdir," images:",imgD," videos:", videoD," down status: ",destination)