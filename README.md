# Agentics Research News 🏹

> AI/Agentic news aggregator with a focus on Chinese AI developments.

Built and maintained by **Meow** for **stancsz**.

## Repository Structure

```
agentics-research-news/
│
├── AGENT.md              # ← Agent specification (START HERE)
├── README.md             # This file
├── MISSION.md            # Long-term roadmap and study plan
│
├── .claude/
│   └── skills/
│       └── agentics-research-news/
│           └── SKILL.md  # ← Claude Code skill for this repo
│
├── .github/
│   └── workflows/
│       └── agent.yml     # GitHub Actions: daily automated runs
│
├── scripts/
│   └── fetch_arxiv.py    # Fetch latest papers from Arxiv
│
├── docs/                 # GitHub Pages site (github.io)
│   ├── index.md          # Landing page
│   ├── MISSION.md        # Mirrors root MISSION.md
│   └── research/          # Deep-dive research reports
│
├── news/                 # Daily news aggregations
│   ├── README.md         # Format guide
│   └── content/
│       └── YYYYMMDD/
│           └── index.md  # Daily entry
│
├── studies/              # Deep-dive studies on AI leaders
│   ├── karpathy/         # Andrej Karpathy
│   ├── mollick/         # Ethan Mollick
│   ├── fridman/          # Lex Fridman
│   ├── tan/              # Garry Tan
│   ├── raschka/          # Sebastian Raschka
│   ├── howard/           # Jeremy Howard
│   └── hermes-agent/     # Nous Research Hermes Agent
│
└── repos/                # Cloned repos for code study
    ├── llm.c/            # Karpathy's LLM in pure C
    ├── minGPT/           # Minimal GPT implementation
    └── nanoGPT/           # nanoGPT (production-focused)
```

## Quick Links

| Section | Description |
|---------|-------------|
| [docs/](docs/) | GitHub Pages site |
| [news/content/](news/content/) | Daily AI/Agentic news |
| [studies/](studies/) | Deep dives on AI leaders |
| [repos/](repos/) | Studied code repositories |

## For Agents

Load the **agentics-research-news skill** before working in this repo:

```bash
git clone https://github.com/stancsz/agentics-research-news /tmp/arn
mkdir -p .claude/skills/agentics-research-news
cp /tmp/arn/.claude/skills/agentics-research-news/SKILL.md .claude/skills/agentics-research-news/
```

Then read `AGENT.md` for your full instructions.

## Tech Stack

- **Arxiv API** for paper fetching
- **GitHub Actions** for daily automation
- **GitHub Pages** for public site (docs/)
- **Meow brain** for memory and context

---

*Last updated: 2026-04-21*