Theek hai — main ne jo link diya tha woh padha aur ab us content ko bohot simple, step-by-step aur beginner level mein tumhare hi lafzon (English letters) mein samjha raha hoon. Har bada point aasan sentences mein, phir chhota example ya action. (Source: Spec-Kit Plus page). ([GitHub][1])

---

# 1) Sab se pehle — spec-driven development ka seedha matlab

* Matlab: pehle **spec** (ek clear plan/contract) likhte hain, phir us spec ke mutabiq code banate hain.
* Benefit: kam guesswork, fewer surprises, aur better quality code. ([GitHub][1])

---

# 2) Kyun ab yeh important hai (2025 ki wajah se) — bohot short

* AI tools jaldi bohot code bana dete hain — lekin agar spec nahi hogi to “acha nazar aane wala magar bekaar code” mil sakta hai.
* Agent platforms aur multi-agent systems se galat spec ka nuksan barhta hai.
* Isi liye industry ab “spec-first” workflows ki taraf ja rahi hai. ([GitHub][1])

---

# 3) SDD (Spec-Driven Development) chalanay ke liye 3 zaroori cheezen — bohot asaan

1. **Alignment (sab ki razamandi)**

   * Kya karna hai, scope kya hai, user ka safar kaisa hoga, aur kya nahi karna hai — yeh sab PM, dev, designer, QA, stakeholders se pehle clear karo.
   * Simple action: meeting karo aur 1-page intent brief banao. ([GitHub][1])

2. **Durable artifacts (spec repo mein rakhna)**

   * Spec, plan, aur tests repo mein file ki tarah raho — chat nahin.
   * Simple action: `spec.md` aur `examples/tests` ko repo mein add karo aur PR se review karwao. ([GitHub][1])

3. **Integrated enforcement (spec ka test se bandhna)**

   * Spec ko tests/CI se jodo — agar tests missing hon to PR fail ho jaye.
   * Simple action: har PR mein batao ke yeh spec ke kis section ko pura karta hai. ([GitHub][1])

---

# 4) Practical SDD workflow — step by step (booht simple)

1. **Intent brief** — ek line ya ek page: “Hum kya banana chahte hain?”

   * Example: “Expense tracker jahan user expenses add kar sake.” ([GitHub][1])

2. **AI-drafted spec → human review loop**

   * AI se spec ka draft nikalwa lo, phir team usay edit kare aur clear kare.
   * Action: AI draft ko open karo, unclear points pe team decide kare. ([GitHub][1])

3. **Plan → tasks**

   * Spec ko chhote tasks mein tod do (har task verifiable hona chahiye).
   * Example task: “Add expense form with date, amount, category — test: entry saved.” ([GitHub][1])

4. **Implementation (AI/agent + humans)**

   * Tasks ko assign karo — AI agents code generate karein ya dev likhe, par tests sath mein hon. ([GitHub][1])

5. **Continuous verification**

   * PRs mein spec section ka reference likho aur required tests daalo. CI agar tests fail kare to PR block ho. ([GitHub][1])

---

# 5) Chhote chhote fayde — kyu vibe coding se behtar hai

* Decisions repo mein likhe rehte hain (chat threads mein kho nahi hotay).
* Naye log jaldi samajh jate (onboarding easy).
* Tests se behaviour anchor hota hai, is se rework kam hota. ([GitHub][1])

---

# 6) SDD cycle ko practice karne ke steps (Spec-Kit Plus ke guide ke mutabiq) — seedha list

1. Setup environment — tools/CLI install karo.
2. Define constitution — project ke basic rules aur goals likho.
3. Specify & clarify — spec likho aur unclear cheezen fix karo.
4. Define plan — spec ko tasks mein tod do.
5. Generate task list — har task ko detail do.
6. Implement — code + tests likho.
7. Capstone/chatbot — ek final project ya demo banao.
8. Clarify & analyze — spec ko dobara dekho aur improve karo.
9. Operationalize — spec ko daily workflow mein daal do. ([GitHub][1])

(Ye steps simple actions bhi batate hain: inputs, actions, quality gates, aur common pitfalls — jise guide detail mein explain karti hai.) ([GitHub][1])

---

# 7) Short take-home checklist — jo abhi karo (3-4 chizein)

1. Har feature se pehle **1-page intent brief** aur simple acceptance criteria likho.
2. `spec.md`, `plan.md`, aur `examples/tests` repo mein rakho aur PR se review karwao.
3. Har PR mein likho: “Main is spec ke section X ko implement kar raha hoon” + required tests.
4. Spec ko bhi time-to-time refactor karo — sirf code nahi. ([GitHub][1])

---

Theek hai — ab main bohot hi seedha, step-by-step aur beginner level mein bataunga **kis tarah** yeh 4 cheezen karni hain. Har step ke saath ek chhota template/example bhi de raha hoon. (Urdu — English letters)

---

# Step 0 — chhota context

Feature example lete hain: **“Add Expense”** (user ek expense add kare, save ho jaye). Ab isi ke liye 1-page brief, spec.md, plan.md, tests aur PR banayenge.

---

# 1) **Har feature se pehle — 1-page intent brief**

Kya karo:

1. Ek simple text file banao (ek page ya 5–8 lines).
2. Is mein likho: purpose, basic user flow, aur 2–3 acceptance criteria.

**File:** `intent_add_expense.md`
**Template (copy-paste kar ke bharo):**

```
Title: Add Expense

Purpose:
User apna kharcha (expense) asani se add kar sake.

User flow:
1. User "Add Expense" form kholta hai.
2. User date, amount aur category dalta hai.
3. User "Save" karta hai aur entry list mein dikhai deti hai.

Acceptance criteria:
- AC1: Form se expense add karne par woh list mein aye.
- AC2: Page reload ke baad bhi added expense dikhe (saved).
- AC3: Max 100 entries allowed.
```

Simple hi rakho. Yeh file team ko batati hai “hum kya banana chahte hain”.

---

# 2) **Repo mein spec.md, plan.md, examples/tests rakhna**

Kya karo:

* Repo root ya `docs/` mein ye files add karo: `spec.md`, `plan.md`, `examples/` folder (tests/examples wahan rakho).
* `spec.md` mein detailed rules aur acceptance criteria rakho.
* `plan.md` mein kaam ke chote tasks likho (who does what, rough time).

**spec.md (simple):**

```
Feature: Add Expense

Intent:
User can add an expense with date, amount, category.

Behavior:
- On submit, expense saved to storage.
- Validation: amount must be > 0, date required.
- Limit: max 100 entries.

Acceptance tests (examples):
- Add "Buy milk, 10, 2025-09-30" -> expect list contains that entry.
- Reload page -> expect entry still present.
- Add 101st item -> expect error: "Max 100 entries".
```

**plan.md (simple task list):**

```
Plan:
1. Create AddExpense form (owner: Ali) — 1 day
2. Save to localStorage / backend (owner: Sara) — 1 day
3. Add tests for add and reload (owner: Ali) — 0.5 day
4. PR and review — 0.5 day
```

**examples/tests (pseudo):**

* `examples/add_expense.test.md` with short test steps:

```
Test: Add expense
1. Open app.
2. Open Add form.
3. Fill "Buy milk, 10, today".
4. Click Save.
Expect: list shows "Buy milk".
```

---

# 3) **Har PR mein likho: “Main is spec ke section X ko implement kar raha hoon” + required tests**

Kya karo:

1. Feature pe separate branch banao (`git checkout -b feat/add-expense`).
2. Kaam karne ke baad commit and push karo, phir PR kholo.
3. PR description mein yeh exact cheezein likho:

**PR title:** `feat: implement Add Expense (spec section: Add Expense)`

**PR description template (copy):**

```
Implements: spec.md — "Add Expense" section.

What I changed:
- Added AddExpense form (file: src/components/AddExpense).
- Save logic to localStorage (file: src/lib/storage.js).
- Tests: examples/add_expense.test.md and unit test src/tests/addExpense.test.js

Spec reference:
- spec.md — lines: "Feature: Add Expense" (see file)

How to test:
1. Run `npm start`
2. Go to /app
3. Follow steps in examples/add_expense.test.md

Reviewer checklist:
- [ ] Does behavior match spec.md AC1-AC3?
- [ ] Tests pass locally?
- [ ] Edge cases handled (amount <= 0)?
```

Reviewer (or CI) ko yeh sab chahiye taake woh turant dekh lein ke PR kis spec ko fulfill kar raha hai.

---

# 4) **Spec ko time-to-time refactor karo — sirf code nahi**

Kya karo:

1. Jab product ka requirement badle → spec.md update karo.
2. Spec change bhi commit + PR me bhejo (spec changes ko code changes jaisa review karo).
3. PR ka title likho: `docs(spec): update Add Expense to allow notes field` — taki log samajh saken.

Simple rules:

* Har spec change ka reason likho (example: "Users asked for notes field").
* Update examples/tests accordingly.
* Agar spec change se code break ho sakta hai, uske liye migration steps likho (small note in `plan.md`).

---

# Chhota practical flow (commands) — beginner friendly

```
# 1. New branch
git checkout -b feat/add-expense

# 2. Work: add spec.md, plan.md, examples/, code files

# 3. Save and commit
git add spec.md plan.md examples/ src/...
git commit -m "feat: add expense feature + spec and tests"

# 4. Push
git push origin feat/add-expense

# 5. Open PR on GitHub and paste the PR description template above
```

---

# Reviewer quick checklist (jab tum PR review karo)

* Kya PR spec.md mein diye gaye acceptance criteria ko pura karta hai? (AC1, AC2, AC3)
* Kya tests/examples updated hain aur pass karte hain?
* Kya PR description mein spec section ka reference hai?
* Kya edge-cases handle huye? (validation, errors)

---

# Summary — seedha aur simple

1. **Intent brief** = ek page — kya banana hai.
2. **spec.md** = detailed rules + acceptance criteria. **plan.md** = tasks. **examples/tests** = manual steps ya unit tests.
3. **PR** = batao exactly kis spec section ko implement kar rahe ho + include tests.
4. **Spec update** = agar requirement badle, spec file bhi update karo aur PR se review karwao — spec ko bhi code jaisa treat karo.

---

# Add Expense — Ready files (copy into your repo)

Ye document mein 5 ready files diye gaye hain. Copy-paste karke apne repository mein add kar lo.

---

## File: `intent_add_expense.md`

```
Title: Add Expense

Purpose:
User apna kharcha (expense) asani se add kar sake.

User flow:
1. User "Add Expense" form kholta hai.
2. User date, amount aur category dalta hai.
3. User "Save" karta hai aur entry list mein dikhai deti hai.

Acceptance criteria:
- AC1: Form se expense add karne par woh list mein aye.
- AC2: Page reload ke baad bhi added expense dikhe (saved).
- AC3: Max 100 entries allowed.
```

---

## File: `spec.md`

```
Feature: Add Expense

Intent:
User can add an expense with date, amount, and category. The expense should be saved so it remains after page reload.

Behavior (rules):
- When user opens "Add Expense" form, they must see fields: Date, Amount, Category (and optional: Note).
- On submit:
  - Validate: Amount must be a number > 0.
  - Validate: Date must be present.
  - If valid, save the expense to storage (localStorage or backend).
  - If invalid, show an inline error message and do not save.
- Limit: Do not allow more than 100 saved expense entries. Attempting to add the 101st should show an error.

Data model (example):
- id: string (uuid)
- date: ISO string (YYYY-MM-DD)
- amount: number
- category: string
- note: string (optional)

Acceptance tests / Examples:
- Test 1 (AC1): Add "Buy milk | 10 | Groceries | 2025-09-30" → expect list contains that entry.
- Test 2 (AC2): After adding an entry, reload the page → expect the entry still visible.
- Test 3 (AC3): When there are 100 items, adding one more shows error "Max 100 entries" and it is not saved.
- Test 4 (Validation): Add with amount = 0 or negative → expect validation error and no save.

Notes:
- Spec file should be updated if data fields change (for example, adding currency or more categories).
```

---

## File: `plan.md`

```
Plan: Add Expense feature (high level)

1. Setup & scaffolding
   - Create AddExpense component and page route (owner: <name>) — 0.5 day
2. Save logic
   - Implement save to localStorage and retrieve on load (owner: <name>) — 0.5 day
3. Validation and limit
   - Add validation logic (amount > 0, date required) and max 100 limit (owner: <name>) — 0.5 day
4. Tests & examples
   - Write manual test steps and unit tests (owner: <name>) — 0.5 day
5. PR & review
   - Open PR linking spec and examples, fix review comments (owner: <name>) — 0.5 day

Milestones / Quality gates:
- Must pass all acceptance tests from `spec.md`.
- Unit tests for save & validation must exist.
- PR must include spec reference and examples/tests.
```

---

## File: `examples/add_expense.test.md`

```
Manual test: Add Expense

1. Open the app in browser at the app route.
2. Click "Add Expense" button.
3. Fill fields:
   - Date: 2025-09-30
   - Amount: 10
   - Category: Groceries
   - Note: (optional)
4. Click Save.

Expectations:
- The list shows an item with "Buy milk" or the entered data.
- Reload the page — the item still visible.
- Try to add amount = 0 — expect a validation error message and no new item.
- If 100 items already exist, try adding one more — expect error "Max 100 entries".

Automated test hints (unit/e2e):
- Unit: call saveExpense(data) and assert localStorage contains the item.
- E2E: use Playwright/Puppeteer to submit form and assert list and reload behavior.
```

---

## File: `pr_description_template.md`

```
PR Title:
feat: implement Add Expense (implements spec: "Add Expense")

PR Description:
Implements: `spec.md` — "Add Expense" section.

What I changed:
- Added `src/components/AddExpense` (form UI and validation).
- Implemented save logic in `src/lib/storage.js` (localStorage helper).
- Added unit tests: `src/tests/addExpense.test.js`.
- Added manual test steps: `examples/add_expense.test.md`.

Spec reference:
- See `spec.md` — section: Feature: Add Expense

How to test locally:
1. `npm install`
2. `npm start`
3. Open app and follow steps from `examples/add_expense.test.md`.

Reviewer checklist:
- [ ] Does the behavior match `spec.md` AC1-AC3?
- [ ] Are validation and limit (max 100) implemented?
- [ ] Are tests present and passing?
- [ ] Are edge cases handled (amount <= 0)?

Notes:
- If you want backend saving later, replace `localStorage` calls with API and update spec.
```

---

# Where to put these files (suggestion)

* `intent_add_expense.md` → `/docs/` or repo root
* `spec.md` → `/docs/spec.md`
* `plan.md` → `/docs/plan.md`
* `examples/add_expense.test.md` → `/docs/examples/add_expense.test.md`
* `pr_description_template.md` → `/docs/pr_description_template.md`

---


