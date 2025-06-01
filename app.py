import os
import re
import shutil
from deep_translator import GoogleTranslator
import os
print(os.getcwd())
# Load functions to scan for
with open('functions.txt', 'r', encoding='utf-8') as f:
    functions_to_translate = [line.strip() for line in f if line.strip()]

# Load blacklist strings (strip quotes and whitespace)
with open('blacklist.txt', 'r', encoding='utf-8') as f:
    blacklist = set(line.strip().strip('"') for line in f if line.strip())

# Ask user mode
mode = input("Do you want to translate a single file or a folder? (file/folder): ").strip().lower()
language = input("To which language you want to translate (e.g., pt, ml, en): ").lower()

translations = {}

def should_translate(text):
    return len(text) > 2 and text not in blacklist

def translate_text(text):
    if not should_translate(text):
        return text
    if text in translations:
        return translations[text]
    try:
        translated = GoogleTranslator(source='en', target=language).translate(text)
        print(f"🔁 {text} → {translated}")
        translations[text] = translated
        return translated
    except Exception as e:
        print(f"⚠️ Error translating '{text}': {e}")
        translations[text] = text
        return text

def translate_line(line):
    if any(func in line for func in functions_to_translate):
        found_strings = re.findall(r'"(.*?)"', line)
        for original in found_strings:
            translated = translate_text(original)
            line = line.replace(f'"{original}"', f'"{translated}"', 1)
    return line

def process_file(filepath, output_path=None, backup=True):
    print(f"\n📄 Processing: {filepath}")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        translated_lines = [translate_line(line) for line in lines]

        if output_path:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.writelines(translated_lines)
            print(f"✅ Saved: {output_path}")
        else:
            if backup:
                os.makedirs("backup", exist_ok=True)
                shutil.copy(filepath, os.path.join("backup", os.path.basename(filepath)))
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(translated_lines)
            print(f"✅ Overwritten: {filepath}")
    except Exception as e:
        print(f"❌ Error: {e}")

if mode == "file":
    filename = input("Enter the Lua file name (with extension): ").strip()
    if os.path.isfile(filename):
        process_file(filename)
    else:
        print("❌ File not found.")

elif mode == "folder":
    foldername = input("Enter the folder path: ").strip()
    if os.path.isdir(foldername):
        output_folder = f"{foldername}_translated"
        os.makedirs(output_folder, exist_ok=True)

        for root, _, files in os.walk(foldername):
            for file in files:
                if file.endswith(".lua"):
                    original_path = os.path.join(root, file)
                    relative_path = os.path.relpath(original_path, foldername)
                    output_path = os.path.join(output_folder, relative_path)
                    process_file(original_path, output_path=output_path, backup=False)
        print(f"\n🎉 All translated files saved to: {output_folder}")
    else:
        print("❌ Folder not found.")
else:
    print("❌ Invalid mode. Please type 'file' or 'folder'.")

print("\n✅ Done.")