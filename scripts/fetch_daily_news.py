import os
import time
import requests
import feedparser
import json
from datetime import datetime, timedelta, timezone
import xml.etree.ElementTree as ET
import urllib.request
import urllib.parse

def fetch_feed(url, source_name):
    print(f"Fetching {source_name}: {url}")
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=15)
        feed = feedparser.parse(response.content)
        return feed.entries
    except Exception as e:
        print(f"Error fetching {source_name}: {e}")
        return []

def main():
    sources = [
        ("QbitAI", "https://www.qbitai.com/feed"),
        ("Synced", "https://www.jiqizhixin.com/rss"),
        ("PaperWeekly", "https://raw.githubusercontent.com/osnsyc/Wechat-Scholar/main/channels/gh_5138cebd4585.xml"),
        ("Qwen-Agent", "https://github.com/QwenLM/Qwen-Agent/releases.atom"),
        ("THUDM/AgentBench", "https://github.com/THUDM/AgentBench/commits/main.atom"),
        ("DeepSeek-V3", "https://github.com/deepseek-ai/DeepSeek-V3/releases.atom"),
        ("Arxiv", "https://export.arxiv.org/api/query?search_query=abs:agent+AND+%28au:Tsinghua+OR+au:BAAI%29&sortBy=submittedDate&sortOrder=descending&max_results=5")
    ]

    recent_items = []
    now = datetime.now(timezone.utc)

    for name, url in sources:
        entries = fetch_feed(url, name)
        for entry in entries:
            # Parse date
            pub_date = None
            if hasattr(entry, 'published_parsed') and entry.published_parsed:
                pub_date = datetime.fromtimestamp(time.mktime(entry.published_parsed), timezone.utc)
            elif hasattr(entry, 'updated_parsed') and entry.updated_parsed:
                pub_date = datetime.fromtimestamp(time.mktime(entry.updated_parsed), timezone.utc)

            if pub_date:
                # Check if within last 24 hours
                if now - pub_date <= timedelta(hours=24):
                    recent_items.append({
                        "source": name,
                        "title": entry.get('title', ''),
                        "link": entry.get('link', ''),
                        "summary": entry.get('summary', entry.get('description', ''))[:1000], # truncate summary
                        "date": pub_date.isoformat()
                    })

    # Fetch more from cs.AI arxiv
    print(f"Fetching Arxiv RSS: https://export.arxiv.org/rss/cs.AI")
    req = urllib.request.Request("https://export.arxiv.org/rss/cs.AI", headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            root = ET.fromstring(data)
            for item in root.findall(".//item"):
                title = item.findtext("title", "").strip()
                link = item.findtext("link", "").strip()
                desc = item.findtext("description", "").strip()
                pub_date = item.findtext("pubDate", "")
                # Assume today since we fetch daily
                recent_items.append({
                    "source": "Arxiv cs.AI",
                    "title": title,
                    "link": link,
                    "summary": desc[:1000],
                    "date": now.isoformat()
                })
    except Exception as e:
        print(f"Error fetching cs.AI: {e}")

    with open('recent_news.json', 'w', encoding='utf-8') as f:
        json.dump(recent_items, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    main()
