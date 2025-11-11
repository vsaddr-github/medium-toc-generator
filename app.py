from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from bs4 import BeautifulSoup
import uvicorn

app = FastAPI(title="Medium TOC Generator")

STYLE = """
<style>
body { font-family: system-ui, sans-serif; margin: 2em; background:#fafafa; }
.container { max-width: 720px; margin: auto; background:white; padding:2em; border-radius:12px;
             box-shadow:0 2px 8px rgba(0,0,0,0.1); }
h1, h2 { text-align:center; }
textarea { width:100%; height:320px; font-family:monospace; }
ul.custom-bullets { list-style: none; padding-left: 1.2em; }
ul.custom-bullets li::before {
  content: "● "; color: black; font-size: 1.3em; font-weight: bold;
}
.button {
  background:#0b66ef; color:white; padding:8px 16px; border:none;
  border-radius:6px; cursor:pointer; font-size:1em;
}
a { color:#0b66ef; text-decoration:none; }
footer { text-align:center; margin-top:2em; font-size:0.9em; color:#777; }
.copy-box { margin-top: 1em; }
.logo { text-align:center; font-weight:bold; font-size:1.2em; margin-bottom:1em; }
</style>
"""

HTML_HEAD = f"""
<head>
<meta charset="UTF-8">
<title>Medium TOC Generator | Vlad’s Test Target</title>
<meta name="description" content="Generate a Table of Contents for your Medium articles directly from saved HTML. Upload, process, copy, and paste — quick and simple.">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🎞️</text></svg>">
{STYLE}
</head>
"""

HTML_FORM = f"""
<html>{HTML_HEAD}<body>
<div class='container'>
<div class='logo'>📸 Scan Film Sharp TOC Generator</div>
<h1>Medium Table of Contents Generator</h1>
<p>This tool parses a Medium article saved as HTML (via <b>Save As → Webpage, Complete</b>
or the <b>SingleFile</b> plugin). It extracts all headers and builds a ready-to-paste
Table of Contents that works on both desktop and mobile.</p>

<form action="/upload" enctype="multipart/form-data" method="post">
<input type="file" name="file" accept=".html,.htm" required>
<p><button class="button" type="submit">Generate TOC</button></p>
</form>

<p><a href="https://buymeacoffee.com/" target="_blank">☕ Buy me a coffee</a></p>
</div>
<footer>Made by <b>Vlad’s Test Target</b></footer>
</body></html>
"""

def generate_toc(html_text: str) -> str:
    soup = BeautifulSoup(html_text, "html.parser")
    links = []
    preserve_case = {
        # Personal pronouns (case sensitive)
        'i':'I','I': 'I', 'I\'m': 'I\'m', 'I\'ve': 'I\'ve', 'I\'ll': 'I\'ll', 'I\'d': 'I\'d',
        # Brands (case-insensitive lookup)
        'canon': 'Canon', 'nikon': 'Nikon', 'sony': 'Sony','rodagon': 'Rodagon',
        'fuji': 'Fuji', 'fujifilm': 'Fujifilm', 'leica': 'Leica', "benro": "Benro","oben": "Oben","leofoto": "Leofoto","neewer": "Neewer","bresser": "BRESSER",
        'hasselblad': 'Hasselblad', 'sigma': 'Sigma', 'tamron': 'Tamron','lpl': 'LPL',
        'zeiss': 'Zeiss', 'schneider': 'Schneider', 'kreuznach': 'Kreuznach',
        # Products and technical terms (some case-sensitive)
        'gfx100s': 'GFX100S', 'apo': 'APO', 'mtf': 'MTF',
        # Common acronyms (case-sensitive)
        'usb': 'USB', 'led': 'LED', 'mp': 'MP', 'raw': 'RAW', 'jpeg': 'JPEG','diy': 'DIY',
    }
    for header in soup.find_all(["h1","h2","h3","h4","h5","h6"]):
        prev_p = header.find_previous(["p","li"])
        if prev_p and (prev_p.get("id") or prev_p.get("name")):
            link_text = header.get_text(strip=True)
            words = link_text.split()
            processed = []
            for i, w in enumerate(words):
                wl = w.lower()
                if wl in preserve_case:
                    processed.append(preserve_case[wl])
                elif i == 0:
                    processed.append(w.capitalize())
                else:
                    processed.append(w.lower())
            link_text = " ".join(processed)
            anchor = prev_p.get("id") or prev_p.get("name")
            links.append(f'<li><a href="#{anchor}">{link_text}</a></li>')
    toc_html = "<ul class='custom-bullets'>\n" + "\n".join(links) + "\n</ul>"
    return toc_html or "<p><i>No headers found with valid IDs.</i></p>"

@app.get("/", response_class=HTMLResponse)
async def home():
    return HTML_FORM

@app.post("/upload", response_class=HTMLResponse)
async def upload(file: UploadFile = File(...)):
    html_bytes = await file.read()
    toc_html = generate_toc(html_bytes.decode("utf-8", errors="ignore"))

    return f"""
    <html>{HTML_HEAD}<body><div class='container'>
    <div class='logo'>📸 Scan Film Sharp TOC Generator</div>
    <h1>Generated Table of Contents</h1>

    <p>✅ Below is your rendered Table of Contents.  
    Just select and copy it directly from the page, then paste it into your Medium article.</p>

    <div id="toc-view" style="border:1px solid #ddd; padding:1em; border-radius:8px; background:#fff;">
      {toc_html}
    </div>

    <details style="margin-top:1em;">
      <summary>🔍 Show HTML source (optional)</summary>
      <pre style="background:#f8f8f8; padding:1em; border-radius:6px; overflow:auto;">{toc_html.replace('<','&lt;').replace('>','&gt;')}</pre>
    </details>

    <p style="margin-top:1.5em;"><a href="/">← Back to start</a></p>
    <p><a href="https://buymeacoffee.com/" target="_blank">☕ Buy me a coffee</a></p>
    </div><footer>Made by <b>Vlad’s Test Target</b></footer></body></html>
    """

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=7860)
