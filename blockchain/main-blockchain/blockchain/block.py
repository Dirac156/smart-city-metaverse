from ast import arg
import json
from nis import cat
import string
from sys import stderr
import time

from blockchain.lib.hash import encrypt_string

class Block:

    __default_block_limiit_size = 4000 # size in bytes
    __default_block_type="default"

    # create new block
    def __init__(self, items=None, **kwargs) -> None:
        self.time_stamp = None
        """ initialize a single Block """
        if items == None:
            for key, value in kwargs.items():
                # construct the block from 
                setattr(self, key, value)
        else:
            self.time_stamp = time.time()
            self.state = [{}]
            self.transactions = items["transactions"]
            self.miner = items["miner_address"]
            self.previous_hash = items["previous_hash"]
            self.proof_of_validation=0
            self.block_size=0
            self.block_type=__class__.__default_block_type
            self.block_hash="0"
            self.signature=items["signature"]

    def to_dict(self):
        """ returns the dictionnary representation of the block """
        return self.__dict__
    
    def get_block_hash(self):
        """ return the hash of the block """
        return self.block_hash

    def jsonDumps(self)->str:
        """ load json data from block dictionnary """
        return json.dumps(self.to_dict())
    
    def set_block_hash(self, hash: str)-> None:
        """ set the block hash"""
        self.block_hash = hash

    def set_proof_of_validation(self, proof_of_validation: int) -> None:
        """ set the block nonce/proof of validation """
        self.proof_of_validation = proof_of_validation

    def set_block_size(self) -> None:
        """ set block size in byte """
        import sys
        self.block_size = sys.getsizeof(self.to_dict())


    def hash(self, nonce=None):
        """
        hash
        ----
        hash the block
        return: the hash of the block
        """
        try:
            if nonce:
                data = self.jsonDumps() + str(nonce)
            else:
                data = self.jsonDumps()
            return encrypt_string(data)
        except Exception as e:
            print("The block was not hashed: ", e, file=stderr)

        
    # print block
    def display(self) -> None:
        """
        display
        -------
        Print a representation of the blockchain to the user.
        """
        print(self.__dict__)


