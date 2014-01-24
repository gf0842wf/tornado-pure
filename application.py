# -*- coding: utf-8 -*-

"""settings"""

from urls import urls
from handlers.uimodules import *

import tornado.web
import os

SETTINGS = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    ui_modules=[{'Hero': HeroModule}, {'Home': HomeModule}],
    )

application = tornado.web.Application(
    handlers=urls,
    **SETTINGS
    )
