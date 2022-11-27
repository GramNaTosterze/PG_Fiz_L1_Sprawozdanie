# Python program to find the
# regression line

# Function to calculate b
def calculateB(x, y, n):

	# sum of array x
	sx = sum(x)

	# sum of array y
	sy = sum(y)
	
	# for sum of product of x and y
	sxsy = 0

	# sum of square of x
	sx2 = 0

	for i in range(n):
		sxsy += x[i] * y[i]
		sx2 += x[i] * x[i]
	b = (n * sxsy - sx * sy)/(n * sx2 - sx * sx)
	return b

# Function to find the
# least regression line
def leastRegLine(X,Y,n):
	
	# Finding b
	b = calculateB(X, Y, n)
	meanX = int(sum(X)/n)
	meanY = int(sum(Y)/n)

	# Calculating a
	a = meanY - b * meanX

	# Printing regression line
	print("Regression line:")
	print("Y = ", '%.3f'%b,"*x + ",'%.3f'%a, sep="")

# Driver code

# Statistical data

#pierwsza sprężyna, metoda statyczna
X = [0, 50.320, 100.342  , 150.596, 200.861 ]
Y = [0, 5, 10, 15, 20 ]
n = len(X)
leastRegLine(X, Y, n)

#pierwsza sprężyna, metoda dynamiczna
X = [0, 50.152 , 100.508 , 150.830, 201.095 ]
Y = [0, (9.31+9.21+9.23)/3, (12.59+12.68+12.56)/3, (15.25+15.17+15.16)/3, (17.40+17.41+17.28)/3 ]
n = len(X)
leastRegLine(X, Y, n)

#druga sprężyna, metoda statyczna
X = [0, 50.155 , 100.478 , 150.614, 200.790 ]
Y = [0, 4.8, 10, 15.3, 20.5 ]
n = len(X)
leastRegLine(X, Y, n)

#druga sprężyna, metoda dynamiczna
X = [0, 50.155, 100.478 , 150.614, 200.790 ]
Y = [0, (9.53+9.49)/2, (12.89+12.93)/2, (15.57+15.43)/2, (17.76+17.77)/2 ]
n = len(X)
leastRegLine(X, Y, n)

#szeregowo sprężyny, metoda statyczna
X = [0, 50.155, 100.478 , 150.614, 200.790 ]
Y = [0, 2.5, 5.2, 7.8, 10.2 ]
n = len(X)
leastRegLine(X, Y, n)

#szeregowo sprężyny, metoda dynamiczna
X = [0, 50.155, 100.478 , 150.614, 200.790 ]
Y = [0, (8.54+8.53+8.36)/3, (10.56+10.55+10.55)/3, (12.15+12.13+12.11)/3, (13.58+13.57+13.59)/3 ]
n = len(X)
leastRegLine(X, Y, n)

#rownolegle sprężyny, metoda statyczna
X = [0, 50.155, 100.478 , 150.614, 200.790 ]
Y = [0, 10.5, 20.8, 31.1, 41.3 ]
n = len(X)
leastRegLine(X, Y, n)

#rownolegle sprężyny, metoda dynamiczna
X = [0, 50.155, 100.478 , 150.614, 200.790 ]
Y = [0, (13.91+13.88+13.96)/3, (18.58+18.45+18.40)/3, (22.16+22.15+22.16)/3, (25.32+25.36+25.30)/3 ]
n = len(X)
leastRegLine(X, Y, n)

# This code is contributed by avanitrachhadiya2155
