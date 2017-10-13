import re

text="""<h3 class="heading">General Purpose</h3>"""
pattern="(<.*?>)(.*)(<.*?>)"

g=re.search(pattern,text)
g.group(2)
print (g.group(2))
t2=''
t2='<figure class="gallery__img--main thumbnail" itemprop="associatedMedia"' 
' itemscope itemtype="http://schema.org/ImageObject">'  
   '<a href="autumn-twilight-in-a-forest-1960.jpg" itemprop="contentUrl"'        
  ' data-size="513x512">' 
  '<img src="../static/echo/blank.gif" data-echo="autumn-twilight-in-a-forest-1960.jpg" alt="autumn-twilight-in-a-forest-1960.jpg" itemprop="thumbnail" title="" />'
'</a>'
'<figcaption itemprop="caption description">'
'autumn-twilight-in-a-forest-1960.jpg - </figcaption></figure>'
'<figure class="gallery__img--secondary thumbnail" itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">'
'<a href="birds-admist-willow.jpg" itemprop="contentUrl" data-size="374x570">'	
'<img src="../static/echo/blank.gif" data-echo="thumbnails/birds-admist-willow.jpg" alt="birds-admist-willow.jpg" itemprop="thumbnail" title="" />'									 
' </a>'							   
'<figcaption itemprop="caption description">birds-admist-willow.jpg - '
'</figcaption>'
'<figcaption itemprop="caption description">'
'autumn-twilight-in-a-forest-1960.jpg - </figcaption>'
p2 = '(<figcaption itemprop="caption description">)(.*)(</figcaption>)'
g2=re.search(p2,t2)
g2.group(2)
print (g2.group(2))
