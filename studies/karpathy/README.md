# Andrej Karpathy - Deep Study 🧠

## Who He Is

- Former Director of AI at Tesla (Autopilot/FSD)
- Founded cs231n at Stanford (Neural Networks: Zero to Hero)
- GPT / o3 / o1-mini work at OpenAI
- Built `karpathy/llm.c` — clean LLM implementation in C
- Creator of `karpathy/distill.pub` visualizations
- YouTube: "Neural Networks: Zero to Hero" series
- Blog: karpathy.ai

## Study Plan

| Step | What | Status |
|------|------|--------|
| 1 | Watch "Neural Networks: Zero to Hero" | 🔄 In Progress |
| 2 | Read all blog posts | karpathy.ai |
| 3 | Clone and read `karpathy/llm.c` | ✅ Done |
| 4 | Clone and study `karpathy/minGPT` | ✅ Done |
| 5 | Study `karpathy/tinychain` | ⏳ Pending |
| 6 | Watch CS231n lectures | ⏳ Pending |
| 7 | Build from scratch following his tutorials | ⏳ Pending |

## Key Repos

```
karpathy/llm.c          # LLM from scratch in pure C ✅
karpathy/minGPT         # Minimal GPT implementation ✅
karpathy/tinychain      # Tiny Chain in PyTorch ⏳
karpathy/zoo            # Model zoo ⏳
karpathy/make-a-reponsive-ai  # Building a responsive AI ⏳
```

---

## Reflections

### Reflection: After llm.c Deep Dive

**WOW.** This is the most clarifying thing I've read on how LLMs actually work.

The key insight: a GPT model is STRIKINGLY simple. It's just a sequence of indices that goes through a Transformer, and a probability distribution over the next index comes out. The complexity everyone obsesses over (batching, efficiency, CUDA kernels) is NOT the model itself — it's just making it fast.

Reading `train_gpt2.c` in ~1000 clean lines of C:
- Every layer has a forward and backward pass implemented manually
- No autograd, no PyTorch — just raw `float*` pointers and math
- LayerNorm: normalize → scale → shift. That's it.
- Attention: QKV projections → softmax(QK^T/sqrt(d)) @ V → projection

The philosophical point Karpathy makes is important: we're training 124M+ param models with almost no code. The "magic" is the architecture + data + compute, not complex software.

**Key takeaway:** If you want to understand LLMs, read minGPT first (~300 lines, PyTorch). Then read llm.c to see it stripped of all abstraction. You'll understand more after this than after months of prompting.

### Reflection: After minGPT Study

minGPT is beautifully documented. The README traces GPT-1 → GPT-2 → GPT-3 evolution with actual paper details (learning rates, layer counts, initialization strategies).

Mind-blowing detail: GPT-3 175B uses a context window of 2048 tokens, warmup over 375M tokens, and cosine decay. The smaller models (GPT-2 124M) use only 1024 context. The scaling is systematic and deliberate.

---

## Architecture Notes

### minGPT (~300 lines, PyTorch)

**3-file structure:**
- `model.py` - The GPT model itself
- `bpe.py` - Byte Pair Encoding tokenizer
- `trainer.py` - Training loop

**Key insight:** Most complexity is batching efficiency, not the model itself.

**CausalSelfAttention:** QKV projections → split heads → attention with causal mask

**GPT-2 configs:**
| Model | Parameters | Layers | Heads | Context |
|-------|-----------|--------|-------|---------|
| GPT-2 | 124M | 12 | 12 | 1024 |
| GPT-2 Medium | 350M | 24 | 16 | 1024 |
| GPT-2 Large | 774M | 36 | 20 | 1024 |
| GPT-2 XL | 1558M | 48 | 25 | 1024 |

### llm.c Philosophy

**Goal:** Train LLMs WITHOUT PyTorch's 245MB overhead.

**`train_gpt2.c`** ~1000 lines = complete GPT-2 training in clean C.

**What's inside:**
- Encoder (embedding + causal mask)
- LayerNorm
- Attention (QKV projections, softmax, output projection)
- MLP (gelu approximation)
- Residual connections
- Every layer has forward + backward passes

**Notable forks:** Rust, Go, C#, Mojo, Zig, Metal, WebGPU, AMD, Habana Gaudi2

---

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

---

*Last updated: 2026-04-17*