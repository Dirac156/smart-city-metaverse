from block import Block
from ...helpers import errors

class Blockchain:

    __miners_fee = 0 # use own servers to mine using AI/Sensors/Validators

    def __init__(self) -> None:
        """ Initialize a blockchain """
        self.chain = []
        # create new blockchain
        candidate_block = Block([], 0)

        if candidate_block == None:
            raise Exception(errors.block_creation_error)
        else:
            # add the newly created block at the end of the blockchain
            self.chain.append(candidate_block)

    def print_blockchain(self):
        """ display blockchain """

        for n in self.chain:
            print(n)
        