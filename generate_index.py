import os

REPO_DIR = "addons"
DOCS_DIR = "docs"
OUTPUT_FILE = os.path.join(DOCS_DIR, "index.html")

def find_addons():
    addons = []
    for root, dirs, files in os.walk(REPO_DIR):
        for f in files:
            if f.endswith(".zip") and "repository" not in root:
                rel_path = os.path.relpath(os.path.join(root, f), DOCS_DIR)
                addon_id = os.path.basename(root)
                addons.append((addon_id, rel_path.replace("\\", "/")))
    return sorted(addons)

def generate_index(addons):
    html = """<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8" />
  <title>Repozytorium Kodi – azman</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 800px; margin: 3em auto; padding: 0 2em; background: #f9f9f9; color: #333; }
    h1 { color: #007acc; }
    a { color: #0066cc; text-decoration: none; }
    a:hover { text-decoration: underline; }
    ul { padding-left: 1em; }
  </style>
</head>
<body>
  <h1>📺 Repozytorium Kodi</h1>
  <p>Oficjalne repozytorium dodatków do Kodi od <strong>azman26</strong>.</p>

  <h2>📦 Repozytorium</h2>
  <ul>
    <li><a href="../addons/repository.azman/repository.azman-1.0.0.zip">📦 Pobierz repozytorium azman (ZIP)</a></li>
    <li><a href="../addons.xml">📄 addons.xml</a></li>
    <li><a href="../addons.xml.md5">📄 addons.xml.md5</a></li>
  </ul>

  <h2>📺 Dostępne dodatki video</h2>
  <ul>
"""
    for addon_id, path in addons:
        html += f'    <li><a href="../{path}">{addon_id}</a></li>\n'
    html += """  </ul>
  <p>Dodaj w Kodi jako źródło:<br><code>https://azman26.github.io/kodi-addons/</code></p>
</body>
</html>
"""
    return html

if __name__ == "__main__":
    os.makedirs(DOCS_DIR, exist_ok=True)
    addons = find_addons()
    index_content = generate_index(addons)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(index_content)
    print(f"✅ Wygenerowano {OUTPUT_FILE}")
