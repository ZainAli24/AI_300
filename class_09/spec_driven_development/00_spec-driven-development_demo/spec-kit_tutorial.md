## 1) SpecKit kya hai? (bahut simple)

Spec-Kit ek **framework** hai jo developer aur coding agent dono ko discipline deta hai ke wo bina random coding ke sirf specifications follow karke kaam karein.

Spec-Kit ek coding agent nahi hai, balki ek toolkit hai jo coding agents aur developers ko spec-driven workflow follow karne mein madad karta hai.

---

## 2) Core idea — kyu useful hai (1-2 lines)

* Pehle **socho** (requirements), phir **plan banao**, phir **code** aur phir **test** karo.
* Is se code zyada saaf, kam bugs wala, aur Git history clean rahegi. ([GitHub][1])

---

## 3) Quick setup (basic commands) — seedha aur simple

1. **UV install** (mac/linux example):

   * `curl -LsSf https://astral.sh/uv/install.sh | sh`
     Ye command UV tool install karta hai jo SpecKit chalata hai.
2. **SpecKit install karna** (project folder mein):

   * `uvx speckit .`
     Is command se `.speckit/` aur agent folders ban jate hain; phir tum agent choose karte ho (Claude, Cursor, etc.). ([GitHub][1])

---

## 4) Project structure — kya files banengi aur unka matlab

```
.your-project/
├── .speckit/
│   ├── memory/constitution.md     # project rules & standards
│   ├── scripts/                   # helper scripts
│   └── templates/                 # spec/plan/task templates
├── .cursor/                        # for Cursor agent
├── .codeium/                       # for Codeium prompts
└── .claude/                        # for Claude commands
```

* **constitution.md** = project ke rules (coding style, framework choices).
* **templates/** = jaha spec/plan/task templates milengi.
* **scripts/** = git branch banane aur workflow automate karne ke scripts. ([GitHub][1])

---

## 5) Step-by-step workflow — har step asaan alfaaz mein

### A) Constitution (ek martaba, project start mein)

* Command: `/constitution`
* Karo: ek short sentence do jaise `Write clean and modular code and use Next.js 15 best practices`.
* Result: agent ek `constitution.md` banata hai jisme project ke rules likhe hote hain. Tum inko review kar ke edit kar saktay ho.

### B) Specify (business requirements, non-technical)

* Command: `/specify`
* Karo: simple batao kya chahte ho, example: `I want a basic expense tracker: add/view/delete expenses...`
* Result: spec file banta hai jisme user scenarios, edge cases, acceptance criteria likhe hote hain. Agent ek feature branch bhi bana deta hai.

### C) Clarify (optional — agent sawal karega)

* Command: `/clarify`
* Jab spec incomplete lage to agent sawal karega: e.g. `Recent = last 30 days?`
* Tum jawab do — phir spec aur clear ho jata hai.

### D) Plan (technical plan)

* Command: `/plan`
* Karo: technical instructions do (framework, storage, routes). Example: `Use Next.js app router, server actions, store in localStorage.`
* Result: `plan.md`, `quick-start.md`, `research.md` ban jate hain — yeh developer ko clear roadmap dete hain.

### E) Tasks (break into small tasks)

* Command: `/tasks`
* Result: features small tasks mein divide hotay hain (T001, T002...). Har task chota aur actionable hota hai.

### F) Implement (code likhna)

* Command: `/implement` (ya `/implement T001 to T005` ya `/implement phase 3.1`)
* Strategy: chote chunks mein implement karo — tests pehle (TDD) fir code, phir tests pass. Agent files update karta hai aur tasks mark karta hai.

### G) Test & Merge

* Manual testing quick-start guide se karo.
* Jab sab theek ho to feature branch PR banao aur merge karo. ([GitHub][1])

---

## 6) Test-Driven Development (TDD) — seedha matlab

1. Tests pehle likho.
2. Tests fail hone chahiye (pehle).
3. Code likho taake tests pass ho jayen.
4. Jab tests pass ho jayein, refactor kar lo.
   SpecKit tests folder aur test suites automatically banata hai.

---

## 7) Different agents ka use (simple)

* **Claude / Cursor**: slash commands direct bhejo (`/plan` etc.).
* **Codeium**: agar slash commands nahi hai to `.codeium/prompts/` se prompt file drag-and-drop karo in chat. Yeh manual but kaam karta hai. ([GitHub][1])

---

## 8) New features kaise add karein (baad mein)

* `/specify` se naya feature define karo. SpecKit new feature branch banayega aur wahi workflow follow karega (clarify → plan → tasks → implement).

---

## 9) Pro tips aur troubleshooting (fast)

* Chat clear rakhna: major steps ke baad chat clear karo taake context clean rahe.
* Chote phases mein implement karo — context window khatam nahi hogi.
* Human-in-the-loop: generated files zaroor review karo — agent perfect nahi hota.
* Agar scripts nahi chal rahi: permissions check karo aur UV sahi install hua hai ya nahi.
* Agent commands nahi mil rahe? Agent-specific folder se prompts drag karo (Codeium case). ([GitHub][1])

---

## 10) Example: Expense tracker — asaan flow (what you type and expect)

1. `/constitution` → type: `Write clean and modular code using Next.js 15 best practices`
2. `/specify` → type: `Build expense tracker: add/view/delete, amount/date/category/description, no auth.`
3. `/clarify` → allow agent to ask: `Recent = last 30 days?` → tum: `Yes.`
4. `/plan` → type: `Use Next.js app router, server actions, store in localStorage.`
5. `/tasks` → agent makes T001, T002...
6. `/implement T001 to T003` → agent writes code, runs tests, marks done.
7. Manual test per quick-start instructions → merge.

---

