# -*- coding: utf-8 -*-

"""settings"""

from urls import urls
from handlers.uimodules import *

import tornado.web
import os

get_path = lambda d: os.path.join(os.path.dirname(__file__), d)
SETTINGS = dict(
    template_path=get_path("templates"),
    static_path=get_path("static"),
    ui_modules=[{'Hero': HeroModule}, {'Home': HomeModule}],
    )

application = tornado.web.Application(
    handlers=urls,
    **SETTINGS
    )
