#https://stackoverflow.com/questions/31748444/how-to-update-twitter-status-with-image-using-image-url-in-tweepy
import requests
import os
import tweepy
from time import sleep
from credentials import *
import sys
import codecs
import json
import datetime

reload(sys)
sys.setdefaultencoding('utf-8')

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#4502
#maxid = '907845557850435584'
def findMaxid(ft,laxid):
    laxid = 9999999999999999999
    fin = open(ft,'r')
    twidArr = []
    for line in fin:
        tidArr = line.split('||')
        twidArr.append(tidArr[1]) 
        #print tidArr[1]
    darr = [int(numeric_string) for numeric_string in twidArr]
    if len(darr) > 0:
       laxid = min(darr)
    print laxid
    return laxid

def getMaxID(twi_id,src,srcDown,maxid):
    source = os.listdir(src)
    source2 = os.listdir(srcDown)
    #print twi_id
    for ft in source:
        #ffArr = ft.split('-')
        #ff = ffArr[0]
        #print ft

        if ft.startswith(twi_id):
           fn = src+'\\'+ft
           print fn
           faxid =findMaxid(fn,maxid)
           if faxid < maxid:
               maxid = faxid
           #print "getMaxID:",fn,"maxid:",maxid
    for fst in source2:
        
        if fst.startswith(twi_id):
           fsn = srcDown+'\\'+fst
           print fsn
           faxid=findMaxid(fsn,maxid)
           if faxid < maxid:
               maxid = faxid
           print "getMaxID:",fsn,"maxid:",maxid
    return maxid

def getTwi(twi_id,maxid,count):
    
         line = ""
         #print maxid
         maxid = maxid - 1
         twi_id = twi_id.replace('\n','')
         #ss = api.user_timeline(id=twi_id, max_id = maxid, count=200)
         ss = api.user_timeline(id=twi_id, max_id = maxid, count=count)
         for status in ss:
             iurl = ''
             vurl = ''
             #print status.retweet_count, status.favorite_count
             retwi = status.retweet_count
             fav = status.favorite_count
             sid = status._json['id']
             stext = status.text.encode('utf-8')
             stext = stext.replace('\r',' ')
             stext = stext.replace('\n',' ')
             #api.retweet(sid)
             #print status._json['media_url']
             #surl = status._json['entities']['media'][0]['media_url_https']
             #tweepy.Cursor(api.search, q="#hashtag", count=5, include_entities=True)
             if 'media' in status.entities:
               for image in  status.entities['media']:
                   iurl = image['media_url_https']
                   if 'video' in iurl:
                       if 'media' in status.extended_entities:
                            for video in status.extended_entities['media']:
                                if 'video_info' in video:
                                    if len( video['video_info']['variants']) >1 :
                                        vurl = video['video_info']['variants'][1]['url']
                                        #print vurl
    
                                  #print iurl
                                  #print status._json
             line = line + twi_id+'||'+str(sid)+'||'+str(retwi)+'||'+str(fav)+'||'+stext+'||'+iurl+'||'+vurl+'\n'
         return line
             #print line.encode('utf-8')
    #json.dump(status._json,ft)
#print line
#print surl

now =  datetime.datetime.now()
timestr = str(now).replace(' ','-').replace(':','-')
#print str(now)+'\n'+timestr+'\n'+timestr[:19]

twi = "twi_list_01.txt"
#fout = codecs.open(out,"w",encoding="utf-8")
ftwi = codecs.open(twi,'r',encoding="utf-8")
count = 200
cdir = '.\\status-art'
srcDown = '.\\status-down-art'
maxid = 9999999999999999999
i = 0
twiArr = []
for twi_id in ftwi:
     twiArr.append(twi_id)

for tid in twiArr: 
     i = i + 1
     print i,tid
     tid = tid.replace('\n','')
     tid = tid.replace('\r','')
     maxid = getMaxID(tid,cdir,srcDown,maxid)
     print "last: twi_id:"+tid+" maxid:"+str(maxid)
     tstatus = getTwi(tid,maxid,count)
     out = cdir+'\\'+tid+'-'+timestr[:16]+'.txt'
     out = out.replace('\r\n','')
     fout = codecs.open(out,"w",encoding="utf-8")
     fout.write(tstatus)
     print "input: "+ tid+"\ncount: "+str(count)+ "\noutput: "+out