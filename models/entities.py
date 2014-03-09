# -*- coding: utf-8 -*-

from pony import orm
from settings import DB, DBDEBUG

db = orm.Database("mysql", **DB)


class Person(db.Entity):
    _table_ = "person" # 注意是 _table_,而不是__table__
    
    name = orm.Required(unicode)
    age = orm.Required(int)
    motto = orm.Optional(unicode)
    cars = orm.Set("Car")


class Car(db.Entity):
    _table_ = "car"
    
    owner = orm.Required(Person)
    model = orm.Required(unicode) 
    

orm.sql_debug(DBDEBUG)
db.generate_mapping(create_tables=False)

__all__ = ["Person", "Car", "db"]
