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
        self.blockchain = []
        self.length = 0

    def add_block(self, data=None):
        """
        Adds a block to the blockchain
        :return: None
        """

        # Edge case
        if data is None:
            print("Can't add block without data")
            return

        # If we're adding the first block
        if self.length == 0:
            block = Block(data, previous_hash=0)
        else:
            block = Block(data, self.blockchain[self.length - 1].hash)

        self.blockchain.append(block)
        self.length += 1

    def __repr__(self):

        # Edge case
        if len(self.blockchain) == 0:
            return "Blockchain empty"

        s = ''
        for i in range(len(self.blockchain)):
            s += "Block " + str(i) + "\n"
            s += str(self.blockchain[i]) + "\n"
        s += f"Blockchain size is : {blockchain.size()}"
        return s

    def size(self):
        return self.length


# Edge test cases
blockchain = BlockChain()
blockchain.add_block()
print(blockchain)


# Test cases
blockchain = BlockChain()
blockchain.add_block("0")
blockchain.add_block("12")
blockchain.add_block("24535")
print(blockchain)

blockchain = BlockChain()
blockchain.add_block("0")
blockchain.add_block("1")
blockchain.add_block("2")
blockchain.add_block("")
print(blockchain)
