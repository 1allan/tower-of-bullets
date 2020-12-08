import pickle
import time

from dao.DAO import DAO


class SaveDAO(DAO):
    
    def __init__(self, arquivo):
        super().__init__(arquivo)

    def add(self, payload):
        '''
          dict[timestamp] = payload
          payload = {
            score: 'x',
            gold: 'y'
          }
        '''
        payload["timestamp"] = time.time()
        super().add(payload)

    def get(self, timestamp):
        return super().get(timestamp)

    def remove(self, payload):
        return super().remove(payload.timestamp)

    def get_all(self):
        return super().get_all()

    def length(self):
        return len(super().get_all())
