#!/usr/bin/env python3
"""生成示例 Excel 文件"""
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Cities"

# 表头
ws.append(["city", "country"])

# 示例数据
cities = [
    ["Beijing", "cn"],
    ["Shanghai", "cn"],
    ["Tokyo", "jp"],
    ["New York", "us"],
    ["London", "uk"]
]

for city in cities:
    ws.append(city)

wb.save("cities.xlsx")
print("已生成 cities.xlsx")
