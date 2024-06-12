'''l = [6,6,6,6,7]
d={}
for i in l:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)
n = len(l)//2
for i in d:
    if d[i] > n:
        n = d[i]
        break
print(i)'''
'''l = [1,1,2,2,1]
count = 1
won = l[0]
for i in range(1,len(l)):
    if(l[i]==won):
        count += 1
    else:
        count -= 1
        if count == 0:
            count = 1
            won = l[i]
print(won)
'''
'''n = int(input())
l = [0,5,3,6,7,2,4]
for i in range(n+1):
    if i in l:
        continue
    else:
        print(i)
        break'''
'''n = int(input())
l =[0,5,3,6,7,2,1]
sum1=sum(l)
sumn=(n*(n+1))//2
number = sumn-sum1
print(number)'''
'''n = int(input())
key = int(input())

'''
'''n = int(input())
m = int(input())
l=[]
l1=[]
count = 0
for i in range (1,n+1):
    if n%i == 0:
        l.append(i)
for i in range (1,m+1):
    if m%i == 0:
        l1.append(i)
for i in l:
    for j in l1:
        if i==j:
            count +=1
if count == 1:
    print("Co Prime")
else:
    print("Not Co Prime")
'''
'''import math
n = int(input())
m = int(input())
l=math.gcd(n,m)
if l==1:
    print("Co Prime")
else:
    print("Not Co Prime")'''
'''n = int(input())
m = int(input())
for i in range(2,(min(n,m))+1):
    if(n%i == 0) and (m%i==0):
        print("Not Co Prime")
        break
else:
    print("Co Prime")
    '''
'''s = input()
l1=['{','[','(']
l2=['}',']',')']
l=[]
for i in range(len(s)):
    if s[i] in l1:
        l.append(s[i])
    else:
        if l[-1] =='{' and s[i]=='}':
            l.pop()
        elif l[-1] =='[' and s[i]==']':
            l.pop()
        elif l[-1] =='(' and s[i]==')':
            l.pop()
        else:
            print(i+1)
            break
if len(l)==0:
    print("-1")'''