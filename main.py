from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from core import server_config, time_to_complete
from routes import heroes

server = FastAPI(
    title="SQLModel: heroes",
    description="this api is a tutorial from tiangolo that is based on a superheroes database",
)

# routers
server.include_router(
    router=heroes,
    prefix=server_config.CURRENT_API_URL,
)

# middlewares
server.add_middleware(BaseHTTPMiddleware, dispatch=time_to_complete)


def main():
    import uvicorn

    from assets import SQLModel, engine

    # start db engine
    SQLModel.metadata.create_all(engine)

    # start server
    uvicorn.run("main:server", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
