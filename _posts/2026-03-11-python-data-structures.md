---
layout: post
title: "Python 数据结构 - 阶段1第2课"
date: 2026-03-11
categories: [learning]
tags: [Python, 数据结构, 学习笔记]
---

Python 有四种内置数据结构：list, dict, set, tuple

## List（列表）

有序可变的集合，类似于数组。

```python
# 创建列表
fruits = ["apple", "banana", "orange"]

# 添加元素
fruits.append("grape")
fruits.insert(0, "mango")  # 插入到指定位置

# 删除元素
fruits.remove("banana")    # 删除指定值
deleted = fruits.pop()     # 删除最后一个

# 遍历
for fruit in fruits:
    print(fruit)

# 列表推导式
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## Dict（字典）

键值对，无序但可通过键快速查找。

```python
# 创建字典
person = {
    "name": "Freeloop",
    "age": 25,
    "city": "Beijing"
}

# 访问值
print(person["name"])           # Freeloop
print(person.get("email", "N/A"))  # N/A（默认值）

# 添加/修改
person["email"] = "test@example.com"
person["age"] = 26

# 遍历
for key, value in person.items():
    print(f"{key}: {value}")

# 字典推导式
scores = {"Alice": 90, "Bob": 85, "Charlie": 92}
passing = {k: v for k, v in scores.items() if v >= 60}
print(passing)  # {'Alice': 90, 'Bob': 85, 'Charlie': 92}
```

## Set（集合）

无序不重复的元素集合。

```python
# 创建集合
colors = {"red", "green", "blue"}

# 添加元素
colors.add("yellow")
colors.add("red")  # 重复元素会被忽略

# 删除元素
colors.discard("green")  # 不存在不会报错
colors.remove("blue")    # 不存在会报错

# 集合运算
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1 & set2)  # 交集: {3, 4}
print(set1 | set2)  # 并集: {1, 2, 3, 4, 5, 6}
print(set1 - set2)  # 差集: {1, 2}
```

## Tuple（元组）

有序不可变的列表，创建后不能修改。

```python
# 创建元组
point = (10, 20)
rgb = (255, 128, 0)

# 访问元素
print(point[0])  # 10

# 解包
x, y = point
print(f"x={x}, y={y}")  # x=10, y=20

# 元组作为字典键（因为不可变）
locations = {
    (10, 20): "Point A",
    (30, 40): "Point B"
}
```

## 实战：学生信息管理

```python
students = [
    {"name": "Alice", "score": 90},
    {"name": "Bob", "score": 85},
    {"name": "Charlie", "score": 92}
]

# 按成绩排序
students_sorted = sorted(students, key=lambda x: x["score"], reverse=True)
print(students_sorted)

# 计算平均分
avg_score = sum(s["score"] for s in students) / len(students)
print(f"平均分: {avg_score:.2f}")
```

---

## 小结

| 类型 | 有序 | 可变 | 用途 |
|------|------|------|------|
| list | ✅ | ✅ | 有序列表 |
| dict | ❌ | ✅ | 键值对映射 |
| set | ❌ | ❌ | 去重集合 |
| tuple | ✅ | ❌ | 固定数据 |

> 下节预告：文件处理 JSON, CSV
