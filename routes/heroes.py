from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from controllers import create_new_hero
from core import SESSION_DEPENDENCY
from models import CreateHero, Hero
from crud import get_all

# init heroes router
heroes: APIRouter = APIRouter(
    prefix="/heroes",
    tags=["superheroes"],
)


# create a new hero
@heroes.post(path="/new", status_code=201, response_model=Hero)
async def create_a_hero(
    session: SESSION_DEPENDENCY,
    hero: CreateHero,
):
    # handle request
    request = await create_new_hero(db=session, data=hero)

    # in events of the response being null
    if not request:
        raise HTTPException(
            status_code=400,
            detail=f"this hero data could not be added in db",
        )

    # response to json
    response = {
        "message": f"hero created succesfully",
        "data": jsonable_encoder(request),
    }

    return JSONResponse(
        content=response,
        status_code=201,
    )


# get all heroes
@heroes.get(path="/all", status_code=200, response_model=list[Hero])
async def get_all_heroes(session: SESSION_DEPENDENCY):
    try:
        # handle request
        request = await get_all(model=Hero, db=session)

        # in events of resonse being null
        if not request:
            raise HTTPException(
                status_code=400,
                detail=f"error fetching...",
            )

        # response to json
        response = {
            "message": f"all heroes",
            "data": jsonable_encoder(request),
        }

        return JSONResponse(
            content=response,
            status_code=200,
        )

    except HTTPException as error:
        raise error
