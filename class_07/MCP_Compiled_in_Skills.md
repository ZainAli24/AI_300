# Compiling MCP to Skills (MCP Ko Skills Mein Compile Karna)

## Roman Urdu Mein Beginner-Friendly Summary (Exam Ke Liye)

---

## Core Concept (Bunyadi Concept)

MCP servers startup pe **SAARI tool definitions load** kar dete hain (har ek **5,000-8,000+ tokens**), jisse **token bloat** (tokens ka fuzool barhna) paida hota hai. Pre-compiled skills context consumption ko **97-99% tak reduce** kar deti hain jabke **poori functionality qaim** rehti hai — **SKILL.md (~150 tokens) + local script execution (context mein 0 tokens)** baar baar tool definition loading ki jagah le leti hai.

---

## Key Mental Models (Samajhne Ke Zaroori Tareeqe)

---

### Token Bloat (Tokens Ka Fuzool Barhna)

MCP **eagerly (jaldi baazi mein) sab kuch load** kar deta hai; tum un tools ke liye **pay kar rahe ho jo tum use nahi kar rahe**. 

- **1,000 tools wala Agent** = pehli request se pehle hi **150,000 tokens** load ho jaate hain
- **2 ghante ka workflow** shayad **50,000+ tokens waste** kare

---

### Code Execution Pattern (Code Chalane Ka Tareeqa)

MCP tools ko directly Claude ke context ke through call karne ki jagah, compiled skills **locally bash ke zariye scripts** chalaati hain — Claude **orchestrate (manage)** karta hai, `mcp-client.py` **context ke BAAHAR execute** karta hai.

---

### Progressive Disclosure — 3-Stage Loading (3 Marhale Mein Loading)

Skills **teen-level loading** use karti hain context mein tokens kam rakhne ke liye:

1. **Discovery (Khoj) — Sirf description load hoti hai** (~30 tokens)
2. **Activation (Chalana) — Poori SKILL.md load hoti hai** (~150 tokens)
3. **Execution (Amal) — Scripts locally chalte hain** (context mein 0 tokens)

---

### Content-Type Filtering (Content Ki Qism Se Chhanna)

`fetch-library-docs` jaisi skills responses ko **locally filter** karti hain (setup, examples, api-ref), sirf **relevant content return** karke **60-90% mazeed saving** deti hain.

---

## Critical Patterns (Zaroori Patterns)

- Skills Lab se **pre-compiled skills** use karo: `browsing-with-playwright`, `fetch-library-docs`
- Skills **bash commands execute** karti hain: `python mcp-client.py call -t browser_navigate ...`
- Scripts Claude ke **context ke BAAHAR chalte hain** — bhaari operations **zero tokens** consume karte hain
- **Content-type filtering:** `--content-type setup` vs `--content-type examples` **alag alag filtered results** return karta hai
- **Token usage compare karo:** Direct MCP (~15,000-24,000 tokens) vs compiled skill (~150-250 tokens)

---

## Common Mistakes (Aam Galtiyan)

- **Repeated workflows ke liye direct MCP use karna** — token waste har call ke saath multiply hota hai
- Docs fetch karte waqt **content-type specify na karna** — filtered content ki jagah **sab kuch return** hota hai
- **Is lesson mein skills banana expect karna** — skill creation advanced lessons mein cover hoti hai
- `browsing-with-playwright` use karte waqt **MCP server start/stop karna bhool jaana**

---

## Decision Framework (Faisla Karne Ka Tareeqa)

### Direct MCP Kab Use Karein:

- **One-off queries** (ek baar ke sawaal)
- **Low-token servers** (<1,500 tokens)
- **Tezi se badalne wale APIs** (rapidly-changing)
- **Chhote ache format wale results** (small well-formatted)

### Compiled Skill Kab Use Karein:

- **Repeated workflows** (3+ calls) — baar baar hone wale kaam
- **High-token servers** (5,000+) — zyada tokens khaane wale servers
- **Bade datasets jinhe filtering chahiye** — bohot saara data jismein se thoda chahiye
- **Multi-step workflows** — kai qadam wale kaam
- **Team sharing** — team ke saath share karna
- **Privacy-sensitive data** — niji data

---

## Connections (Doosre Lessons Se Taluq)

### Is Se Pehle Kya Seekha:

- **Skills (Lessons 08-09):** SKILL.md format aur Skills Lab ke liye
- **MCP Integration (Lesson 12):** MCP servers samajhne ke liye

### Is Ke Baad Kya Aayega:

- **Settings Hierarchy (Lesson 16):** Configuration management ke liye
- **Advanced lessons:** Apni khud ki compiled skills banana seekhne ke liye

---

## Sabse Zaroori Baatein Yaad Rakhein (Exam Ke Liye)

1. **MCP ka problem = Token Bloat** — startup pe SAARI tool definitions load hoti hain, chahe tum unhe use na karo
2. **1,000 tools = 150,000 tokens** pehli request se pehle hi load — yeh bohot fuzool hai
3. **Compiled skills 97-99% tokens bacha deti hain** — SKILL.md (~150 tokens) + local scripts (0 tokens in context)
4. **Code Execution Pattern:** Claude orchestrate karta hai, `mcp-client.py` context ke BAAHAR execute karta hai
5. **3-Stage Loading:** Discovery (~30 tokens) → Activation (~150 tokens) → Execution (0 tokens) — yeh progressive disclosure hai
6. **Direct MCP: ~15,000-24,000 tokens** vs **Compiled Skill: ~150-250 tokens** — yeh comparison yaad rakhein
7. **Content-Type Filtering:** `--content-type setup` ya `--content-type examples` specify karo — filtered content milta hai, sab kuch nahi
8. **Content-type filtering se 60-90% mazeed saving** hoti hai
9. **Scripts context ke BAAHAR chalte hain** — bhaari operations zero tokens consume karte hain, yahi asli saving hai
10. **Direct MCP kab:** One-off queries, low-token servers (<1,500), rapidly-changing APIs, small results
11. **Compiled Skill kab:** Repeated workflows (3+), high-token servers (5,000+), large datasets needing filtering, multi-step workflows, team sharing
12. **Skills intelligent guides bhi hain** — SKILL.md mein decision logic hota hai jo Claude ko batata hai kab Tool Search use kare kab compiled pattern
13. **Skills format portable hai** — Claude Code, OpenAI Codex, aur Goose teeno mein kaam karti hai
14. **Aam galti:** Repeated workflows mein direct MCP use karna = token waste multiply hota hai har call ke saath