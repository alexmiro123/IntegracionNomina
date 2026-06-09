import uvicorn

from src.shared.config.settings import settings

if __name__ == "__main__":

    uvicorn.run(
        "src.main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=True
    )