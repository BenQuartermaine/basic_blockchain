from block import Block
import datetime as dt

# First element in list is genesis block
block_chain = [Block.create_genesis_block()]

# Create 10 blocks
for i in range(1, 11):
    block_chain.append(Block(block_chain[i-1].hash, f"Block number {i}", dt.datetime.now()))
    
    print(f"Block {i} created.")
    print(f"Hash: {block_chain[-1].hash}")
