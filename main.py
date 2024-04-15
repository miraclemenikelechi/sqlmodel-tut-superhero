from fastapi import FastAPI

from core import server_config
from routes import heroes

server = FastAPI(
    title="SQLModel: heroes",
    description="this api is a tutorial from tiangolo that is based on a superheroes database",
)

server.include_router(
    router=heroes,
    prefix=server_config.CURRENT_API_URL,
)


def main():
    import uvicorn

    from assets import SQLModel, engine

    SQLModel.metadata.create_all(engine)
    uvicorn.run("main:server", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
