from sqlalchemy import engine_from_config
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from instance.config import SQLALCHEMY_DATABASE_URI


engine = engine_from_config({'SQLALCHEMY_TRACK_MODIFICATIONS': False},
                            url=SQLALCHEMY_DATABASE_URI)
SessionFactory = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))

Base = declarative_base()
Base.query = SessionFactory.query_property()
