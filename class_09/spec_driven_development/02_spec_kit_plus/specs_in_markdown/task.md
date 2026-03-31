# Tasks : 
----

### **Tasks Ka Matlab Sirf Yeh Hai:**

> **"Plan ko chhote chhote kaamon mein tod do."**

- Yeh **technical implementation** ka hissa hai, yeh **developer ki zubani baat** hai, yani yahan hum **plan ko actionable steps** mein break karte hain.  
- Har task ek **chhota aur testable piece** hona chahiye — jaise ek chhota kaam jo 1-2 hours mein ho jaye aur check kar sako ke sahi hai ya nahi.

- Yeh **developer level** pe sochna hai, **user ya business level pe nahi**.

---

### **Focus Hamesha Developer Par Hota Hai**

| Sawal | Asaan Jawab (Example: Calculator) |
|------|----------------------------------|
| **Plan ko kaise todna hai?** | Chhote tasks mein, jaise T001: "Add button banao" |
| **Har task kya hoga?** | Ek chhota kaam jo test kar sako, jaise "5+3=8 dikhe" |
| **Dependencies kya hain?** | Pehle test likho, phir code — TDD follow karo |
| **Checkpoint kya hai?** | Har phase ke baad review karo, commit karo, next bolo |

---

## **Tasks Mein Kya Likhna Hai? (Sirf Yeh 4 Cheezain)**
---

### **1. Plan ko Break Karo**  
**Matlab:** Poora bada plan → **chhote-chhote tasks** mein tod do.  
Har task ko **T001, T002…** number do.

| **Galat** | **Sahi** |
|-----------|----------|
| "Calculator banao" | **T001:** "Add button banao" |

**Example (Calculator):**  
```
T001: Display component banao (sirf UI)
T002: Add button banao (sirf button)
T003: Click pe number display ho
```

---

### **2. Har Task Chhota Rakho**  
**Matlab:** Ek task **1-2 hours** mein khatam ho jaye aur **test kar sako**.

| **Galat** | **Sahi** |
|-----------|----------|
| "Poora math logic likho" | **T004:** "Add(5,3) = 8 test pass karwao" |

**Example:**  
```
T004: RED test likho → expect(add(5,3)).toBe(8)
T005: add() function likho → test pass ho jaye
```

> **Testable =** Ya to test pass ho jaye, ya UI mein dikhe.

---

### **3. Dependencies Aur Order (TDD)**  
**Matlab:** Har cheez ka **order fix** karo:  
**Test pehle → Code baad mein → Refactor last**

| **RED** | **GREEN** | **REFACTOR** |
|--------|-----------|--------------|
| Test likho (fail ho) | Code likho (pass ho) | Code clean karo |

**Example:**  
```
T006: RED test → expect(subtract(5,3)).toBe(2)
T007: GREEN → subtract() function likho
T008: REFACTOR → variable names behtar karo
```

---

### **4. Checkpoint Pattern**  
**Matlab:** Har **group** (phase) ke baad **ruk jao**, check karo, commit karo, phir aage badho.

| **Galat** | **Sahi** |
|-----------|----------|
| Sab ek saath karo | **Phase 1 khatam → review → commit → Phase 2 shuru** |

**Example:**  
```
Phase 1 (UI) Complete:
→ T001 to T005 done
→ Review: Sab buttons dikhte hain?
→ Git commit: "feat: basic UI"
→ Next: Phase 2 (Math Logic)
```

---

## **Ek Dum Simple Summary**

| Point | Kya Karna Hai? |
|------|----------------|
| **1. Break** | Plan → T001, T002… |
| **2. Chhota** | 1-2 hours + testable |
| **3. Order** | RED → GREEN → REFACTOR |
| **4. Checkpoint** | Phase khatam → review + commit → next |

---

## **Tumhare Calculator Ka Real Tasks Example**

```bash
/sp.tasks
Plan ko TDD style mein tod do:

T001: RED test → Display component dikhe
T002: GREEN → <CalculatorDisplay /> banao
T003: REFACTOR → class names Tailwind se

T004: RED test → Button "1" click pe "1" dikhe
T005: GREEN → CalcButton component + onClick
T006: REFACTOR → reusable button

Checkpoint: UI Phase 1 complete → review → commit → next
```

---

Yeh 4 points **sirf itna** kehte hain:  
> **"Bada plan → chhote tasks → test pehle → code baad → check karo → aage badho"**

---

### **Command to Run Tasks**

```
/sp.tasks
Plan ko chhote tasks mein tod do: T001 se shuru.
TDD follow: Pehle RED test, phir GREEN implement.
Har phase ke baad checkpoint: Review aur commit.
Example: T001: Add test likho, T002: Add implement karo.
```

---

### **Ek Line Mein Samjho**

> **Tasks = "Yeh chhota kaam karo, test karo, review karo — phir next!"**

Bas itna hi!