import time

class Block:

    __default_block_limiit_size = 4000 # size in bytes
    __default_block_type="default"

    # create new block
    def __init__(self, transactions, previous_hash, miner_address, nonce=0):
        self.time_stamp = time.time()
        self.transaction = transactions
        self.miner = miner_address
        self.nonce = nonce
        self.state = []
        self.previous_hash= previous_hash
        self.block_type=__class__.__default_block_type
        self.block_size=""
        self.block_size_limit=__class__.__default_block_limiit_size
        
    # print block
    def printMe(self) -> dict:
        """   """
        return self.__dict__

    # def __str__(self) -> dict:
    #     return self.__dict__
