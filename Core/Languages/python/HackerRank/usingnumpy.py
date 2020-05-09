import numpy
from numpy import eye
R,C = list(map(int,raw_input().split()))
# can be used to take multiple line inputs depending upon number of rows or columns
A = list(map(int,raw_input().split()) for i in range(R))
B = list(map(int,raw_input().split())for i in range(R))
Amat = numpy.array(A)
Bmat = numpy.array(B)
addition = numpy.add(Amat,Bmat)
subtraction = numpy.subtract(Amat,Bmat)
mutliplication = numpy.multiply(Amat,Bmat)
division = numpy.divide(Amat,Bmat)
modulus = numpy.mod(Amat,Bmat)
power = numpy.power(Amat,Bmat)
#print "[", addition ,"]"
print addition
print subtraction
print mutliplication
print division
print modulus
print power

'''
numpy.set_printoptions(sign=' ')
print eye(3,3,0)
numbers = [1,2,3,4,5]
print numpy.mean(numbers)
print numpy.median(numbers)
print numpy.std(numbers)
'''