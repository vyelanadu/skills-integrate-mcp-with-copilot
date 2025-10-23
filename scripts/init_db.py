"""Create database and seed initial activities."""
from src.db import engine, Base
from src.models import Activity


def init_db():
    Base.metadata.create_all(bind=engine)

    # seed only if no activities exist
    from sqlalchemy.orm import Session
    session = Session(bind=engine)
    try:
        count = session.query(Activity).count()
        if count == 0:
            sample = [
                Activity(name="Chess Club", description="Learn strategies and compete in chess tournaments", schedule="Fridays, 3:30 PM - 5:00 PM", max_participants=12, participants=["michael@mergington.edu", "daniel@mergington.edu"]),
                Activity(name="Programming Class", description="Learn programming fundamentals and build software projects", schedule="Tuesdays and Thursdays, 3:30 PM - 4:30 PM", max_participants=20, participants=["emma@mergington.edu", "sophia@mergington.edu"]),
                Activity(name="Gym Class", description="Physical education and sports activities", schedule="Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM", max_participants=30, participants=["john@mergington.edu", "olivia@mergington.edu"]),
            ]
            session.add_all(sample)
            session.commit()
    finally:
        session.close()


if __name__ == "__main__":
    init_db()
