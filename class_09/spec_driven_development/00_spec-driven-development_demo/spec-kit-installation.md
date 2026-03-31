# Spec-kit installation Guid:
1. **Maqsad (short):**
   Apni machine ko ready karna taake *Spec Kit / SpecifyPlus* tools friction ke baghair chal saken. ([GitHub][1])

2. **Jo cheezein chahiye (Inputs) — simple:**

   * `Git` installed aur apke editor ke sath configure hona chahiye.
   * `Python 3.10+` ya phir *Astral uv* runtime (jis se `uvx` chal sakay).
   * Ek coding agent set up karo — jaise GitHub Copilot, Claude Code, Gemini CLI, Cursor, waghera.
     Ye basic requirements docs mein likhi hain. ([GitHub][1])

3. **SpecifyPlus install karna — commands (recommended):**

   * Persistent install (recommended):

   ```bash
   pip install specifyplus
   ```

   * Agar tum *uv* toolchain use karte ho to:

   ```bash
   uv tool install specifyplus
   ```

   * One-off chalaane ke liye (agar install nahi karna):

   ```bash
   uvx specifyplus --help
   uvx specifyplus init <PROJECT_NAME>
   # shortcut:
   uvx sp init <PROJECT_NAME>
   ```

   (Ye instructions docs se li gayi hain — pip/uv dono options diye gaye hain). ([GitHub][1])

4. **Readiness checks (confirm karo tool sahi laga):**

   ```bash
   specifyplus --help
   # ya
   sp --help

   specifyplus check
   # ya
   sp check
   ```

   Agar `--help` aur `check` sahi exit code return karen to install theek hai. ([GitHub][1])

5. **Project bootstrap karna (naya project banana):**

   ```bash
   specifyplus init MyProject
   # ya
   sp init MyProject
   ```

   * Is se ek naya repo scaffold banta hai.
   * Dekho `.github/` aur `.specify/` folders — `.github` mein agent prompts/automation rehte hain aur `.specify` mein specs, plans aur tasks hotay hain. Jab samajh aa jaye to sandbox (temporary folder) delete kar do. ([GitHub][1])

6. **Slash-command flow (coding agent ke andar chalana):**
   Ye commands agent ke andar type kar ke chalate ho — sequence follow karna hota hai:

   * `/constitution` — project ke rules aur guardrails banane/ update karne ke liye.
   * `/specify` — feature ka “what” aur “why” record karne ke liye (spec likhna).
   * `/clarify` — agar koi ambiguity ho to clear karo (ye `/plan` se pehle chalana zaroori hai, jab tak explicitly skip na kiya ho).
   * `/plan` — technical approach, stack choices aur quickstart banata hai.
   * `/tasks` — plan ko chhote actionable tasks mein todta hai.
   * `/analyze` — tasks ke baad check karta hai ke sab coverage hai ya koi gap hai.
   * `/implement` — tasks ko sequence se execute karta hai (automated guardrails ke sath).
     Har command ka maksad docs mein seedha likha hua hai — simple flow follow karo. ([GitHub][1])

7. **Deliverables (kya milna chahiye):**

   * Ek fresh repository jo Spec Kit ke liye ready ho.
   * Ek verified `uvx` runner jo `specifyplus` ko invoke kar sake. Ye doc mein expected outputs hain. ([GitHub][1])

8. **Quality gates (simple checks):**

   * `uvx specifyplus --help` exit status 0 de.
   * `git status` nayi project folder mein clean working tree dikhaye (no uncommitted changes).
     Agar ye dono theek hain to basic gate pass mana jata hai. ([GitHub][1])

9. **Common pitfalls (dhyan rakho):**

   * `uvx` ko npm se install karna deprecated/galat ho sakta hai — official `uv` installer use karo.
   * Agar agent prompts properly configure nahi hue to slash commands expected tarah behave nahi karenge. ([GitHub][1])

10. **Quick tips (practice ke liye):**

    * Pehle ek sandbox folder banake `sp init test` chala kar result dekho. `.github` aur `.specify` ka structure dekh lo.
    * Commands ek ek karke chalao: pehle `--help`, phir `check`, phir `init`.
    * Agar koi error aaye to `git status` aur `specifyplus check` outputs copy kar lo — error solve karna asaan ho jayega.

---

# Short summary + links (for reference)

* Main docs page (jo aap ne bheji): Spec Kit Plus setup docs. ([GitHub][1])
* Original Spec Kit (GitHub) — explains `.github` aur `.specify` roles. ([GitHub][2])
* SpecifyPlus package info (PyPI / package listing). ([data.safetycli.com][3])

---

Agar chaho to main abhi aap ke liye **bilkul step-by-step commands** ka chhota checklist bana doon (jo aap terminal mein copy-paste kar sako) — seedha aur minimal. Batao main wohi paste kar doon?

[1]: https://github.com/panaversity/spec-kit-plus/tree/main/docs-plus/05_spec_driven_development/01_setup_speckit_plus "spec-kit-plus/docs-plus/05_spec_driven_development/01_setup_speckit_plus at main · panaversity/spec-kit-plus · GitHub"
[2]: https://github.com/github/spec-kit?utm_source=chatgpt.com "Toolkit to help you get started with Spec-Driven Development"
[3]: https://data.safetycli.com/packages/pypi/specifyplus/?utm_source=chatgpt.com "specifyplus | Safety DB"
