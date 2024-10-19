from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings
from models import Base


engine = create_engine(
    url=settings.POSTGRES_DSN,
    echo=True
)

session_factory = sessionmaker(engine)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
