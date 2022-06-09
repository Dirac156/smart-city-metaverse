import json
import blockchain
from blockchain.lib.hash import encrypt_string
from .block import Block
from .helpers import errors
from .helpers import miners_address

class Blockchain:
    """  """


    __block_size = 5
    __dificulty_level = 5
    __miners_fee = 0 # use own servers to mine using AI/Sensors/Validators
    __miners = miners_address.miners
    __default_database_link=""
    # __default_miners={"address": "00", "name": "", "type": "proof_of_work"}
    __default_transaction={"sender": "", "receiver": "", "value": "", "signature": ""}
    

    def __init__(self) -> None:
        """ Initialize a blockchain """
        self.chain: list[Block] = []
        self.transactions: list[dict] = []
        self.state: list[dict] = [{}]
        self.transactions_time=[]
        self.database_link=__class__.__default_database_link
        self.database_schema=0

        # initialize blockchain

        if blockchain.loaded_chain == None:
            self.make_transaction([{}])
            self.transacte()
        else:
            # add existing block to the chain
            for block in blockchain.loaded_chain:
                self.chain.append(block)

    def jsonDumps(self, data):
        """ return json data """
        return json.dumps(data)

    def hash_transaction(self):
        """ return hash of the transaction """
        return encrypt_string(self.jsonDumps(self.transactions))


    def make_transaction(self, transactions: list[dict]) -> None:
        """ add new transaction to the queue """
        if type(transactions) is list:
            self.transactions.append(transactions[0])
        else:
            self.transactions.append(transactions)

    def transacte(self):
        """ validate transactions and add transaction to the blockchain """
        transactions = []
        i = 0
        while len(self.transactions) > 0:
            item = self.transactions[0]
            transactions.append(item)
            self.transactions.pop(0)
            i += 1
            if (i == self.__block_size):
                break
        
        hashed_transactions = self.hash_transaction()
        self.create_block(transactions=transactions, signature=hashed_transactions)

    
    def validate_hash(self, hash):
        """ validate hash """
        test = "0" * self.__dificulty_level
        val = hash[0: self.__dificulty_level]
        return test == val

    def proof_of_work(self, block: Block):
        """
        proof
        """
        n = 0
        hashed_value = block.hash(n)
        while self.validate_hash(hashed_value) == False:
            n += 1
            hashed_value = block.hash(n)

        return hashed_value, n

    def get_previous_hash(self):
        """ return the last block hash """
        if len(self.chain) > 0:
            return self.chain[-1].get_block_hash()
        else:
            return 0

    def add_block_to_blockchain(self, block: dict)->dict:
        """ add block inside of the blockchain """
        self.chain.append(block)
        blockchain.storage.new(block)
        blockchain.storage.save()

    def generate_block(self, transactions: list[dict], signature: str)->dict:
        """ generate block from the class Block """
        previous_hash = self.get_previous_hash()
        items = { "previous_hash": previous_hash, "transactions": transactions, "signature": signature, "miner_address":__class__.__miners["default_miner"] }
        candidate_block = Block(items=items)
        
        if candidate_block == None:
            raise Exception(errors.block_creation_error)

        return candidate_block


    def create_block(self, transactions: list[str], signature: str) -> None:
        """
        create block
        ------------
        Arguments:
            * transactions: A list of all transactions to add inside the block.
            [{"sender_address": "", "receiver_address": "",  "value": ""}]
            * proof_of/work/consensus/validation: a number

        Return: Created Block  
        """
        import time

        start = time.time()

        block: Block = self.generate_block(transactions=transactions, signature=signature)
        block_hash, proof_of_validation = self.proof_of_work(block)
        block.set_block_hash(block_hash)
        block.set_proof_of_validation(proof_of_validation)
        block.set_block_size()
        self.add_block_to_blockchain(block)

        end = time.time()
        self.transactions_time.append(end - start)
        print("Block creation time:", end - start, "seconds")


    def print_blockchain(self):
        """ display blockchain """

        for n in self.chain:
            n.display()
        