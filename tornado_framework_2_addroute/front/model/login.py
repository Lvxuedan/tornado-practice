# -*- coding: utf-8 -*-

import motor
from tornado import gen


class ModelLogin(object):

    @gen.coroutine
    def get_all_callboards(self):
        callboards = yield motor.Op(self.db.test.find().to_list, 50)
        raise gen.Return((callboards))
