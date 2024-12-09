# -------------------------------------
# Author        : Daniel Saravia
# Date          : 12/9/2024
# Institution   : GCU
# Project       : Blockchain Basics
# Description   : Basic implementation of a blockchain
# -------------------------------------

import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        """
        Initialize a Block with the given parameters.

        :param index: The position of the block in the blockchain
        :param timestamp: The time the block was created
        :param data: The data stored in the block
        :param previous_hash: The hash of the previous block in the chain
        """
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculate the hash of the block using SHA-256.

        :return: The calculated hash as a hexadecimal string
        """
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        print("Block string for hash computation:", block_string)
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def __str__(self):
        """
        Return a string representation of the block.

        :return: A string representing the block's details
        """
        return (f"Block(Index: {self.index}, "
                f"Timestamp: {self.timestamp}, "
                f"Data: {self.data}, "
                f"Previous Hash: {self.previous_hash}, "
                f"Hash: {self.hash})")
    
class Blockchain:
    def __init__(self):
        """
        Initialize the blockchain with a genesis block.
        """
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        """
        Create the first block in the blockchain, known as the genesis block.

        :return: The genesis block instance
        """
        return Block(0, datetime.datetime.now(), "Genesis Block", "0")
    
    def get_latest_block(self):
        """
        Retrieve the most recent block in the blockchain.

        :return: The latest block in the chain
        """
        return self.chain[-1]

    def add_block(self, new_data):
        """
        Add a new block to the blockchain.

        :param new_data: The data to be stored in the new block
        """
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), datetime.datetime.now(), new_data, latest_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Verify the integrity of the blockchain by checking the hash of each block.

        :return: True if the blockchain is valid, False otherwise
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Validate the hash of the current block
            if current_block.hash != current_block.calculate_hash():
                print(f"Block {current_block.index} has been tampered with!")
                return False

            # Validate the link between blocks
            if current_block.previous_hash != previous_block.hash:
                print(f"Block {current_block.index} is not properly linked!")
                return False

        return True

    def __str__(self):
        """
        Return a string representation of the entire blockchain.

        :return: A string representing all blocks in the chain
        """
        return "\n".join(str(block) for block in self.chain)

# Example Usage
if __name__ == "__main__":
    # Initialize the blockchain
    blockchain = Blockchain()

    # Add some blocks
    blockchain.add_block("First block data")
    blockchain.add_block("Second block data")
    blockchain.add_block("Third block data")

    # Print the blockchain
    print("Blockchain:")
    print(blockchain)

    # Validate the blockchain
    print("\nIs blockchain valid?", blockchain.is_chain_valid())
