#!/usr/bin/python3
""" New db engine """
from sqlalchemy import create_engine
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.schema import MetaData
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {'User': User, 'Place': Place,
           'State': State, 'City': City,
           'Review': Review, 'Amenity': Amenity
           }


user = getenv('HBNB_MYSQL_USER')
passwd = getenv('HBNB_MYSQL_PWD')
host = getenv('HBNB_MYSQL_HOST')
database = getenv('HBNB_MYSQL_DB')
v_env = getenv('HBNB_ENV')


class DBStorage:
    """ Creates a new database """
    __engine = None
    __session = None
    __objects = {}

    def __init__(self):
        """ Intialization """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(user, passwd, host, database), pool_pre_ping=True)

        if v_env == 'test':
            metadata = MetaData(self.__engine)
            metadata.reflect()
            metadata.drop_all()

    def all(self, cls=None):
        """ Query on current db session """
        object_dict = {}

        if cls is not None:
            for obj in self.__session.query(cls).all():
                object_dict.update({'{}.{}'.format(type(cls).__name__,
                                                   obj.id): obj})
        else:
            for name in classes.values():
                object_list = self.__session.query(name)
                for obj in object_list:
                    object_dict.update({'{}.{}'.format(type(obj).__name__,
                                                       obj.id): obj})
        return object_dict

    def new(self, obj):
        """add obj to current db session"""
        self.__session.add(obj)

    def save(self):
        """commit changes of current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from current db session"""
        self.__session.delete()

    def reload(self):
        """creates all tables in db"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.state import State
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        session = scoped_session(Session)
        self.__session = session()

    def close(self):
        """ Ends private session attributes """
        self.__session.remove()
