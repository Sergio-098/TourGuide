from sqlmodel import Session, select
from Trip import Day

def create_day(session: Session, day: Day):
    session.add(day)
    session.commit()
    session.refresh(day)
    return day

def get_days_by_trip_id(session: Session, trip_id: int):
    return session.exec(select(Day).where(Day.trip_id == trip_id)).all()
