from inspect import _void
import time

class Block:

    # create new block
    def __init__(self, transaction, previous_hash):
        self.time_stamp = time.time()
        self.transaction = transaction
        self.nonce = 0
        self.state = []
        self.previous_hash= previous_hash

    # print block
    def printMe(self) -> dict:
        """   """
        return self.__dict__

    def __str__(self) -> dict:
        return self.__dict__
