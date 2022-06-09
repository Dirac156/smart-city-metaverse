from blockchain.blockchain import Blockchain

# test creation of new block

BC = Blockchain()

# BC.print_blockchain()
BC.make_transaction([{"sender": "00x", "receiver": "00x1", "value": "0"}])
BC.make_transaction([{"sender": "00x", "receiver": "00x1", "value": "0"}])
BC.make_transaction([{"sender": "00x", "receiver": "00x1", "value": "0"}])
BC.make_transaction([{"sender": "00x", "receiver": "00x1", "value": "0"}])
BC.transacte()
# BC.print_blockchain()

# print("DIFFICULTY LEVEL:", BC.__dificulty_level)
print("AVERAGE_TIME:", sum(BC.transactions_time) / len(BC.transactions_time))
print("BLOCKS:", len(BC.transactions_time))
