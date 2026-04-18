# Hermes Agent — Nous Research (97k stars)
> "The only agent with a built-in learning loop"

## What It Is

An open-source **self-improving AI agent** built by Nous Research. It creates skills from experience, improves them during use, searches its own past conversations, and builds a deepening model of the user across sessions.

## Key Architectural Insights

### 1. Multi-Platform Backend
```
hermes agent runs on: local, Docker, SSH, Daytona, Singularity, Modal
```
Daytona/Modal = serverless persistence (hibernates when idle, wakes on demand). Deploy from $5 VPS to GPU cluster.

### 2. Multi-Interface Design
- **Local CLI** — full TUI interactive session
- **Messaging Gateway** — Telegram, Discord, Slack, WhatsApp, Signal, email
- One gateway process handles ALL messaging integrations

### 3. Memory System (The Core Innovation)
The `MemoryManager` orchestrates **one builtin provider + at most ONE external provider** (prevents tool schema bloat):

```python
class MemoryManager:
    # Providers register themselves
    def add_provider(self, provider: MemoryProvider) -> None:
        # Builtin provider always first
        # Only ONE external provider allowed at a time
        ...

    # Lifecycle hooks
    def prefetch_all(query, session_id)     # Pre-turn recall
    def sync_all(user_msg, assistant_msg)   # Post-turn persistence
    def queue_prefetch_all(query)           # Background prefetch for next turn
    def on_turn_start(turn_number, message) # Per-turn notification
    def on_session_end(messages)            # Session boundary
    def on_pre_compress(messages)          # Before context compression
```

**Memory Context Injection Pattern:**
```python
# Fenced injection prevents model from treating recall as user discourse
def build_memory_context_block(raw_context: str) -> str:
    return (
        "<memory-context>\n"
        "[System note: The following is recalled memory context, "
        "NOT new user input. Treat as informational background data.]\n\n"
        f"{clean}\n"
        "</memory-context>"
    )
```

### 4. Skill System (Procedural + Self-Improving)
Skills are markdown files with YAML frontmatter:
```yaml
---
name: github
platforms: [macos, linux]
metadata:
  hermes:
    config:
      - key: wiki.path
        description: Path to LLM Wiki knowledge base
        default: "~/wiki"
        prompt: Wiki directory path
---
# Skill body...
```

**Key skill utils (`skill_utils.py`):**
- `parse_frontmatter()` — YAML frontmatter + body separation
- `skill_matches_platform()` — OS compatibility check
- `get_disabled_skill_names()` — reads from `config.yaml`
- `get_external_skills_dirs()` — supports external skill directories
- `extract_skill_conditions()` — `fallback_for_toolsets`, `requires_toolsets`
- `extract_skill_config_vars()` — declare config.yaml deps in frontmatter

**Skills indexed by `build_skills_system_prompt()`** with two-layer caching (in-process LRU + disk snapshot).

### 5. Context Engine Plugin Architecture
`ContextEngine` is a pluggable ABC. Default: `ContextCompressor`. Swap via `context.engine` in `config.yaml`.

```python
class ContextEngine(ABC):
    def update_from_response(usage)  # After each LLM call
    def should_compress(prompt_tokens) -> bool
    def compress(messages) -> List[Dict]  # Summarize/split/etc
    # Lifecycle
    def on_session_start(session_id)
    def on_session_end(session_id, messages)
    def on_session_reset()  # On /new or /reset
    # Tools (optional)
    def get_tool_schemas()  # e.g. lcm_grep, lcm_expand
```

### 6. Prompt Builder (`prompt_builder.py`)
Assembles system prompts from:
- `.hermes.md` / `HERMES.md` (walks to git root)
- `SOUL.md` (from HERMES_HOME)
- `AGENTS.md` / `CLAUDE.md` / `.cursorrules`
- **Skills system prompt** (cached, categorized index)
- **Platform hints** (WhatsApp, Telegram, Discord, Slack, email, CLI, etc.)
- **Model-specific guidance** (OpenAI tool enforcement, Google operational guidance)
- **Environment hints** (WSL filesystem translation)

**Prompt injection detection:** Scans context files for hidden unicode, instruction overrides, exfiltration attempts.

### 7. Model Flexibility
Any provider via `hermes model`: Nous Portal, OpenRouter (200+ models), NVIDIA NIM, Hugging Face, OpenAI, custom endpoints.

### 8. Zero-Cost RPC
Write Python scripts calling agent tools via RPC — collapses multi-step pipelines.

### 9. Parallel Subagents
Spawn isolated subagents for parallel workstreams. Memory system has `on_delegation()` hook.

## Code Structure

```
agent/
├── memory_manager.py      # Core memory orchestrator
├── memory_provider.py     # ABC for memory backends
├── builtin_memory_provider.py
├── context_engine.py      # ABC for compression strategies
├── context_compressor.py  # Default summarization engine
├── prompt_builder.py      # System prompt assembly
├── skill_utils.py         # Skill discovery & frontmatter parsing
├── skill_commands.py      # /skill slash commands
├── retry_utils.py         # Error classification & retry logic
├── trajectory.py          # RL trajectory handling
└── models_dev.py          # Model metadata & routing

gateway/                   # Messaging platform integrations
skills/                    # Skill definitions (categorized)
├── autonomous-ai-agents/
├── github/
├── research/
├── mlops/
├── productivity/
... (25+ categories)
```

## Key Lessons for Agent Architecture

1. **Single external memory provider** — prevents schema bloat and conflicts
2. **Fenced memory context** — prevents recall from being treated as user input
3. **Lifecycle hooks everywhere** — `on_turn_start`, `on_session_end`, `on_pre_compress`, `on_delegation`
4. **Skill frontmatter > code config** — declare dependencies in YAML frontmatter, not hardcoded
5. **Context compression is pluggable** — swap summarization strategy without rewriting agent core
6. **Two-layer tool routing** — `MemoryManager` routes to provider, each provider handles its own tools
7. **Background prefetch queue** — queue next-turn memory prefetch during current turn (latency hiding)

## Source
- Repo: https://github.com/nousResearch/hermes-agent
- Docs: hermes-agent.nousresearch.com/docs
- Latest: v0.10.0, MIT License
