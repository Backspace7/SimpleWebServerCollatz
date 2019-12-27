import functools

def collatz(integer):
	module=integer%2
	if module == 0:
		return integer/2
	else:
		return integer*3 +1

def collatz_sequence(integer):
	sequence = []
	count = 0
	sequence.append({'indx {}'.format(count):integer})
	count = count +1
	if integer == 1:
		sequence.append({'indx {}'.format(count):collatz(integer)}) 
		integer = collatz(integer)
		count = count +1
		sequence.append({'indx {}'.format(count):collatz(integer)}) 
		integer = collatz(integer)
		count = count +1
		sequence.append({'indx {}'.format(count):collatz(integer)}) 
		integer = collatz(integer)
		count = count +1

		return sequence
	else:
		while integer!=1:
			collatz(integer)
			sequence.append({'indx {}'.format(count):collatz(integer)}) 
			integer = collatz(integer)
			count = count +1

		return sequence 


def compare(test,result):
	if functools.reduce(lambda i, j : i and j, map(lambda m, k: m == k, test, result), True) :  
		status=' - - PASS - -'
	else:
		status=' - - ERROR - -'

	return status



