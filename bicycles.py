bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# 访问列表元素
print(bicycles[0])
print(bicycles[0].title())

# 修改元素列表
bicycles[0] = bicycles[0].title()
print(bicycles)

# 在列表中添加元素
## 在列表尾部添加元素
bicycles.append('ducati')
print(bicycles)

## 在列表插入元素
bicycles.insert(0, 'ducati')
print(bicycles)

# 从列表中删除元素
## 从列表中删除元素
del bicycles[0]
print(bicycles)

## 从列表尾部删除元素
pop_elm = bicycles.pop()
print(pop_elm)
print(bicycles)

## 根据值删除元素
bicycles.remove('cannondale')
print(bicycles)

# 使用sort对列表进行排序
arr = [10,9,8,7,6,5,4,3,2,1]
arr.sort()
print(arr)
arr.sort(reverse = True)
print(arr)

# 反转序列
bicycles.reverse()
print(bicycles)

# 查看序列长度
print(f'bicycles length: {len(bicycles)}')
