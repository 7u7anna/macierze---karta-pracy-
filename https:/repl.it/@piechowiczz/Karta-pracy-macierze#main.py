from random import randint 
# 1. Deklarowanie macierzy

# a) stwórz macierz: [[1,1,1], [2,4,8], [3,9,27] ... [100, 10000, 1000000]]

M = []
for i in range(1,101):
  M.append([i, i**2, i**3])
print(M)

# b) stwórz macierz: [[1], [1,2], [1,2,3] ... [1,2,3 ... 50]]

M = []
for i in range(53):
  M.append([])
  for j in range(1, i - 1):
      M[i].append(j)
print(M)

# c) stwórz macierz 5x5 z wędrującą jedynką:
# [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], 
# [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]

M = []
for i in range(5):
  M.append([])
  for j in range(5):
    if i == j:
      j = 1
    else :
      j = 0
    M[i].append(j)
print(M)


# 2. Wygeneruj macierz 12x4 wypełnioną losowymi liczbami trzycyfrowymi

M = [[randint(100,999) for i in range(4)] for j in range(12)]
print(M)

# a) Wypisz 10% wartości jaka kryje się na końcu siódmego wiersza

print(M[6][3]*0.1)

# b) Wypisz ilość tych liczb, które są niemniejsze niż 500 i mniejsze niż 600

for lst in M:
  for elem in lst:
    if elem > 500 and elem < 600:
      print(elem, end = " ")

# c) Wypisz te listy z macierzy, w których suma dwóch lewych elementów 
#    jest większa niż suma dwóch prawych.

for i in range(12):
  if M[i][0] + M[i][1] < M[i][2] + M[i][3]:
    print(M[i], end = " ")

# d) Wypisz te listy macierzy, z których nie udałoby się zbudować czworokątu

for i in range(12):
  maksik = 0
  for j in range(4):
    if j > maksik :
       maksik = j

for i in range(12):
  s = 0
  for j in range(4):
    if M[i][j] != maksik:
      s+= M[i][j]
  if s < maksik :
    print(M[i], end = " ")


# 3. Wygeneruj macierz kwadratową 10x10 wypełnioną losowo cyframi od 0 do 9

M = [[randint(0,9) for i in range(10)] for j in range(10)]
print(M)

# a) oblicz sumę cyfr w czterech rogach macierzy

s = 0
for lst in M[::9]:
  for elem in lst[::9]:
    s+= elem
print(s)

# b) podaj ile macierz zawiera elementów, które są równe 0 lub 9

s = 0 
for lst in M:
  for elem in lst:
    if elem == 9:
      s+= 1
    elif elem == 0:
      s+= 1
print(s)

# c) oblicz sumę cyfr w 2 kolumnie

s = 0
for i in range(len(M)):
  for j in range(len(M[i])):
    if j == 1:
      s+= M[i][j]
print(s)

# d) oblicz sumę cyfr w parzystych wierszach

for lst in M[1::2]:
  s = 0
  for elem in lst:
    s+= elem
  print(s)

# e) oblicz sumę cyfr na jednej i drugiej przekątnej

n = 10 
s1 = 0
s = 0
for i in range(10):
  s1+= M[i][n-1-i]
  for j in range(10):
    if i == j:
      s+= M[i][j]
print("prawa :", s1, "lewa :", s)

# f) sprawdź ile wierszy i ile kolumn kończy się i zaczyna tą samą cyfrą

s = 0
s1 = 0
for i in range(10):
  if M[0][i] == M[9][i]:
    s+= 1
  elif M[i][0] == M[i][9]:
    s1+= 1
print("wiersze :", s1, "kolumny :", s)

# g) wypisz te wiersze macierzy które mają więcej parzystych niż nieparzystych cyfr

for i in range(10):
  s = 0
  for j in range(10):
    if M[i][j]%2 == 0:
      s+= 1
  if s > 5:
    print(M[i], end = " ")

# h*) podaj ile jest takich sytuacji w macierzy, że jej sąsiednie elementy 
#     mają taką samą wartość. Sąsiedztwo może być w poziomie albo w pionie

s = 0
for i in range(len(M)-1):
  for j in range(len(M[i])):
    if M[i][j] == M[i+1][j]:
      s+= 1

for i in range(len(M)):
  for j in range(len(M)-1):
    if M[i][j] == M[i][j+1]:
      s+=1
print(s)
