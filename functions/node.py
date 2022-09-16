from itertools import count
from typing_extensions import Self


class Node:

    def __init__(self):
        self.counter=0
    
    def addCount(self):
       self.counter+=1
       return str(self.counter)

    def resetCount(self):
        self.counter=0
