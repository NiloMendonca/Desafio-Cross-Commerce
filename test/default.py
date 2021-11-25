import os
import sys
sys.path.append("..") 

import tempfile
import pytest

from app.controllers.default import *

def test_home():
	assert home() == []

def test_getList():
	assert getList(1) == []

def test_partition():
	x = [9,8,7,6,5,4,3,2,1]
	assert partition(x, 0, 9) == 10

def test_medianOfThree():
	x = [9,8,7,6,5,4,3,2,1,0]
	b = medianOfThree(x, 0, len(x)-1)
	print(x)
	assert b == 5

def test_swap():
	x = [9,8,7,6,5,4,3,2,1,0]
	swap(x, 0, len(x)-1)
	assert x == [0,8,7,6,5,4,3,2,1,9]
	swap(x, 2, 4)
	assert x == [0,8,5,6,7,4,3,2,1,9]

def test_quicksort():
	x = [9,8,7,6,5,4,3,2,1,0]
	quicksort(x, 0, len(x)-1)
	print(x[len(x)-1])
	assert x == [0,1,2,3,4,5,6,7,8,9]

