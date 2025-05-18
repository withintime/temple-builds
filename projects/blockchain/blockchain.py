# blockchain.py
# Auto-generated starter file

import hashlib

def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

print("Hash of 'blockchain':", hash_data("blockchain"))

import hashlib

text = "this is my genesis block"
result = hashlib.sha256(text.encode()).hexdigest()

print("Hash of the genesis block:", result)
