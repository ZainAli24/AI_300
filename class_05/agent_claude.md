
## **"The Universal Standard: AGENTS.md" - Universal Standard**

CLAUDE.md sirf Claude Code ke liye hai. Lekin agar aap **dusre AI tools** use karte hain (Cursor, GitHub Copilot, Gemini CLI waghaira)?

**AGENTS.md** - ye **universal standard** hai jo **har AI tool** ke saath kaam karta hai.

### **AGENTS.md Kya Hai?**

Ye simple markdown file hai (CLAUDE.md jaise) jo **kisi bhi** AI coding agent ko project-specific guidance deti hai. OpenAI ne banaya, ab 60,000+ open source projects use karti hain.

**Main difference:**
- **CLAUDE.md** → Claude Code specific (rich features)
- **AGENTS.md** → Universal (har jagah kaam karta hai)

### **Kyun Important Hai: Agentic AI Foundation**

9 December 2025 ko, OpenAI, Anthropic, aur Block ne apne standards Linux Foundation ko donate kiye, **Agentic AI Foundation (AAIF)** bana:

| Project | Kisse Donate Hua | Purpose |
| --- | --- | --- |
| **MCP** | Anthropic | AI ko tools/data se connect karne ka protocol |
| **AGENTS.md** | OpenAI | Universal project instructions for agents |
| **Goose** | Block | Open-source agent framework |

Ab AGENTS.md **neutral, vendor-independent standard** hai - jaise Kubernetes containers ke liye, ya HTTP web ke liye.

### **Dono Ka Best Use**

**Dono use karo:**

```
your-project/  
├── CLAUDE.md      # Claude Code ke liye rich context
├── AGENTS.md      # Kisi bhi AI agent ke liye universal context
├── src/  
└── ...
```

**CLAUDE.md mein**, AGENTS.md ko reference karo:

```
# Project Context  
See @AGENTS.md for universal project guidelines.  

## Claude-Specific Instructions  
[Claude Code specific stuff]
```

**Faida:**
✅ **Portability**: Koi bhi AI agent AGENTS.md se samajh jaye ga
✅ **Depth**: Claude Code ko CLAUDE.md se rich context milta hai
✅ **No duplication**: Common info AGENTS.md mein, Claude-specific CLAUDE.md mein

### **AGENTS.md vs CLAUDE.md Mein Kya Likhen?**

| Content | AGENTS.md | CLAUDE.md |
| --- | --- | --- |
| Project overview | ✅ | Reference @AGENTS.md |
| Tech stack | ✅ | Reference @AGENTS.md |
| Directory structure | ✅ | Reference @AGENTS.md |
| Claude skills | ❌ | ✅ |
| MCP configs | ❌ | ✅ |
| Subagents | ❌ | ✅ |

**Rule:** Universal context → AGENTS.md. Claude features → CLAUDE.md.

---
