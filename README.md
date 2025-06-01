# FiveM-CitizenIV-Lua-string-transilator
A python bulk transilator used to transilate lua strings expecially for CitizenIV and FiveM.


🌍 Lua String Translator for CitizenIV / FiveM

This Python tool helps developers translate Lua string values in their CitizenIV and FiveM scripts into any language using Google Translate. It is highly customizable and safe, with support for:

🔎 Translating only within specific function calls

📂 File or folder translation modes

📄 Automatic backup (for single file mode)

⛔ Word blacklist support

🧠 Ignores short or sensitive terms (1–2 letters, event names, etc.)



---

📦 Features

✅ Translate strings in Lua files
✅ Translate specific functions only (defined in functions.txt)
✅ Skip sensitive terms using blacklist.txt
✅ Automatically backup files (in file mode)
✅ Translate entire folder (outputs to <foldername>_translated)
✅ Ignores short strings like "a", "ok" etc.


---

🛠 How It Works

1. Scans Lua files for lines containing function names (e.g. ShowText("Hello"))


2. Translates all "quoted strings" in those lines (unless blacklisted or too short)


3. Saves the result to:

A backup folder (backup/) for single file mode

A new folder (yourfolder_translated/) for folder mode





---

📁 File Structure

├── translator.py          # Main script
├── functions.txt          # Functions to scan for
├── blacklist.txt          # Strings to skip translating
├── backup/                # Backup of original file (file mode only)
├── myscript.lua           # Original script
├── myscript_translated/   # Output folder for translated Lua files (folder mode)


---

✏️ Setup

1. Install Requirements



pip install deep-translator

2. Create helper files:



functions.txt: Add one function per line (e.g. ShowText, DisplayHelp)

blacklist.txt: Add words or event names to exclude from translation (e.g. "STRING", "event:trigger")



---

🚀 Usage

Run the script:

python translator.py

Choose mode:

Type file → then enter a Lua file (e.g. main.lua)

Type folder → then enter a folder name (e.g. client_scripts/)


Enter target language:

Examples:

pt → Portuguese

ml → Malayalam

en → English



---

🧠 How to Customize

Add functions you want to scan in functions.txt

ShowText
DrawText3D
NotifyPlayer

Add blacklist words to skip:

"STRING"
"event:message"

Change translation language by typing new code when prompted (e.g. fr for French)



---

❗ Known Limitations

Translates only lines with matching function names or lines starting with words inisde functions.txt

Does not parse Lua deeply (just regex + line matching)

May mistranslate phrases if the original string is ambiguous



---

🧊 Example

Original Lua:

ShowText("Welcome", "You are entering the zone")
TriggerEvent("noticeme:info", "STRING")

Translated (e.g. to French):

ShowText("Bienvenue", "Vous entrez dans la zone")
TriggerEvent("noticeme:info", "STRING") -- skipped bcz those words are blacklisted!


---

👨‍💻 Made For

CitizenIV GTA IV servers

FiveM GTA V environments

Works on any Lua script with string functions


---

📜 License

MIT License — Free to use and modify!


---
