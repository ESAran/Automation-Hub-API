import fastapi
import uvicorn

from api.routes.automations import router as automation_router

app = fastapi.FastAPI()

@app.get("/health")
def health_check():
    return {"status":"ok"}

app.include_router(automation_router)
