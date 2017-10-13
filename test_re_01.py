import re

text="""<h3 class="heading">General Purpose</h3>"""
pattern="(<.*?>)(.*)(<.*?>)"

g=re.search(pattern,text)
g.group(2)
print (g.group(2))

t2='<figcaption itemprop="caption description">autumn-twilight-in-a-forest-1960.jpg - </figcaption>'
p2 = '(<figcaption itemprop="caption description">)(.*)(</figcaption>)'
g2=re.search(p2,t2)
g2.group(2)
print (g2.group(2))
