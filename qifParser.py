#
#

import io
import transaction


class qifParser:
	
	def __init__(self):
		self.qifHeaders = []
		self.qifTransactions = []
	
	def open(self, fileName):				
		self.fileBuffer = io.open(fileName,"rb")
	
	def read(self):
		while '!' in self.fileBuffer.peek(1)[0]:
			self.qifHeaders.append(self.fileBuffer.readline().strip())
		for transaction_fields in [tran.strip().split("\n") for tran in self.fileBuffer.read().split("^")]:
			if len(transaction_fields) > 1:
				self.qifTransactions.append(transaction.transaction(transaction_fields))
