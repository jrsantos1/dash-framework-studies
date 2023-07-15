import os

class Config:
    @classmethod
    def get_root_path(cls):
        path = os.path.dirname(os.path.abspath(__file__))
        return path

