num=input()
num1=num[::-1]

num2=num1.lstrip('0')
print(int(num2))

if num==num1:
    print('YES')

else: print("NO")

