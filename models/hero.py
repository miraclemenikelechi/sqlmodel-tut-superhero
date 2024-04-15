from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class HeroBase(SQLModel):
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)


class CreateHero(HeroBase):
    hq: str


class Hero(CreateHero, table=True):
    id: UUID | None = Field(default_factory=uuid4, primary_key=True)
