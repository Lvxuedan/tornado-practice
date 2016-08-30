# -*- coding: utf-8 -*-
from tornado.web import RequestHandler
from tornado import gen

from handler import BaseHandler

import os, sys 
sys.path.append(os.path.realpath('../'))
from framework.route import route

@route('/', name='login')
class LoginHandler(BaseHandler):
    @gen.coroutine
    def get(self):

        self.write("Hello, 3 page")
        result = yield self.model.get_all_callboards()# ?  @gen.engine  result = yield gen.Task(self.model.get_all_callboards)
        self.data['person_list'] = result
        self.render('../template/login.html')

