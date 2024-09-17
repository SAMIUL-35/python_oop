t=int(input())
for k in range(t):
    n=int(input())
    li=map(int,input().split())
    li1=list(li)
    ans=[]

    for i in range(n-1):
        for j in range(i+1,n):
            ans.append(li1[i]+li1[j]+j-i)

    print(min(ans))

