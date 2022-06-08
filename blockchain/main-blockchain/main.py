from blockchain.block import Block

# test creation of new block

newBlock = Block({"hey": "hey"}, "previous hash")

print(newBlock.printMe())