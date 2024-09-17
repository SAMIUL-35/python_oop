a,b = map(int,input().split()) 

def is_lucky(num):

    return all(digit in '47' for digit in str(num))


lucky=[]

for num in range(a, b + 1):
    if is_lucky(num):
        lucky.append(num)


if lucky:
    print(' '.join(map(str, lucky)))
else:
    print(-1)