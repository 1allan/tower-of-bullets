from abc import ABC
import pickle


class DAO(ABC):
    def __init__(self, datasource: str):
        self.datasource = datasource
        self.cache = {}

        try:
            self.load()
        except FileNotFoundError:
            self.dump()

    def dump(self):
        pickle.dump(self.cache, open(self.datasource, 'wb'))

    def load(self):
        self.cache = pickle.load(open(self.datasource, 'rb'))

    def add(self, obj):
        self.cache[obj['timestamp']] = obj
        self.dump()

    def get(self, key):
        try:
            return self.cache[key]
        except KeyError:
            return False

    def remove(self, key):
        try:
            self.cache.pop(key)
            self.dump()
        except KeyError:
            return False

    def get_all(self):
        return self.cache.values()
