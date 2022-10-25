#!/usr/bin/python3
""" New db engine """
from sqlalchemy import (create_engine)
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.schema import MetaData
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.base_model import Base


user = getenv('HBNB_MYSQL_USER')
passwd = getenv('HBNB_MYSQL_PWD')
host = getenv('HBNB_MYSQL_HOST')
database = getenv('HBNB_MYSQL_DB')
v_env = getenv('HBNB_ENV')
#print("The passwd we got: {}".format(passwd))

class DBStorage:
    """ Creates a new database """
    __engine = None
    __session = None
    __objects = {}

    def __init__(self):
        """ Intialization """
        #print("the passwd we got: {}".format(passwd))
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(user, passwd, host, database), pool_pre_ping=True)

        if v_env == 'test':
            metadata = MetaData(engine)
            metadata.reflect()
            metadata.drop_all()

    def all(self, cls=None):
        """ Query on current db session """
        #self.__session = sessionmaker(bind=engine)
        #session = self.__session()
        session = self.__session

        if cls is None:
            session.query(User, State, City, Amenity, Place, Review)
            return DBStorage.__objects

    def new(self, obj):
        """add obj to current db session"""
        self.__session.add()

    def save(self):
        """commit changes of current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from current db session"""
        self.__session.delete()

    def reload(self):
        """creates all tables in db"""
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(self.__session)
