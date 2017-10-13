import re

text="""<h3 class="heading">General Purpose</h3>"""
pattern="(<.*?>)(.*)(<.*?>)"

g=re.search(pattern,text)
g.group(2)
print (g.group(2))