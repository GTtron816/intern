stri ="hey hey hey there"
l=len(stri)
c=stri.find('hey there')
for x in range(c,l):
  print(stri[x],end="")