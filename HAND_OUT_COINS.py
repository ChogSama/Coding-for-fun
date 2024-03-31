n,m=map(int,input().split())
a=[]
for i in range (m):
    L,R=map(int,input().split())
    if (L<=R):
        a.append((L,0))
        a.append((R,1))
    else:
        a.append((L,0))
        a.append((n,1))
        a.append((1,0))
        a.append((R,1))
a.sort()
count_seg_color,ans=0,0
max_seg_color=[]
for i in range (len(a)):
    if (a[i][1]==0):
        count_seg_color+=1
    else:
        if (ans<=count_seg_color):
            ans=count_seg_color
            max_seg_color.append((ans,a[i][0]-a[i-1][0]+1))
        count_seg_color-=1
count_seg_color=0
for i in range (len(max_seg_color)):
    if (max_seg_color[i][0]==ans):
        count_seg_color+=max_seg_color[i][1]
print(str(ans)+' '+str(count_seg_color))
