# 使用range函数打印1-4
for value in range(1,5):
    print(value)

# 使用range函数为list初始化
even_number = list(range(1,5))
print(even_number)

# 使用有步增的range函数
even_number = list(range(2,11,2))
print(even_number)

# 打印（1，10）的平方
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

# 简单统计计算
digits = [1,2,3,4,5,6,7,8,9,0]
print(max(digits))
print(min(digits))
print(sum(digits))

# 使用切片
players = ['charles', 'martina', 'minchael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[-3:])

# 遍历切片
for player in players[-3:]:
    print(player.title())

# 复制列表
copy_players = players[:]
print(copy_players)





