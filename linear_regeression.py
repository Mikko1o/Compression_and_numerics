# Python 2.7.1.


# Simple linear regression, find k and b, y = kx + b
# First line of input file should be labels of x and y
# First column of input file should be values of x
# Second column of input file should be values of y
# Both columns should be of equal length
# Returns (k, b)
def linear_regression(filename):
    f = open(filename, 'r')
    firstline = f.readline()
    x_label, z, y_label = firstline.partition(" ")
    y_label = y_label.rstrip('\n')
    x = []
    y = []
    for line in f:
        x_i, z, y_i = line.partition(" ")
        y_i = y_i.rstrip('\n')
        x.append(float(x_i))
        y.append(float(y_i))
    f.close()
    x_mean = 0.0
    y_mean = 0.0
    for v in x:
        x_mean = x_mean + v
    for v in y:
        y_mean = y_mean + v
    x_mean = x_mean / x.__len__()
    y_mean = y_mean / y.__len__()
    denominator = 0.0
    nominator = 0.0
    for v, w in zip(x, y):
        denominator = denominator + (v - x_mean) * (w - y_mean)
        nominator = nominator + (v - x_mean) * (v - x_mean)
    k = denominator / nominator
    b = y_mean - k * x_mean
    return k, b

print(linear_regression('data.txt'))