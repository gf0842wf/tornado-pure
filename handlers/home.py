# -*- coding: utf-8 -*-

import tornado.web

# from model.entity import Entity

menus = [["Home", "home"], ["About", "#"], ["Product", "#"], ["Contact", "#"]]
    
class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("home.html", menus=menus, nop=None, sel=0)