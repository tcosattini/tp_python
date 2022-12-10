import turtle
import random
# 1
# Pour passer à la ligne : \n

#2
i = 0

while i < 100 :
  i+=1

for i in range(100):
  i+=1
  print(i)

carre = turtle.Turtle()

for i in range(4):
  carre.forward(100)
  carre.left(90) 

triangle = turtle.Turtle ()
triangle.forward (100) 
triangle.left (120)
triangle.forward (100)
triangle.left (120)
triangle.forward (100)

# 3

emptyArray = []
array = [1,2,3,4,5]
len(array)

array[0]= 99
array.pop(2)
array.append(100)
print(array)

for arr in array :
  print(arr)

for i in range(0, len(array)):
	print (array[i])


# 4
randomNum = random.randint(3, 9)
randomNumInrange = random.randrange(3, 9)
randomArray = random.choice(array)
randomSuffleArray = random.shuffle(array)
