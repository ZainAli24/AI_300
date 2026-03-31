# Plan:
**Plan Ka Matlab Sirf Yeh Hai:**  
> **"Sirf yeh batao: Kaise banega"**
yani hum kia tech-stack use karen ge, kia structure ho ga ye hum plan mien btate hai.
---

* Yeh **user ki zubani nahi**, yeh **developer ki zubani baat** hai.  
* Yahan hum **technical details** daalte hain (jaise Next.js, Tailwind, components).  
* Isme hum **kya bana rahe hain** nahi, **kaise bana rahe hain** batate hain — yani **tech stack, structure, rules, order**.

* Yeh **developer level** pe sochna hai, **business level pe nahi**.

---

### **Focus Hamesha Developer Par Hota Hai**

| Sawal | Asaan Jawab (Example: Calculator) |
|------|----------------------------------|
| **Kaise banega?** | Next.js 16.0.1 + Tailwind se |
| **Kya kya parts banenge?** | Display, Buttons, History Panel |
| **Pehle kya, baad mein kya?** | Pehle UI → phir math → phir tests |
| **Kya rules follow karne hain?** | TDD, 85% coverage, mobile responsive |

---

### **Plan Mein Kya Likhna Hai? (Sirf Yeh 4 Cheezain)**

1. **Kaise banega? (Tech Stack)**  
   → Next.js 16.0.1, Tailwind CSS, TypeScript

2. **Kya kya banega? (Components)**  
   → `CalculatorDisplay`, `CalcButton`, `HistoryPanel`

3. **Order kya hoga? (Phases)**  
   →  
   1. UI skeleton  
   2. Math logic  
   3. Error + History  
   4. Theme + Tests

4. **Kya rules honge? (Requirements)**  
   →  
   - Tests pehle likho (TDD)  
   - 85%+ coverage  
   - Keyboard support  
   - No external CSS

---

### **Plan Mein Kya Nahi Likhna**

- User kaise use karega  
- Kyun bana rahe ho  
- Success kaisa dikhega  
- Business problem kya hai  

**Yeh sab Specify mein tha — ab nahi!**

---

### **Command to Run Plan**

```bash
/sp.plan
Next.js 16.0.1 + Tailwind se interactive calculator banao.
Components: Display, Buttons, History.
Phases: UI → Logic → Tests.
Rules: TDD, 85% coverage, keyboard support.
```

---

### **Ek Line Mein Samjho**

> **Plan = Developer ki zubani bolna: "Next.js se banao, components alag karo, pehle tests likho, Tailwind use karo!"**

---

### **Edge Cases Ka Plan Mein Kya Role?**

| Specify Mein | Plan Mein |
|-------------|-----------|
| **Edge case bataya** → "10 ÷ 0 error de" | **Kaise handle karega** → "Error message red mein fade-in, 2 sec baad gayab" |

**Plan mein edge case ka "kaise" likha jata hai**, na ke "kya".

---

**Bas itna hi!**  

-----