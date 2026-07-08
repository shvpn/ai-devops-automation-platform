# Runbook

## Local Development

Create a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r app\requirements.txt
```

Run the API:

```powershell
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/health
http://127.0.0.1:8000/docs
```

## Test

Run:

```powershell
pytest
```

## Basic Troubleshooting

If `uvicorn` is not found:

```powershell
pip install -r app\requirements.txt
```

If Python cannot import `app.main`, run commands from the project root:

```powershell
D:\DevSecopts
```

If the app port is already in use, stop the old process or run on another port:

```powershell
uvicorn app.main:app --reload --port 8001
```
