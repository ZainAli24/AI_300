# **Understanding `/Context`:**

**Context Window kya hai?**

Claude Code ka context window uski total memory hai — tumhare case mein **200k tokens**. Ismein sab kuch hota hai: system prompt, tools, tumhare messages, code files — sab kuch ek hi jagah mein fit hota hai.

**Ab 33k Autocompact Buffer exactly kya hai?**

Ye 33k tokens context window ka ek **permanently reserved hissa** hai. Ye tumhare kaam ke liye available nahi hai. Iska matlab ye hai ke tumhare actual usable tokens **200k nahi, balke ~167k** hain.

Ye reserved space isliye rakha gaya hai kyunke jab compaction trigger hoti hai, toh Claude Code ko us waqt kaam karne ke liye jagah chahiye — purani conversation padhna, uska summary banana, aur wo summary wapas likhna. Ye sab process in 33k tokens ke andar hota hai.

**Trigger kab hota hai?**

Jab tumhare messages, code, tools waghaira milke wo **167k ki usable space poori bhar dein** (yaani free space zero ho jaye), toh auto-compact fire hota hai. Us waqt Claude Code tumhari purani conversation history ko **summarize** karke chota kar deta hai taake dobara free space ban jaye aur kaam continue ho sake.

**Summarization mein kya hota hai?**

Claude Code purani conversation ko padhta hai, usmein se key decisions, important code changes, aur zaroori context nikaalta hai, aur baaki detail discard kar deta hai. Iska nuksaan ye hai ke kuch specific cheezein — jaise exact variable names, error messages, ya shuru ki detailed instructions — kho sakti hain.

**Tumhare screenshot ka breakdown:**

| Category | Tokens | Meaning |
|---|---|---|
| System prompt | 5.5k | Claude Code ke internal instructions |
| System tools | 8.7k | Available tools ki definitions |
| Skills | 237 | Loaded skills |
| Messages | 8 | Tumhari abhi tak ki conversation (almost empty) |
| Free space | 153k | Ye tumhara actual available kaam ka space hai |
| Autocompact buffer | 33k | Reserved — tumhare liye available nahi |

Toh jab wo **153k free space** bhar jayega (messages, code reads, tool outputs se), tab auto-compact trigger hoga.

**Ek important baat:** Pehle ye buffer 45k tokens hota tha, lekin Claude Code ne recently apna autocompact buffer 45k se 33k tokens tak reduce kar diya hai — jo tumhein roughly 12k extra usable space deta hai. Ye change officially announce nahi kiya gaya tha.

Agar tum chahte ho ke auto-compact tumhare kaam ke beech mein trigger na ho, toh **logical breakpoints** pe khud manually `/compact` command chalao — isse tum control mein rehte ho ke kab summarization ho aur kya preserve ho.