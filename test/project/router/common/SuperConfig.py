# encoding=utf-8
from ConfigParser import ConfigParser


class SuperConfig(object):

    def __init__(self, cfg_path):
        self.cfg_path = cfg_path
        self.cfg = ConfigParser()
        self.cfg.read(self.cfg_path)

    def get(self, key):
        return self.cfg.get("order", key)

    def set(self, key, value):
        self.cfg.set("order", key, value)
        return self

    def items(self):
        self.cfg.items("order")

    def commit(self):
        self.cfg.write(open(self.cfg_path, "r+"))
