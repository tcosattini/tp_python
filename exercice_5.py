import random
from exercice_4 import triBulle, tri_extraction,tri_insertion
import time

array = [1,2,3,4,5,6,7,8,9]
# 1
def copie (t):
  tCopy = []
  for i in t :
    tCopy.append(i)
  return tCopy

# print(copie(array))


# 2
def inverse (t):
  tCopy = []
  i = t[len(t)-1]
  while i > 0 :
    i -=1
    tCopy.append(t[i])
  return tCopy


# print(inverse(array))

#3 a
def tableau_premiers_entiers (n) :

  check_me = range(2, n)

  primes = []
  for i in check_me:
      for j in range(2, i):
          if not i % j:
              break
      else:
          primes.append(i)
  return primes   

# print(tableau_premiers_entiers(100))

#3 b
def tableau_premiers_entiers_melanges (n) :
  primes = tableau_premiers_entiers(n)
     
  n=len(primes)-1
  for i in range(n):
    random_index = random.randint(0, n)
    temp = primes.pop(random_index)
    primes.append(temp)
  return primes

# print(tableau_premiers_entiers_melanges(100))

#3 c
def tableau_premiers_entiers_inverses (n):
  primes = tableau_premiers_entiers(n)
  primes.sort(reverse = True)
  return primes

# print(tableau_premiers_entiers_inverses(100))



#4

def ligne_dans_fichier (f,n,t) :
  obFichier = open(f,'a')
  obFichier.write(str(n))
  obFichier.write("\t")
  obFichier.write(str(t))
  obFichier.write("\n")
  obFichier.close()

# ligne_dans_fichier("2","2","2")  

#5

def temps_tri_bulles (t) :
  tCopy = copie(t)
  start_time = time.time()
  triBulle(tCopy)
  return str(time.time() - start_time) + " secs"

# print(temps_tri_bulles(tableau_premiers_entiers_inverses (10000)))


#6  
def stats_melange (nmin,nmax,pas, fois):
  i = nmin
  while i <= nmax:
    x = 1;
    exeMoy = []
   
    while x <= fois:    
      tabs = random.sample(range(nmin, nmax*2), i)
      print(i)
      start_time = time.time()
      triBulle(tabs)
      finishedTime = time.time()
      exTime = finishedTime - start_time
      print(exTime, len(tabs))
      exeMoy.append(exTime)
      if len(exeMoy)== fois :
        ligne_dans_fichier ("tri_a_bulle_melange.dat",len(tabs),sum(exeMoy)/len(exeMoy))
        print(" ======== Temps moyen d'execution pour",fois," fois ", "tab de longueur ", len(tabs),"cases"," ===>", sum(exeMoy)/len(exeMoy),"=======")
      x+=1
    i+=pas

# print(stats_melange(100,1000,100,5))    

#7
def stats_ordonne (nmin,nmax,pas, fois):
  i = nmin
  while i <= nmax:
    x = 1;
    exeMoy = []
   
    while x <= fois: 
      tabs = random.sample(range(nmin, nmax*2), i)
      tabs.sort()
      start_time = time.time()
      triBulle(tabs)
      finishedTime = time.time()
      exTime = finishedTime - start_time
      print(exTime, len(tabs))
      exeMoy.append(exTime)
      if len(exeMoy)== fois :
        ligne_dans_fichier ("tri_a_bulle_ordonne.dat",len(tabs),sum(exeMoy)/len(exeMoy))
        print(" ======== Temps moyen d'execution pour",fois," fois ", "tab de longueur ", len(tabs),"cases"," ===>", sum(exeMoy)/len(exeMoy),"=======")
      x+=1
    i+=pas

# print(stats_ordonne(100,1000,100,5))    

#8
def stats_inverse (nmin,nmax,pas, fois):
  i = nmin
  while i <= nmax:
    x = 1;
    exeMoy = []
   
    while x <= fois: 
      tabs = random.sample(range(nmin, nmax*2), i)
      tabs.sort(reverse=True)
      start_time = time.time()
      triBulle(tabs)
      finishedTime = time.time()
      exTime = finishedTime - start_time
      print(exTime, len(tabs))
      exeMoy.append(exTime)
      if len(exeMoy)== fois :
        ligne_dans_fichier ("tri_a_bulle_inverse.dat",len(tabs),sum(exeMoy)/len(exeMoy))
        print(" ======== Temps moyen d'execution pour",fois," fois ", "tab de longueur ", len(tabs),"cases"," ===>", sum(exeMoy)/len(exeMoy),"=======")
      x+=1
    i+=pas

# print(stats_inverse(100,1000,100,5))    


def stats_melange_extraction (nmin,nmax,pas, fois):
  i = nmin
  while i <= nmax:
    x = 1;
    exeMoy = []
   
    while x <= fois: 
      tabs = random.sample(range(nmin, nmax*2), i)
      start_time = time.time()     
      tri_extraction(tabs)
      finishedTime = time.time()
      exTime = finishedTime - start_time
      print(exTime, len(tabs))
      exeMoy.append(exTime)
      if len(exeMoy)== fois :
        ligne_dans_fichier ("tri_extraction_melange.dat",len(tabs),sum(exeMoy)/len(exeMoy))
        print(" ======== Temps moyen d'execution pour",fois," fois ", "tab de longueur ", len(tabs),"cases"," ===>", sum(exeMoy)/len(exeMoy),"=======")
      x+=1
    i+=pas

# print(stats_melange_extraction(100,1000,100,5))   

def stats_melange_insertion (nmin,nmax,pas, fois):
  i = nmin
  while i <= nmax:
    x = 1;
    exeMoy = []
   
    while x <= fois: 
      tabs = random.sample(range(nmin, nmax*2), i)
      start_time = time.time()     
      tri_insertion(tabs)
      finishedTime = time.time()
      exTime = finishedTime - start_time
      print(exTime, len(tabs))
      exeMoy.append(exTime)
      if len(exeMoy)== fois :
        ligne_dans_fichier ("tri_insertion_melange.dat",len(tabs),sum(exeMoy)/len(exeMoy))
        print(" ======== Temps moyen d'execution pour",fois," fois ", "tab de longueur ", len(tabs),"cases"," ===>", sum(exeMoy)/len(exeMoy),"=======")
      x+=1
    i+=pas

# print(stats_melange_insertion(100,1000,100,5))   