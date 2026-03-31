## Plugins — Beginner Level Explanation (Roman Urdu)

---

### 🔷 CORE CONCEPT

**"Plugins bundled packages hote hain jo Claude Code ki multiple capabilities — skills, agents, hooks, commands, aur MCP — ko ek saath ek installable unit mein combine karte hain."**

Iska matlab simple hai: Socho tumhare paas alag alag cheezein hain — ek skill, ek agent, ek hook. Inhe alag alag lagana padta. Plugin ek **gift box** ki tarah hai jisme sab kuch pehle se packed hai. Ek baar install karo, sab kuch kaam karne lagta hai.

**"Check marketplaces before building custom solutions; reuse is strategic, reinvention is waste."**

Yani pehle dekho kya **already bana hua hai**. Agar koi plugin exist karta hai jo tumhara kaam kar sake, toh khud se banana time barbaad karna hai. Smart log pehle marketplace check karte hain.

---

### 🔷 KEY MENTAL MODELS

---

**1. Composition Over Creation**

*"Existing plugins solve common workflow needs (design, testing, document processing) — leverage community intelligence before building custom."*

**"Composition Over Creation"** ka matlab: **Pehle se bani cheezein use karo, khud banana aakhri option ho.**

Duniya mein bahut log pehle se Claude ke liye useful plugins bana chuke hain — design ke liye, testing ke liye, documents process karne ke liye. Yeh sab **community intelligence** hai yaani doosron ki mehnat aur tajurba. Toh agar pehle se kuch bana hua hai, use use karo. Khud se banana tab karo jab koi option na ho.

---

**2. Bundled Intelligence**

*"A plugin's manifest declares its components, allowing one install to add skills, agents, hooks, commands, and MCP together."*

Har plugin ke andar ek **manifest** hota hai — yeh basically ek **list/form** hoti hai jo batati hai: "Is plugin mein yeh yeh cheezein hain."

Jab tum plugin install karte ho, yeh manifest padhta hai aur ek saath **skills + agents + hooks + commands + MCP** sab install ho jaate hain. Tumhe alag alag kuch nahi karna. Yeh hai "bundled intelligence" — sab kuch aik jagah packed.

---

**3. Marketplace-First Discovery**

*"Start with Anthropic's skills repository (`anthropics/claude-plugins-official`) and custom marketplaces before considering custom development."*

Jab bhi tumhein koi naya kaam karna ho, **pehla qadam yeh hona chahiye:** marketplace kholo aur dekho kya available hai.

Anthropic ka official marketplace hai: `anthropics/claude-plugins-official` — yahan verified, tested plugins milte hain. Pehle yahan dekho, phir doosre marketplaces dekho, aur **sab se aakhir mein** socho "khud banao."

---

### 🔷 CRITICAL PATTERNS (Zaroori Commands aur Cheezein)

---

**`/plugin marketplace add anthropics/claude-plugins-official`**

Yeh command Anthropic ka **official marketplace** Claude Code mein add karta hai. Socho jaise Play Store ya App Store add karna. Ek baar add karo, phir usse plugins install kar sako.

---

**`/plugin install example-skills@claude-plugins-official`**

Yeh command kisi specific plugin ko install karta hai. `example-skills` plugin ka naam hai, aur `claude-plugins-official` marketplace ka naam hai jahan se install ho raha hai. Bilkul jaise: "WhatsApp install karo Play Store se."

---

**`/plugin marketplace list`**

Yeh command batata hai ki **kon kon se marketplaces** abhi add hain. Jaise dekho kitne app stores connected hain.

---

**"Plugin manifest (`plugin.json`) declares all components with paths."**

`plugin.json` ek **ingredients list** ki tarah hai. Jaise kisi dish ke packet pe likha hota hai "isme yeh yeh cheezein hain" — plugin.json mein likha hota hai "is plugin mein yeh skills hain, yeh agents hain, yeh hooks hain, aur yeh raste hain inke files ke."

---

**"Skills install to `.claude/skills/` and activate automatically when Claude detects matching requests."**

Jab tum plugin install karte ho, uski skills automatically `.claude/skills/` folder mein save ho jaati hain. Aur **sabse important baat:** Claude khud detect karta hai kab kaunsi skill use karni hai. Tumhe baar baar batana nahi padta — Claude samajh jaata hai context se.

---

### 🔷 COMMON MISTAKES (Jo Galtiyan Beginners Karte Hain)

---

**Galti 1: "Building capabilities from scratch without checking what already exists in marketplaces."**

Sabse common aur badi galti — **bina check kiye khud banana shuru kar dena.** Pehle marketplace dekho. 90% chances hain koi pehle se bana chuka hai.

---

**Galti 2: "Creating 'mega-skills' that do too much instead of focused, composable skills Claude can combine."**

Yeh bahut important point hai. Log ek aisi skill banate hain jo **sab kuch** karti ho — yeh galat hai. Choti choti **focused skills** banao jo ek kaam achhi tarah karein. Claude inhe khud combine karta hai zaroorat ke mutabiq. Ek "mega tool" banane se behtar hai 5 chhote aur sharp tools.

---

**Galti 3: "Writing vague skill descriptions without specific trigger scenarios and examples."**

Skill ka description likhte waqt **vague (dhamela)** mat likho jaise "yeh skill kaam karta hai." Likho ke **kab trigger hoga** aur **kya example hai.** Claude description padhkar decide karta hai skill use karni hai ya nahi — agar description saaf nahi, Claude confuse ho jaata hai.

---

**Galti 4: "Treating components as separate (skills here, agents there) instead of bundling related capabilities together."**

Jo skills, agents, hooks ek saath kaam karte hain — unhe **alag alag mat rakho.** Unhe ek plugin mein bundle karo. Yeh best practice hai aur isse sab kuch organized aur reusable rehta hai.

---

### 🔷 CONNECTIONS

---

**"Builds on: All Claude Code features (CLAUDE.md, MCP, subagents, skills, hooks, settings) from Lessons 01-15."**

Yeh lesson (Plugins) koi nai cheez nahi seekha raha — yeh **pehle ke saare lessons ka combination** hai. CLAUDE.md, MCP, subagents, skills, hooks — jo sab seekha, plugins unhe ek jagah bundle karne ka tarika hai.

---

**"Leads to: Custom plugin creation and distribution strategies (Part 5+)."**

Aage Part 5 mein tum **khud ke plugins banana aur share karna** seekhoge — apni team ke saath ya public ke liye. Yeh lesson uska foundation hai.

---

### ✅ Ek Line Mein Poora Lesson

> **"Khud se kuch mat banao jab tak marketplace check na kar lo — aur jo bhi banao, usse ek clean plugin mein bundle karo taake doosre bhi use kar sakein."**

