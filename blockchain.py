''' Sample code by k5trismegistus from https://github.com/k5trismegistus/pynaivechain
	Tutorial by Siraj
	Modified and commended by Kin

lessons
- classmethod (Python)


Keypoints:
- Sybil Attack

'''


import time
import block
import block_params


class BlockChain():

	def __init__(self):
		self.blockchain_store = self.fetch_blockchain()

	def latest_block(self):
		return self.blockchain_store[-1]

	def generate_next_block(self, data):
		index = len(self.blockchain_store)
		previous_hash = self.latest_block().hash
		timestamp = int(time.time())

		params = block_params.BlockParams(index, previous_hash, timestamp, data)
		new_block = block.Block(params)
		self.blockchain_store.append(new_block)

	def fetch_blockchain(self):
		return [block.Block.genesis_block()]

	def receive_new_block(self, new_block):
		previous_block = self.latest_block()

		if not new_block.has_valid_index(previous_block):
			print('invalid index')
			return

		if not new_block.has_valid_previous_has(previous_block):
			print('invalid previous hash')
			return

		if not new_block.has_valid_hash():
			print('invalid hash')
			return

		self.blockchain_store.append(new_block)