'''famous chinese puzzle
In a cage housing some chicken and rabbits. There are total of  35 heads, and 94 legs. Find how many chicken and rabbits ?'''

def puzz(h,l):
    n=h*2
    rem=l-n
    rabits=int(rem/2)# no of rabbit
    hens=h-rabits#no of hens
    print(rabits,hens)

# no of heads are 34 and legs are 94
puzz(35,94)
