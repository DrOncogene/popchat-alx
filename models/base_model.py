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
    def __init__(self):
        """
        __init__ initializes basic or common instance attributes

        Args:
            (Inclusive for now)

        Returns:
            return Null
        """
        #: str: unique instance attribute
        self.id = str(uuid4())
        #: datetime: time and date instance created
        self.created_at = datetime.now()
