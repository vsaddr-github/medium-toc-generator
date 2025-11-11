# 📸 Medium Table of Contents Generator  
### by [Vlads Test Target](https://film4ever.info/vtt)

A lightweight **FastAPI web tool** that automatically generates a working **Table of Contents (TOC)** for any Medium article — directly from a saved `.html` file.  

If you’ve ever wished Medium had a “Insert TOC” button — this is it.  
Upload your article’s saved HTML, and the app instantly extracts all headers (`H1–H6`) and builds clickable section links that work both on desktop and inside the Medium mobile app.  

---

## ✨ Features

✅ Generates a ready-to-paste HTML Table of Contents  
✅ Works with Medium’s **Save As → Webpage, Complete** or **SingleFile** plugin output  
✅ Supports both **desktop** and **mobile** Medium layouts  
✅ Smart case handling (sentence-case with preserved brands and acronyms)  
✅ Live rendered preview — no HTML escapes or textarea clutter  
✅ Optional “Show HTML Source” toggle for inspection  
✅ Instant copy-and-paste into your Medium editor  
✅ No uploads stored — everything runs in memory  
✅ Optional “☕ Buy Me a Coffee” donation link  

---

## 🧰 Tech Stack

| Component | Purpose |
|------------|----------|
| **FastAPI** | Web framework and request handling |
| **BeautifulSoup4** | HTML parsing and tag extraction |
| **Uvicorn** | ASGI server |
| **HTML/CSS** | Lightweight responsive front-end |
| *(optional)* **Render.com** | One-click cloud deployment |

---

## 🖼️ Screenshot (placeholder)
> _Example: live preview and copy-ready TOC output_
>
> ![screenshot-placeholder](https://via.placeholder.com/700x400?text=Medium+TOC+Generator+Preview)

---

## 🚀 Quick Start (Run Locally)

This is just enough to generate Medium TOC localy


For local Python Installation see **PythonInstall.md** file (you need it before you do anything else here)

### 1. Clone this repository
```bash
git clone https://github.com/YOURUSERNAME/medium-toc-generator.git
cd medium-toc-generator
2. (Optional) Create a virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run the app
python app.py

You’ll see something like:

INFO:     Uvicorn running on http://127.0.0.1 (Press CTRL+C to quit)

5. Open your browser

Go to → http://127.0.0.1:7860

You’ll see:

Upload field for .html files

Checkbox to keep original header casing

“Generate TOC” button

Upload your file → get a rendered preview → copy the HTML directly into your Medium article.

🌐 Deploy to Render (optional) 

Push this repo to GitHub.

Go to Render.com
.

Choose New Web Service → connect your repo.

Render will detect render.yaml automatically.

Deploy — no config needed.

You’ll get a public URL like:

https://medium-toc-generator.onrender.com


Share that link — anyone can upload a Medium .html file and generate a TOC instantly.

🧾 File Overview
File	Description
app.py	Main FastAPI application
requirements.txt	Python dependencies
render.yaml	Render deployment config
README.md	This documentation
.gitignore	Keeps local venv/ and temp files out of Git
(optional) .gitattributes	Normalizes line endings and sets syntax highlighting
🧠 How It Works

Upload a saved Medium .html file.

The app parses it using BeautifulSoup.

It finds every H1–H6 header and the paragraph immediately preceding it.

It uses the id of that paragraph to build a clean href="#id" link.

This ensures the section header is visible below the Medium banner,
rather than being hidden behind it.

The result is a <ul> list of section links, ready to paste into your article.

Example:

<ul class="custom-bullets">
  <li><a href="#6cae">Can I use my camera’s kit lens for film digitization?</a></li>
  <li><a href="#38f4">How does focal length affect film digitization?</a></li>
</ul>

⚙️ Options

Keep original header casing
Check the box to leave headings as-is.
Unchecked (default) → automatic sentence-case conversion with smart brand handling.

Show HTML source
Expand the <details> section to inspect or manually copy the HTML.

🧩 Example Use Case

If you write technical, tutorial, or FAQ-style articles — particularly about film digitization, lenses, or camera scanning — a TOC near your hero image gives readers a clear overview and boosts engagement.

Medium doesn’t provide this natively, but your readers will thank you for it.

🪶 Troubleshooting

Problem: TOC links open the article at the top on the Medium mobile app.
Fix: Use only the hash (#id) in your links — do not include the full article URL.

This app already generates links that comply with that rule.

Problem: Some headers don’t appear in TOC.
Fix: Ensure they’re formatted as true headers (H2, H3, etc.) in Medium’s editor, not just bold paragraphs.

Problem: Output HTML doesn’t match your style.
Fix: You can edit CSS inside your Medium article’s code view, or modify the <ul> structure here.

💡 Design Notes

The app intentionally uses the previous paragraph’s ID for linking —
ensuring Medium’s fixed top banner doesn’t cover the section header.

Case handling rules preserve key camera brands, acronyms, and model names (e.g., Canon, GFX100S, MTF).

All processing happens client-side; no data is saved.

☕ Support

If this saved you from pressing F12 again,
consider buying me a coffee
 ☕
and help fund the next set of film-scanning tools and tutorials.

🧑‍💻 Contributing

Pull requests are welcome!
Ideas for improvements:

Custom CSS themes for the output list

Drag-and-drop upload with instant preview

Optional download of generated .html

Multi-article batch processing

Fork the repo → make your changes → submit a PR.

🛡️ License

MIT License
© 2025 Vlad’s Test Target

Permission is granted to use, copy, modify, and distribute this software for any purpose,
provided this notice appears in all copies.

“The medium is still the message — but the message finally got its Table of Contents.”