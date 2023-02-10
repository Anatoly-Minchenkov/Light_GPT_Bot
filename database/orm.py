from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, find_dotenv

from os import getenv

from .models import Base, Users, Questions

load_dotenv(find_dotenv())

engine = create_engine(getenv('SQL_PATH'), echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


def add_user(tg_id, name, username):
    session = Session()
    user = session.query(Users).filter(Users.username == username).first()
    if user is None:
        new_user = Users(tg_id=tg_id, name=name, username=username)
        session.add(new_user)
        session.commit()


def add_questions(message, response, username):
    session = Session()
    user = session.query(Users).filter(Users.username == username).first()
    new_question = Questions(message=message, response=response, owner=user.username)
    session.add(new_question)
    session.commit()
