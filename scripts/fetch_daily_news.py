import urllib.request
import feedparser
from datetime import datetime, timedelta, timezone

def fetch_feed(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
            d = feedparser.parse(data)
            return d.entries
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []

urls = [
    "https://www.qbitai.com/feed",
    "https://www.jiqizhixin.com/rss",
    "https://raw.githubusercontent.com/osnsyc/Wechat-Scholar/main/channels/gh_5138cebd4585.xml",
    "https://github.com/QwenLM/Qwen-Agent/releases.atom",
    "https://github.com/THUDM/AgentBench/commits/main.atom",
    "https://github.com/deepseek-ai/DeepSeek-V3/releases.atom",
    "https://export.arxiv.org/api/query?search_query=abs:agent+AND+%28au:Tsinghua+OR+au:BAAI%29&sortBy=submittedDate&sortOrder=descending&max_results=5",
    "https://export.arxiv.org/api/query?search_query=all:agent&sortBy=submittedDate&sortOrder=descending&max_results=5"
]

all_entries = []
now = datetime.now(timezone.utc)
twenty_four_hours_ago = now - timedelta(hours=24)

for url in urls:
    entries = fetch_feed(url)
    for e in entries:
        if 'published_parsed' in e and e.published_parsed:
            dt = datetime(*e.published_parsed[:6], tzinfo=timezone.utc)
            if dt >= twenty_four_hours_ago:
                all_entries.append((dt, url, e.title, e.link, getattr(e, 'description', getattr(e, 'summary', ''))))

valid_entries = []
for dt, url, title, link, summary in sorted(all_entries):
    title_lower = title.lower()
    summary_lower = summary.lower()
    if 'agent' in title_lower or 'agent' in summary_lower or '智能体' in title or '智能体' in summary:
        # Exclude generic AI news without agentic focus
        valid_entries.append((dt, url, title, link, summary))

print(f"Found {len(valid_entries)} valid entries in the last 24 hours:")
for e in valid_entries:
    print("-" * 50)
    print(f"Title: {e[2]}")
    print(f"Link: {e[3]}")
    print(f"Source URL: {e[1]}")
    print(f"Date: {e[0]}")
    print(f"Summary Snippet: {e[4][:200]}...")
