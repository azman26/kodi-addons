import os
import hashlib

REPO_DIR = "addons"
OUTPUT_XML = "addons.xml"
OUTPUT_MD5 = "addons.xml.md5"

def collect_addon_xml():
    addons = []
    for root, dirs, files in os.walk(REPO_DIR):
        if "addon.xml" in files:
            with open(os.path.join(root, "addon.xml"), encoding="utf-8") as f:
                content = f.read().strip()
                if content.startswith('<?xml'):
                    # usuń nagłówek XML, jeśli występuje
                    content = "\n".join(content.split("\n")[1:])
                addons.append(content)
    return addons

def write_addons_xml(addons):
    with open(OUTPUT_XML, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<addons>\n')
        for addon in addons:
            f.write(addon + "\n")
        f.write("</addons>\n")
    print(f"Zapisano: {OUTPUT_XML}")

def write_md5():
    with open(OUTPUT_XML, "rb") as f:
        data = f.read()
        md5_hash = hashlib.md5(data).hexdigest()
        with open(OUTPUT_MD5, "w") as md5file:
            md5file.write(md5_hash)
    print(f"Zapisano: {OUTPUT_MD5}")

if __name__ == "__main__":
    print("🔄 Generowanie addons.xml...")
    addons = collect_addon_xml()
    write_addons_xml(addons)
    write_md5()
    print("✅ Gotowe.")
