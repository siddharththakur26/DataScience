import numpy 
arr = map(float,raw_input().split())
arr = numpy.array(arr)
numpy.set_printoptions(sign=' ')
print numpy.floor(arr)
print numpy.ceil(arr)
print numpy.rint(arr)