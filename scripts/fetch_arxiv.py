#!/usr/bin/env python3
"""
Fetch latest AI/Agentic papers from Arxiv.
Writes results to news/content/YYYYMMDD/arxiv.md
"""

import os
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime

ARXIV_RSS = "https://export.arxiv.org/rss/cs.AI"
TODAY = datetime.now().strftime("%Y%m%d")
OUT_DIR = f"news/content/{TODAY}"
OUT_FILE = f"{OUT_DIR}/arxiv.md"


def fetch_arxiv_feed(url=ARXIV_RSS):
    print(f"Fetching Arxiv RSS: {url}")
    req = urllib.request.Request(url, headers={"User-Agent": "Meow-Agent/1.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read()


def parse_rss(data):
    root = ET.fromstring(data)
    items = []
    for item in root.findall(".//item"):
        title = item.findtext("title", "").strip()
        link = item.findtext("link", "").strip()
        desc = item.findtext("description", "").strip()
        pub_date = item.findtext("pubDate", "")
        items.append({"title": title, "link": link, "desc": desc, "date": pub_date})
    return items


def build_markdown(items):
    lines = [
        f"## Arxiv AI Papers — {datetime.now().strftime('%Y-%m-%d')}\n",
        f"*Source: [arXiv cs.AI](https://arxiv.org/list/cs.AI/recent)*\n",
    ]
    for it in items:
        lines.append(f"### [{it['title']}]({it['link']})")
        lines.append(f"**Published:** {it['date']}")
        desc = it["desc"].replace("<![CDATA[", "").replace("]]>", "").strip()
        if desc:
            lines.append(f"**Summary:** {desc[:300]}...")
        lines.append("")
    return "\n".join(lines)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    data = fetch_arxiv_feed()
    items = parse_rss(data)
    print(f"Found {len(items)} papers")

    md = build_markdown(items)

    # Append to existing or create new
    if os.path.exists(OUT_FILE):
        with open(OUT_FILE) as f:
            existing = f.read()
        # Avoid duplicates
        if "Arxiv AI Papers" in existing:
            print("Arxiv section already exists, skipping.")
            return

    with open(OUT_FILE, "a") as f:
        f.write("\n" + md)

    print(f"Written to {OUT_FILE}")


if __name__ == "__main__":
    main()