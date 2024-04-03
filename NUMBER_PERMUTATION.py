s=input();ans=''
s=s.replace('\n','')
sum_digit=0
digit=[0]*10
for k in s:
    sum_digit+=ord(k)-48
    digit[ord(k)-48]+=1
if (sum_digit%3!=0 or digit[0]==0):
    print(str(-1))
else:
    for i in range (9,-1,-1):
        for j in range (1,digit[i]+1):
            ans+=str(i)
    print(ans)
