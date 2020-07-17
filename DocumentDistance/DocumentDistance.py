#Given two documents, distance between two documents
#What is distance? Well, how different are they?
#toy problem, but let's think about how to define distance

import math

#Assumptions:
#Document is a sequence of words
#Words are sequences of alphanumeric characters
class Document:
    def __init__(self, words):
        self.words = words

#treats each document with words as a vector
#find the angle between vectors as a measure of closeness
def distance(document1, document2):
    pass

#get the inner product for keys with numeric values - calling each a vector
#each vector is a dictionary
def inner_product(vector1, vector2):
    if vector1 is None or vector2 is None:
        raise ValueError

    sum = 0.0

    for key in vector1:
        if key in vector2:
            sum += vector1[key] * vector2[key]
    
    return sum

def vector_angle(vector1, vector2):
    if vector1 is None or vector2 is None:
        raise ValueError

    numerator = inner_product(vector1, vector2)
    denominator = math.sqrt(inner_product(vector1, vector1) + inner_product(vector2, vector2))

    return math.acos(numerator/denominator)