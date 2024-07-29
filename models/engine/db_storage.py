#!/usr/bin/python3
"""db_storage module
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from ..base_model import Base
from ..user import User
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..place import Place
from ..review import Review


class DBStorage:
    """Class DBStorage"""

    __engine = None
    __session = None

    def __init__(self):
        """Instanciate new DBStorage"""
        db_user = os.getenv('HBNB_MYSQL_USER')
        db_pwd = os.getenv('HBNB_MYSQL_PWD')
        db_host = os.getenv('HBNB_MYSQL_HOST')
        db_name = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
                "mysql+mysqldb://{}:{}@{}/{}".format(
                    db_user, db_pwd, db_host, db_name),
                pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query all objects depending of the class name"""
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """Calls close() on the class Session"""
        self.__session.remove()
