"""module for describing user class which inhered from class Base"""
from datetime import datetime, timedelta  # timedelta defines how long token will be valid
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_jwt_extended import create_access_token
from passlib.hash import bcrypt


engine = db.create_engine('postgresql://postgres:19865421@localhost:5432/english_learning', echo=True)
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = session.query_property()


class Student(Base):
    """model describe relation student"""
    __tablename__ = 'student'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(20), nullable=False)
    user_surname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    date_of_registration = db.Column(db.DateTime, default=datetime.utcnow)
    confirmed = db.Column(db.Boolean, default=False)
    words = relationship("EnglishWord", back_populates='student')
    # we can use, words = relationship("EnglishWord", backref='student', lazy=True)

    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.user_name = kwargs.get('user_name')
        self.user_surname = kwargs.get('user_surname')
        self.email = kwargs.get('email')
        self.password = bcrypt.hash(kwargs.get('password'))
        self.date_of_registration = kwargs.get('date_of_registration')
        self.confirmed = kwargs.get('confirmed')
        self.words = kwargs.get('words')

    def get_token(self, expire_time=24):
        expire_delta = timedelta(expire_time)
        token = create_access_token(identity=self.user_id, expire_time=expire_delta)
        return token

    @classmethod
    def authenticate(cls, email, password):
        user = cls.query.filter(cls.email == email).one()
        if not bcrypt.verify(password, user.password):
            raise Exception('Wrong password')
        return user

    def __repr__(self):
        return f'<Class User, users\'s name  is {self.user_name}>'


class EnglishWord(Base):
    """model describe relation english_words"""
    __tablename__ = 'english_words'

    word_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    word = db.Column(db.String(20), nullable=False)
    transcription = db.Column(db.String(20), nullable=False)
    notes = db.Column(db.String(50))
    date_of_adding = db.Column(db.DateTime, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('student.user_id'))
    student = relationship('Student', back_populates='words')

    def __repr__(self):
        return f'<Class EnglishWord, word  is {self.word}>'


def create_tables():
    """create all relation in db"""
    Base.metadata.create_all(engine)

# from app.models.models import create_tables, session, Student
# u = Student(user_name='Dmitriy',user_surname='shypilov',email = 'shypilovd@gmail.com', password = 'sdfsdf')
# Student.query.all()  show list with all objects of class Student
# session.add(u)
# session.commit()
