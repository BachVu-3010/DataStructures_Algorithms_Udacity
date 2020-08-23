import hashlib
import time


class Block:

    def __init__(self, timestamp=None, data=None, previous_hash=None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = str(self.data).encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def __str__(self):
        return (f'Timestamp: {self.timestamp}\nData: {self.data}\nPrevious Hash: {self.previous_hash}\nHash: {self.hash}')


class BlockChain:

    def __init__(self):
        self.current_block = Block()

    def add_block(self, data):

        timestamp = time.gmtime()
        previous_hash = self.current_block.hash if self.current_block else 0
        self.current_block = Block(
            timestamp, data, previous_hash=previous_hash)


blockchain = BlockChain()

blockchain.add_block(1)
print(blockchain.current_block)

blockchain.add_block(2)
print(blockchain.current_block)

blockchain.add_block(3)
print(blockchain.current_block)
