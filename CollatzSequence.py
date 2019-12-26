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
	if integer == '' or  integer==' ' or type(integer)==str:
		return "not number provided, please entire a number"
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

	if integer == 0:
		return "Error Not valid number field provided. Please specify an entire number."
	else:
		while integer!=1:
			collatz(integer)
			sequence.append({'indx {}'.format(count):collatz(integer)}) 
			integer = collatz(integer)
			count = count +1

		return sequence 


def compare(test,result):
	count =0
	status = 'test pass'
	for obj in test:
		if obj not in result:
			status='error'

	return status