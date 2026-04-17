# Agentics & AI Mastery Mission 🏹

> *"Know the leaders, know the frameworks, build the future."*

## Mission Overview

**Goal:** Learn everything about agentics, AI, top leaders, top frameworks — using browser MCP, GitHub repos, code study, reflections, and systematic tracking.

**Duration:** 12 weeks (flexible)
**Status:** 🚧 In Progress

---

## The Roadmap

### Phase 1: Foundations (Weeks 1-3)
- [ ] Set up browser MCP for web research
- [ ] Identify and study top 10 AI/agentics leaders
- [ ] Research top 5 agentics frameworks
- [ ] Read/watching key publications from leaders

### Phase 2: Deep Dive (Weeks 4-7)
- [ ] Clone and study 10+ relevant GitHub repos
- [ ] Run and experiment with frameworks locally
- [ ] Write reflection posts on each major discovery
- [ ] Build small projects to test understanding
- [ ] **Architectural deep-dives** — understand how major systems work under the hood
- [ ] **Paper implementation** — read latest papers and implement key ideas

### Phase 3: Build & Ship (Weeks 8-12)
- [ ] Identify gaps in current agentics landscape
- [ ] Build original project using learned frameworks
- [ ] Document findings in public-facing format
- [ ] Teach others (write tutorial/blog post)

---

## Andrej Karpathy — Deep Study Focus

Andrej Karpathy is one of the most influential figures in AI/Deep Learning. This section is your dedicated study lane for him.

### Who He Is
- Former Director of AI at Tesla (Autopilot/FSD)
- Founded Sir Andrej Karpathy's Zero-to-Beat GAN (cs231n at Stanford)
- GPT / o3 / o1-mini work at OpenAI
- Built `karpathy/llm.c` — clean LLM implementation in C
- Creator of `karpathy/distill.pub` visualizations
- YouTube: `"Neural Networks: Zero to Hero"` series
- Blog: `karpathy.ai`

### Study Plan (Weeks 1-4 for Karpathy focus)

| Step | What | Link/Resource |
|------|------|----------------|
| 1 | Watch "Neural Networks: Zero to Hero" | YouTube playlist |
| 2 | Read all blog posts | karpathy.ai |
| 3 | Clone and read `karpathy/llm.c` | github.com/karpathy/llm.c |
| 4 | Clone and study `karpathy/minGPT` | github.com/karpathy/minGPT |
| 5 | Study `karpathy/tinychain` | github.com/karpathy/tinychain |
| 6 | Watch CS231n lectures (Stanford) | YouTube |
| 7 | Read `karpathy/make-a-reponsive-ai` | github.com/karpathy/make-a-reponsive-ai |
| 8 | Build from scratch following his tutorials | — |

### Key Repos to Clone

```
karpathy/llm.c          # LLM from scratch in pure C
karpathy/minGPT         # Minimal GPT implementation
karpathy/tinychain      # Tiny Chain in PyTorch
karpathy/zoo            # Model zoo
karpathy/make-a-reponsive-ai  # Building a responsive AI
```

### Reflections on Karpathy

> *Placeholder for your notes/reflections as you study each resource.*

#### Reflection 1: [After watching "Zero to Hero" playlist]
*Pending...*

#### Reflection 2: [After cloning and reading llm.c]
**WOW.** This is the most clarifying thing I've read on how LLMs actually work.

The key insight: a GPT model is STRIKINGLY simple. It's just a sequence of indices that goes through a Transformer, and a probability distribution over the next index comes out. The complexity everyone obsesses over (batching, efficiency, CUDA kernels) is NOT the model itself — it's just making it fast.

Reading `train_gpt2.c` in ~1000 clean lines of C:
- Every layer has a forward and backward pass implemented manually
- No autograd, no PyTorch — just raw `float*` pointers and math
- LayerNorm: normalize → scale → shift. That's it.
- Attention: QKV projections → softmax(QK^T/sqrt(d)) @ V → projection

The philosophical point Karpathy makes is important: we're training 124M+ param models with almost no code. The "magic" is the architecture + data + compute, not complex software.

**Key takeaway:** If you want to understand LLMs, read minGPT first (~300 lines, PyTorch). Then read llm.c to see it stripped of all abstraction. You'll understand more after this than after months of prompting.

#### Reflection 3: [After minGPT study]
minGPT is beautifully documented. The README traces GPT-1 → GPT-2 → GPT-3 evolution with actual paper details (learning rates, layer counts, initialization strategies).

Mind-blowing detail: GPT-3 175B uses a context window of 2048 tokens, warmup over 375M tokens, and cosine decay. The smaller models (GPT-2 124M) use only 1024 context. The scaling is systematic and deliberate.

---

## Ethan Mollick — Deep Study Focus

Ethan Mollick is a Wharton professor focused on AI adoption and human-AI collaboration. One of the most practical voices on getting AI into real workflows.

### Who He Is
- Professor at Wharton School, University of Pennsylvania
- Runs the `One Useful Thing` blog — practical AI adoption insights
- Leading research on how organizations actually use AI
- Co-developed AI course materials used by major companies
- Known for "AI Homework" experiments with students

### Study Plan (Weeks 2-3 for Mollick focus)

| Step | What | Link/Resource |
|------|------|----------------|
| 1 | Read all `One Useful Thing` blog posts | oneusefulthing.org |
| 2 | Watch his AI adoption talks | YouTube |
| 3 | Study his AI course materials | Coursera/Wharton online |
| 4 | Read research papers on human-AI collaboration | Google Scholar |
| 5 | Follow his AI experiments and case studies | Substack |

### Key Resources

```
oneusefulthing.org     # Blog - practical AI adoption
Wharton AI Course      # Business AI application
```

### Reflections on Mollick

> *Placeholder for your notes/reflections.*

#### Reflection 1: [After reading One Useful Thing archives]
*Pending...*

#### Reflection 2: [After studying his AI adoption framework]
*Pending...*

---

## Lex Fridman — Deep Study Focus

Lex Fridman is a researcher and podcast host known for long-form technical interviews with the brightest minds in AI, robotics, and neuroscience.

### Who He Is
- Research scientist at MIT (formerly)
- Hosts the Lex Fridman Podcast — 200+ hours of deep conversations
- Background in autonomous vehicles, machine learning
- Interviewed virtually every major AI leader (Karpathy, Ng, Sutskever, etc.)
- Known for technical, nuanced questions

### Study Plan (Weeks 3-5 for Fridman focus)

| Step | What | Link/Resource |
|------|------|----------------|
| 1 | Watch "Lex Fridman Podcast" AI episodes playlist | YouTube |
| 2 | Study his published research papers | scholar.google.com |
| 3 | Watch specific AI leader interviews (Karpathy, Ng, etc.) | YouTube |
| 4 | Listen to his Tesla/autonomous vehicle discussions | YouTube |
| 5 | Read his published papers on deep learning | arxiv.org |

### Key Episodes to Watch

```
# AI Masters series - must watch
- Andrej Karpathy on Lex Fridman (multiple appearances)
- Andrew Ng on Lex Fridman
- Yann LeCun on Lex Fridman
- Ilya Sutskever on Lex Fridman
- Dario Amodei on Lex Fridman

# AI Fundamentals
- The State of AI (annual discussions)
- Deep Learning for code
- AI in autonomous vehicles
```

### Reflections on Fridman

> *Placeholder for your notes/reflections.*

#### Reflection 1: [After watching his AI interview series]
*Pending...*

#### Reflection 2: [After studying his research background]
*Pending...*

---

## Garry Tan — Deep Study Focus

Garry Tan is a Y Combinator partner and one of the most influential voices in AI startups and the Silicon Valley ecosystem.

### Who He Is
- Partner at Y Combinator (现任)
- Former CEO of Posthog (analytics platform)
- Investor in 100+ AI startups
- Blog at `garrytan.com` on startups and AI
- Known for understanding what makes AI startups succeed

### Study Plan (Weeks 4-5 for Tan focus)

| Step | What | Link/Resource |
|------|------|----------------|
| 1 | Read all blog posts on `garrytan.com` | garrytan.com |
| 2 | Watch Y Combinator AI startup videos | YouTube/Y Combinator |
| 3 | Study his investment thesis for AI cos | YC blog |
| 4 | Follow his thoughts on AI go-to-market | Twitter/X |
| 5 | Study successful YC AI companies | ycombinator.com |

### Key Content

```
garrytan.com           # Blog on startups/AI
Y Combinator           # AI startup school videos
Posthog                # His company - study product-led growth
```

### Reflections on Garry Tan

#### Reflection 1: [After reading his blog archives]
*Pending...*

#### Reflection 2: [After YC AI startup study]
*Pending...*

---

## Sebastian Raschka — Deep Study Focus

Sebastian Raschka is an AI educator and researcher known for making deep learning accessible through his books, courses, and clear technical explanations.

### Who He Is
- Author of "Python Machine Learning" (best-seller)
- Creator of StatQuest (Josh Starmer collaboration reference)
- Lightning AI researcher/educator
- PhD in ML from UW-Madison
- Known for `lightning` ecosystem and practical ML education

### Study Plan (Weeks 5-6 for Raschka focus)

| Step | What | Link/Resource |
|------|------|----------------|
| 1 | Read "Python Machine Learning" book | Amazon |
| 2 | Study his Lightning AI courses | lightning.ai |
| 3 | Follow his research on LLM architecture | arxiv.org |
| 4 | Watch his deep learning tutorials | YouTube |
| 5 | Study his GitHub repos (model implementations) | github.com/sebastianraszchka |

### Key Repos

```
sebastianraszchka/python-machine-learning-book    # The book code
lightning-ai/lightning                            # PyTorch Lightning
```

### Reflections on Raschka

#### Reflection 1: [After studying his ML book]
*Pending...*

#### Reflection 2: [After Lightning AI course]
*Pending...*

---

## Jeremy Howard — Deep Study Focus

Jeremy Howard is a data scientist and educator known for fast.ai — making deep learning accessible to everyone.

### Who He Is
- Co-founder of fast.ai (with Rachel Thomas)
- Former President of Kaggle
- Distinguished Research Scientist at USF
- Known for "Practical Deep Learning for Coders" course
- Focus on democratizing AI education

### Study Plan (Weeks 6-7 for Howard focus)

| Step | What | Link/Resource |
|------|------|----------------|
| 1 | Complete fast.ai "Practical DL for Coders" course | fast.ai |
| 2 | Study fast.ai library source code | github.com/fastai |
| 3 | Watch his conference talks | YouTube |
| 4 | Read his research on model efficiency | arxiv.org |
| 5 | Study his Kaggle competition winning solutions | Kaggle |

### Key Resources

```
fast.ai courses              # Practical DL for Coders
fastai/fastai                # The library
Jeremy Howard's Talks        # YouTube
```

### Reflections on Howard

#### Reflection 1: [After completing fast.ai course]
*Pending...*

#### Reflection 2: [After studying fastai library]
*Pending...*

---

## Key Leaders to Study

| Leader | Focus | Status |
|--------|-------|--------|
| **Andrej Karpathy** | LLMs, Neural nets, Tesla AI, Zero-to-Hero | 🔬🔬 In progress |
| **Ethan Mollick** | AI adoption, Human-AI collaboration, One useful thing blog | 🔬 To study |
| **Lex Fridman** | AI research, Deep learning, Long-form interviews | 🔬 To study |
| **Garry Tan** | YC, startups, AI investments, Codex/silicon valley | 🔬 To study |
| **Sebastian Raschka** | LLM architecture, Deep learning, StatQuest, Lightning AI | 🔬 To study |
| **Jeremy Howard** | Developer productivity, Fast.ai, Practical DL | 🔬 To study |
| **Andrew Ng** | AI education, ML, DeepLearning.ai, Coursera | 🔬 To study |
| Jim Fan | AI agents, NVIDIA | 🔬 To study |
| Yann LeCun | LLMs, self-supervised | 🔬 To study |
| Soumith Chintala | PyTorch | 🔬 To study |
| OpenAI Team | LLMs, RLHF | 🔬 To study |
| Anthropic Team | Constitutional AI | 🔬 To study |
| Google DeepMind | Multi-modal, AlphaCode | 🔬 To study |

## Top Frameworks to Explore

| Framework | Language | Stars | Status |
|-----------|----------|-------|--------|
| LangChain | Python/JS | 85k+ | 📦 To explore |
| AutoGPT | Python | 120k+ | 📦 To explore |
| CrewAI | Python | 25k+ | 📦 To explore |
| Microsoft Semantic Kernel | C#/Python | 18k+ | 📦 To explore |
| LlamaIndex | Python | 20k+ | 📦 To explore |
| AutoGen | Python | 30k+ | 📦 To explore |

## GitHub Repos to Study

```
# Cloned and studying
/app/data/repos/llm.c          # LLM from scratch in pure C (DONE)
/app/data/repos/minGPT         # Minimal GPT implementation in PyTorch (DONE)
/app/data/repos/tinychain      # Tiny Chain in PyTorch (FAILED - network error, retry later)
```

## Study Log

### 2026-04-17: minGPT + llm.c Deep Dive

**minGPT Architecture (~300 lines)**
- Clean 3-file structure: `model.py`, `bpe.py`, `trainer.py`
- GPT model is just a Transformer decoder: sequence of tokens → probability distribution over next index
- Key insight: most complexity is batching efficiency, not the model itself
- CausalSelfAttention: QKV projections → split heads → attention with causal mask
- GPT-2 config options: 124M, 350M, 774M, 1558M parameters

**llm.c Philosophy**
- Goal: train LLMs WITHOUT PyTorch's 245MB overhead
- `train_gpt2.c` ~1000 lines = complete GPT-2 training in clean C
- Every layer (encoder, layernorm, attention, MLP) implemented from scratch with forward + backward passes
- Interesting: uses raw `float*` buffers, manual softmax, manual matmul
- Notable forks: Rust, Go, C#, Mojo, Zig, Metal, WebGPU, AMD, Habana Gaudi2

## Reflections

### Reflection 1: [Date]
*Pending...*

### Reflection 2: [Date]
*Pending...*

---

## Progress Tracking

| Week | Focus | Completion |
|------|-------|------------|
| 1 | Setup + Andrej Karpathy study | 15% |
| 2 | Ethan Mollick + Framework survey | 0% |
| 3 | Lex Fridman deep-dive | 0% |
| 4 | Garry Tan + Sebastian Raschka | 0% |
| 5-6 | Jeremy Howard + Andrew Ng | 0% |
| 7 | Architectural deep-dives + paper implementation | 0% |
| 8-12 | Build phase | 0% |

---

## Next Action Items

1. ✅ **Done:** Clone llm.c + minGPT
2. ✅ **Done:** Read core model files, write reflections
3. 🔄 **In progress:** Watch Karpathy "Zero to Hero" YouTube series
4. 🔁 **Next:** Retry tinychain clone + watch CS231n lectures
5. 📋 **Next:** Start Ethan Mollick study (One Useful Thing blog)

---

*Last updated: 2026-04-17*
*Use `/mission status` to check progress*
