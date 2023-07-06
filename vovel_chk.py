def vovel_check(a):
  if a=='a' or a=='e' or a=='i' or a=='o' or a=='u':
        return a
    
def isvovel():
    stri="this is a string to print the vovels"
    l=len(stri)
    x=0
    for i in range(x,l):
     ret=vovel_check(stri[i])
     if ret:
      print("vovel: ",ret)
    print(stri)
isvovel()