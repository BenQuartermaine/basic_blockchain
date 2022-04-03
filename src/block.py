import datetime as dt
import hashlib


class Block:
    def __init__(self, previous_hash, data, timestamp):
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp
        # Instances method
        self.hash = self.get_hash()
        
    def create_genesis_block():
        state_of_the_world = "Sunday 3 april, 2022: US M2 money supply increased by more than 50% since pandemic start"

        return Block("0", state_of_the_world, dt.datetime.now())
    
    def get_hash(self):
        header_bin = (str(self.previous_hash) +
                      str(self.data) +
                      str(self.timestamp))

        inner_hash = hashlib.sha256(header_bin.encode()).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest()
        return outer_hash
