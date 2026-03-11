---
layout: post
title: "FastAPI Web 框架 - 阶段1第5课"
date: 2026-03-11
categories: [learning]
tags: [Python, FastAPI, Web, API, 学习笔记]
---

FastAPI 是现代 Python Web 框架，用于构建 API，速度快、易上手。

## 安装

```bash
pip install fastapi uvicorn
```

## 快速开始

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 定义数据模型
class Item(BaseModel):
    name: str
    price: float
    is_available: bool = True

# GET 请求
@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "name": "Item"}

# POST 请求
@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price}
```

## 运行服务

```bash
uvicorn main:app --reload
```

访问 http://127.0.0.1:8000 查看，自动生成 API 文档：http://127.0.0.1:8000/docs

## 路由与参数

```python
from fastapi import FastAPI, Query, Path, Header
from typing import Optional

app = FastAPI()

# 查询参数
@app.get("/search")
def search(q: str = Query(..., min_length=2), limit: int = Query(10, le=100)):
    return {"query": q, "limit": limit}

# 路径参数
@app.get("/users/{user_id}")
def get_user(user_id: int = Path(..., gt=0)):
    return {"user_id": user_id}

# Header 参数
@app.get("/headers")
def get_headers(user_agent: Optional[str] = Header(None)):
    return {"user_agent": user_agent}
```

## 请求体与响应

```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    name: str
    email: str
    age: Optional[int] = None

class UserResponse(BaseModel):
    name: str
    email: str

@app.post("/users/", response_model=UserResponse)
def create_user(user: User):
    """创建用户，返回简化后的响应"""
    return UserResponse(name=user.name, email=user.email)
```

## 实战：简单的 AI 对话 API

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI(title="AI Chat API")

class ChatRequest(BaseModel):
    message: str
    model: str = "gpt-3.5-turbo"

class ChatResponse(BaseModel):
    response: str
    model: str

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """简单的 AI 对话接口"""
    if not request.message:
        raise HTTPException(status_code=400, message="消息不能为空")

    # 这里替换为实际的 API 调用
    return ChatResponse(
        response=f"收到消息: {request.message} (使用模型: {request.model})",
        model=request.model
    )

@app.get("/models")
def get_models():
    """获取可用模型列表"""
    return {
        "models": [
            "gpt-3.5-turbo",
            "gpt-4",
            "claude-3-haiku"
        ]
    }
```

## 中间件

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 错误处理

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id == 0:
        raise HTTPException(status_code=400, detail="ID 不能为 0")
    return {"item_id": item_id}
```

## 项目结构建议

```
myapi/
├── main.py           # 主应用
├── routers/          # 路由模块
│   ├── users.py
│   └── items.py
├── models/           # 数据模型
├── services/         # 业务逻辑
└── requirements.txt
```

---

## 练习

1. 创建一个天气预报 API
2. 编写一个文件上传接口
3. 实现用户认证功能

> 阶段1 完结！下一步：AI 开发基础 - 调用 LLM API
