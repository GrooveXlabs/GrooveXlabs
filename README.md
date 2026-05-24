<div align="center">

<!-- Animated Typing Header -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=26&duration=2500&pause=700&color=FF006E&center=true&vCenter=true&width=550&lines=GrooveXlabs+Password+Analyzer;Check+Strength.+Learn+Security." alt="Typing Animation" />

<br>

<!-- Cyberpunk Banner -->
<img src="https://capsule-render.vercel.app/api?type=venom&color=0:0f0c29,50:302b63,100:24243e&height=150&section=header&text=Password%20Strength%20Analyzer&fontSize=35&fontColor=00d4ff&animation=fadeIn&fontAlignY=55&desc=Security-first%20password%20complexity%20checker%20built%20for%20learning&descSize=14&descAlignY=75&descColor=a8a8b3" width="100%" />

<br><br>

<!-- Badges -->
<a href="https://github.com/GrooveXlabs/GrooveXlabs">
  <img src="https://img.shields.io/badge/🔒%20Security-First-ff006e?style=for-the-badge&labelColor=0f0c29" />
</a>
<a href="https://github.com/GrooveXlabs/GrooveXlabs">
  <img src="https://img.shields.io/badge/🐍%20Python-3.10+-3776AB?style=for-the-badge&labelColor=0f0c29" />
</a>
<a href="https://github.com/GrooveXlabs/GrooveXlabs">
  <img src="https://img.shields.io/badge/📡%20Open%20Source-Always-7b2cbf?style=for-the-badge&labelColor=0f0c29" />
</a>
<a href="LICENSE">
  <img src="https://img.shields.io/badge/📜%20License-MIT-00d4ff?style=for-the-badge&labelColor=0f0c29" />
</a>

<br><br>

<!-- Divider -->
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png" width="100%" />

</div>

## 🔐 Overview

**GrooveXlabs Password Strength Analyzer** is a lightweight, educational Python tool that evaluates password security based on length, character diversity, and common weakness patterns. Built for learning cybersecurity fundamentals — because strong passwords are the first line of defense.

---

## ✨ Features

| Check | Description | Points |
|-------|-------------|--------|
| **Length** | 8+ chars = +1, 12+ chars = +2 | 1–2 |
| **Uppercase** | Contains `A–Z` | +1 |
| **Lowercase** | Contains `a–z` | +1 |
| **Digits** | Contains `0–9` | +1 |
| **Special Chars** | Contains `!@#$%^&*(),.?":{}\|<>]` | +1 |
| **Pattern Check** | No common weak patterns (`123`, `password`, `qwerty`, etc.) | +1 |

**7 strength levels** from *Very Weak* → *Excellent*, with actionable feedback on every check.

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/GrooveXlabs/GrooveXlabs.git
cd GrooveXlabs

# Run the CLI analyzer
python password_checker.py
```

**Example:**
```bash
$ python password_checker.py
Enter a password to test: MyS3cur3!P@ss

Password Strength: Excellent
Your password looks strong!
```

---

## 📊 Scoring Logic

```
┌─────────────────────────────────────────────────────────────┐
│  Score  │  Rating                                            │
├─────────────────────────────────────────────────────────────┤
│   0     │  Very Weak  →  Immediately crackable               │
│   1     │  Weak       →  Guessable in seconds                │
│   2     │  Moderate   →  Resists basic attacks               │
│   3     │  Good       →  Decent for low-risk accounts        │
│   4     │  Strong     →  Brute-force resistant               │
│   5     │  Very Strong→  Enterprise-grade                    │
│   6     │  Excellent  →  Maximum entropy achieved            │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛡️ Security Principles Applied

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   🔐 NEVER TRUST INPUT     🛡️ LEAST PRIVILEGE     🧱 DEFENSE DEPTH │
│                                                                     │
│   🔒 PRIVACY BY DESIGN     ✅ SECURE BY DEFAULT    ⚠️ FAIL SECURELY │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

> **Privacy Note:** This tool runs entirely offline. No passwords are ever transmitted, logged, or stored.

---

## 🗺️ Related GrooveXlabs Projects

| Repository | Description |
|---|---|
| [simple-port-scanner](https://github.com/GrooveXlabs/simple-port-scanner) | Educational TCP port scanner |
| [security-notes](https://github.com/GrooveXlabs/security-notes) | Curated cybersecurity learning notes |
| [toolsmith-agent](https://github.com/GrooveXlabs/toolsmith-agent) | Autonomous tool discovery & builder |

---

## 🧠 Learning Path

1. **Start here** — Understand what makes passwords weak
2. **Try the scanner** — Test your own passwords safely (offline!)
3. **Read the code** — See how regex, scoring, and feedback loops work
4. **Extend it** — Add dictionary checks, entropy calculation, or Have I Been Pwned integration

---

## 🤝 Contributing

Found a bug or want to add a new check? PRs are welcome!

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<div align="center">

<br>

<sub>🔒 Built with security in mind. Open source by conviction.</sub>
<br>
<sub>Maintained by <strong>GrooveXlabs</strong></sub>

</div>
