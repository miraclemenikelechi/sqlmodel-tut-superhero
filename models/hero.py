from sqlmodel import Field, SQLModel
from uuid import UUID, uuid4


class HeroBase(SQLModel):
    name: str
    secret_name: str
    age: int | None = None


class CreateHero(HeroBase):
    hq: str


class Hero(CreateHero, table=True):
    id: UUID | None = Field(default_factory=uuid4, primary_key=True)
