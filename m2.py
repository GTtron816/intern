stud=[]
for j in range(0,5):
    mark=[]
    for i in range(0,5):
        mark.append(int(input('enter mark')))
    stud.append(mark)
print(stud)
 

for i in range(0,5):
   print(sum(stud[i])/len(stud[i])) 
     