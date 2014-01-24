# -*- coding: utf-8 -*-

import tornado.web


class HeroModule(tornado.web.UIModule):

    def render(self, nop):
        return self.render_string("modules/hero.html", nop=nop)


class HomeModule(tornado.web.UIModule):

    def render(self, nop):
        return self.render_string("modules/home.html", nop=nop)

__all__ = ["HeroModule", "HomeModule"]