# Dane kontaktowe:
# Szymon Chlebowski, szymon.chlebowski@amu.edu.pl lub MsTeams chat
# Dyżury (pokój 97, budynek AB) 
# wtorek 9.30-10.30 oraz między 11.30 a 13.00 (po uprzednim umówieniu się)

# 20 punktów: kolokwium (indywidualne przy komputerze), 
# 30 punktów: indywidualne wejściówki/wyjściówki i/lub praca w małych grupach.
 
# kod zajęć będzie dostępny na Githubie a link będzie udostepniany na stronie:
# http://sc52172.home.amu.edu.pl/

# Temat pierwszych zajęć: 
# - rozgrzewka;
# 

# 1a. Zdefiniuj funkcję silnia, używając standardowej rekurencji. 

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

# 1b. Zdefiniuj funkcję silnia, używając rekurencji ogonowej.

def factorial_tail(n,m):
    if n==0:
        return m
    else:
        return factorial_tail(n-1, n*m)
   
# 1c. Zdefiniuj funkcję silnia, używając iteracji (pętli).

def factorial_iter(n):
    if n==0:
        return 1
    else:
        f=1
        for i in range(1,n+1):
            f = f*i
        return f

# 2a. Zdefiniuj funkcję zwracającą największy element w liście - wersja iteracyjna.

def maximum_iter(list):
    max = list[0]
    for x in list:
        if x > max:
            max = x
    return max

# 2b. Zdefiniuj funkcję zwracającą największy element w liście - wersja rekurencyjna.

def maxx(lista):
      if len(lista)==1:
            return lista[0]
      else:
            reszta = lista[1:]
            if lista[0] > maxx(reszta):
                  return lista[0]
            else:
                  return maxx(reszta)
            
# 3a. Zdefiniuj funkcję odwracającą kolejność elementów w liście - wersja rekurencyjna.

# 3b. Zdefiniuj funkcję odwracającą kolejność elementów w liście - wersja iteracyjna.

# 4a. Zdefiniuj funkcję, która konkatenuje dwie listy - wersja rekurencyjna.

# 4b. Zdefiniuj funkcję, która konkatenuje dwie listy - wersja iteracyjna.

# 5a. Zdefiniuj funkcję, która wylicza największy wspólny dzielnik dwóch liczb - wersja rekurencyjna.

# 5b. Zdefiniuj funkcję, która wylicza największy wspólny dzielnik dwóch liczb - wersja iteracyjna.
 
# 6a. Zdefinuj funkcję, która sprawdza, czy dany element znajduje się na liście - wersja rekurencyjna.

# 6b. Zdefinuj funkcję, która sprawdza, czy dany element znajduje się na liście - wersja iteracyjna.