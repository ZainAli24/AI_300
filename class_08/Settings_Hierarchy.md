# Settings Hierarchy (Settings Ka Darajabandi Nizam)

## Roman Urdu Mein Beginner-Friendly Summary (Exam Ke Liye)

---

## Shuruat — Yeh Lesson Kis Baare Mein Hai?

Tumne Skills banaye (Lesson 9), Subagents use kiye (Lesson 11), aur MCP servers connect kiye (Lesson 12). Jaise jaise tumhara agent system barhta hai, **complexity bhi barhti** hai.

Tum in saare tools ke liye **permissions kaise control** karo ge? Tum kaise ensure karo ge ke tumhari team **same safety rules** use kare? Tum har file edit kiye bina **models kaise switch** karo ge?

---

## Settings Kya Hain?

Claude Code ke paas ek **settings system** hai jo tumhe customize karne deta hai ke woh kaise behave kare. Yeh settings in cheezon ko control karti hain:

- **Permission modes** (kya Claude edits se pehle poochhe)
- **Output preferences** (Claude responses kaise format kare)
- **Project-specific defaults** (Claude kaunse tools ko priority de)
- **Team standards** (collaborative kaam ke liye shared rules)

Ek global settings file ki jagah, Claude Code ek **three-level hierarchy** (teen-satah ka darajabandi nizam) use karta hai. Yeh design tumhe **personal preferences, project standards, aur temporary overrides** sab ek saath rakhne deta hai.

---

## Teen Settings Levels (Teen Satahein)

Claude Code settings **teen levels** pe exist karti hain, general se specific tak:

---

### Level 1: User Settings (Sabse General)

**Location:** `~/.claude/settings.json`

**Scope:** Tumhari machine pe tumhare **saare Claude Code projects** pe apply hoti hain

**Kab use karein:**

- Tumhari **personal preferences** (hamesha dark mode use karo, verbose output prefer karo)
- Tumhara **coding style** (consistent formatting choices)
- Tumhare **workflow defaults** (safety ke liye hamesha plan mode prefer karo)

**Example content:**

```json
{
  "model": "claude-sonnet-4-5-20250929",
  "outputStyle": "Concise",
  "includeCoAuthoredBy": true
}
```

---

### Level 2: Project Settings (Beech Ka Level)

**Location:** `.claude/settings.json` (tumhare project directory ke andar)

**Scope:** **Sirf is project** pe apply hoti hain

**Kab use karein:**

- **Team standards** (tumhari team permission settings pe agree karti hai)
- **Project-specific customizations** (yeh project alag framework use karta hai)
- **Temporary standards** (alpha testing ke dauran zyada strict permissions use karo)

**Example content:**

```json
{
  "permissions": {
    "defaultMode": "acceptEdits",
    "allow": ["Bash(npm run test:*)"],
    "deny": ["Read(./.env)"]
  },
  "env": {
    "PROJECT_ENV": "development"
  }
}
```

---

### Level 3: Local Settings (Sabse Specific)

**Location:** `.claude/settings.local.json` (tumhare project directory ke andar)

**Scope:** **Sirf is project pe, sirf tumhari machine pe** apply hoti hain

**Kab use karein:**

- **Temporary overrides** (aaj ke liye alag settings chahiye)
- **Personal experiments** (locally naya workflow test kar rahe ho)
- **Machine-specific settings** (tumhare laptop ko desktop se alag settings chahiye)

**Example content:**

```json
{
  "outputStyle": "Verbose",
  "sandbox": {
    "enabled": true
  }
}
```

---

## Settings Hierarchy Kyun Matter Karti Hai

### Organizational Intelligence Framework

**Team Collaboration Bina Conflicts Ke:** Settings hierarchy teams ko standards share karne deti hai jabke personal customization aur local experimentation bhi allow karti hai — sab bina ek doosre ke kaam mein dakhal diye.

### Context Ki Teen Layers (General Se Specific Tak):

1. **User settings** (`~/.claude/settings.json`): Tumhari personal AI preferences jo tumhare **SAARE projects** mein follow karti hain
2. **Project settings** (`.claude/settings.json`): Team ke agree kiye standards jo project pe **har koi share** karta hai (git ke zariye share hoti hain)
3. **Local settings** (`.claude/settings.local.json`): Tumhare private testing aur experiments (gitignored, kabhi commit nahi hote)

### Pichle Lessons Se Connection:

- **CLAUDE.md (Lesson 05)** project level pe content context provide karta hai
- **Skills (Lesson 09)** hierarchy ke kisi bhi level pe enable ho sakti hain
- **Plugins (Lesson 16)** bundled capabilities configure karne ke liye yahi hierarchy use karenge

---

## Practical Applications (Amaliyaat)

### 1. Cross-Project Preferences (User Level)

Tum hamesha verbose output aur specific model settings prefer karte ho.
→ Inhe `~/.claude/settings.json` mein set karo
→ Yeh preferences tumhare **SAARE projects** mein follow karti hain
→ Project ya local settings specific needs ke liye override kar sakti hain

```json
{
  "model": "opus",
  "outputStyle": "Verbose",
  "includeCoAuthoredBy": true
}
```

### 2. Team Standards (Project Level)

Tumhari team decide karti hai: "Saare projects ko security ke liye .env files ka access deny karna chahiye."
→ Project level pe (`.claude/settings.json`) `permissions.deny: ["Read(./.env)"]` set karo
→ Team ka **har banda automatically** yeh standard le leta hai
→ Is project ke liye user-level settings ko **override** karta hai

```json
{
  "permissions": {
    "defaultMode": "acceptEdits",
    "deny": ["Read(./.env)"]
  },
  "env": {
    "PROJECT_ENV": "development"
  }
}
```

### 3. Personal Workflow Experiments (Local Level)

Tum team ko affect kiye bina naya workflow test karna chahte ho.
→ `.claude/settings.local.json` mein apni experimental settings banao
→ Tumhare changes **private rehte hain, team ko dikhte nahi**
→ Local overrides **project aur user settings dono pe precedence** leti hain
→ File delete karo toh **project/user standards pe wapas** aa jaao

```json
{
  "outputStyle": "Concise",
  "sandbox": {
    "enabled": true
  }
}
```

### Real-World Impact

Is hierarchy ke bina, teams ya toh **rigid standards enforce** karti hain (koi personal customization nahi) ya **chaos mein gir jaati** hain (har kisi ka setup alag). Teen-level system tumhe **consistency AUR flexibility dono** deta hai.

---

## Precedence: Kaunsi Settings Jeetein? (Kaunsi Apply Hogi)

Jab wohi setting multiple levels pe exist kare, Claude Code yeh **precedence order** follow karta hai (sabse specific jeetta hai):

### **Local > Project > User**

Iska matlab:

- **Local settings** project aur user settings dono ko **override** karti hain
- **Project settings** user settings ko **override** karti hain
- **User settings** fallback hain jab kuch zyada specific na ho

### Visual Hierarchy

```
┌─────────────────────────────────┐
│   LOCAL SETTINGS                │
│   .claude/settings.local.json    │  ← Sabse Specific (Sabse Zyada Priority)
│   (sirf tumhari machine, temporary) │
└─────────────────┬───────────────┘
                  ↑ Override karta hai
┌─────────────────────────────────┐
│   PROJECT SETTINGS              │
│   .claude/settings.json          │  ← Team/Project Level
│   (team ke saath share hoti hai) │
└─────────────────┬───────────────┘
                  ↑ Override karta hai
┌─────────────────────────────────┐
│   USER SETTINGS                 │
│   ~/.claude/settings.json        │  ← Sabse General (Fallback)
│   (is machine ke saare projects) │
└─────────────────────────────────┘
```

---

## Example: Settings Precedence Action Mein

### Scenario 1:

Maano tumhare paas hai:

**User level** (`~/.claude/settings.json`):
```json
{ "outputStyle": "Concise" }
```

**Project level** (`.claude/settings.json`):
```json
{ "outputStyle": "Explanatory" }
```

**Local level** (`.claude/settings.local.json`):
```json
{ // Khali ya set nahi }
```

**Result:** Claude Code `outputStyle: "Explanatory"` use karta hai (project level se, kyunke woh user level ko override karta hai)

### Scenario 2: Agar Local Level Bhi Set Ho?

Ab tum temporary local override add karo:

**Local level** (`.claude/settings.local.json`):
```json
{ "outputStyle": "Verbose" }
```

**Naya Result:** Claude Code `outputStyle: "Verbose"` use karta hai (local level se, jo project aur user dono ko override karta hai)

**Yeh kyun matter karta hai:** Tum apne project ke standards ya personal preferences ko affect kiye bina **temporarily apna workflow badal** sakte ho. Kal jab tum local settings file delete karo ge, tum wapas "Explanatory" (project level) pe aa jaao ge.

---

## .claude/ Directory: Isse Delete Mat Karo

Tum shayad apne project mein `.claude/` directory dekho aur sochho: "Kya yeh zaroori hai? Kya mein delete kar sakta hoon?"

**Chhota jawab: Delete mat karo.**

### Ismein Kya Hota Hai:

- `settings.json` — Project-level settings
- `settings.local.json` — Tumhare local, temporary overrides
- Doosri configuration files jo Claude Code ko chahiye

`.claude/` directory woh tareeqa hai jisse Claude Code **project customization store** karta hai. Delete karne se tumhari saari project settings **defaults pe reset** ho jaayengi.

### Kya Karna Chahiye:

- `.claude/settings.json` ko apne `.gitignore` ya `package.json` ki tarah treat karo — yeh tumhari **project configuration ka hissa** hai. Isse **version control mein include** karo (team ke saath share karo).
- Lekin `.claude/settings.local.json` ko tumhare **`.gitignore` mein hona chahiye** (isse personal rakho).

---

## Abhi Configure Nahi Karna — Yeh Part 5 Ka Content Hai

Yeh lesson tumhe sikhata hai ke settings **exist karti hain** aur hierarchy **kaise kaam karti** hai. Tumhe inhe **abhi configure karne ki zaroorat nahi**. Basic Claude Code usage defaults ke saath **bilkul theek kaam karti** hai.

Detailed settings configuration (specific settings kya karti hain, kaise badlein, team policies) **Part 4 content** hai (Spec-Driven Development, team workflows). Abhi ke liye, **bas itna jaano:**

- ✅ Settings **teen levels** pe exist karti hain
- ✅ Precedence hai: **Local > Project > User**
- ✅ Yeh hierarchy **team collaboration + personal customization** enable karti hai

Documentation mein jab `.claude/settings.json` references milein toh samajhne ke liye **itna kaafi** hai.

---

## Sabse Zaroori Baatein Yaad Rakhein (Exam Ke Liye)

1. **Settings system** Claude Code ke behavior ko customize karne deta hai — permissions, output, defaults, team standards
2. **Ek global file ki jagah teen-level hierarchy** hai — personal preferences, project standards, aur temporary overrides ek saath
3. **Level 1: User Settings** (`~/.claude/settings.json`) = Sabse general, saare projects pe apply, personal preferences
4. **Level 2: Project Settings** (`.claude/settings.json`) = Sirf is project pe, team ke saath share hoti hai via git
5. **Level 3: Local Settings** (`.claude/settings.local.json`) = Sabse specific, sirf tumhari machine, private experiments
6. **Precedence order: Local > Project > User** — sabse specific setting jeetti hai
7. **Local settings** project AUR user dono ko override karti hain
8. **Project settings** user settings ko override karti hain
9. **User settings fallback** hain jab kuch zyada specific na ho
10. **Team collaboration bina conflicts ke:** Team standards share karo + personal customization allow karo + safe experimentation space
11. **`.claude/settings.json`** version control mein hona chahiye (team ke saath share)
12. **`.claude/settings.local.json`** `.gitignore` mein hona chahiye (personal, kabhi commit nahi)
13. **`.claude/` directory delete mat karo** — project customization store karti hai, delete karne se sab defaults pe reset
14. **Temporary override ke liye:** Local settings file banao → kaam karo → file delete karo → wapas project/user standards pe
15. **Abhi configure nahi karna** — sirf jaano ke exist karti hain, hierarchy kaise kaam karti hai, precedence kya hai
