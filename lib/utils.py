# -*- coding: utf-8 -*-

import logging as log

class LogMixin(object):
    def msg(self, *arg, **kwargs):
        log.warning(*arg, **kwargs)

__all__ = ["log", "LogMixin"]
