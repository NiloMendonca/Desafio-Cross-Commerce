from app import app
from flask import Flask, request, render_template, jsonify
from flask_jwt_extended import JWTManager
import requests
import json

from flask_cors import CORS, cross_origin

CORS(app, support_credentials=True)
JWTManager(app)

listNumbers = []

# Funcao executada uma unica vez para carregar e ordenar os numeros
@app.before_first_request
def init():
	print("Init")
	print("Getting numbers from the API...")
	i = 1
	global listNumbers
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

		############## Usado apenas para testes no desenvolvimento
		# if i>50:
			# break
		###############################

	print("Sorting the numbers...")
	quicksort(listNumbers, 0, len(listNumbers)-1)
	print("Ready! Data available")

# Rota para disponiblizar os numeros para visualizacao no navegador
@app.route("/")
@cross_origin(supports_credentials=True)
def home():
	global listNumbers
	page = request.args.get('page')
	if page:
		page = int(page)
		return render_template('home.html', data=listNumbers[page*100-100:page*100])

	return render_template('home.html', data=listNumbers)

# Rota para disponiblizar os numeros para consumo da API 
@app.route("/numbers")
@cross_origin(supports_credentials=True)
def list():
	global listNumbers
	page = request.args.get('page')
	if page:
		page = int(page)
		return {'numbers': listNumbers[page*100-100:page*100]}

	return {'all-numbers':listNumbers}
	
# Realiza o Get dos numeros em todas as paginas
def getList(i):
	response = requests.get('http://challenge.dienekes.com.br/api/numbers?page=' + str(i)).text
	json_data = json.loads(response)
	if 'numbers' not in json_data:
		return []
	
	if json_data == {'numbers': []}:
		return None

	return json_data['numbers']

# Funcao separa utilizada pelo algoritmo QuickSort para ordenacao dos numeros
def partition(x, left, right):
	pivot = x[left]

	i = left + 1
	j = right

	done = False
	while not done:
		while i <= j and x[i] <= pivot:
			i = i + 1

		while x[j] >= pivot and j >= i:
			j = j - 1

		if j < i:
			done = True
		else:
			temp = x[i]
			x[i] = x[j]
			x[j] = temp

	temp = x[left]
	x[left] = x[j]
	x[j] = temp

	return j

# Funcao mediana de 3, utilizada para tornar o algoritmo QuickSort mais eficiente
def medianOfThree(x, left, right):
    temp = int((left + right)/2)
    if x[right] < x[left]:
        swap(x, left, right)        
    if x[temp] < x[left]:
        swap(x, temp, left)
    if x[right] < x[temp]:
        swap(x, right, temp)
    return temp

# Funcao que realiza a troca da posicao de dois elementos no vetor
def swap(x, left, right):
    temp = x[left]
    x[left] = x[right]
    x[right] = temp    

# Algoritmo de ordenacao QuickSort
def quicksort(x, left, right):
	if left >= right:
		return

	m = medianOfThree(x, left, right)
	x[left], x[m] = x[m], x[left]

	pivot = partition(x, left, right)
	quicksort(x, left, pivot - 1)
	quicksort(x, pivot + 1, right)