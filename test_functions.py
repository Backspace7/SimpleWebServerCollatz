import requests 
import CollatzSequence
import json
import sys

URL = "http://127.0.0.1:5000/resources/collatz"

def test_1_(num):
	PARAMS = {'num':num} 
	response = requests.get(url = URL, params = PARAMS) 
	result = response.json() 
	test =[{"indx 0": 4},{"indx 1": 2},{"indx 2": 1}]
	print('TEST : ', test)
	print('API: ', result)
	print (CollatzSequence.compare(test,result))


def test_2_(text):
	PARAMS = {'num':text} 
	response = requests.get(url = URL, params = PARAMS) 
	result = response.json() 
	test ="Value is not a number please enter a number"
	print('TEST : ', test)
	print('API: ', result)
	print (CollatzSequence.compare(test,result))


def test_3_(num):
	PARAMS = {'num':num} 
	response = requests.get(url = URL, params = PARAMS) 
	result = response.json() 
	test ="Number is not valid, please enter a positive divisible number"
	print('TEST : ', test)
	print('API: ', result)
	print (CollatzSequence.compare(test,result))

def test_4_(text):
	PARAMS = {'num':text} 
	response = requests.get(url = URL, params = PARAMS) 
	result = response.json() 
	test ="Value is not a number please enter a number"
	print('TEST : ', test)
	print('API: ', result)
	print (CollatzSequence.compare(test,result))


def test_5_(text):
	PARAMS = {'num':text} 
	response = requests.get(url = URL, params = PARAMS) 
	result = response.json() 
	test ="Value is not a number please enter a number"
	print('TEST : ', test)
	print('API: ', result)
	print (CollatzSequence.compare(test,result))


def test_6_(num):
	PARAMS = {'num':num} 
	response = requests.get(url = URL, params = PARAMS) 
	result = response.json() 
	test ="Number is not valid, please enter a positive divisible number"
	print('TEST : ', test)
	print('API: ', result)
	print (CollatzSequence.compare(test,result))

def test_7_(num):
	PARAMS = {'':num} 
	response = requests.get(url = URL, params = PARAMS) 
	result = response.json() 
	test ="No number field provided. Please specify a number field."
	print('TEST : ', test)
	print('API: ', result)
	print (CollatzSequence.compare(test,result))