# def sa():
#     print('samiul')

# sa()

# def double_it(num):
#     result = num *2
#     print(result)


# double_it(8)
# def sum(num1,num2):
#     result =num1 +num2
#     return result
# total = sum(8,16)
# print(total)

def all_sum(*numbers):
    print(numbers)
    sum=0
    for num in numbers:
        sum += num
    return sum

total = all_sum(45,15,20)
print('all sum ',total)