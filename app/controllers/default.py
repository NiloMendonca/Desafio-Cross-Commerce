from app import app
from flask import Flask, request, render_template, jsonify
from flask_jwt_extended import JWTManager
import requests
import json

from flask_cors import CORS, cross_origin

CORS(app, support_credentials=True)
JWTManager(app)

@app.route("/")
@cross_origin(supports_credentials=True)
def home():
	i = 1
	listNumbers = []
	listNumbers = listNumbers + getList(i)
	temp = []

	while 1:
		i = i+1
		temp = getList(i)
		if temp is not None:
			if temp != []:
				listNumbers = listNumbers + temp
		else:
			break
	
	quicksort(listNumbers, 0, len(listNumbers)-1)	
		
	return render_template('home.html', data=listNumbers)

def getList(i):
	response = requests.get('http://challenge.dienekes.com.br/api/numbers?page=' + str(i)).text
	json_data = json.loads(response)
	if 'numbers' not in json_data:
		return []
	
	if json_data == {'numbers': []}:
		return None

	return json_data['numbers']

def partition(x, left, right):
	pivot = x[left]

	i = left
	j = right
	while i <= j:
		while x[i] <= pivot:
			i += 1
			if i == right:
				break

		while pivot <= x[j]:
			j -= 1
			if j == left:
				break

		if i >= j:
			break

		x[i], x[j] = x[j], x[i]

	pivot, x[j] = x[j], pivot
	return j

def medianOfThree(x, left, right):
    temp = int((left + right)/2)
    if x[right] < x[left]:
        swap(x, left, right)        
    if x[temp] < x[left]:
        swap(x, temp, left)
    if x[right] < x[temp]:
        swap(x, right, temp)
    return temp

def swap(x, left, right):
    temp = x[left]
    x[left] = x[right]
    x[right] = temp    

def quicksort(x, left, right):
	if left >= right:
		return

	m = medianOfThree(x, left, right)
	x[left], x[m] = x[m], x[left]

	pivot = partition(x, left, right)
	quicksort(x, left, pivot - 1)
	quicksort(x, pivot + 1, right)