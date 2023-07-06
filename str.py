def rev(a):
 a = a
 l=len(a)
 n= l-1
 for x in range(n,-1,-1):
    print (a[x],end='')
rev("hello")