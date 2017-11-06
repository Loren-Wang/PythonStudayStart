# message = "hello world"
# print(message)
# message = "hello python world"
# print(message)
#
# # 首字母大写
# print("哈哈 abc def".title())
# # 制表符
# print("\tPython")
# # 移除空白
# # 移除首部空白
# print("  Hello World ".lstrip())
# # 移除尾部空白
# print("  Hello World ".rstrip())
# # 移除两侧空白
# print("  Hello World ".strip())
# # 移除首部H
# print("HHHHello World ".lstrip("H"))
# # 移除尾部d
# print("Hello Worlddd".rstrip("d"))
# # 移除两侧Hd
# print("HHHHello Worldddd".strip("Hd"))
# # 移除首部h
# print("HHHHello World ".lstrip("h"))
# # 移除尾部D
# print("Hello Worlddd".rstrip("D"))
# # 移除两侧hD
# print("HHHHello Worldddd".strip("hD"))
#
#
# print(10 * 0.1)
#
# # 删除列表元素
# listContent = ['t','f','s']
# popValue = listContent.pop(listContent.index('f'))
# print(listContent)
# print(popValue)
#
# # 列表循环输出
# animals = ['cat','dog','pig']
# for animal in animals:
#     print(animal)
# print('\n')
#
# for animal in animals:
#     print(animal)
#     print(animal)
# print('\n')
#
# for animal in animals:{
#     print(animal),
#     print(animal),
#     print(animal)
# }
# print('\n')
#
# for rang in range(1,5):
#     print(rang)


# 打印1-20
print('打印1-20')
for int in range(1,21):
    print(int)



# 计算1-1000000的和
print('\n\n计算1-1000000的和')
print(sum(range(1,1000001)))

print('\n\n计算1-1000000的最小值以及最大值')
print(min(range(1,1000001)))
print(max(range(1,1000001)))

print('\n\n循环打印1-20中的所有奇数')
for int in range(1,21,2):
    print(int)




print('\n\n生成一个可以被3整除的数组并使用for循环打印')
for int in range(3,30,3):
    print(int)

print('\n\n生成1-10的立方，并用for循环打印')
for int in range(1,10):
    value = int ** 3
    print(value)


print('\n\n使用列表解析生成一个包含十个整数立方的列表')
ints = [value ** 3 for value in range(1,10)]
print(ints)


























