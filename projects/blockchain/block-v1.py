import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(content.encode()).hexdigest()

# Create the first block (genesis)
genesis_block = Block(0, "Genesis Block", "0")

# Print the block's info
print("Genesis Block")
print("Index:", genesis_block.index)
print("Timestamp:", genesis_block.timestamp)
print("Data:", genesis_block.data)
print("Previous Hash:", genesis_block.previous_hash)
print("Hash:", genesis_block.hash)

# Create the second block
second_block = Block(
    index=1,
    data="Second block in the chain",
    previous_hash=genesis_block.hash
)

print("\nSecond Block")
print("Index:", second_block.index)
print("Timestamp:", second_block.timestamp)
print("Data:", second_block.data)
print("Previous Hash:", second_block.previous_hash)
print("Hash:", second_block.hash)

# Chain integrity check
def is_chain_valid(block1, block2):
    return block2.previous_hash == block1.hash

print("\nChain Valid:", is_chain_valid(genesis_block, second_block))

# Tampering with the data
print("\n--- Tampering ---")
genesis_block.data = "Fake Genesis Block"
genesis_block.hash = genesis_block.calculate_hash()

# Recheck validity
print("\nGenesis Block Hash:", genesis_block.hash)
print("Chain Valid After Tampering:", is_chain_valid(genesis_block, second_block))