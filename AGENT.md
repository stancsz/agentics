# Agentic AI News Fetching Guide

This repository contains daily updates for Chinese AI research news, specifically strictly filtered for "Agentic AI" (autonomous agents, multi-agent frameworks, tool-use, embodied AI, and planning models). This guide explains how to fetch, filter, and format tomorrow's updates.

## Fetching and Filtering
We use a Node.js script to fetch the latest feeds from the following primary sources:
- Media (QbitAI): https://rsshub.app/wechat/mp/msv/gh_1b14da2db2c9
- Media (Synced/机器之心): https://rsshub.app/jiqizhixin/daily
- Media (PaperWeekly via Zhihu): https://rsshub.app/zhihu/people/paperweekly/activities
- Framework (Qwen-Agent): https://github.com/QwenLM/Qwen-Agent/releases.atom
- Academic Repo (Tsinghua THUDM): https://github.com/THUDM/AgentBench/commits/main.atom
- Commercial Repo (DeepSeek): https://github.com/deepseek-ai/DeepSeek-V3/releases.atom
- Academic Papers: http://export.arxiv.org/api/query?search_query=abs:agent+AND+(au:Tsinghua+OR+au:BAAI)&sortBy=submittedDate&sortOrder=descending&max_results=5

1. Run a script using `rss-parser` (for RSS) and `axios` / `xml2js` (for Arxiv) to fetch items.
2. **Handle RSSHub blocks**: If standard `rsshub.app` domains fail, fallback to another active instance (e.g. `rsshub.rssforever.com`) or expand your search to general sources like Arxiv API with queries such as `all:agent AND cat:cs.AI`.
3. Filter content using a date check (only items published in the last 24 hours relative to the current date).
4. Strictly filter content using keywords like "agent", "tool-use", "planning model", "embodied ai", and "multi-agent".

## Deduplication and Translation
1. Ensure the item doesn't already exist in today's file.
2. Translate all Chinese content into professional English.

## File Update Format
Create or append to the file `src/content/YYMMDD/index.md` (e.g., `src/content/260422/index.md` for tomorrow). If the file doesn't exist, create it with the following YAML frontmatter:

```yaml
---
layout: default
title: "Agentic AI Updates: [YYYY-MM-DD]"
date: [YYYY-MM-DD]
---
```

For each new unique item, append it strictly in this format:

```markdown
### [English Translation of Title]
**Sources:** [List of sources, e.g., Synced, Qwen GitHub]
**Links:** [List of URLs]
**TL;DR:** [2-3 sentences summarizing the core breakthrough]
**Agentic Focus:** [1 sentence identifying the specific agentic capability]
```

## Exit Conditions
If no new valid "Agentic AI" items are found within the last 24 hours after checking both primary sources and expanding the search as a fallback, safely exit the run without modifying files or opening a PR.
