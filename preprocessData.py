import csv

def preprocess(path):
	dataset = []
	with open(path,'r') as readFile:
		for row in csv.reader(readFile):
			dataset.append(row)
	#	Iris-setosa		-	0
	#	Iris-versicolor	-	1
	#	Iris-virginica	-	2
	for i in dataset:
		i[0] = float(i[0])
		i[1] = float(i[1])
		i[2] = float(i[2])
		i[3] = float(i[3])
		if i[4] == 'Iris-setosa':
			i[4] = 0
		elif i[4] == 'Iris-versicolor':
			i[4] = 1
		else:
			i[4] = 2

	count = 1
	with open('train.csv','wb') as train, open('test.csv','wb') as test:
		writer_test = csv.writer(test)
		writer_train = csv.writer(train)
		for i in dataset:
			if count%5 == 0:
				writer_test.writerow(i)
			else:
				writer_train.writerow(i)
			count += 1