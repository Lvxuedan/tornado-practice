# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler

import setting
import handler

import os, sys 
sys.path.append(os.path.realpath('../'))
sys.path.append(os.path.realpath('../../'))
sys.path.append(os.path.realpath('../../../'))


from framework.route import route
import model
def runserver():
    print (route.get_routes())
    application = tornado.web.Application(route.get_routes()+[
    ], **{
        'model':      model.Model(setting.mongo_uri, 50, setting.mongo_database),
        'debug':      setting.debug
    })

    application.listen(setting.listen_port, setting.listen_host)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    runserver()