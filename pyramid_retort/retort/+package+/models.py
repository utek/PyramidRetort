import datetime
import hashlib
import uuid

import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.Unicode(255),
                         unique=True,
                         nullable=False,
                         index=True)
    _password = sa.Column(sa.Unicode(255), nullable=False)
    salt = sa.Column(sa.Unicode(32), nullable=False)
    last_logged = sa.Column(sa.DateTime, default=datetime.datetime.utcnow)

    def check_password(self, password):
        pass_hash = hashlib.sha512("{salt}:{password}".format(
            salt=self.salt, password=password)).hexdigest()
        return self.password == pass_hash

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        salt = uuid.uuid4().hex
        self.salt = salt
        pass_hash = hashlib.sha512("{salt}:{password}".format(
            salt=salt, password=value)).hexdigest()
        self._password = pass_hash

    @classmethod
    def by_username(cls, username):
        return DBSession.query(cls).filter(cls.username == username).first()
