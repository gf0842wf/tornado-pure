# -*- coding: utf-8 -*-

"""启动web server"""

import tornado.ioloop

from application import application
from tornado.options import define, options
from twisted.python import log, logfile
# from lib.utils import LogMixin

define("port", 8888, help="port", type=int)

if __name__ == "__main__":
    # 定义日志格式
    lf = logfile.DailyLogFile("xxx.log","var/log/")
    log.FileLogObserver.timeFormat = "%Y-%m-%d %H:%M:%S"
    log.startLogging(lf)
    options.parse_command_line()
    application.listen(options.port)
    log.msg("start ioloop")
    tornado.ioloop.IOLoop.instance().start()
