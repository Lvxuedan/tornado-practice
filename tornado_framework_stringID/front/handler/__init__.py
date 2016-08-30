# -*- coding: utf-8 -*-
from tornado.web import RequestHandler
from tornado import gen 

import time 
import sys, os
sys.path.append(os.path.realpath('../'))
sys.path.append(os.path.realpath('../../'))
sys.path.append(os.path.realpath('../../../'))


class BaseHandler(RequestHandler):

    @gen.coroutine
    def prepare(self):
        if self.get_argument('lang','').lower() in ('en', 'zh'):
            self.lang = self.get_argument('lang','').lower() #get lang by get parameter

        elif self.get_cookie('lang', ''):
            self.lang = self.get_cookie('lang', 'zh') #get lang by cookie

        else:
            locale = self.get_browser_locale() #get by locale
            if locale.name == 'English (US)':
                self.lang = 'en'
            else:
                self.lang = 'zh'

        self.set_cookie('lang', self.lang, '', time.time() + 86400 * 60)
        i = __import__('language.%s'% self.lang , fromlist=[''])
        self.language = i.lang #languege bag


    @property
    def model(self):
        return self.application.settings['model']

    @property
    def data(self):
        if not hasattr(self, '_data'):
            self._data = {}
        return self._data

    def render_string(self, template_name, **kwargs):
        kwargs['language']                          = self.language
        
        for k, v in self.data.iteritems():
            kwargs.setdefault(k, v)

        return super(BaseHandler, self).render_string(template_name, **kwargs)   


import login