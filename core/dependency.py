from typing import Annotated, Generator

from fastapi import Depends

from assets import Session, engine


def db_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SESSION_DEPENDENCY = Annotated[Session, Depends(db_session)]
