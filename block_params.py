''' Sample code by k5trismegistus from https://github.com/k5trismegistus/pynaivechain
	Tutorial by Siraj
	Modified and commended by Kin

lessons
- classmethod (Python)


Keypoints:
- Sybil Attack

'''


GENESIS_INDEX = 0
GENESIS_PREVIOUS_HASH = '0'
GENESIS_TIMESTAMP = 1495851750
GENESIS_DATA = 'first block - this is Genesis'

class BlockParams():

	def __init__(self, index, previous_hash, timestamp, data):
		self.index = index
		self.previous_hash = previous_hash
		self.timestamp = timestamp
		self.data = data

	def __str__(self):
		return str(self.index) + self.previous_hash + str(self.timestamp) + self.data

	@classmethod
	def genesis_params(cls):
		return cls(GENESIS_INDEX, GENESIS_PREVIOUS_HASH, GENESIS_TIMESTAMP, GENESIS_DATA)

