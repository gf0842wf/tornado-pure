# -*- coding: utf-8 -*-

from pony import orm
from settings import DB, DBDEBUG

db = orm.Database("mysql", **DB)


class Person(db.Entity):
    __table__ = "person"
    
    name = orm.Required(unicode)
    age = orm.Required(int)
    motto = orm.Optional(unicode)
    cars = orm.Set("Car")


class Car(db.Entity):
    __table__ = "car"
    
    owner = orm.Required(Person)
    model = orm.Required(unicode) 
    

orm.sql_debug(DBDEBUG)
db.generate_mapping(create_tables=False)

__all__ = ["Person", "Car", "db"]
