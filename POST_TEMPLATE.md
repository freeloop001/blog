# 文章模板

创建新文章时，在 `_posts` 目录下新建文件，命名格式：`YYYY-MM-DD-title.md`

```yaml
---
layout: post-toc
title: "文章标题"
date: 2026-03-11 16:00:00 +0800
categories: [learning]
tags: []
toc: |
  <a href="#1-标题1">1. 标题1</a>
  <a href="#2-英文-subtitle">2. 英文 Subtitle</a>
---

## 1. 标题1

内容...

## 2. 英文 Subtitle

内容...
```

**注意**：
- `layout`: 使用 `post-toc`（有目录）或 `post`（无目录）
- `date`: 必须包含精确时间，格式为 `YYYY-MM-DD HH:MM:SS +0800`
- `toc`: 目录链接需与正文中 `##` 标题的 id 对应

**Kramdown ID 生成规则**：
- 标题 `## 1. 标题1` → id `#1-标题1`
- 标题 `## 2. English Title` → id `#2-english-title`
- 标题 `## 3. 英文 (Subtitle)` → id `#3-英文-subtitle`
- 标题中的括号内容也会转为小写连字符
