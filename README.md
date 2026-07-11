# Shashank U

CSE undergraduate at REVA University, Bengaluru (B.Tech, 2024–2028).

I build full-stack web apps, systems-level tools in C, and applied ML/CV projects. Current focus: DSA in C/C++, backend engineering, and agentic AI systems.

- 🏆 Winner — Apify Track & SuperPlane Challenge, Bot-a-thon 2026 (FileMind)
- Top 25 on the REVA University leaderboard, GeeksforGeeks
- Completed the Wadhwani Foundation Ignite India program

---

## FileMind — Bot-a-thon 2026 winner (Apify Track · SuperPlane Challenge)

A codebase investigation agent built in 48 hours with [Pranav Rao](https://github.com/PranavOaR). Instead of RAG over pre-indexed embeddings, the agent explores a repository the way a developer does — start at the root, read the tree, grep for patterns, follow imports — so every answer comes with an auditable reasoning trail and exact `file:line` citations, and there's no index to go stale.

- Agent loop on Claude Opus 4.5 (up to 25 iterations) over five primitives: `tree`, `read`, `grep`, `jump` (definition navigation), and `summarize` (Claude Haiku 4.5 with per-file caching)
- Next.js frontend + Express backend; the investigation trace streams to the client over Server-Sent Events
- Import graph built across module systems; immutable session state for replay/debugging
- My part: remote GitHub repo ingestion via Apify Actors, investigation event tracking with SuperPlane, and deployment

[Repo](https://github.com/Shashank-U-04/botathon) · [Live](https://botathon-nine.vercel.app) · [Write-up](https://pranavrao.vercel.app/blog/filemind-botathon)

---

## Projects

**[CodeVisionAI](https://github.com/Shashank-U-04/CodeVisionAI)** — Interactive code execution visualizer for Python, C, C++, and Java. Step through programs line by line with live stack and heap views. Python runs in-browser via Pyodide (WebAssembly); C/C++ use GDB via pygdbmi and Java uses JDI, all streaming a unified `EngineEvent` format over SSE from a FastAPI backend. Next.js + Monaco Editor + Zustand frontend in a Turborepo monorepo.

**[NRL Adaptive Learning System](https://github.com/Shashank-U-04/NRL-Adaptive-Learning-System)** — Cybersecurity learning platform with real-time difficulty adaptation. Three-phase engine: deterministic safety rules → optional PyTorch DQN policy (trained offline) → heuristic fallback, so it works with or without trained weights. FastAPI + async SQLAlchemy 2.0 on PostgreSQL (Neon), Supabase Auth with server-side JWT validation, Next.js 16 / React 19 frontend.

**[Plagiarism Detector](https://github.com/Shashank-U-04/Plagiarism-Detector)** — Native Windows desktop app in C99 (Win32 + GDI, no frameworks) that compares up to 10 documents using LCS dynamic programming — a rolling two-row DP for the N×N similarity matrix and full-table DP to recover matched segments. Handles plain text, native-text PDFs, and scanned/handwritten PDFs with auto-detected OCR routing through Tesseract and Poppler.

**[SentinelAI](https://github.com/Shashank-U-04/SentinelAI-Autonomous-Cyber-Defense)** — Autonomous cyber defense pipeline: ingests logs, flags anomalies with an Isolation Forest, classifies threats (brute force, port scans, exfiltration, suspicious logins) with rule-based logic mapped to MITRE ATT&CK, and executes responses like IP blocking with full incident logging. Python, scikit-learn, Streamlit dashboard.

**[Football League Management System](https://github.com/Shashank-U-04/Football-League-Management-System)** — Tournament management app used as a DBMS deep-dive: MySQL schema normalized to 3NF with triggers for automatic leaderboard updates, stored procedures for transactional score recording, views, and custom statistical functions. Node.js/Express REST API, Next.js frontend.

**[Real-Time Writing with Fingers](https://github.com/Shashank-U-04/Real-Time-Writing-with-Fingers)** — Draw on a virtual canvas through a webcam using hand gestures. MediaPipe hand landmark detection with finger-state classification for draw / select / erase modes, OpenCV frame pipeline merging the canvas layer with live video, runs in real time on CPU.

**[Text Encryption/Decryption](https://github.com/Shashank-U-04/Text-Encryption-Decryption-system-GUI)** — Caesar and Vigenère ciphers implemented twice: as a C Win32 GUI application, and as a [Node.js/Express web app](https://github.com/Shashank-U-04/Text-Encryption-Decryption-system-Web_Application) with `.txt` file upload/download via Multer. Started as a data structures course project.

---

## Tech Stack

**Languages**

<p>
<img src="https://img.shields.io/badge/c-%2300599C.svg?style=flat&logo=c&logoColor=white" alt="C" />
<img src="https://img.shields.io/badge/c++-%2300599C.svg?style=flat&logo=c%2B%2B&logoColor=white" alt="C++" />
<img src="https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54" alt="Python" />
<img src="https://img.shields.io/badge/typescript-%23007ACC.svg?style=flat&logo=typescript&logoColor=white" alt="TypeScript" />
<img src="https://img.shields.io/badge/javascript-%23323330.svg?style=flat&logo=javascript&logoColor=%23F7DF1E" alt="JavaScript" />
<img src="https://img.shields.io/badge/sql-%2307405e.svg?style=flat&logo=postgresql&logoColor=white" alt="SQL" />
</p>

**Frontend**

<p>
<img src="https://img.shields.io/badge/react-%2320232a.svg?style=flat&logo=react&logoColor=%2361DAFB" alt="React" />
<img src="https://img.shields.io/badge/Next-black?style=flat&logo=next.js&logoColor=white" alt="Next.js" />
<img src="https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=flat&logo=tailwind-css&logoColor=white" alt="TailwindCSS" />
<img src="https://img.shields.io/badge/html5-%23E34F26.svg?style=flat&logo=html5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/css3-%231572B6.svg?style=flat&logo=css3&logoColor=white" alt="CSS3" />
</p>

**Backend**

<p>
<img src="https://img.shields.io/badge/node.js-6DA55F?style=flat&logo=node.js&logoColor=white" alt="Node.js" />
<img src="https://img.shields.io/badge/express.js-%23404d59.svg?style=flat&logo=express&logoColor=%2361DAFB" alt="Express.js" />
<img src="https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi&logoColor=white" alt="FastAPI" />
<img src="https://img.shields.io/badge/JWT-black?style=flat&logo=JSON%20web%20tokens" alt="JWT" />
</p>

**Databases**

<p>
<img src="https://img.shields.io/badge/postgres-%23316192.svg?style=flat&logo=postgresql&logoColor=white" alt="PostgreSQL" />
<img src="https://img.shields.io/badge/mysql-4479A1.svg?style=flat&logo=mysql&logoColor=white" alt="MySQL" />
<img src="https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=flat&logo=mongodb&logoColor=white" alt="MongoDB" />
<img src="https://img.shields.io/badge/Supabase-3ECF8E?style=flat&logo=supabase&logoColor=white" alt="Supabase" />
</p>

**ML / CV**

<p>
<img src="https://img.shields.io/badge/opencv-%23white.svg?style=flat&logo=opencv&logoColor=white" alt="OpenCV" />
<img src="https://img.shields.io/badge/MediaPipe-000000?style=flat" alt="MediaPipe" />
<img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat&logo=scikit-learn&logoColor=white" alt="scikit-learn" />
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white" alt="PyTorch" />
<img src="https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white" alt="NumPy" />
<img src="https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white" alt="Pandas" />
</p>

**Systems & Tooling**

<p>
<img src="https://img.shields.io/badge/Win32%20API-0078D6?style=flat&logo=windows&logoColor=white" alt="Win32 API" />
<img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/git-%23F05033.svg?style=flat&logo=git&logoColor=white" alt="Git" />
<img src="https://img.shields.io/badge/vercel-%23000000.svg?style=flat&logo=vercel&logoColor=white" alt="Vercel" />
<img src="https://img.shields.io/badge/Google_Cloud-4285F4?style=flat&logo=google-cloud&logoColor=white" alt="Google Cloud" />
</p>

---

## GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=Shashank-U-04&theme=github_dark&show_icons=true&hide_border=true" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Shashank-U-04&layout=compact&hide=html,css&theme=github_dark&hide_border=true" />
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=Shashank-U-04&theme=github-dark&hide_border=true" />
</p>

---

## Contact

- Email: shashank.u.shashu1359@gmail.com
- LinkedIn: [shashank-u-016b54330](https://www.linkedin.com/in/shashank-u-016b54330/)
