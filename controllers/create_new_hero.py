from fastapi import HTTPException
from sqlmodel import select

from core import SESSION_DEPENDENCY
from crud import create
from models import Hero


async def create_new_hero(_data: dict, db: SESSION_DEPENDENCY) -> Hero:
    try:
        # check if hero exists
        hero_exists: str | None = db.exec(
            statement=select(Hero).where(Hero.name == _data.name)
        ).first()

        # raise an error info
        if hero_exists:
            raise HTTPException(
                status_code=400,
                detail=f"superhero with the name {_data.name} already exist.",
            )

        # create a new hero dictionary
        created_hero: Hero = {
            "name": _data.name,
            "secret_name": _data.secret_name,
            "age": _data.age,
            "hq": _data.hq,
        }

        # create in db
        db_hero: Hero = await create(param=created_hero, model=Hero, db=db)

        # return created hero
        return db_hero

    except HTTPException as error:
        raise error
