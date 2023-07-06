stri ="hey hey hey there"
l=len(stri)
sub="hey"
count = 0
sp=0
start=0
i=0
while i != l:
  if stri[i]==' ' or i == l-1:
      sp=i
      if i == l-1:
          sp=i+1
      
      if sub==stri[start:sp]:
          print(stri[start:sp])
          count=count+1
      start=sp+1 
  i=i+1
print(count)  