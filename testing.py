
# importing the requests library 
import requests 
import CollatzSequence
import json
import sys

# api-endpoint 
URL = "http://127.0.0.1:5000/resources/collatz"
#num=input() 
#num = sys.argv[1]
#print('type' ,type(num))

array=['da',4,13,0,'',' ',5]

for num in array:
	PARAMS = {'num':num} 
	response = requests.get(url = URL, params = PARAMS) 
	result = response.json() 
	test = CollatzSequence.collatz_sequence(num)
	print('TEST : ', test)
	print('API: ', result)

	print (CollatzSequence.compare(test,result))

