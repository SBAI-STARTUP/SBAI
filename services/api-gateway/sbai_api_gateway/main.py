from fastapi import FastAPI

app = FastAPI(
    title="SBAI API Gateway",
    version="0.1.0",
)


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "api-gateway",
        "version": "0.1.0",
    }
