#Dichiarare le variabili di tipo float
x = float(input("What's x? "))
y = float(input("What's y? "))

#Arrotonda la somma di x + y
z = round(x + y)

#Stampa il risultato con il separatore delle migliaia
print(f'{z:.}')