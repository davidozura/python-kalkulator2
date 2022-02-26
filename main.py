print("Živijo, jaz sem tvoj domači kalkulatorček.")

import time
time.sleep(3)

print("Vem skoraj vse o številkah in o računanju.")

import time
time.sleep(3)

print("Ne verjameš? Lahko me preizkusiš. :-)")

import time
time.sleep(3)

name = input("Še prej pa me zanima tvoje ime: ")
print(name, ", vnesi dve naravni celi števili in določi osnovno računsko operacijo med njima - seštevanje (+), odštevanje (-), množenje (*) ali deljenje (/)")

numberone = int(input("Vnesi prvo število: "))

numbertwo = int(input("Vnesi drugo število: "))

operation = input("Določi osnovno računsko oparacijo  + ali - ali * ali / : ")

print("Trenutek, razmišljam....")

import time
time.sleep(4)

print("Samo še malo rabim....")

import time
time.sleep(3)

if operation == "+":
    print("Hmmmm, seštevanje. Rezultat je: ", numberone + numbertwo)
elif operation == "-":
    print("Uffff, odštevanje. Rezultat je: ", numberone - numbertwo)
elif operation == "*":
    print("Aha, že vem. Na krat mi gre dobro. Rezultat je: ", numberone * numbertwo)
elif (operation == "/") and (numberone == 0 or numbertwo == 0):
    print("Hja, z nič pa ne morem deliti, v običajni matematiki to ne gre.")
else:
    print("To pa ni bilo težko, čeprav je deljenje. Rezultat je: ", numberone / numbertwo)
