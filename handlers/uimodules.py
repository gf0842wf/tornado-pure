# -*- coding: utf-8 -*-

import tornado.web


class HeroModule(tornado.web.UIModule):

    def render(self, nop):
        return self.render_string("modules/hero.html", mnop=nop)


class HomeModule(tornado.web.UIModule):

    def render(self, nop):
        return self.render_string("modules/home.html", mnop=nop)

__all__ = ["HeroModule", "HomeModule"]