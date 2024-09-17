s = input().split()

for i in range(len(s)):
    if i != len(s) - 1:
        print(s[i][::-1], end=" ")
    else:
        print(s[i][::-1])
