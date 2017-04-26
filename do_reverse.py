L = []


def get_num(n):
    while n > 0:
        L.insert(0, n % 10)
        n = n // 10


while True:
    temp = input('Input a num: ')
    if temp.isdigit():
        get_num(int(temp))
        break
    else:
        print('', end='')
# while True:
#     try:
#         temp = input("Input a num: ")
#         get_num(int(temp))
#         break
#     except ValueError:
#         print('', end='')

print(L)


strA = input("Input the Int:")
order = []
for i in strA:
    order.append(i)
print(order)
order.reverse()  # 将列表反转
print(''.join(order))  # 将list转换成字符串
