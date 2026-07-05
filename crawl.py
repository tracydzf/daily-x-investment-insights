import os
from datetime import datetime, timedelta
import json

# 博主列表 (可配置)
BLOGGERS = [
    "blknoiz06", "aleabitoreddit", "qinbafrank",
    "xiaomustock", "yijiangren", "AntonLaVay",
    "yuyue_chris", "labubu_trader"
]

def get_today():
    return datetime.now().strftime("%Y-%m-%d")

def create_daily_folder(date_str):
    folder = date_str
    os.makedirs(folder, exist_ok=True)
    return folder

def generate_summary(date_str):
    summary = f"""# {date_str} Daily Investment Insights

## 博主采集列表
{chr(10).join([f'- @{{b}}' for b in BLOGGERS])}

## 核心投资洞见
(自动化总结占位 - 实际集成 X 数据分析)

**更新时间**: {{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}}

仅供参考，非投资建议。
"""
    with open(f"{{date_str}}/summary.md", "w", encoding="utf-8") as f:
        f.write(summary)
    print(f"Generated summary for {{date_str}}")

if __name__ == "__main__":
    today = get_today()
    create_daily_folder(today)
    generate_summary(today)
    print("✅ Daily crawl completed!")