a,b=map(int,(input().split()))
c=input()
ans=False
if a+b+1==len(c) and c[a]=='-':
    ans=True

for i,j in enumerate(c):
   if i==a:
       continue
   else:
       if not j.isdigit():
           ans=False
    
if ans:
    print("Yes")
else:
    print("No")