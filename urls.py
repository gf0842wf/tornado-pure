# -*- coding: utf-8 -*-

from handlers.hero import HeroHandler
from handlers.home import HomeHandler

urls = [
    (r"/", HeroHandler),
    (r"/home", HomeHandler),
    ]

