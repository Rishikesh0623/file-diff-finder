# File Diff Finder

A multi-engine file comparison web application built using Flask.

This tool supports two distinct diff modes:

- Semantic Diff (Set-Based)
- Structural Diff (Sequence-Based with Side-by-Side View)

---

## 🔹 Features

### 1. Semantic Diff
Designed for configuration-style files where:
- Order does not matter
- Duplicate lines are ignored
- Focus is on unique entries

Best for:
- `.env` files
- `.cfg`, `.ini`
- YAML / property files
- Feature flag lists

---

### 2. Structural Diff
Designed for code or structured documents where:
- Order matters
- Context matters
- Changes must align visually

Uses Python's `difflib.HtmlDiff` to generate:
- Side-by-side comparison
- Highlighted insertions
- Highlighted deletions
- Change context

Best for:
- Source code
- Scripts
- Documentation
- Structured text files

---

## 🔹 File Restrictions

- Only text and script files are allowed.
- Maximum upload size: 5MB.
- Binary files (images, videos, zip, etc.) are rejected.

---

## 🔹 Architecture Overview
app.py
│
├── diff_finder/
│ ├── set_diff.py → Semantic comparison engine
│ ├── sequence_diff.py → Structural comparison engine
│
└── templates/
├── upload.html
└── result.html


The app follows a modular engine-based architecture:

- Presentation layer: Flask + Jinja templates
- Engine layer: Pluggable diff implementations
- Routing layer: Engine selection via dropdown

---

## 🔹 Known Limitations

1. Memory-Based Processing  
   Entire files are loaded into memory for comparison.

2. No Authentication  
   Public upload endpoint without access control.

3. No Streaming Support  
   Large file handling is limited by Flask memory behavior.

4. No Persistent Storage  
   Results are not stored or cached.

5. No Concurrent Scaling  
   Not optimized for multi-user production environments.

---

## 🔹 Performance Bottlenecks

- `difflib.HtmlDiff` is CPU intensive for large files.
- Set-based diff converts entire file into a Python set.
- Large simultaneous uploads could exhaust server memory.

---

## 🔹 Security Considerations

- File extension filtering is basic.
- No deep MIME type validation.
- No content sanitization beyond HTML safe rendering.
- Debug mode should be disabled in production.

---

## 🔹 Future Improvements

### 🔥 Short-Term Upgrades
- Add proper MIME validation
- Add drag-and-drop upload UI
- Improve UI styling
- Add file size progress indicator

### 🚀 Medium-Term
- Add user authentication
- Store diff history
- Add download/export option
- Support Git-style unified diff output

### 🧠 Long-Term
- Implement streaming diff for very large files
- Add line numbering with collapse support
- Add inline comments (code review style)
- Containerize using Docker
- Deploy to cloud (AWS / Azure / GCP)
- Add API version for programmatic access

---

## 🔹 Running Locally

```bash
pip install -r requirements.txt
python app.py
http://127.0.0.1:5000
```

🔹 Tech Stack

Python 3

Flask

difflib

HTML/CSS

Jinja2 templating


---
