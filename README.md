# Algorithms‑in‑Action 🧠➡️🎨

> **Live Demo →** *coming soon*

A study‑driven playground where classic data‑structures & algorithms come to life through bite‑sized Python implementations and interactive Streamlit visuals. Learn, iterate, and share—while your résumé quietly levels‑up.

---

## ✨ Features - Coming soon

| Category            | What you get                                                                                                       |
| ------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Algorithms**      | Sorting (Bubble, Insertion, Merge, Quick, Heap) • Graph (BFS, DFS, Dijkstra) • Dynamic Programming (LCS, Knapsack) |
| **Visuals**         | Auto‑play animations or slider‑scrub frames rendered in Streamlit—no JavaScript required                           |
| **Clean Code**      | Each algorithm ≤ 50 LOC, type‑hinted, pep8‑formatted, with complexity docs                                         |
| **Unit Tests**      | `pytest` + GitHub Actions CI keep every refactor safe                                                              |
| **Benchmarks**      | Tiny timing harness to compare implementations                                                                     |
| **Container Ready** | Single `Dockerfile` + optional `docker‑compose.yml` (PostgreSQL/Redis examples)                                    |
| **AWS Samples**     | IaC snippets for App Runner, ECS Fargate (Compose CLI), and Elastic Beanstalk                                      |

---

## 🚀 Quick Start

```bash
# clone + install dev deps
$ git clone https://github.com/<you>/algorithms-in-action.git
$ cd algorithms-in-action
$ pip install -r requirements.txt

# run the app
$ streamlit run streamlit_app.py
# http://localhost:8501
```

Or fire up Docker:

```bash
$ docker compose up --build  # http://localhost:8501
```

---

## 🗂️ Repo Layout

```
algorithms-in-action/
├─ algorithms/
│  ├─ sorting/
│  │   ├─ merge_sort.py
│  │   └─ tests/
│  └─ graphs/
│      └─ dijkstra.py
├─ viz/              # Streamlit front‑end
│  └─ streamlit_app.py
├─ benchmarks/
├─ Dockerfile
├─ docker-compose.yml
├─ .github/workflows/ci.yml
└─ README.md
```

---

## 🖥️ Live Deployment Cheatsheet

### Streamlit Community Cloud

1. Push the repo to GitHub (public).
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) → **New app** → select repo/branch.
3. Set `main file = viz/streamlit_app.py` → **Deploy**.

### AWS App Runner

1. Fork the repo to a private or public GitHub.
2. App Runner console → **Create service** → *Source code*.
3. Expose port **8501**; autopilot build.

More options (ECS Fargate via Docker‑Compose, Elastic Beanstalk) inside `aws/`.

---

## 📊 Algorithms Implemented - Coming soon

| Group               | Algorithms                                       | Status |
| ------------------- | ------------------------------------------------ | ------ |
| Sorting             | Bubble, Selection, Insertion, Merge, Quick, Heap | ✅      |
| Graphs              | BFS, DFS, Dijkstra, Topological Sort             | ✅      |
| Dynamic Programming | Fibonacci (memo/tab), LCS, 0‑1 Knapsack          | 🚧     |
| Misc.               | Binary Search, Union‑Find                        | ✅      |

*Check the ****[Projects](https://github.com/<you>/algorithms-in-action/projects)**** board for the current roadmap.*

---

## 🤝 Contributing

1. **Fork & clone** the repo.
2. Create a new branch: `git checkout -b feat/your‑awesome‑algo`.
3. Add code **+ unit tests** (`pytest -q`).
4. Run `pre‑commit run --all-files`.
5. Open a PR 🙂.

Please avoid posting verbatim premium problem statements—paraphrase or link.

---

## 📄 License

Released under the MIT License—see `LICENSE` for details.

---

### 🙏 Acknowledgements

* Inspired by *VisuAlgo*, *AlgoExpert*, and countless open‑source contributors.
* Streamlit logo © Streamlit Inc.; used per Apache 2.0 license.

> Built with ❤️ by **Mahdi Ashrafee** — feedback & stars welcome!

