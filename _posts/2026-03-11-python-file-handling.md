---
layout: post
title: "Python 文件处理 - 阶段1第3课"
date: 2026-03-11
categories: [learning]
tags: [Python, 文件处理, JSON, CSV, 学习笔记]
---

文件处理是 Python 开发中非常重要的技能。

## JSON 文件处理

JSON 是最常用的数据交换格式。

```python
import json

# 写入 JSON 文件
data = {
    "name": "Freeloop",
    "age": 25,
    "skills": ["Python", "JavaScript", "Go"],
    "is_developer": True
}

with open("user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 读取 JSON 文件
with open("user.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print(loaded_data["name"])  # Freeloop

# 字符串与 JSON 互转
json_str = json.dumps(data, ensure_ascii=False)
parsed = json.loads(json_str)
```

## CSV 文件处理

```python
import csv

# 写入 CSV 文件
users = [
    ["name", "age", "city"],
    ["Alice", "25", "Beijing"],
    ["Bob", "30", "Shanghai"],
    ["Charlie", "28", "Guangzhou"]
]

with open("users.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(users)

# 读取 CSV 文件
with open("users.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# 读取为字典格式
with open("users.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])
```

## 实战：学生成绩管理系统

```python
import json
import csv

# 保存成绩到 JSON
def save_scores(scores, filename="scores.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(scores, f, ensure_ascii=False, indent=2)

# 从 JSON 加载成绩
def load_scores(filename="scores.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# 保存成绩到 CSV
def export_to_csv(scores, filename="scores.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["姓名", "科目", "成绩"])
        for s in scores:
            writer.writerow([s["name"], s["subject"], s["score"]])

# 测试
scores = [
    {"name": "Alice", "subject": "Math", "score": 95},
    {"name": "Bob", "subject": "Math", "score": 87},
    {"name": "Alice", "subject": "English", "score": 92}
]

save_scores(scores)
export_to_csv(scores)
print("数据已保存!")
```

## 其他常用文件操作

```python
# 读取整个文件
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 按行读取
with open("file.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# 写入文件
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello World!\n")
    f.write("第二行")

# 追加内容
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("\n新日志条目")
```

---

## 练习

1. 读取一个 CSV 文件，计算某一列的总和
2. 将 JSON 数据转换为 CSV 格式
3. 创建一个简单的文本文件日志系统

> 下节预告：网络请求 requests, httpx
