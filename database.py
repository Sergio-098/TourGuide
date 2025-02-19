from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "postgresql://postgres:sergio@localhost:5432/TravelGuide"

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

