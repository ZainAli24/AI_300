# constitution: آئین / قانون :
Constitution phase Spec Kit Plus mein bohot important hai, especially jab tum AI agents ke saath production-ready apps bana rahe ho. Main ne di gayi link ko read kiya hai, aur ab is ko asaan words mein, beginner level pe samjhaata hoon. Yeh ek tarah ka "rule book" hai jo tumhare poore project ke liye banaya jata hai. Step by step har cheez ko explain karta hoon, taake clear ho jaye ke constitution ka matlab kya hai aur usme hum kya likhte hain.

### 1. Constitution Ka Matlab Kya Hai?
- Constitution ek single document hai (jaise ek file) jo tumhare project ke har hisse (features, code, tests, etc.) ke liye strict rules define karta hai. Yeh "immutable" hota hai, matlab ek baar banao to change nahi karte, taake sab kuch consistent rahe.
- Yeh ek "rules ki kitab" hai jo poore project ke liye hoti hai. Jaise school mein ek rule book hota hai jo sab bachon pe apply hota hai (jaise "class mein shor mat karo"), yahan constitution sab code aur kaam ke rules ek jagah rakhta hai. Is se guarantee hoti hai ke chahe AI machine code likhe ya tum khud (human) likho, sab same rules follow karenge. Koi alag tarike se nahi karega.
- Simple example: Ek mulk (country) ka constitution laws banata hai jo sab citizens pe lagte hain, jaise "Chori mat karo" – yeh sab ke liye same hota hai, ameer ho ya ghareeb. Isi tarah, project ka constitution code ke "laws" banata hai, jaise "Code mein comments dalo" ya "Tests pehle likho." Yeh sab features aur processes pe apply hota hai, taake sab kuch organized rahe.
- Purpose: Quality maintain karna, bugs kam karna, aur "drift" prevent karna (matlab time ke saath standards change na hon). Yeh ensure karta hai ke har feature same level pe ho, traceability ho (kuch galat ho to track kar sako), aur poora project maintainable(matlab project ko future mein change karna asaan rahe, na ke mushkil) bane.

### 2. Constitution Kya Hai Aur Kya Nahi Hai?
- Yeh **global rules** hai jo poore project pe apply hotay hain, na ke ek specific feature pe.
- Yeh alag hai **Specification** se: Specification ek single feature ke bare mein hoti hai (jaise "calculator app mein add aur subtract functions"), lekin constitution sab features ke common rules ke bare mein (jaise "har function mein type hints use karo").
- Example table se samjho (link se liya gaya):

| Constitution (Poore Project Ke Liye) | Specification (Ek Feature Ke Liye) |
|--------------------------------------|------------------------------------|
| Har function mein type hints lagao   | Calculator add, subtract, multiply support kare |
| Code 100% test-covered ho            | Power operation negative exponents handle kare  |
| PEP-8 naming follow karo, lines 100 chars se kam | Results float mein 6 decimal precision ke saath  |

- Yeh "cascade" system banata hai: Constitution se start hota hai, phir specification, plan, tasks, aur code tak quality flow hoti hai. Agar constitution weak ho, to baqi sab weak ho jata hai.

### 3. Constitution Mein Hum Kya Likhte Hain?
- Constitution ek markdown file hoti hai (.specify/memory/constitution.md), jo project-specific hoti hai. Matlab, agar project calculator ka hai, to usme calculator-related rules, na ke kisi data pipeline ke.
- Main sections jo likhte hain (examples ke saath):
  - **Project Principles**: Basic philosophies, jaise "Write tests first (TDD)", "Follow SOLID, DRY, KISS principles" (yeh code design ke rules hain: SOLID matlab single responsibility, etc.; DRY matlab don't repeat yourself; KISS matlab keep it simple stupid).
  - **Technical Standards**: Code ke rules, jaise "Python 3.12+ use karo with type hints on every parameter/return", "PEP-8 naming follow karo, lines ≤ 100 characters", "No magic numbers – named constants use karo" (magic numbers matlab hard-coded numbers jaise 5, instead constant jaise MAX_VALUE = 5).
  - **Testing Requirements**: Testing ke rules, jaise "100% test coverage", "pytest suite use karo, run with uv run pytest".
  - **Quality Gates**: Checks jo pass hone chahiye, jaise "All CI checks must pass before merge", "Code coverage ≥ 80%".
  - **Error Handling**: Jaise exception hierarchy, logging, messages.
  - **Security**: No hard-coded secrets, input validation.
  - **Documentation**: README, code comments, ADRs (Architecture Decision Records) ke rules.
- Rules ko concrete aur testable banana chahiye, na ke vague (jaise "good code" nahi, balke "type hints use karo" jo check kar sako).
- Example excerpt (link se):
  ```
  # Constitution – Calculator Project

  ## Project Principles
  - Write tests first (TDD)
  - Follow SOLID, DRY, KISS
  - Document decisions with ADRs

  ## Technical Standards
  - Python 3.12+ with type hints on every parameter/return
  - PEP-8 naming, lines ≤ 100 characters
  - No magic numbers – use named constants

  ## Testing Requirements
  - 100% test coverage
  - pytest suite, run with `uv run pytest`

  ## Quality Gates
  - All CI checks must pass before merge
  - Code coverage ≥ 80% (strict for new features)
  ```

### 4. Constitution Ko Kaise Banate Aur Use Karte Hain? (Step-by-Step Guide)
Yeh one-time setup hai, project start pe. Har feature ke liye repeat nahi hota.

1. **Create**: AI agent se start karo. Command: `/sp.constitution` aur short prompt do, jaise "Provide a short list of project principles, technical stack, and quality requirements." Agent file generate karega.
2. **Refine**: File ko manually edit karo ya agent se improve karwao. Concrete rules add karo jaise type hints, docstrings, etc.
3. **Review**: Check karo ke har rule testable hai aur categories cover kar raha hai. Prompt use karo: "Show me the generated constitution file and explain what it contains."
4. **Commit**: File ko git mein commit karo. Command: `/sp.git.commit_pr Commit and push the constitution along with current work.` Yeh branch pe push karega aur PR (pull request) open karega.
5. **Validate**: AI se check karwao. 3 prompts use:
   - Clarity check: File clear hai?
   - Cascade validation: Rules downstream (jaise spec, plan) mein apply ho rahe hain? (Example: Divide operation ke constraints).
   - Realism check: Rules practical hain?

Phir, har new feature ke liye: /sp.specify, /sp.clarify, etc. use karo, aur constitution auto apply hota hai.

### 5. Best Practices Aur Tips
- **Commit early**: Feature work se pehle constitution git mein dalo.
- **Project-specific rakho**: Dusre project se copy mat karo bina change ke.
- **Testable rules banao**: Vague mat rakho, measurable criteria use karo.
- **Cascade prompts use karo**: Confirm karo ke rules baqi steps mein flow kar rahe hain.
- **AI se review karwao**: Validation prompts run karo taake strong ho.

### 6. Common Pitfalls (Galtiyan Jo Avoid Karo)
- Copy-paste bina adaptation ke: Irrelevant rules aa jate hain.
- Vague standards: "Good quality" jaise, jo enforce nahi ho sakte; measurable banao.

Yeh constitution project ko strong foundation deta hai, taake AI agent consistent code banaye. Agar tum Spec Kit Plus use kar rahe ho, to pehle yeh banao, phir features add karo. Agar example project try karna ho, jaise calculator, to upar wala excerpt use kar sakte ho. 