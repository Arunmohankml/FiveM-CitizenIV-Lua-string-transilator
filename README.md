---

# 🌍 FiveM & CitizenIV Lua String Translator

A Python-based bulk translator designed to **translate Lua strings** in scripts for **CitizenIV** and **FiveM**. This tool utilizes **Google Translate** to localize your game scripts while ensuring sensitive or short strings stay untouched.

---

## 🚀 Features

✅ Translate strings in Lua files  
✅ Target **specific functions** only (defined in `functions.txt`)  
✅ 🔒 Skip sensitive strings using `blacklist.txt`  
✅ 🧠 Ignores short/1-2 letter strings like `"a"`, `"ok"`  
✅ 📦 Automatically backs up files (in file mode)  
✅ 📂 Translate entire folders — outputs to a new `_translated` folder  

---

## 📁 File Structure

├── translator.py             # Main translator script  
├── functions.txt             # List of function names to scan (one per line)  
├── blacklist.txt             # List of blacklisted words/phrases to skip  
├── backup/                   # Backup of original Lua file (file mode only)  
├── myscript.lua              # Example original Lua script  
├── myscript_translated/      # Translated output (folder mode)
---

## 🛠️ How It Works

1. 🔍 Scans for function names defined in `functions.txt`  
2. 🧠 Looks for all double-quoted strings in those lines  
3. 🌐 Translates strings using Google Translate (unless blacklisted or too short)  
4. 💾 Saves the result either as:
   - A **backup copy** (`backup/`) for single file mode
   - A **new folder** (`yourfolder_translated/`) for folder mode

---

## 🧩 Setup

### 1. Install Required Library
```
bash
pip install deep-translator
```

2. Create Helper Files

functions.txt

List Lua functions whose strings you want to translate:

ShowText
DrawText3D
NotifyPlayer

blacklist.txt

Words/phrases you want to skip during translation:

"STRING"
"noticeme:info"

---

🧪 Usage

Run the Script

python translator.py

Choose Mode

file → Enter a Lua filename (e.g. main.lua)

folder → Enter a folder name (e.g. client_scripts/)


Enter Language Code

Examples:

pt → Portuguese  
ml → Malayalam  
en → English  
fr → French  
hi → Hindi

---

🌍 Supported Languages

Google Translate supports 100+ languages. View the full list [here](https://cloud.google.com/translate/docs/LANGUAGES)or check below for some common ones:


Code	Language	
en	English	
pt	Portuguese	
ml	Malayalam	
es	Spanish	
ar	Arabic	
zh-cn	Chinese 
ru russian
....

---

✨ Example

🎯 Original Lua

ShowText("Welcome", "You are entering the zone")
TriggerEvent("noticeme:info", "STRING")

🔁 After Translation (e.g., to French)

ShowText("Bienvenue", "Vous entrez dans la zone")
TriggerEvent("noticeme:info", "STRING") -- skipped (blacklisted)


---

⚙️ Customization Tips

Add new function names in functions.txt

Add event names or critical terms to blacklist.txt

Change the translation target anytime via prompt

Only strings inside "double quotes" get translated



---

⚠️ Known Limitations

❌ Does not parse complex Lua syntax deeply — relies on regex

❌ Won't translate strings outside of defined function lines

❌ May mistranslate rare or ambiguous words — review results if needed



---

👨‍💻 Made For

🎮 CitizenIV (GTA IV servers)

🚓 FiveM (GTA V roleplay servers)

🧪 Any Lua-based scripts needing string localization



---

📜 License

MIT License — Free to use, modify, and contribute!


---

🌟 Contribute or Star!

If this saved you time, consider starring ⭐ the repo or contributing via pull requests!

---

