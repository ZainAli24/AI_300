Main pehle is link ko achhi tarah se read karta hoon, phir aapko **har ek line** detail mein samjhata hoon.Bilkul! Main ne poora page parh liya. Ab main aapko **har ek line**, **har ek cheez** bohot asaan Roman Urdu mein samjhata hoon. Kuch bhi miss nahi karunga!

---

# **Hooks: Event-Driven Automation**

## **📌 Page Ki Title Aur Opening Lines**

**Title:** "Hooks: Event-Driven Automation"

**Opening definition (pehli 4 bullets):**

```
Hooks are your commands that run automatically when Claude does something.
```

**"Hooks" kya hain?**
- **Hooks** = Aapke wo commands (instructions) jo **automatically** chaltay hain jab Claude kuch karta hai

**Examples diye gaye hain:**

1. **"Claude edits a file → your formatting command runs"**
   - Claude koi file edit karta hai → Aapka formatting command (jaise Prettier) automatically chal jata hai

2. **"Claude runs a bash command → your logging command runs"**
   - Claude koi bash command (terminal command) chalata hai → Aapka logging command (jo record karta hai kya hua) automatically chal jata hai

3. **"You submit a prompt → your context injection runs"**
   - Aap koi prompt submit karte hain (Claude ko kuch kehte hain) → Aapka context injection (extra information automatically add karna) chal jata hai

4. **"Session starts → your setup script runs"**
   - Session shuru hota hai → Aapka setup script (tayyari ka code) automatically chal jata hai

---

### **"Why this matters" (Yeh Kyun Important Hai):**

```
You can *tell* Claude "always format code after editing"—but it might forget. A hook *guarantees* it happens every time, because it's your code running automatically, not Claude choosing to run it.
```

**Simple words mein:**

**Bina Hook:**
- Aap Claude ko **bol** sakte ho: "Code edit karne ke baad hamesha format kar dena"
- Lekin Claude **bhool** sakta hai

**Hook ke sath:**
- Hook **guarantee** deta hai ke yeh har baar hoga
- Kyunki yeh **aapka code** automatically chal raha hai
- Claude choose nahi kar raha, yeh **automatically** ho raha hai

**Real life example:**
- Alarm clock = Hook (guarantee ke aap uthoge)
- Yaad rakhna = Bina hook (bhool sakte ho)

---

## **Section 1: Why Hooks?**

### **"Without hooks" (Bina Hooks):**

Page kehta hai ke bina hooks aap **hope** (ummeed) karte ho ke Claude yeh sab yaad rakhe:

1. **"Format code after editing"** - Code edit karne ke baad format kar de
2. **"Run tests after changes"** - Changes ke baad tests chala de
3. **"Follow your naming conventions"** - Aapke naming conventions (naam rakhne ke qayde) follow kare
4. **"Avoid touching sensitive files"** - Sensitive files (important files jise chuna nahi chahiye) se door rahe

**Problem:** Yeh sab **instructions** hain jo Claude bhool sakta hai

---

### **"With hooks" (Hooks ke sath):**

Page kehta hai ke aap yeh sab **guarantee** kar sakte ho:

1. **"`PostToolUse` hook runs Prettier after every file edit"**
   - **PostToolUse** hook har file edit ke baad Prettier (code formatting tool) chalata hai
   - **PostToolUse** = Tool use hone ke **baad** (after)

2. **"`PreToolUse` hook blocks edits to `.env` files"**
   - **PreToolUse** hook `.env` files (environment files jismein passwords hote hain) ki editing **block** karta hai
   - **PreToolUse** = Tool use hone se **pehle** (before)

3. **"`SessionStart` hook loads project context automatically"**
   - **SessionStart** hook session shuru hote hi project ka context (information) automatically load kar deta hai

4. **"`Notification` hook sends Slack alerts when Claude needs input"**
   - **Notification** hook jab Claude ko input chahiye toh Slack pe alert bhejta hai

---

### **"The key insight" (Khaas Baat):**

```
By encoding rules as hooks instead of prompting instructions, you turn suggestions into **app-level code** that executes every time.
```

**Asaan lafzon mein:**
- Rules ko **hooks** (automatic code) mein daalne se
- Woh **suggestions** (jo bhulaye ja sakte hain) se **app-level code** (jo hamesha chalta hai) ban jaate hain
- **Har baar** execute hote hain — guaranteed!

---

## **Section 2: The Five Main Hook Events**

Yeh table batata hai 5 main hook events kya hain:

| Event | When It Fires | Common Use Cases |
|-------|---------------|------------------|
| **PreToolUse** | Before a tool runs | Validate commands, block dangerous operations, modify inputs |
| **PostToolUse** | After a tool completes | Format code, run tests, log activity |
| **UserPromptSubmit** | When you submit a prompt | Add context, validate input, inject system info |
| **SessionStart** | When Claude Code starts | Load environment variables, show project info |
| **SessionEnd** | When session closes | Cleanup, save logs |

**Har ek ko detail mein samajhte hain:**

### **1. PreToolUse**
- **Kab:** Koi tool chalane se **pehle**
- **Use cases:**
  - **Validate commands** = Commands check karo sahi hain ya nahi
  - **Block dangerous operations** = Dangerous kaam rok do (jaise important files delete karna)
  - **Modify inputs** = Inputs ko change kar do agar zarurat ho

### **2. PostToolUse**
- **Kab:** Tool complete hone ke **baad**
- **Use cases:**
  - **Format code** = Code ko properly format kar do
  - **Run tests** = Tests chala do
  - **Log activity** = Kya hua record kar lo

### **3. UserPromptSubmit**
- **Kab:** Jab aap koi prompt submit karte ho (Claude ko kuch kehte ho)
- **Use cases:**
  - **Add context** = Extra information add kar do
  - **Validate input** = Input check karo theek hai ya nahi
  - **Inject system info** = System ki information automatically add kar do

### **4. SessionStart**
- **Kab:** Jab Claude Code shuru hota hai
- **Use cases:**
  - **Load environment variables** = Environment variables load kar lo
  - **Show project info** = Project ki information dikhao

### **5. SessionEnd**
- **Kab:** Jab session band hota hai
- **Use cases:**
  - **Cleanup** = Saaf-safai karo (temporary files delete karo)
  - **Save logs** = Logs save kar lo

---

**"There are also advanced events..."**

Page kehta hai kuch aur **advanced events** bhi hain:
- `Stop` 
- `SubagentStop`
- `PermissionRequest`
- `Notification`

Yeh specialized workflows (khaas kaam) ke liye hain.

---

## **Section 3: How Hooks Work**

```
Event fires → Hook script runs → Script output affects Claude
```

**Simple flow:**
1. Koi **event** hoti hai (jaise aap prompt submit karte hain)
2. Hook **script** chalti hai (aapka code)
3. Script **output** deti hai jo Claude ko affect karti hai

---

### **"The pattern" (Tarika):**

5 steps batayi gayi hain:

1. **"An event occurs (e.g., you submit a prompt)"**
   - Koi event hoti hai (example: aap prompt submit karte ho)

2. **"Claude Code runs your hook script"**
   - Claude Code aapki hook script chala deta hai

3. **"Script receives JSON input via stdin"**
   - Script ko **JSON format mein input** milti hai **stdin** (standard input) ke zariye
   - **stdin** = Input ka standard tarika (keyboard input jaise)

4. **"Script produces output via stdout"**
   - Script **output** produce karti hai **stdout** (standard output) ke zariye
   - **stdout** = Output ka standard tarika (screen pe print jaise)

5. **"Output gets injected into Claude's context"**
   - Yeh output Claude ke **context** mein inject (daal di jaati) hai
   - Matlab Claude ise dekh ke samajhta hai

---

### **"Exit codes matter" (Exit Codes Important Hain):**

```
• 0 = Success (stdout processed)
• 2 = Block the action (show error)
• Other = Non-blocking warning
```

**Exit code** = Script khatam hone pe jo number return hota hai

- **0** = Kamyabi (Success) — stdout ko process karo
- **2** = Action **block** kar do — error dikhao
- **Koi aur number** = Warning do lekin block mat karo (non-blocking)

**Real example:**
- Script check kare agar `.env` file edit ho rahi hai
- Agar haan, toh exit code **2** return kare
- Action block ho jayega!

---

## **Section 4: Configuring Hooks (Hooks Setup Karna)**

Hooks ko setup karne ke **2 tarike** hain:

---

### **Option 1: Use the /hooks Command (Sabse Asaan)**

**"Run: `/hooks`"**

- Claude Code mein `/hooks` command chalao

**"This opens an interactive menu where you:"**

Yeh ek interactive menu khol deta hai jahan aap:

1. **"Select an event (PreToolUse, PostToolUse, etc.)"**
   - Koi event select karo (PreToolUse, PostToolUse, etc.)

2. **"Add a matcher (which tools to match)"**
   - **Matcher** add karo (kaun se tools ke liye yeh hook chalega)
   - Matcher = Pattern jo decide karta hai kis tool pe apply ho

3. **"Add your hook command"**
   - Apna hook command add karo (jo script chalani hai)

4. **"Choose storage location (User or Project)"**
   - Storage location choose karo:
     - **User** = Sirf aapke liye (sab projects mein)
     - **Project** = Sirf is project ke liye

---

### **Option 2: Edit settings.json Directly (Seedha File Edit Karo)**

**"Hooks are configured in `.claude/settings.json`:"**

Hooks `.claude/settings.json` file mein configure hote hain.

**Example configuration:**

```json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "ToolPattern",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/your-script.sh"
          }
        ]
      }
    ]
  }
}
```

**"Key fields" (Important Fields):**

1. **`EventName`:** Kaun sa event trigger karega (jaise `PreToolUse`, `PostToolUse`)
2. **`matcher`:** Kaun se tools match honge (jaise `Bash`, `Write`, `Edit`, `Read`)
3. **`command`:** Kaun si script chalani hai

---

### **Matcher Patterns (Pattern Matching):**

Yeh table batata hai different patterns kya match karte hain:

| Pattern | Matches |
|---------|---------|
| `"Bash"` | Sirf Bash tool |
| `"Write|Edit"` | Write **YA** Edit tools (dono mein se koi bhi) |
| `"Notebook.*"` | Sab Notebook tools (jo bhi "Notebook" se shuru ho) |
| `""` or omit | Sab tools (us event ke liye) |

**`|`** = OR (ya)
**`.*`** = Wildcard (kuch bhi ho sakta hai)

---

## **Section 5: Try It Now — Your First Hook**

**"Let's log every Bash command Claude runs."**

Chalo har Bash command jo Claude chalata hai use log karte hain (record karte hain).

---

### **Prerequisite (Zaroori Cheez):**

**"Install `jq` for JSON processing"**

- **jq** install karna hoga — yeh JSON ko process karta hai
- macOS: `brew install jq`
- Linux: `apt install jq`

---

### **Method 1: Using /hooks (Sabse Tez)**

5 steps hain:

1. **"Run `/hooks` in Claude Code"**
   - Claude Code mein `/hooks` chalao

2. **"Select `PreToolUse`"**
   - `PreToolUse` select karo (tool chalane se pehle)

3. **"Add matcher: `Bash`"**
   - Matcher add karo: `Bash` (sirf Bash commands ke liye)

4. **"Add hook command:"**
   ```bash
   jq -r '"\(.tool_input.command) - \(.tool_input.description // "No description")"' >> ~/.claude/bash-log.txt
   ```

   **Yeh command kya karta hai:**
   - `jq` JSON ko parse karta hai
   - `.tool_input.command` = Jo command chalani hai woh nikalta hai
   - `.tool_input.description` = Command ki description nikalta hai (agar nahi hai toh "No description")
   - `>>` = Append karta hai (file ke end mein add karta hai)
   - `~/.claude/bash-log.txt` = Is file mein save hota hai

5. **"Choose `User settings` for storage"**
   - `User settings` choose karo (sab projects ke liye)

6. **"Press `Esc` to save"**
   - `Esc` press karke save karo

---

**"Now ask Claude to run `ls` and check your log:"**

Ab Claude se `ls` command chalwao aur log check karo:

```bash
cat ~/.claude/bash-log.txt
```

Aapko dikhai dega ke `ls` command log mein save ho gayi!

---

### **Method 2: Edit settings.json Directly**

**"Add to `.claude/settings.json`:"**

`.claude/settings.json` file mein yeh add karo:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '\"\\(.tool_input.command) - \\(.tool_input.description // \"No description\")\"' >> ~/.claude/bash-log.txt"
          }
        ]
      }
    ]
  }
}
```

**Note:** JSON mein backslashes double hote hain (`\\`)

**"Restart Claude Code and test it."**
- Claude Code restart karo aur test karo

---

## **Section 6: Real Example — UserPromptSubmit Hook**

**"Here's a real hook that tracks prompts (from this book's codebase):"**

Yeh ek real hook hai jo prompts track karta hai (is book ke codebase se liya gaya):

---

### **Script (`.claude/hooks/track-prompt.sh`):**

```bash
#!/usr/bin/env bash
# Track user prompt submissions

# Read JSON input from stdin
INPUT=$(cat)

# Parse the prompt field
PROMPT=$(echo "$INPUT" | jq -r '.prompt // empty')

# Skip if no prompt
[ -z "$PROMPT" ] && exit 0

# Log it
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
echo "{\"timestamp\": \"$TIMESTAMP\", \"prompt\": \"$PROMPT\"}" >> .claude/activity-logs/prompts.jsonl

exit 0
```

**Line by line samjhte hain:**

1. **`#!/usr/bin/env bash`** 
   - Yeh **shebang** hai — batata hai ke yeh bash script hai

2. **`# Track user prompt submissions`**
   - Comment — script ka purpose

3. **`INPUT=$(cat)`**
   - `cat` stdin se input read karta hai
   - `$()` isse variable mein store karta hai
   - `INPUT` variable mein JSON input aa jata hai

4. **`PROMPT=$(echo "$INPUT" | jq -r '.prompt // empty')`**
   - `echo "$INPUT"` = JSON ko output karo
   - `|` = Pipe — output ko next command ko input do
   - `jq -r '.prompt // empty'` = JSON se `.prompt` field nikalo, agar nahi hai toh empty
   - Result `PROMPT` variable mein

5. **`[ -z "$PROMPT" ] && exit 0`**
   - `[ -z "$PROMPT" ]` = Check karo PROMPT empty hai ya nahi
   - `&&` = Agar haan (empty hai), toh
   - `exit 0` = Script successfully band karo (kuch log mat karo)

6. **`TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")`**
   - Current UTC timestamp generate karo
   - Format: `2026-02-18T10:30:00Z`

7. **`echo "{\"timestamp\": \"$TIMESTAMP\", \"prompt\": \"$PROMPT\"}" >> .claude/activity-logs/prompts.jsonl`**
   - JSON object banao timestamp aur prompt ke sath
   - `>>` se file mein append karo
   - `.jsonl` = JSON Lines format (har line ek JSON object)

8. **`exit 0`**
   - Successfully exit karo

---

### **Configuration:**

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/track-prompt.sh"
          }
        ]
      }
    ]
  }
}
```

**Kya hota hai:**

1. Aap prompt submit karte ho
2. Hook JSON receive karta hai: `{"prompt": "your message", "session_id": "..."}`
3. Script prompt extract karti hai, timestamp ke sath log karti hai
4. Session normally continue hota hai

---

## **Section 7: Real Example — PreToolUse Hook**

**"Track when skills are invoked:"**

Jab skills use hoti hain unko track karo:

### **Configuration:**

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Skill",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/track-skill-invoke.sh"
          }
        ]
      }
    ]
  }
}
```

**"What this does:"**

- **"Fires before the Skill tool runs"** - Skill tool chalane se **pehle** fire hota hai
- **"Only matches the `Skill` tool (not Bash, Write, etc.)"** - Sirf `Skill` tool pe match hota hai (Bash, Write pe nahi)
- **"Can log, validate, or modify the tool call"** - Log kar sakte ho, validate kar sakte ho, ya tool call modify kar sakte ho

---

## **Section 8: Real Example — PostToolUse Hook**

**"Track subagent results:"**

Subagent ke results track karo:

### **Configuration:**

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Task",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/track-subagent-result.sh"
          }
        ]
      }
    ]
  }
}
```

**"What this does:"**

- **"Fires after the Task tool completes"** - Task tool complete hone ke **baad** fire hota hai
- **"Receives the task result in JSON input"** - Task ka result JSON input mein milta hai
- **"Can log, analyze, or trigger follow-up actions"** - Log kar sakte ho, analyze kar sakte ho, ya follow-up actions trigger kar sakte ho

---

## **Section 9: Hook Input Format**

**"All hooks receive JSON via stdin. Common fields:"**

Sab hooks ko JSON **stdin** ke zariye milti hai. Common fields yeh hain:

```json
{
  "session_id": "abc123",
  "cwd": "/path/to/project",
  "hook_event_name": "PreToolUse",
  "tool_name": "Bash",
  "tool_input": {
    "command": "npm test",
    "description": "Run tests"
  }
}
```

**Fields ki tafseel:**

- **`session_id`** = Session ki unique ID
- **`cwd`** = Current working directory (kis folder mein kaam ho raha hai)
- **`hook_event_name`** = Kaun sa hook event fire hua
- **`tool_name`** = Kaun sa tool use ho raha hai
- **`tool_input`** = Tool ko kya input diya gaya

---

**"Event-specific fields:"**

Har event ki apni fields hoti hain:

- **`UserPromptSubmit`:** `{"prompt": "user's message"}`
- **`PreToolUse/PostToolUse`:** `{"tool_name": "...", "tool_input": {...}}`
- **`SessionStart`:** Basic session info

---

## **Section 10: Hook Output Format**

### **Simple (Asaan Tarika):**

**"Just print text to stdout:"**

Seedha text print kar do:

```bash
echo "Current time: $(date)"
exit 0
```

---

### **Advanced (Advanced Tarika):**

**"Output JSON for more control:"**

JSON output karo zyada control ke liye:

```bash
echo '{"decision": "allow", "reason": "Auto-approved"}'
exit 0
```

---

### **Block an action (Kisi Action Ko Rokna):**

```bash
echo "Blocked: dangerous command" >&2
exit 2
```

- `>&2` = stderr (error stream) pe print karo
- `exit 2` = Exit code 2 = Action block ho jayega

---

## **Section 11: Combining Multiple Hooks**

**"You can have multiple hooks for the same event:"**

Ek hi event ke liye multiple hooks ho sakte hain:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/validate-bash.sh"
          }
        ]
      },
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/check-files.sh"
          }
        ]
      }
    ]
  }
}
```

**"Different matchers trigger different scripts based on which tool is used."**

Alag alag matchers = alag alag scripts trigger hoti hain based on kaun sa tool use ho raha hai

---

## **Section 12: Debugging Hooks**

**"If hooks aren't working:"**

Agar hooks kaam nahi kar rahe:

1. **"Check the script is executable:"**
   ```bash
   chmod +x .claude/hooks/your-script.sh
   ```
   - Script executable hai ya nahi check karo

2. **"Test manually:"**
   ```bash
   echo '{"test": "data"}' | bash .claude/hooks/your-script.sh
   ```
   - Manually test karo script ko

3. **"Check settings.json syntax:"**
   - Valid JSON hai? Correct structure hai?

4. **"Use debug mode:"**
   ```bash
   claude --debug
   ```
   - Debug mode se hook execution dikhta hai

---

## **Section 13: Where Hooks Live**

**File structure:**

```
.claude/
├── settings.json      # Hook configuration
└── hooks/             # Hook scripts
    ├── _common.sh     # Shared utilities (optional)
    ├── session-info.sh
    ├── track-prompt.sh
    └── validate-bash.sh
```

**"Tip: Use a `_common.sh` file for shared functions like JSON parsing."**

- `_common.sh` file banao shared functions (jaise JSON parsing) ke liye

---

## **Section 14: What's Next**

**"Lesson 16 introduces Plugins..."**

Lesson 16 mein **Plugins** introduce honge:

- **Plugins** = Pre-packaged bundles (ready-made packages)
- Skills, hooks, agents, aur MCP servers ek sath
- Marketplace se install kar sakte ho
- Doosron ne banaye hain

**Difference:**
- **Hooks** = Aap khud customize karte ho Claude Code ka behavior
- **Plugins** = Ready-made capability packages install karte ho

---

## **Section 15: Try With AI (Exercises)**

5 exercises diye gaye hain:

### **Exercise 1: Create a Simple Hook**

> "Help me create a SessionStart hook that shows the git branch and last commit message when I start Claude Code."

**Seekhna kya hai:**
- Complete hook lifecycle (script → configuration → testing)

---

### **Exercise 2: Understand Hook Events**

> "I want to automatically run prettier after Claude edits a JavaScript file. Which hook event should I use?"

**Seekhna kya hai:**
- Event selection aur pattern matching

---

### **Exercise 3: Validation Hook**

> "Help me create a PreToolUse hook that warns me before Claude runs any command with 'rm' or 'delete' in it."

**Seekhna kya hai:**
- Safety guardrails — warnings without blocking

---

### **Exercise 4: Logging Hook**

> "I want to log all the tools Claude uses during a session."

**Seekhna kya hai:**
- Observability — AI behavior ko debug aur analyze karna

---

### **Exercise 5: Debug a Hook**

> "My hook isn't running. Help me debug."

**Seekhna kya hai:**
- Hook debugging methodology

---

## **📝 Complete Summary — Poore Page Ka Khulaasa:**

Yeh page aapko **Hooks** sikhata hai:

1. **Hooks kya hain:** Automatic commands jo events pe trigger hote hain
2. **Kyun zaroori hain:** Instructions bhule ja sakte hain, hooks guarantee dete hain
3. **5 main events:** PreToolUse, PostToolUse, UserPromptSubmit, SessionStart, SessionEnd
4. **Kaise kaam karte hain:** Event → Script runs → Output affects Claude
5. **Kaise setup karein:** `/hooks` command ya `settings.json` edit karo
6. **Real examples:** Bash logging, prompt tracking, skill tracking
7. **Input/Output formats:** JSON input via stdin, text/JSON output via stdout
8. **Debugging:** Executable check, manual testing, debug mode
9. **File structure:** `.claude/settings.json` aur `.claude/hooks/` folder

**Core message:** Hooks se aap Claude Code ka behavior **automatically control** kar sakte ho — har baar guaranteed execution, koi bhoolna nahi!


-----------------------

<br> </br>


--------------------------


Bilkul! Yeh hain **ek line mein** har hook event ki definition — asaan alfaaz mein:

---

## **Advanced Hook Events — One Line Definitions:**

---

### **1. `Stop`**
**Kya karti hai:** Jab aap Claude Code ko manually **stop** karte ho (session abhi chal rahi ho lekin aap rok dete ho)  
**Kab call hoti hai:** Stop button dabane pe ya forcefully session rokne pe

---

### **2. `SubagentStop`**
**Kya karti hai:** Jab koi **subagent** (chhota helper agent jo Claude ne bulaya tha) apna kaam khatam kar ke band hota hai  
**Kab call hoti hai:** Subagent ka task complete hone pe ya subagent fail hone pe

---

### **3. `PermissionRequest`**
**Kya karti hai:** Jab Claude aapse koi **permission** (ijazat) maangta hai kuch karne se pehle (jaise important file delete karna)  
**Kab call hoti hai:** Claude jab approve/deny maange kisi action ke liye

---

### **4. `Notification`**
**Kya karti hai:** Jab Claude aapko koi **notification** (khabar/alert) bhejna chahta hai (jaise "Input chahiye" ya "Error aayi")  
**Kab call hoti hai:** Claude ko jab aapki taraf se koi action ya response chahiye ho

---

**Quick Reference Table:**

| Hook Event | Ek Line Mein |
|------------|--------------|
| **Stop** | Manual stop pe — session rokne pe chalti hai |
| **SubagentStop** | Subagent band hone pe — helper agent khatam hone pe |
| **PermissionRequest** | Permission maangne pe — approve/deny se pehle |
| **Notification** | Alert bhejna ho — jab Claude ko aapka dhyaan chahiye |

Yeh sab **specialized workflows** ke liye hain — matlab advanced use cases jahan precise control chahiye! 🎯

