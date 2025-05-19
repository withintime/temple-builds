# block-v2.py
# Auto-generated starter file

import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash, difficulty=2):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.difficulty = difficulty
        self.hash = self.mine_block()

    def calculate_hash(self):
        content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(content.encode()).hexdigest()

    def mine_block(self):
        prefix = '0' * self.difficulty
        while True:
            self.hash = self.calculate_hash()
            if self.hash.startswith(prefix):
                break
            self.nonce += 1
        return self.hash

class Blockchain:
    def __init__(self, difficulty=2):
        self.difficulty = difficulty
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0", self.difficulty)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        prev_block = self.get_latest_block()
        new_block = Block(len(self.chain), data, prev_block.hash, self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True

# === Build and Test the Chain ===
my_chain = Blockchain(difficulty=5)

print("Mining block 1...")
my_chain.add_block("First real block")

print("Mining block 2...")
my_chain.add_block("Second real block")

print("\nIs chain valid?", my_chain.is_chain_valid())

# Print blocks
for block in my_chain.chain:
    print(f"\nBlock {block.index}")
    print("Hash:", block.hash)
    print("Previous Hash:", block.previous_hash)
    print("Nonce:", block.nonce)
    print("Data:", block.data)

