# -*- coding: utf-8 -*-

"""启动web server"""

import tornado.ioloop
import logging

from application import application
from tornado.options import define, options

define("port", 8001, help="define port", type=int) # tornado没有的命令要通过define定义(logging等命令有了)

if __name__ == "__main__":
    options.logging = "debug"           # *1
#     options.log_file_prefix = "var/log/test_log@8001.log"
    options.parse_command_line()
    application.listen(options.port)
    logging.debug("ioloop ... ")
    tornado.ioloop.IOLoop.instance().start()
    # python main.py --port=8001 --logging=warning  # 这里的会覆盖 *1行的
