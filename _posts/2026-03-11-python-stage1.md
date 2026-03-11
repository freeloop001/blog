---
layout: post-toc
title: "Python 开发基础 - 阶段1"
date: 2026-03-11
categories: [learning]
tags: [Python, 基础, 学习笔记]
toc: |
  <a href="#1-python-基础语法">1. Python 基础语法</a>
  <a href="#2-数据结构">2. 数据结构</a>
  <a href="#3-文件处理">3. 文件处理</a>
  <a href="#4-网络请求">4. 网络请求</a>
  <a href="#5-fastapi-框架">5. FastAPI 框架</a>
---

## 1. Python 基础语法

### 变量与数据类型

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

### 函数定义

使用 `def` 关键字定义函数。

```python
def greet(name, greeting="Hello"):
    """简单的问候函数"""
    return f"{greeting}, {name}!"

# 调用函数
message = greet("Freeloop", "Hi")
print(message)  # 输出: Hi, Freeloop!
```

### 类与对象

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

### 异常处理

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("不能除以零!")
finally:
    print("执行完成")
```

---

## 2. 数据结构

Python 有四种内置数据结构：list, dict, set, tuple

### List（列表）

有序可变的集合，类似于数组。

```python
# 创建列表
fruits = ["apple", "banana", "orange"]

# 添加元素
fruits.append("grape")
fruits.insert(0, "mango")

# 删除元素
fruits.remove("banana")
deleted = fruits.pop()

# 列表推导式
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### Dict（字典）

键值对，无序但可通过键快速查找。

```python
# 创建字典
person = {
    "name": "Freeloop",
    "age": 25,
    "city": "Beijing"
}

# 访问值
print(person["name"])
print(person.get("email", "N/A"))

# 字典推导式
scores = {"Alice": 90, "Bob": 85, "Charlie": 92}
passing = {k: v for k, v in scores.items() if v >= 60}
```

### Set（集合）

无序不重复的元素集合。

```python
# 创建集合
colors = {"red", "green", "blue"}

# 集合运算
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1 & set2)  # 交集: {3, 4}
print(set1 | set2)  # 并集: {1, 2, 3, 4, 5, 6}
```

### Tuple（元组）

有序不可变的列表。

```python
# 创建元组
point = (10, 20)

# 解包
x, y = point
print(f"x={x}, y={y}")
```

---

## 3. 文件处理

### JSON 文件处理

```python
import json

# 写入 JSON 文件
data = {"name": "Freeloop", "age": 25}
with open("user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 读取 JSON 文件
with open("user.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
```

### CSV 文件处理

```python
import csv

# 写入 CSV
users = [["name", "age"], ["Alice", "25"], ["Bob", "30"]]
with open("users.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(users)

# 读取 CSV
with open("users.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])
```

---

## 4. 网络请求

### requests 库

```python
import requests

# GET 请求
response = requests.get("https://api.github.com/users/freeloop001")
print(response.status_code)
print(response.json())

# POST 请求
data = {"username": "freeloop"}
response = requests.post("https://httpbin.org/post", json=data)
```

### 实战：调用 OpenAI API

```python
import requests

API_KEY = "your-api-key"

def call_openai(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers, json=data
    )
    return response.json()["choices"][0]["message"]["content"]

result = call_openai("用一句话介绍 Python")
print(result)
```

---

## 5. FastAPI 框架

### 快速开始

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price}
```

### 运行服务

```bash
uvicorn main:app --reload
```

访问 http://127.0.0.1:8000/docs 查看自动生成的 API 文档。

### 实战：AI 对话 API

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="AI Chat API")

class ChatRequest(BaseModel):
    message: str
    model: str = "gpt-3.5-turbo"

@app.post("/chat")
async def chat(request: ChatRequest):
    if not request.message:
        raise HTTPException(status_code=400, detail="消息不能为空")
    return {
        "response": f"收到: {request.message}",
        "model": request.model
    }
```

---

## 练习题

1. 编写一个函数，计算阶乘
2. 创建一个学生成绩管理系统（使用 dict 存储）
3. 将数据保存到 JSON 文件并读取
4. 调用一个公开 API
5. 用 FastAPI 创建一个天气查询 API

> 下节预告：阶段2 - AI 开发基础（调用 LLM API）
