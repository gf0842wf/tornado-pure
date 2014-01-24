# -*- coding: utf-8 -*-

import tornado.web

# from model.entity import Entity

menus = [["Home", "home"], ["About", "#"], ["Product", "#"], ["Contact", "#"]]

class HeroHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("hero.html", menus=menus, nop=None, sel=-1)