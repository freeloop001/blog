---
layout: post
title: "Python 基础语法 - 阶段1第1课"
date: 2026-03-11
categories: [learning]
tags: [Python, 基础, 学习笔记]
---

## 变量与数据类型

Python 是动态类型语言，不需要声明变量类型。

```python
# 基础变量
name = "Freeloop"      # 字符串
age = 25               # 整数
height = 1.75          # 浮点数
is_student = True      # 布尔值

# 打印输出
print(f"姓名: {name}, 年龄: {age}")
```

## 函数定义

使用 `def` 关键字定义函数。

```python
def greet(name, greeting="Hello"):
    """简单的问候函数"""
    return f"{greeting}, {name}!"

# 调用函数
message = greet("Freeloop", "Hi")
print(message)  # 输出: Hi, Freeloop!
```

## 类与对象

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        return f"你好，我叫 {self.name}"

# 创建对象
person = Person("Freeloop", 25)
print(person.say_hello())
```

## 异常处理

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("不能除以零!")
finally:
    print("执行完成")
```

## 实战：创建一个简单的计算器

```python
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("除数不能为零")
        return a / b

# 使用
calc = Calculator()
print(calc.add(10, 5))      # 15
print(calc.divide(10, 2))   # 5.0
```

---

## 练习题

1. 编写一个函数，计算阶乘
2. 创建一个 `Student` 类，包含姓名、学号、成绩
3. 尝试捕获一个除零异常

> 下节预告：数据结构 list, dict, set, tuple
