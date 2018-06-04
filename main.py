import preprocessData as preprocess
import sys
import csv
import math

def read(file):
	dataset = []
	with open(file,'r') as readFile:
		for row in csv.reader(readFile):
			dataset.append(row)
	return dataset

def computeDistanceP2P(a,b):
	x = (a[0]-b[0])**2
	y = (a[1]-b[1])**2
	w = (a[2]-b[2])**2
	z = (a[3]-b[3])**2
	#print math.sqrt(x+y+z+w)
	return math.sqrt(x+y+z+w)

def computeDistance(train, x):
	dictionary = {}
	i = 0
	for obj in train:
		dictionary[i] = computeDistanceP2P(obj, x)
		i += 1
	return dictionary

def main():
	preprocess.preprocess(sys.argv[1])
	k = int(sys.argv[2])
	
	train = read('train.csv')
	for row in train:
		for n in range(0,5):
			row[n] = float(row[n])
	
	test = read('test.csv')
	for row in test:
		for n in range(0,5):
			row[n] = float(row[n])

	total_prediction = 0
	correct_prediction = 0
	for row in test:
		dictionary = computeDistance(train, row)
		x = sorted(dictionary, key=dictionary.get)
		i = 0
		nearestNeighbour = []
		for neighbour in x:
			if i >= k:
				break
			else:
				nearestNeighbour.append(neighbour)
			i += 1
		
		data = {}
		actual_value = row[-1]
		for val in nearestNeighbour:
			label = train[val][4]
			if label in data:
				data[label] += 1
			else:
				data[label] = 1
		#print data,
		predicted_value = sorted(data, key=data.get, reverse=True)
		predicted_value = predicted_value[0]
		#print predicted_value, actual_value
		if actual_value == predicted_value:
			correct_prediction += 1
		total_prediction += 1
	print "For k = %d; Accuracy = %f"%(k,(float(correct_prediction)/total_prediction)*100)



if __name__ == '__main__':
	main()