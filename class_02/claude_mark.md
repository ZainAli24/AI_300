## **Page Ka Title: "CLAUDE.md Context Files"**

Ye lesson aapko sikhaye ga ke CLAUDE.md file kya hoti hai aur ye aapki coding life ko kaise asaan bana sakti hai.

---

## **Opening Story (Pehli Kahani)**

**Kahani ye hai:**
Socho aap kisi Python project pe kaam kar rahe hain Claude Code ke saath. Kai hafton se. Claude ne aapke **naming conventions** (names dene ka tareeqa) seekh liya, aapki **project structure** samajh li, aur aapka coding style bhi samajh gaya.

Phir aap raat ko apna terminal band kar dete hain.

Agli subah aap naya Claude Code session khol te hain aur apne project ke baare mein kuch puchte hain. 

**Aur kya hota hai?** Claude aise jawab deta hai jaise use kuch pata hi nahi. Wo bilkul fresh start karta hai. Aapko phir se batana parta hai:
- Aapka tech stack kya hai
- Aapki directories kahan kahan hain
- Aapki team ke rules kya hain

**Isko kehte hain "context friction"** - matlab **har session mein wohi cheezein dubara explain karna**. Ye bohot time waste karta hai.

**Solution kya hai?** CLAUDE.md file! 

---

## **"What Is CLAUDE.md?" - CLAUDE.md Kya Hai?**

**Simple definition:**
CLAUDE.md aik **simple markdown file** hai jo aap apne **project ke root folder** mein rakhte hain. Jab bhi aap Claude Code start karte hain, wo **automatically is file ko read karta hai**.

**Sochiye iske jaise:**
Ye file aik **persistent project brief** hai - matlab aik permanent note jo aapke code ke saath rehta hai aur har session mein Claude ko batata hai:
- Aapka project kya karta hai (X, Y, Z kaam)
- Aap kaun si technology use karte hain (Python 3.13, FastAPI, PostgreSQL waghaira)
- Aapki files kahan hain (`src/` mein code, `tests/` mein tests, `alembic/` mein database migrations)
- Aapko kaun sa style pasand hai (type hints chahiye, Google-style docstrings, custom exception handling)
- Important commands kya hain (jaise `uvicorn main:app --reload` ya `pytest`)

**Faida kya hai?**
Jab Claude Code naya session shuru karta hai, wo pehle CLAUDE.md file ko read karta hai. Is tarah se Claude **turant aapke project ko samajh jata hai** bina aapke kuch bole.

**Diagram ki explanation:**
Page pe aik image hai jo **four-layer context architecture** dikhati hai:
1. **Working Directory (base)** - aapki actual files
2. **.claude/context files (project knowledge)** - project ki specific knowledge 
3. **Message History (conversation state)** - aapki conversation
4. **Current Tools (active capabilities)** - jo tools abhi available hain

Ye sab layers information flow dikha rahi hain ke kaise data Claude tak pohanchta hai.

---

## **"How Claude Code Works Behind the Scenes" - Parde Ke Peechay Kya Hota Hai**

Ye section bohot important hai kyunke ye explain karta hai ke **LLMs kaise kaam karte hain**.

**Process:**
Jab aap Claude Code mein message likhte hain, ye hota hai:

```
Aap → Claude Code (CLI tool) → AI Model (LLM) → Response wapis aapko
```

**Samjho:**
- Claude Code wo **interface** hai jisse aap baat karte hain
- Ye **AI model** ko call karta hai (Claude) backend mein
- Model response deta hai jo aapko dikhta hai

**Shocking fact:**
**AI model ko koi memory nahi hoti sessions ke beech.**

Matlab agar aap apna terminal band kar ke kal dobara kholen, Claude ko **kuch yaad nahi rehta**:
- Na aapka tech stack
- Na aapki file structure
- Na ye bhi ke aap kal baat kar rahe the

**Isko kehte hain "stateless"** - matlab AI ke paas koi permanent state (memory, history, context) nahi hai requests ke beech.

**Lekin conversation continuous lagti hai kyun?**
Kyunke Claude Code **extra kaam karta hai**:

1. Aap message #1 bhejte hain → Claude Code use Claude ko bhejta hai
2. Aap message #2 bhejte hain → Claude Code **message #1 + #2 dono** bhejta hai
3. Aap message #3 bhejte hain → Claude Code **#1 + #2 + #3 teeno** bhejta hai

LLM har baar **puri history fresh read karta hai**. Ye continuous lagti hai kyunke Claude Code history dubara dubara bhej raha hai.

ChatGPT aur Claude.ai bhi yahi trick use karte hain.

**Table explanation (coding work ke liye):**

| Approach (Tareeqa) | Good For (Kis ke liye acha) | Problem (Mushkil) |
| --- | --- | --- |
| Chat history dubara bhejna | Chhoti conversations | Lambi hone pe mushkil |
| Har baar project explain karna | Simple projects | Complex projects mein thak jao ge |
| Har baar fresh start | Quick questions | Project understanding kho jati hai |

**Claude Code ka solution:**
Wo aapki **file system ko external memory ki tarah use karta hai**.

**Samajhne wali baat:**
Aapki code files mein already aapke project ki state hai! Project describe karne ki bajaye, Claude **seedha aapke files read karta hai**.

**Insight:**
- **Stateless LLM** + **File System Access** = Permanent state aapki actual files ke zariye
- **CLAUDE.md** = Wo orientation guide jo Claude har session mein pehle padhta hai
- **Har session**: Claude CLAUDE.md padhta hai, project samajh jata hai, kaam shuru karta hai

LLM stateless hai. Lekin aapki files permanent hain. CLAUDE.md ensure karta hai ke Claude ka pehla kaam har session mein ye hota hai ke wo context read kare.

---

## **"How CLAUDE.md Auto-Loads" - Kaise Ye Automatically Load Hoti Hai**

**Simple explanation:**
Aapko kuch karna nahi parta! Jab aap apne directory mein `claude` command run karte hain, **Claude Code automatically CLAUDE.md file ko detect aur read karta hai** aur turant context mein load kar leta hai.

Aik baar setup karo. Hamesha ka faida.

---

## **"What Goes Into CLAUDE.md" - Isme Kya Likha Jata Hai**

CLAUDE.md mein normally **6 sections** hote hain:

**1. Project Overview:**
- Aapka project kya karta hai?
- Kaun sa problem solve karta hai?

**2. Technology Stack:**
- Languages, frameworks, databases
- Important dependencies (jo libraries chahiye)

**3. Directory Structure:**
- Files kahan hain ye structure dikhaiye
- Taake Claude samjhe ke code kahan hai

**4. Coding Conventions:**
- Aapka style kya hai
- Naming patterns kya hain
- Team ke rules kya hain

**5. Key Commands:**
- Project kaise run karte hain
- Tests kaise run karte hain
- Deploy kaise karte hain

**6. Important Notes:**
- Gotchas (choti choti cheezein jinse bachna hai)
- Dependencies
- Security ki baatein

---

## **"How to Create Your CLAUDE.md" - Kaise Banate Hain**

Manual type karne ki zarurat nahi! **Claude Code se hi banwa lo**.

### **Step 1: Ask Claude Code to Generate CLAUDE.md**

Apne project directory mein Claude Code start karo aur pucho:

```
claude "Help me create a CLAUDE.md file for this project.  
What are the main sections I should include, and can you generate a template  
based on what you see in the codebase?"
```

Claude aapki actual files dekhe ga aur CLAUDE.md structure suggest kare ga based on aapke real project pe.

**Practice Exercise:**
Apne AI se pucho: "Mere [Python/Node/Go/etc] [project type] project ke liye CLAUDE.md banao. Include karo: Project Overview (2 sentences), Technology Stack (list), Directory Structure (tree), Coding Conventions (list), Key Commands (list), Important Notes (gotchas). Jo tum codebase mein dekh rahe ho uspe specific banao."

**Expected result:** Claude aapke liye CLAUDE.md bana de ga with sab sections populated.

### **Step 2: Review and Refine**

Claude ki output aik starting point hai. Dhyan se parho. Kya ye aapke project se match karta hai? Conventions sahi hain? Agar Claude ne galat guess kiya ya koi cheez miss ki, to refine karo.

### **Step 3: Save the File**

Claude ka output `CLAUDE.md` ke naam se save karo apne **project root** mein (jahan `package.json`, `pyproject.toml` waghaira hain).

### **Step 4: Verify Auto-Loading**

Claude Code se bahar aao (`exit` type karo ya terminal band karo). Naya terminal kholo same directory mein:

```
claude
```

Naye session mein, apne project ke baare mein kuch pucho:

```
"What's the tech stack for this project?"
```

**Agar Claude aapka stack bata de bina aapke repeat kiye - CLAUDE.md successfully load ho gayi!**

---

## **"Why This Matters: Context as Productivity" - Kyun Zaroori Hai**

**Jo aapne achieve kiya:**

✅ **One-time creation**: Sirf 10-15 minutes mein CLAUDE.md likho
✅ **Automatic benefit**: Har session full context ke saath shuru hota hai  
✅ **No friction**: Project structure, conventions, setup explain karne ki zarurat nahi
✅ **Team alignment**: Naye team members CLAUDE.md parh ke project samajh sakte hain

**Principle:** "Specify once, benefit always" - aik baar define karo, har future session mein full understanding.

Baad ke lessons mein aap dekhoge ke **subagents** (Lesson 11) aur **skills** (Lesson 09) kaise is CLAUDE.md context ko inherit aur extend karte hain.

---

## **"Continue Practicing" - Practice Jari Rakho**

### **Create a CLAUDE.md for Your Exercises**

`basics-exercises` folder kholo (Lesson 06 se download kiya tha). Terminal mein wahan jao aur Claude start karo:

```
claude
```

Claude se CLAUDE.md banwao:

```
Create a CLAUDE.md for this exercises folder. I'm a beginner  
practicing problem-solving with AI. I prefer clear explanations  
and step-by-step verification of results. Look at the modules  
and describe what this project is about.
```

Claude folder read kare ga, sare modules dekhe ga, aur aapke exercises ke liye tailored CLAUDE.md bana de ga.

**Phir test karo:**
- Claude se **exit** karo
- Dobara **start** karo
- Pucho: "What do you know about this project?"

Claude already janta hoga kyunke usne CLAUDE.md automatically load ki thi!

### **Modules 5-8**

Ye modules Modules 1-4 se zyada complex hain. Multi-step tasks hain jahan context **bohot zaroori** hai.

| Module | Kya Practice karoge | CLAUDE.md Kaise Help Karti Hai |
| --- | --- | --- |
| 5. Process Automation | Reusable specs, batch operations | Claude aapke naming conventions yaad rakhta hai |
| 6. Problem Solving | Multi-turn planning, constraints change hona | Claude project context maintain karta hai turns ke beech |
| 7. Quality Control | Output verify karna, specs stress-test karna | Claude aapke quality standards janta hai |
| 8. Capstone Projects | Complete real projects | Full context = behtar results |

Same pattern: exercise folder kholo, `claude` run karo, bolo "Read INSTRUCTIONS.md and do what it says", review karo, iterate karo.

---

## **"Co-Learning: Improving CLAUDE.md Together" - Saath Mein Behtar Banao**

Ye **Three Roles Framework** hai - jahan aap aur Claude aik dusre se seekhte hain.

### **Stage 1: Your First Draft - Aapka Pehla Draft**

Aap basic CLAUDE.md banate hain:

```
# Project Overview  
A Python web app  

# Tech Stack  
- Python  
- FastAPI
```

Basic hai lekin start hai.

### **Stage 2: AI as Teacher - Claude Aapko Sikhaye**

Claude se review mangao:

```
"Review my CLAUDE.md. What important sections am I missing?"
```

**Claude jawab deta hai:**

"I notice your CLAUDE.md is missing several critical sections:
1. **Directory Structure** - Route files kahan hain, models kahan, tests kahan?
2. **Coding Conventions** - Kaun sa style guide? Type hints zaroor hain?
3. **Key Commands** - App kaise run karte hain? Tests kaise?
4. **Database Info** - Kaun sa database? Migration strategy kya hai?
5. **API Documentation** - OpenAPI spec kahan hai?"

**Kya hua?** 🎓 **AI ne aapko sikhaya** CLAUDE.md ke best practices jo aapko pata nahi the.

### **Stage 3: AI as Student - Aap Claude Ko Sikhao**

Ab aap domain-specific knowledge dete hain jo Claude ko nahi hai:

```
"Good points, but our team uses a custom auth pattern. Update CLAUDE.md to reflect:  
- All auth goes through middleware/auth.py  
- We use custom decorators: @require_auth, @require_admin  
- No third-party auth libraries (company policy)  
- JWT tokens stored in httpOnly cookies"
```

**Kya hua?** 🎓 **Aapne AI ko sikhaya** aapki team ke constraints aur patterns.

### **Stage 4: AI as Co-Worker - Saath Mein Kaam**

Aap aur Claude milke refine karte hain:

```
"This is better, but the directory structure doesn't show where database migrations live.  
How should we organize database-related files?"
```

Claude options de ga, aap select karoge team context ke hisaab se.

**Kya hua?** 🎓 **Kisi ke paas bhi** complete picture nahi thi. Conversation ke zariye, aap dono **converge** ho gaye sahi solution pe.

### **Final Result**

Aapki final CLAUDE.md ab complete hai with sab details:
- Project overview
- Tech stack
- Directory structure
- Coding conventions (custom auth patterns included)
- Key commands
- Important notes

**Ye behtar hai kyunke:**
✅ Claude ne aapko sections sikhaye
✅ Aapne Claude ko team patterns sikhaye
✅ Saath mein sahi organization pe converge hue

---

## **"Edge Cases and Troubleshooting" - Agar Mushkil Aaye**

### **CLAUDE.md Load Nahi Ho Rahi?**

**Problem:** Aapne CLAUDE.md banayi lekin Claude Code use reference nahi kar raha.

**Check karo:**
- ✅ File ka naam exactly `CLAUDE.md` hai (case-sensitive)
- ✅ File project root mein hai (`.git`, `package.json` ke saath same level pe)
- ✅ Aapne Claude Code session restart kiya (naya terminal, wohi session nahi)
- ✅ File mein content hai (khali nahi)

**Solution:** Agar sab sahi hai, terminal completely restart karo.

### **Samajh Nahi Aa Raha Kya Likhen?**

**Simple rule:** Khud se pucho: "Kya Claude ko ye janna chahiye taake acha suggestion de sake?"

Agar Claude bina CLAUDE.md ke puchega "What's your tech stack?", to wo information CLAUDE.md mein honi chahiye.

### **File Size Ki Tension?**

Typical CLAUDE.md 1-3 KB hoti hai. Ye bohot chhoti hai. Context sasta hai; clarity expensive hai.

---

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

## **"Try With AI" - AI Ke Saath Try Karo**

Lesson ke end mein prompts hain jo aap try kar sakte hain:

**1. Auto-Generation explore karo:**
"Help me create a complete CLAUDE.md... analyze the codebase..."

**2. Collaborative refinement practice:**
"Review the CLAUDE.md... add my team's constraints..."

**3. Context persistence test:**
"Tell me what tech stack... then I'll exit and verify..."

**4. Workflow optimize:**
"Help me identify what ELSE should go in CLAUDE.md based on my workflow..."

---

## **Summary - Mukhtasar**

**CLAUDE.md file:**
- Aik markdown file jo project root mein hoti hai
- Claude Code automatically ise load karta hai
- Har session mein context provide karti hai
- Aapko dubara explain karne ki zarurat nahi
- Team members bhi isse project samajh sakte hain

**AGENTS.md:**
- Universal standard for all AI tools
- Linux Foundation standard ban gaya
- Har AI agent ke saath kaam karta hai

**Best practice:**
Dono use karo - AGENTS.md for universal, CLAUDE.md for Claude-specific features!

---

-------------
