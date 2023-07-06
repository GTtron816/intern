mark=[]
for i in range(0,5):
    mark.append(int(input('enter mark')))
summ=0
for i in range(0,5):
    summ=summ+mark[i]
print("Average=",summ/5)    
print("Average=",sum(mark)/len(mark))
     