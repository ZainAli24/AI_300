## Int & Float confusion:
**Pehle ye samjho — int aur float kya hai?**

`int` matlab **poora number** (jaise 25, 100, -3) aur `float` matlab **dashamlav wala number** yani decimal point wala (jaise 25.0, 3.14, -7.5).

**Toh Python 25 aur 25.0 ko alag kyun maanta hai?**

Iska jawab hai — **memory mein dono alag tarike se store hote hain.** Socho aise:

- `25` (int) → Python isko seedha poora number ki tarah store karta hai. Simple, chhota, fast.
- `25.0` (float) → Python isko decimal system mein store karta hai. Thoda zyada jagah leta hai memory mein.

Tum khud check kar sakte ho:

```python
print(type(25))     # <class 'int'>
print(type(25.0))   # <class 'float'>
```

`type()` function tumhe batata hai ke ye kis **type** ka data hai.

**Ab sawaal — kya farq padta hai operations mein?**

Zyada tar operations mein result same aata hai, lekin kuch jagah farq dikhai deta hai:

**1. Division (taqseem) →** Ye sabse bada farq hai:

```python
print(25 // 2)     # 12   (floor division — decimal kaat deta hai)
print(25.0 // 2)   # 12.0 (same kaam, lekin result FLOAT mein aata hai)
```

Dekha? Dono ne "12" diya, lekin ek ne `12` (int) diya aur doosre ne `12.0` (float).

**2. Normal division:**

```python
print(25 / 2)      # 12.5 (hamesha float deta hai)
print(25.0 / 2)    # 12.5
```

Python mein `/` hamesha float result deta hai, chahe int ho ya float.

**3. Precision (exactness) ka masla:**

```python
print(0.1 + 0.2)          # 0.30000000000000004 😱
print(0.1 + 0.2 == 0.3)   # False!
```

Ye float ka ek famous masla hai — computers decimals ko 100% sahi store nahi kar paate. Lekin integers (int) mein ye problem kabhi nahi aati.

**4. Comparison (muqabla):**

```python
print(25 == 25.0)    # True  (value same hai)
print(25 is 25.0)    # False (type alag hai, toh ye alag cheezein hain)
```

`==` **value** check karta hai (barabar hai ya nahi), jabke `is` check karta hai ke **bilkul same cheez** hai ya nahi.

**Toh kab kya use karna chahiye?**

| Situation | Kya use karo |
|---|---|
| Counting (ginti) — jaise 5 students | `int` |
| Paisa, weight, temperature | `float` |
| Loop chalana (1 se 10 tak) | `int` |

**Aasan summary:** Python int aur float ko alag isliye rakhta hai kyunke dono ka **kaam alag** hai, **memory mein alag store** hote hain, aur kuch operations mein **result ka type badal** jaata hai. Beginner ke liye golden rule ye hai: agar decimal chahiye toh float uso, warna int kaafi hai.
