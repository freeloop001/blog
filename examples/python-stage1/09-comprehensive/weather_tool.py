#!/usr/bin/env python3
"""
综合实战：读取 Excel 文件，调用天气 API，将结果保存为 JSON
"""

import json
import argparse
import openpyxl
import requests
import os
from datetime import datetime

# 天气 API（免费 API 示例）
# 实际使用时替换为真实的天气 API 服务
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "your-api-key")
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"


def read_cities_from_excel(filepath):
    """从 Excel 文件读取城市列表"""
    wb = openpyxl.load_workbook(filepath)
    ws = wb.active

    cities = []
    # 跳过表头，从第二行开始读取
    for row in ws.iter_rows(min_row=2, values_only=True):
        if row[0]:  # 城市名
            cities.append({
                "city": row[0],
                "country": row[1] if len(row) > 1 else ""
            })

    wb.close()
    return cities


def get_weather(city, country=""):
    """调用天气 API 获取城市天气"""
    params = {
        "q": f"{city},{country}" if country else city,
        "appid": WEATHER_API_KEY,
        "units": "metric"  # 使用摄氏度
    }

    try:
        response = requests.get(WEATHER_API_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            return {
                "city": city,
                "country": data.get("sys", {}).get("country", ""),
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"],
                "wind_speed": data["wind"]["speed"],
                "timestamp": datetime.now().isoformat()
            }
        else:
            return {
                "city": city,
                "error": f"API Error: {response.status_code}",
                "timestamp": datetime.now().isoformat()
            }
    except Exception as e:
        return {
            "city": city,
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }


def save_to_json(data, output_path):
    """保存结果到 JSON 文件"""
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"结果已保存到: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="城市天气查询工具")
    parser.add_argument("excel_file", help="Excel 文件路径")
    parser.add_argument("-o", "--output", default="weather_results.json",
                        help="输出 JSON 文件路径")
    parser.add_argument("-k", "--api-key", default=WEATHER_API_KEY,
                        help="天气 API Key")

    args = parser.parse_args()

    if not os.path.exists(args.excel_file):
        print(f"错误: 文件不存在: {args.excel_file}")
        return

    global WEATHER_API_KEY
    WEATHER_API_KEY = args.api_key

    print(f"读取城市列表: {args.excel_file}")
    cities = read_cities_from_excel(args.excel_file)
    print(f"找到 {len(cities)} 个城市")

    results = []
    print("\n查询天气:")
    for city_info in cities:
        city = city_info["city"]
        country = city_info["country"]
        print(f"  查询 {city}...", end=" ")

        weather = get_weather(city, country)
        results.append(weather)

        if "error" in weather:
            print(f"失败 - {weather['error']}")
        else:
            print(f"{weather['temperature']}°C, {weather['description']}")

    save_to_json(results, args.output)


if __name__ == "__main__":
    main()
