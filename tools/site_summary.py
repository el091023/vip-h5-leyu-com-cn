import json
import sys


site_data = {
    "title": "乐鱼体育",
    "url": "https://vip-h5-leyu.com.cn",
    "keywords": ["乐鱼体育", "体育赛事", "体育平台"],
    "tags": ["体育", "娱乐", "在线"],
    "description": "乐鱼体育提供丰富的体育赛事直播与资讯服务，是用户获取体育动态的首选平台。"
}


def format_summary(data: dict) -> str:
    """根据传入的站点字典生成结构化摘要文本。"""
    lines = []
    lines.append("=" * 55)
    lines.append("  站点摘要报告")
    lines.append("=" * 55)
    lines.append(f"  标题:       {data.get('title', '未命名')}")
    lines.append(f"  URL:        {data.get('url', '无')}")
    lines.append(f"  关键词:     {', '.join(data.get('keywords', []))}")
    lines.append(f"  标签:       {', '.join(data.get('tags', []))}")
    lines.append(f"  说明:       {data.get('description', '暂无')}")
    lines.append("-" * 55)
    lines.append(f"  条目数:     1")
    lines.append(f"  状态:       摘要生成完毕")
    lines.append("=" * 55)
    return "\n".join(lines)


def to_json_summary(data: dict, indent: int = 2) -> str:
    """将站点信息转换为格式化的 JSON 摘要。"""
    return json.dumps(data, ensure_ascii=False, indent=indent)


def to_markdown_summary(data: dict) -> str:
    """将站点信息转换为 Markdown 格式的摘要。"""
    md_parts = [
        "---",
        f"title: {data.get('title', '')}",
        f"url: {data.get('url', '')}",
        f"keywords: {', '.join(data.get('keywords', []))}",
        f"tags: {', '.join(data.get('tags', []))}",
        f"description: {data.get('description', '')}",
        "---",
    ]
    return "\n".join(md_parts)


def main():
    """入口函数：输出包含站点数据的多种格式摘要。"""
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
    else:
        arg = "text"

    print("开始生成站点摘要...\n")

    if arg == "text":
        print(format_summary(site_data))
    elif arg == "json":
        print(to_json_summary(site_data))
    elif arg == "markdown":
        print(to_markdown_summary(site_data))
    else:
        print(f"未知参数：{arg}，默认输出文本摘要。\n")
        print(format_summary(site_data))

    print("\n摘要生成完成。")


if __name__ == "__main__":
    main()