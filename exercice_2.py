import random
import datetime

array = [1,2,25,3,458,5,11,78]

def moyenne (array) : 
  result = 0;
  for i in array :
    result += i
  return result / len(array)

def occurence(array,find) :
  result = []
  for i in array :
    if i == find : 
      result.append(i)
  return len(result)

def maxTen(array) :
  result = []
  for i in array :
    if i >= 10 : 
      result.append(i)
  return len(result)

def triBulle (array) :
  max = 0
  for i in array :
    if i > max : 
      max = i
  return max


def isPresent (array, toFind) :
  for i in array :
    if i == toFind : 
      return toFind, "est présent"
  return toFind, "n'est pas présent"
    

def fillArray (number) : 
  array = []
  a = datetime.datetime.now()
  for i in range(0, number):
    array.append(random.randint(1,999))
  return array, "\ntemps d'execution : ", datetime.datetime.now() - a 

def fillArrayPremier (length) : 
  array = []
  
  def randomPrimeNumber(i, length):
    for y in range (i, length):
      for x in range (2, y):
        if y % x == 0:
          continue
        else:
          return y 
  for i in range (2, length) :
   array.append(randomPrimeNumber(i,length))      
   i +=1 
  return array
