__author__ = 'fdamilola'

import json


class Mars():
    def __init__(self):
        self.storage = open("file.json", "w")
        self.json = ""
        pass

    def send(self, dict_value):
        try:
            self.json = json.dumps(dict_value, skipkeys=True, indent=2)
            self.storage.write(self.json)
            self.storage.close()
            return 1
        except Exception, e:
            self.storage.close()
            raise e

    def receive(self, filename):
        try:
            s = json.loads(open(filename).read())
            return s
        except Exception, e:
            raise e