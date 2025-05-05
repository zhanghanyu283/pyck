print(1000)
print(0b1000)
print(0o1000)
print(0x1000)

print(1000)
print(bin(1000))
print(oct(1000))
print(hex(1000))

a = "0123456789"

# 截取从 2~5 的字符串
result1 = a[2:6]
print("1）从 2~5 的字符串:", result1)
#如果要截取从a到b的字符串，需要写成[a包含:b+1不包含]

# 2）截取从 2 ~末尾 的字符串
result2 = a[2:]
print("2）从 2 ~末尾 的字符串:", result2)

# 3）截取从 开始~5的字符串
result3 = a[:6]
print("3）从 开始~5的字符串:", result3)

# 4）截取完整的字符串
result4 = a[:]
print("4）完整的字符串:", result4)

# 5）从开始位置，每隔一个字符截取字符串
result5 = a[::2]
print("5）从开始位置，每隔一个字符截取字符串:", result5)

# 6）从索引 1 开始，每隔一个取一个
result6 = a[1::2]
print("6）从索引 1 开始，每隔一个取一个:", result6)

# 7）截取从 2~末尾-1 的字符串
result7 = a[2:-1]
print("7）从 2~末尾-1 的字符串:", result7)

# 8）截取字符串末尾两个字符
result8 = a[-2:]
print("8）字符串末尾两个字符:", result8)

# 9）字符串的逆序
result9 = a[::-1]
print("9）字符串的逆序:", result9)


    
    