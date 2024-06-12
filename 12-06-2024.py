'''
def isprime(x):
    if x <= 1:
        return False
    for i in range(2, int(x//2) + 1):
        if x % i == 0:
            return False
    return True

def lprime(n, m):
    for i in range(m - 1, n, -1):
        if isprime(i):
            return i
    return 0

l = list(map(int, input().split()))
s = 0
for i in range(len(l) - 1):
    s += lprime(l[i], l[i + 1])

print(s)
'''
'''
l = [4,9,8,2,14,3,5,6]
for i in range(len(l)-2):
    if (l[i]>l[i+1]):
        l[i],l[i+1] = l[i+1],l[i]
    if(l[i+1]>l[i+1]):
        l[i+1],l[i+2] = l[i+2],l[i+1]
    if(l[i]>l[i+2]):
        l[i],l[i+2] = l[i+2],l[i]
print(l)
'''
'''
d={"hello":5438,"car":214,"book":8799,"apple":2187}
"hello:5438,car:214,book:8799,apple:2187"
res=""
i=0
flag=1
for i in d:
     
    c=len(i)
    
    while flag : 
        if str(c) in str(d[i]) :
            c=int(c)
            res+=i[c-1]
             
            flag=0
        elif c<0 :
            res+='x'
            flag=0
        elif str(c) not in str(d[i]) :
            c=int(c)
            c=c-1
       
    flag=1
    
print(res)
'''
'''
s=input().split(',') 
d={}
for i in s:
    k = i.split(':')
    print(k[0],k[1])
    d.update({k[0]:k[1]})
print(d)
result = ""
flag = 1
for i in d:
    c = len(i)
    while flag:
        if str(c) in str(d[i]):
            c=int(c)
            result+=i[c-1]
            flag=0
        elif c<0 :
            result+='x'
            flag=0
        elif str(c) not in str(d[i]) :
            c=int(c)
            c=c-1
    flag=1
print(result)
'''
a=input().split(',')
s=''
for i in a:
    b=i.split(":")
    l=len(b[0])
    if(str(l) in b[1]):
        s += b[0][-1]
    else:
        for i in range(l-1,0,-1):
            if (str[i] in b[1]):
                s += b[0][i-1]
                break
        else:
            s += 'x'
print(s)
        
        
    