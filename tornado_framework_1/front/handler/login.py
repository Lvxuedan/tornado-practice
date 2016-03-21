# -*- coding: utf-8 -*-
from tornado.web import RequestHandler
from tornado import gen

class ThirdHandler(RequestHandler):

    @property 
    def model(self):
        return self.application.settings['model']

    @property
    def data(self):
        if not hasattr(self, '_data'):
            self._data = {}
        return self._data

    def render_string(self, template_name, **kwargs):
        for k, v in self.data.iteritems():
            kwargs.setdefault(k, v)

        return super(ThirdHandler, self).render_string(template_name, **kwargs)

    @gen.coroutine
    def get(self):

        self.write("Hello, 3 page")
        result = yield self.model.get_all_callboards()# ?  @gen.engine  result = yield gen.Task(self.model.get_all_callboards)
        self.data['person_list'] = result
        self.render('../template/login.html')

