import os
import sys
sys.path.append("..") 

import tempfile
import pytest
import random
import requests

from app.controllers.default import *

def test_getList():
	for t in range(5):
		n = random.randint(0,20000)
		assert (type(getList(n)) == type([]) or getList(n) == None)

def test_partition():
	x = [9,8,7,6,5,4,3,2,1,0]
	assert partition(x, 0, len(x)-1) == 9

def test_medianOfThree():
	x = [9,8,7,6,5,4,3,2,1,0]
	assert medianOfThree(x, 0, len(x)-1) == 4

	x = [0,1,2]
	assert medianOfThree(x, 0, len(x)-1) == 1

	x = [0,1]
	assert medianOfThree(x, 0, len(x)-1) == 0

def test_swap():
	x = [9,8,7,6,5,4,3,2,1,0]
	swap(x, 0, len(x)-1)
	assert x == [0,8,7,6,5,4,3,2,1,9]

	swap(x, 2, 4)
	assert x == [0,8,5,6,7,4,3,2,1,9]

	x = [0,1]
	swap(x, 0, 1)
	assert x == [1,0]

def test_quicksort():
	x = [9,8,7,6,5,4,3,2,1,0]
	quicksort(x, 0, len(x)-1)
	assert x == [0,1,2,3,4,5,6,7,8,9]

	x = [0,1,2,3,4,5,6,7,8,9]
	quicksort(x, 0, len(x)-1)
	assert x == [0,1,2,3,4,5,6,7,8,9]

	x = [1]
	quicksort(x, 0, len(x)-1)
	assert x == [1]

	x = []
	quicksort(x, 0, len(x)-1)
	assert x == []

def testRoutes():
	print("Para passar nesse caso de teste é necessário que a aplicação esteja rodando.")
	response = requests.get('http://127.0.0.1:5000')
	assert response.status_code == 200

	response = requests.get('http://127.0.0.1:5000/numbers')
	assert response.status_code == 200

	for t in range(5):
		n = random.randint(0,20000)
		response = requests.get('http://127.0.0.1:5000?page='+ str(n))
		assert response.status_code == 200

	for t in range(5):
		n = random.randint(0,20000)
		response = requests.get('http://127.0.0.1:5000/numbers?page='+ str(n))
		assert response.status_code == 200