# `<available_skills>` Section — Mukammal Samajh

---

## Background: Pehle Ye Samjho

Jab tum **Claude Code open karte ho**, Claude Code automatically ek **system prompt** banata hai apne andar.

Ye system prompt Claude ko batata hai ke:

- Tum kaun ho
- Kaunse tools available hain
- Kaunse MCP servers hain
- Aur... **kaunsi skills available hain**

> Ye sab kuch **user nahin banata** — Claude Code ka engine khud ye cheezein generate karta hai har session mein.

---

## `<available_skills>` Section Kahan Se Aata Hai?

Ye section us **automatically generated system prompt ka ek hissa** hai.

Claude Code har session start pe ye kaam karta hai:

1. Scan karta hai `.claude/skills/` folders ko
2. Jo bhi skill files milti hain, unke naam aur descriptions uthata hai
3. Unhe `<available_skills>` section mein daal deta hai
4. Ye poora section Claude ko pass ho jaata hai

---

## Tumhare Case Mein Kya Hua?

```
Step 1: Claude Code ne scan kiya       →  koi skill file mili nahin
Step 2: <available_skills> section bana →  lekin andar kuch daalne ko tha hi nahin
Step 3: Section exist karta hai         →  lekin empty
Step 4: Claude ne jawab diya            →  "available_skills is empty"
```

---

## Real-Life Misaal

Socho ek **restaurant ka menu**:

- Menu **hamesha exist karta hai** — chahe khaana ho ya na ho
- Agar chef ne koi dish prepare nahin ki → menu **blank** hoga
- Lekin menu ka exist karna **chef pe depend nahin karta**

Theek usi tarah:

- `<available_skills>` hamesha exist karta hai — chahe tumne skills banayi hon ya nahin
- Tumhara kaam sirf **skill files banana** hai
- Baaki kaam **Claude Code ka system** khud karta hai

---

## Confusion Ka Root Cause

Tum soch rahe the ke:
> *"Section tab exist karta jab main khud banata"*

Lekin actually:
> **Ye system ka kaam hai ye section banana — tumhara kaam sirf us section ko fill karna hai skill files ke zariye.**

---

## Built-In Hai Ya Har Session Mein Banta Hai?

**Dono cheezein sahi hain — aur dono connected hain.**

### Built-In Part:
Claude Code ke source code mein **hardcoded** likha hua hai ke system prompt mein ek `<available_skills>` section hoga. Ye hamesha rahega — user chahe kuch banaye ya na banaye.

### Har Session Mein Banta Hai:
Us section ka **andar ka content** — yaani skill names aur descriptions — ye har session start pe **fresh scan karke fill hota hai**.

> Agar tum nai skill add karo aur session restart karo, wo automatically show ho jaayegi.

---

## Glass Wali Misaal

Socho ek **glass** ke baare mein:

| Cheez | Kya hai | Kab banta hai |
|---|---|---|
| **Glass** (structure) | `<available_skills>` section | Built-in — hamesha exist karta hai |
| **Paani** (content) | Tumhari skill files ka data | Har session start pe scan karke |

> `<available_skills>` section woh **glass** hai. Tumhari skill files woh **paani** hain.

---

## Summary Table

| Cheez | Kab Banti Hai |
|---|---|
| Section ka **existence** | Built-in — hamesha hai |
| Section ka **content** | Har session start pe scan karke generate hota hai |
