---
layout: post
title: "Python 网络请求 - 阶段1第4课"
date: 2026-03-11
categories: [learning]
tags: [Python, requests, httpx, API, 学习笔记]
---

网络请求是 AI 开发中必不可少技能。

## 安装依赖

```bash
pip install requests httpx
```

## requests 库

最常用的 HTTP 库。

```python
import requests

# GET 请求
response = requests.get("https://api.github.com/users/freeloop001")
print(response.status_code)  # 200
print(response.json())       # 解析 JSON 响应

# 带参数的 GET 请求
params = {"page": 1, "per_page": 10}
response = requests.get("https://api.github.com/users", params=params)

# POST 请求
data = {"username": "freeloop", "password": "123456"}
response = requests.post("https://httpbin.org/post", json=data)

# 设置请求头
headers = {"Authorization": "Bearer YOUR_TOKEN"}
response = requests.get("https://api.github.com/user", headers=headers)

# 超时设置
response = requests.get("https://example.com", timeout=10)
```

## httpx 库

支持同步和异步，更现代化。

```python
import httpx

# 同步请求（与 requests 用法类似）
response = httpx.get("https://api.github.com/users/freeloop001")
print(response.status_code)
print(response.json())

# POST 请求
response = httpx.post(
    "https://httpbin.org/post",
    json={"key": "value"}
)

# 异步请求
import asyncio

async def fetch_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/users/freeloop001")
        return response.json()

# 运行异步函数
result = asyncio.run(fetch_data())
print(result)
```

## 实战：调用 OpenAI API

```python
import os
import requests

# 设置 API Key（建议使用环境变量）
API_KEY = os.getenv("OPENAI_API_KEY", "your-api-key")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def call_openai(prompt):
    """调用 OpenAI GPT API"""
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        json=data
    )

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}"

# 使用
result = call_openai("用一句话介绍 Python")
print(result)
```

## 实战：调用 Claude API

```python
import requests

API_KEY = "your-anthropic-api-key"

def call_claude(prompt):
    """调用 Anthropic Claude API"""
    headers = {
        "x-api-key": API_KEY,
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json"
    }

    data = {
        "model": "claude-3-haiku-20240307",
        "max_tokens": 1024,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers=headers,
        json=data
    )

    if response.status_code == 200:
        return response.json()["content"][0]["text"]
    else:
        return f"Error: {response.status_code} - {response.text}"

# 使用
result = call_claude("用一句话介绍 Python")
print(result)
```

---

## 错误处理

```python
import requests

def safe_request(url, retries=3):
    """带重试的请求"""
    for i in range(retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # 检查 HTTP 错误
            return response
        except requests.exceptions.RequestException as e:
            print(f"请求失败 ({i+1}/{retries}): {e}")
    return None
```

---

## 练习

1. 调用一个公开 API（如 GitHub API）
2. 封装一个通用的 API 调用函数
3. 实现请求失败自动重试功能

> 下节预告：FastAPI Web 框架
