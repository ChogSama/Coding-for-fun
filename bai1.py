def get_sum(a,b):
    return (a+b)*(b-a+1)//2
d,c=map(int,input().split())
L,R=d,c
diff=int(1e18)
ans=0
while (L<=R):
    mid=(L+R)//2
    first_sum=get_sum(d,mid)
    last_sum=get_sum(mid+1,c)
    if (diff>abs(first_sum-last_sum)):
        diff=abs(first_sum-last_sum)
        ans=mid
    if (first_sum<last_sum):
        L=mid+1
    else:
        R=mid-1
print(str(ans))