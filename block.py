''' Sample code by k5trismegistus from https://github.com/k5trismegistus/pynaivechain
	Tutorial by Siraj
	Modified and commended by Kin

lessons
- classmethod (Python)


Keypoints:
- Sybil Attack

'''

import hashlib
import block_params


class Block():

	def __init__(self, params):
		self.index = params.index  # the ordering index of this block in the chian
		self.timestamp = params.timestamp  # when it is created, created with timestamp
		self.data = params.data  # data designed by the sender
		self.previous_hash = params.previous_hash  # the previous hash value
		self.hash = self.calc_hash()  # own hash value
										# 1. Hash gives block a unique ID
										# 2. verify the integrity of the data

	def params(self):
		return block_params.BlockParams(
			self.index,
			self.previous_hash,
			self.timestamp,
			self.data
			)

	@classmethod
	def genesis_block(cls):  # here cls is similar to self (just because it is a class method, so use 'cls')
		params = block_params.BlockParams.genesis_params()
		return cls(params)

	def calc_hash(self):
		return hashlib.sha256(str(self.params()).encode()).hexdigest()

	def has_valid_index(self, previous_block):
		return self.index == previous_block.index + 1

	def has_valid_previous_hash(self, previous_block):
		return self.previous_hash == previous_block.hash

	def has_valid_hash(self):
		return self.calc_hash() == self.hash

