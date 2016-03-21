# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler

import setting
import handler

class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello, This is the Main page")

class SecondHandler(RequestHandler):
    def get(self):
        self.write("Hello, 2 page")

# class ThirdHandler(RequestHandler):
#     def get(self):
#         self.write("Hello, 3 page")

import model
def runserver():
    application = tornado.web.Application([
        (r"/main", MainHandler),
        (r"/second", SecondHandler),
        (r"/third", handler.ThirdHandler)
    ], **{

    'model':        model.Model(setting.mongo_uri, 50, setting.mongo_database),
    'debug':        setting.debug

    })

    # if hasattr(setting, 'ssl_options'):
    #     application.listen(setting.listen_port, setting.listen_host, ssl_options=setting.ssl_options)
    # else:
    #     application.listen(setting.listen_port, setting.listen_host)
    application.listen(setting.listen_port, setting.listen_host)


    # tornado.ioloop.IOLoop.current().start()
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    print setting.listen_host,setting.listen_port
    runserver()