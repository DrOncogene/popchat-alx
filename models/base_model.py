#!/usr/bin/python3
"""
    Base Class
"""


from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    BaseModel defines all common instance attributes
    and methods.
    """
    def __init__(self, **kwargs):
        """
        __init__ initializes basic or common instance attributes

        Args:
            Arbitrary length of keyword arguments
        Returns:
            return Null
        """
        if len(kwargs) == 0:
            print(kwargs)
            #: str: unique instance attribute
            self.id = str(uuid4())
            #: datetime: time and date instance created
            self.created_at = datetime.now()
        else:
            try:
                #: datetime obj: created_at converts to datetime obj
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f'
                )
            except Exception:
                if 'id' not in kwargs:
                    self.__init__()
                else:
                    self.created_at = datetime.now()
            try:
                del kwargs['__class__']
            except Exception:
                pass
            self.__dict__.update(kwargs)

    def to_dict(self):
        """
        Convert PopChat instance into dict representation
        Args:
            No required argument
        Returns:
            dictionary if successful, like:
            {
                'id': '3e43-e002-131f-00bf1',
                'created_aat': 2022-11-14T12:05.233348',
                '__class__': 'BaseModel'
            }
        Raises:
            KeyError: dict does not have to_dict
        """
        dict_rep = {}
        for (key, value) in self.__dict__.items():
            if type(value) is datetime:
                dict_rep[key] = value.isoformat()
            else:
                dict_rep[key] = value
        dict_rep['__class__'] = self.__class__.__name__
        return dict_rep

    def __str__(self):
        """
        Prints string representation of any PopChat instance
        Args:
            No argument
        Returns:
            returns string
        """
        return '[{}] ({}) {}'.format(
            type(self).__name__,
            self.id,
            self.to_dict()
        )
