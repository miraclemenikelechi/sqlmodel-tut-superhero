from sqlmodel import Session, SQLModel, create_engine

filepath: str = "/assets/database.sqlite"
url: str = f"sqlite://{filepath}"
engine = create_engine(url, echo=True)
