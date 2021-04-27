from hashlib import sha256
from datetime import datetime
from time import time


class Blockchain:

    def __init__(self):
        self.blocks = []
        self.set_genesis_block()

    def set_genesis_block(self):
        transaction = '$1000\t De: Satoshi\t -> --\t'
        timestamp = datetime.utcnow().timestamp()
        prev_hash = '000000'
        index = 0
        self.hash_block(
            transaction, timestamp, prev_hash, index
        )

    def hash_block(self, transaction, timestamp, prev_hash, index):
        hash = ''
        nonce = 1
        start_time = time()
        while not self.is_hash_valid(hash):
            block = '{}:{}:{}:{}:{}'.format(
                transaction, timestamp, prev_hash, index, nonce
            )
            hash = sha256(block.encode()).hexdigest()
            nonce += 1
        print(f'#{index} - [nonce] - {nonce}\t  - {transaction}\t {prev_hash[-6:]}\t {hash[-6:]}')
        end_time = time()
        duracao = end_time - start_time
        print(f'Tempo de mineração:{duracao}\n')
        self.blocks.append(hash)

    def get_last_hash(self):
        return self.blocks[-1]

    def is_hash_valid(self, hash):
        return hash.startswith('0000')

    def add_new_block(self, transaction):
        index = len(self.blocks)
        prev_hash = self.get_last_hash()
        timestamp = datetime.utcnow().timestamp()
        self.hash_block(
            transaction, timestamp, prev_hash, index
        )

    def get_all(self):
        return self.blocks[:]
