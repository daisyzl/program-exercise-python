#-*-coding:utf-8-*-
import threading


class Singleton():

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            Singleton._instance = object.__new__(cls)
        return Singleton._instance
