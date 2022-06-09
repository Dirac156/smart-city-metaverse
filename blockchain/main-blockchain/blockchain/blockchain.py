from .block import Block
from .helpers import errors
from .helpers import miners_address

class Blockchain:

    __miners_fee = 0 # use own servers to mine using AI/Sensors/Validators
    __miners = miners_address.miners
    __default_database_link=""
    # __default_miners={"address": "00", "name": "", "type": "proof_of_work"}
    __default_transaction={"sender": "", "receiver": "", "value": "", "signature": ""}
    

    def __init__(self) -> None:
        """ Initialize a blockchain """
        self.chain = []
        self.state = {}
        self.database_link=__class__.__default_database_link
        self.database_schema=0

        # initialize blockchain
        self.create_block([])




    def proof_of_work(self, data):
        """
        
        """
        pass

    def create_block(self, transactions):
        """
        create block
        ------------
        Arguments:
            * transactions: A list of all transactions to add inside the block.
            [{"sender_address": "", "receiver_address": "",  "value": ""}]
            * proof_of/work/consensus/validation: a number

        Return: Created Block  
        """
        candidate_block = Block(previous_hash=0, transactions=transactions, nonce=0, miner_address=__class__.__miners["default_miner"])

        if candidate_block == None:
            raise Exception(errors.block_creation_error)
        else:
            # add the newly created block at the end of the blockchain
            self.chain.append(candidate_block)

    def print_blockchain(self):
        """ display blockchain """

        for n in self.chain:
            print(n.printMe())
        