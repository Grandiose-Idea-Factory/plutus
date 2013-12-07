import sys
import qifParser

def	main():
	parser = qifParser.qifParser()
	parser.open(sys.argv[1])
	parser.read()
	print parser.qifHeaders
	for transaction in parser.qifTransactions:
		transaction.print_transaction()

main()
