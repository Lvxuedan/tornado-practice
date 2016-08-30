# -*- coding: utf-8 -*-

import login

import json
import functools
from hashlib import md5
# import pylibmc

def dawacache(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        result = None
        if self.mem_client:
            key = method.__name__ + ''.join(args)
            result = self.get_from_cache(key)
            if result and 'callback' in kwargs:
                kwargs['callback'](result)

            else:
                return method(self, *args, **kwargs)

        else:
            return method(self, *args, **kwargs)
    return wrapper


import pymongo
import motor

from login import ModelLogin


class Model(ModelLogin):

    def __init__(self, mongo_uri, max_pool_size, mongo_database, memcache_pool=None):
        if motor.version_tuple == (0, 1, 2):
            self.db = motor.MotorClient(mongo_uri, max_pool_size=max_pool_size).open_sync()[mongo_database]
        else:
            if mongo_uri.find('replicaSet') > 0:
                self.db = motor.MotorReplicaSetClient(mongo_uri, max_pool_size=max_pool_size, read_preference=pymongo.ReadPreference.SECONDARY_PREFERRED)[mongo_database]
            else:
                self.db = motor.MotorClient(mongo_uri, max_pool_size=max_pool_size)[mongo_database]
        if memcache_pool:
            self.mem_client = pylibmc.Client(memcache_pool, binary=True)
        
    def get_from_cache(self, key):
        if self.mem_client:
            result = self.mem_client.get(key)
        return result

    def set_cache(self, key, value, cache_time=60):
        if self.mem_client:
            self.mem_client.set(key, value, cache_time)
