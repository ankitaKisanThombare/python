'''
program is combination of two gp series and we have to calculate nth term
'''
l=[1,1,3,2,9,4,27,..]
n=int(input())
n=n-1
if n%2==0:
    r=int(l[2]/l[0])
    a=l[0]
    n=int(n/2)
    print((a)*((r)**(n)))
    
else:
    
    r=int(l[3]/l[1])
    
    a=l[1]
    n=int((n+1)/2)
    print((a)*((r)**(n-1)))
    
