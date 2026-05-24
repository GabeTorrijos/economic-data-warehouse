from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# This creates (or connects to) a SQLite database file called economic_data.db
engine = create_engine('sqlite:///economic_data.db', echo=False)

# A session is how we talk to the database (insert, query, etc.)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    """Creates all tables in the database if they don't exist yet."""
    Base.metadata.create_all(engine)

def get_session():
    """Returns a new database session."""
    return SessionLocal()