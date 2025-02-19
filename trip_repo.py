from sqlmodel import Session, select
from Trip import Trip, Day

def create_trip(session: Session, trip: Trip):
    session.add(trip)
    session.commit()
    session.refresh(trip)
    return trip

def get_trips(session: Session):
    return session.exec(select(Trip)).all()

def get_trip_by_id(session: Session, trip_id: int):
    return session.get(Trip, trip_id)
