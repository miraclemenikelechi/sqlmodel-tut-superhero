from typing import Any


async def create(param: dict | Any, model: type, db):
    # init db variable
    created = model(**param)

    # add to database
    db.add(created)
    db.commit()
    db.refresh(created)

    # return created item in db
    return created


async def get_by_param(param: str | int | Any):
    pass
