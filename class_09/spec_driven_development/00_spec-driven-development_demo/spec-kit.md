# **Spec-kit:**
Ye asal mein ek **toolkit / framework** hai jo tumhari development ko **spec-driven development (SDD)** style mein organize karta hai.

* GitHub ne isko release kiya hai taake developers aur AI agents dono ek **clear spec** ke mutabiq kaam kar saken.
* Ye tumhe templates, CLI commands, aur best practices deta hai (jaise `spec.md`, `plan.md`, `examples/tests`) taake tum aur AI tools dono ekhi “source of truth” follow karo.

So, simple lafzon mein:

* **Spec-Kit** = ek helper toolkit/framework (rules + templates).
* **Coding agent** = ek AI jo tumhari coding me madad karta hai (jaise OpenAI Agent SDK se banaya hua agent).
* **Relation** = Spec-Kit agents ko guide karta hai ke wo **spec ke mutabiq code likhen**, na ke vibe coding style mein random code generate karein.

👉 Tum keh sakte ho:
“Spec-Kit ek coding agent nahi hai, balki ek toolkit hai jo coding agents aur developers ko spec-driven workflow follow karne mein madad karta hai.”

---------
Spec-Kit ek framework hai jo developer aur coding agent dono ko discipline deta hai ke wo bina random coding ke sirf specifications follow karke kaam karein.


<br> </br>

---

## **Specify**

* Sirf yeh batao: **kya cheez bana rahe ho aur kyun bana rahe ho**.
* Focus hamesha **user** par hota hai.
* Sawalat:

  * Ye app kaun use karega?
  * Ye app unki problem kaise solve karegi?
  * User kaise use karega?
  * Success kaise nazar aayega?
* Example: “Ek todo app students ke liye, jisme wo apne tasks add aur complete kar saken.”

---

## **Plan**

* Ab batao: **kaise banega** (technical details).
* Stack choose karo (Next.js, Node.js, database, etc.).
* Rules aur requirements likho (security, speed, company standards).
* Yahan coding agent detailed technical plan bana dega.
* Example: “Frontend Next.js, backend Supabase, email login, deploy on Vercel.”

---

## **Tasks**

* Plan ko chhote chhote kaamon mein tod do.
* Har task ek chhota aur testable piece hona chahiye.
* Example:

  * Database mein `tasks` table banao.
  * API endpoint for “add task.”
  * UI mein “add task” form.

---

### **Implement**

* Coding agent har task ek ek karke banata hai.
* Aapko sirf chhote code changes review karne hote hain (na ke bade code dumps).
* Har task independent hota hai → asaan test aur review.

---

➡️ Seedha aur simple line:

* **Specify = Kya aur Kyun (user aur problem).**
* **Plan = Kaise (tech aur rules).**
* **Tasks = Chhote pieces (easy testable).**
* **Implement = Banate jao step by step.**

---

