# -*- coding: utf-8 -*-

from handlers.base import BaseHandler
from pony import orm
from models.entities import Person, Car


class TestPonyHandler(BaseHandler):
    
    def initialize(self, extra):
        self.extra = extra
        
    def get(self):
        with orm.db_session:
            p1 = Person(name="fk", age=24)
            car1 = Car(owner=p1, model="Lexus")
    
    def post(self):
        self.set_header("Context-Type", "application/json")
        print self.repr
        print self.reqbody
        print self.raw
        print self.jsonbody
        self.write({"a":2})
    
    
__all__ = ["TestPonyHandler"]