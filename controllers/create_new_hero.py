from fastapi import HTTPException
from sqlmodel import select

from core import SESSION_DEPENDENCY
from crud import create, exists_in_db
from models import Hero


async def create_new_hero(data: dict, db: SESSION_DEPENDENCY) -> Hero:
    try:
        # check if hero exists
        hero_exists: bool = await exists_in_db(
            param=data.name, arg="name", model=Hero, db=db
        )

        # raise an error info
        if hero_exists:
            raise HTTPException(
                status_code=400,
                detail=f"superhero with the name {data.name} already exist.",
            )

        # create a new hero dictionary
        created_hero: Hero = {
            "name": data.name,
            "secret_name": data.secret_name,
            "age": data.age,
            "hq": data.hq,
        }

        # create in db
        db_hero: Hero = await create(param=created_hero, model=Hero, db=db)

        # return created hero
        return db_hero

    except HTTPException as error:
        raise error
