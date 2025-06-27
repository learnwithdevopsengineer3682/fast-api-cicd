# FastAPI CI/CD Demo with Render & GitHub Actions

A super simple but production-ready FastAPI project that **deploys automatically** to [Render.com](https://render.com) every time you push to GitHub, using **GitHub Actions** for true CI/CD.

##  What You Get

- Python FastAPI app (with `/`, `/health`, and `/reverse` endpoints)
- Modern project structure (no frameworks or boilerplate, just code)
- Live deployment to Render – 100% free tier
- Automated CI/CD pipeline (push to main → instant deploy)
- Ready to extend with real business logic!

---

## 🌐 Endpoints

- `GET /` – Welcome message (update to see CI/CD in action!)
- `GET /health` – Health check endpoint
- `POST /reverse` – Reverses text, example:  
  ```json
  { "text": "YouTube" } ⇒ { "reversed": "ebuTuoY" }
  ```

##  Quick Start

### 1. Clone and Install

```bash
git clone https://github.com/YOUR-USERNAME/fastapi-cicd-demo.git
cd fastapi-cicd-demo
pip install -r requirements.txt
```

### 2. Run Locally

```bash
uvicorn main:app --reload
```
- Browse to: [http://localhost:8000](http://localhost:8000)
- Try `/docs` for Swagger UI!

### 3. Deploy to Render

1. Go to [render.com](https://render.com) and log in or create an account
2. Click **New + > Web Service**
3. Connect your GitHub repo
4. Use these settings:
    - **Build Command:**  
      `pip install -r requirements.txt`
    - **Start Command:**  
      `uvicorn main:app --host 0.0.0.0 --port 10000`
5. Click **Create Web Service**  
   Wait ~1 minute for your app to build and go live.

### 4. Set Up CI/CD with GitHub Actions

1. In your repo, create:  
   `.github/workflows/deploy.yml`  
   Copy the workflow from this repo.
2. On Render, go to your Service > **Settings > Deploy Hooks**  
   Copy your Deploy Hook URL.
3. On GitHub, go to **Settings > Secrets and variables > Actions**  
   - Add new secret:  
     `RENDER_DEPLOY_HOOK` = (Paste your Render Deploy Hook URL)
4. Now, **every push to main will trigger a new deploy!**

---

## 🧑‍💻 File Structure

```
fastapi-cicd-demo/
│
├── main.py                # FastAPI app code
├── requirements.txt       # Dependencies
└── .github/workflows/
    └── deploy.yml         # GitHub Actions workflow
```

---

## 📦 Example `main.py`

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def hello():
    return {"msg": "It works! Auto-deployed by GitHub Actions 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}

class ReverseRequest(BaseModel):
    text: str

@app.post("/reverse")
def reverse(req: ReverseRequest):
    reversed_text = req.text[::-1]
    return {"reversed": reversed_text}
```

---

## 🛠️ Example GitHub Actions Workflow (`.github/workflows/deploy.yml`)

```yaml
name: Deploy to Render

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Trigger Render deploy
      env:
        RENDER_DEPLOY_HOOK: ${{ secrets.RENDER_DEPLOY_HOOK }}
      run: curl -X POST "$RENDER_DEPLOY_HOOK"
```

---

## 🐛 Debugging

- **See a failed deploy?**  
  Check the Render dashboard for build logs.
- **Workflow fails?**  
  Make sure your `RENDER_DEPLOY_HOOK` is set correctly in GitHub repo secrets.

---

## ⭐ Want More?

- Add automated tests (pytest, httpx, etc.)
- Add Docker support
- Add more endpoints or auth
- Ask for help in [Discussions](https://github.com/YOUR-USERNAME/fastapi-cicd-demo/discussions) or by creating an issue!

---

## 🙌 Credits

- [FastAPI](https://fastapi.tiangolo.com/)
- [Render.com](https://render.com)
- [GitHub Actions](https://github.com/features/actions)

---

## 📹 Watch the Full Video

See the full step-by-step guide, including **real CI/CD failures and fixes**, on my YouTube channel:  
👉 [Learn with DevOps Engineer](https://youtube.com/@learnwithdevopsengineer3684)

---

## 📥 Download

All source code is included in this repo (or see the ZIP link below this video!).

---

**Enjoy! If you found this helpful, star the repo and subscribe for more practical DevOps + Python guides!**
