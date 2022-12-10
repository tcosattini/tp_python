
## 1

tab = [98, 22, 15, 32, 2, 74, 63, 70, 10]
tab2 = [1, 3, 4,5,7]
# 1 a

def index_minimum(t,d,f) :
  array = []
  for i in t[d:f]:
    array.append(i)
  minArrayValue = min(array)
  return t.index(minArrayValue)
# print(index_minimum(tab,0,10))

# 1 b
def triBulle(e):
    invert = False
    for n in range(len(e)-1, 0, -1):
        for i in range(n):
            if e[i] > e[i + 1]:
                invert = True
                e[i], e[i + 1] = e[i + 1], e[i]       
        if not invert:
       
            return
 
# triBulle(tab)
# print(tab)

## 2
#2 a
def recherche (array, element) :
  i = 0
  while (array[i] != element):
      i+=1  
      if i == len(array):
        return "Pas trouvé"
  return "Trouvé !", array[i]
  
 
# print(recherche(tab,105))

#2 b
def dichotomie(array, element):
    a = 0
    b = len(array) - 1
    while a <= b:
        m = (a + b) // 2
        if array[m] == element:
            return True
        elif array[m] < element:
            a = m + 1
        else:
            b = m - 1
    return False

# print(dichotomie(tab, 2))

#2 c

def insertion(e,t,n):
  i = 0
  while i <= n-1 :       
      if i == n -1:
        t.append(e)
        return t
      elif t[i] < e and t[i+1] > e  : 
        t.insert(t.index(t[i+1]),e)
        return t
      elif e == t[i]  : 
        t.insert(t.index(t[i]),e)
        return t  
      i+=1    
    
# print(insertion(2, tab2,5))      


##3


#3 a
def tri_extraction (t) :
  var = 0
  rTab = []
  while var <= len(t)-1 :        
    nTab = t[var:-1]
    if nTab :
      tMin = min(nTab);
      t.pop(index_minimum(t,var,-1))
      t.insert(var,tMin)
      rTab.append(tMin)   
    var+=1    
  return rTab

# print(tri_extraction(tab))    

#3 b
def tri_insertion (nlist):
  for index in range(1,len(nlist)):

     currentvalue = nlist[index]
     position = index

     while position>0 and nlist[position-1]>currentvalue:
         nlist[position]=nlist[position-1]
         position = position-1

     nlist[position]=currentvalue
  return nlist     

# print(tri_insertion(tab))



