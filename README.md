
---

# 🧨 REPOBlast

> Delete your GitHub repositories like a machine. Fast. Final. No second chances.

## ⚙️ Setup

```bash
pip install requests
```

Edit the script:

```python
USERNAME = "your-github-username"
TOKEN = "your-personal-access-token"  # Needs 'repo' + 'delete_repo' scopes
```

## 🚀 Run

```bash
python github_repo_cleaner.py
```

Select what dies:

```
Your Repositories:
1. old-project
2. hello-world
3. move-fast-break-things

Enter the numbers of the repositories to delete (comma-separated): 2, 3
```

Boom. Gone.

## 🧠 Notes

* Works with public & private repos.
* Handles pagination. 100+? No problem.
* Deletion is **permanent**. You’ve been warned.

## 🪦 Why?

Because sometimes, you just need to burn it all and start over.

---
