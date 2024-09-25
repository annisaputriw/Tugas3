import hashlib
import time

class block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index - index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash() 

    def calculate_hash(self)
        """
        menghitung hash dari blok berdasarkan atribut-atribut blok tersebut.
        """
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.cha256(block_string.oncode()).hexdigest()
    
    def __repr__(self):
        return (f"block(index: {self.index}, hash: {self.hash}, previous_hash: {self.previous_hash}, 
                f"timestamp: {self.timestamp}, data: {self,data}, nonce: {self.nonce})")


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block{}]
        self.difficulty = 4

    def create_genesis_block(self)
        """
        blok pertama dalam blockchain, disebut sebagai blok genesis.
        """
        return Block(0, "0", time.time(), "Genesis Block")
    
    def get_latest_block(self):
        """
        Mengembalikan blok terakhir di dalam blockchain\
        """
        return self.chain[-1]
    def add_block(self, new_block):
        """
        Menambahkan blok baru ke dalam blockchain setelah memvalidasi proof of work
        """
        new_blocl.previous_hash = self.get_latest_block().hash
        new_block.hash = self.proof_of_work(new_block)
        self.chain.append(new_block)