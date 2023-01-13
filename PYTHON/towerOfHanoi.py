def tower(n,source,dest,temp):
    if n == 1:
        print("Move disk 1 from source",source," to destination", dest)
        return
    tower(n-1,source,temp,dest)
    print("Move disk", n ,"from source",source," to destination", dest)
    tower(n-1,temp,dest,source)

tower(4,'a','b','c')

# tower of hanoi shortcut
''' 2 function calls def f(n,s,d,t)
f(n-1,s,t,d)
f(n-1,t,d,s)
'''

