from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from controllers import create_new_hero
from core import SESSION_DEPENDENCY
from models import CreateHero, Hero

heroes: APIRouter = APIRouter(
    prefix="/heroes",
    tags=["superheroes"],
)


@heroes.post(path="/new", status_code=201, response_model=Hero)
async def create_a_hero(
    session: SESSION_DEPENDENCY,
    hero: CreateHero,
):

    data = await create_new_hero(db=session, _data=hero)

    if not data:
        raise HTTPException(
            status_code=400,
            detail=f"this hero data could not be added in db",
        )

    response = {
        "message": f"hero created succesfully",
        "data": jsonable_encoder(data),
    }

    return JSONResponse(
        content=response,
        status_code=201,
    )
