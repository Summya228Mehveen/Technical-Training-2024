#Breadth First Search
#All possible paths
'''def paths(d,x,e):
    l.append(x)
    if x==e:
        print(l)
        l.pop()
        return
    for i in d[x]:
        if i not in l:
            paths(d,i,e)
    l.pop()
'''
#dfs taversal
'''
def dfs(d,x):
    l.append(x)
    for i in d[x]:
        if i not in l:
            dfs(d,i)
    return l
 
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
paths(d,5,2)
print("DFS Traversal:")
dfs(d,5)
print(l)
'''

# Minimum Path and cost
'''
def pathcost(d,x,e,c,m,l1):
    l.append(x)
    if(x==e):
        if(c<m):
            m=c
            l1=l.copy()
        l.pop()
        return m,l1
    for i in d[x]:
        if i[0] not in l:
            m,l1=pathcost(d,i[0],e,c+i[1],m,l1)
    l.pop()
    return m,l1
d={5:[(7,2),(3,1)],7:[(5,2),(4,6),(3,2)],4:[(7,6),(8,1),(2,2)],8:[(3,1),(4,2),(2,4)],3:[(5,3),(7,4),(8,6)],2:[(4,3),(8,3)]}
l=[]
for i in d.keys():
    print(pathcost(d,5,2,0,99999,[]))
'''
#All possible paths to every node
'''
def paths(d,x,e):
    l.append(x)
    if x==e:
        print(l)
        l.pop()
        return
    for i in d[x]:
        if i not in l:
            paths(d,i,e)
    l.pop()
def allpaths(d,s):
    for i in d.keys():
        paths(d,s,i)
        
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
allpaths(d,5)
'''
#Breadth First Search
'''
def bfs(d,visited,q):
    while q:
        c = q.pop(0)
        if c not in visited:
            visited.append(c)
        for i in d[c]:
            if i not in visited and i not in q:
                q.append(i)
    return visited
        
            
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2,9],3:[5,7,8],2:[4,8]}
#d = {8:[10,12],10:[11],12:[8,13],13:[14],4:[15]}
visited=[]
q=[]
for i in d:
    k=i
    break
q.append(k)
print(bfs(d,visited,q))
'''
#Dijikshtra's Algorithm
'''
def dijikshtra(g,s):
    d={1:9999,2:9999,3:9999,4:9999,5:9999}
    d[s]=0
    visited=[]
    q=[s]
    while q:
        m=9999
        for i in q:
            if(d[i]<m):
                m=d[i]
                x=i
        #x=q.pop(0)
        for i in g[x]:
            #print(i)
            if i[0] not in visited:
                q.append(i[0])
                if d[i[0]] > i[1] + d[x]:
                    d[i[0]] = i[1] + d[x]
                   # q.append(i[0])
                  #  print(q)
        visited.append(x)
        q.remove(x)
       # print(set(visited))
    return d
    


g={1:[(2,2),(3,1)],
   2:[(1,2),(3,3),(4,4),(5,4)],
   3:[(1,1),(4,2)],
   4:[(2,4),(5,3)],
   5:[(3,4),(4,2)] }

s=1
print(dijikshtra(g,s))
'''