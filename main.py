import fastapi
import uvicorn

app = fastapi.FastAPI()

@app.get("/health")
def health_check():
    return {"status":"ok"}