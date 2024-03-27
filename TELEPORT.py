from queue import Queue
tx=[0,-1,0,1]
ty=[-1,0,1,0]
m,n=map(int,input().split())
x,y,z,t=map(int,input().split())
a=[[0]*(n+1)]
for i in range (m):
    b=[0]+list(map(int,input().split()))
    a.append(b)
b=[[0]*(n+1) for i in range (m+2)]
def roi_rac_hoa():
    dict={}
    for i in range (1,m+1):
        for j in range (1,n+1):
            if a[i][j]>0:
                if (dict.get(a[i][j])==None):
                    dict[a[i][j]]=len(dict)+1
                    a[i][j]=len(dict)
                else:
                    a[i][j]=dict[a[i][j]]
def insize(x,y):
    return (1<=x and x<=m and 1<=y and y<=n)
def BFS(x,y):
    b[x][y]=1
    q=Queue()
    q.put((x,y))
    while (q.qsize()>0):
        td=q.get()
        x,y=td[0],td[1]
        if (x==z and y==t):
            return
        for k in range (4):
            if (insize(x+tx[k],y+ty[k])):
                if (a[x+tx[k]][y+ty[k]]>0 and b[x+tx[k]][y+ty[k]]==0):
                    b[x+tx[k]][y+ty[k]]=b[x][y]+1
                    q.put((x+tx[k],y+ty[k]))
        if (len(LIST[a[x][y]])==1):
            continue
        for K in LIST[a[x][y]]:
            if (b[K[0]][K[1]]==0):
                b[K[0]][K[1]]=b[x][y]+1
                q.put((K[0],K[1]))
roi_rac_hoa()
LIST=[[] for i in range (n*m+1)]
for i in range (1,m+1):
    for j in range (1,n+1):
        if (a[i][j]>0):
            LIST[a[i][j]].append((i,j))
BFS(x,y)
print(str(b[z][t]-1))
