from sqlmodel import Field, SQLModel


class HeroBase(SQLModel):
    name: str
    secret_name: str
    age: int | None = None


class CreateHero(HeroBase):
    hq: str


class Hero(CreateHero, table=True):
    id: int | None = Field(default=None, primary_key=True)
