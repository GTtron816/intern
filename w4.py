stri ="hey hey hey there"
l=len(stri)
sub="there"
count = 0
sp=0
start=0
for i in range (0,l):
  if stri[i]==' ' or i == l-1:
      sp=i
      if i == l-1:
          sp=i+1
      
      if sub==stri[start:sp]:
          print(stri[start:sp])
          count=count+1
      start=sp+1 
  
print(count)     
