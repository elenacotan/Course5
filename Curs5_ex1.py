import math
numar_numere_verificate="global"
numar_numere_verificate=0
numar_numere_prime="global"
numar_numere_prime=0



def numar_prim(numarul):
    global numar_numere_verificate
    global numar_numere_prime
    numar_numere_verificate+=1
    if numarul>1:
        for i in range (2,numarul):
            if (numarul%i)==0:
                print (str(numarul) + " nu este un numar prim")
                break
        else:
            print (str(numarul) + " este un numar prim")
            numar_numere_prime+=1
    else:
        print (str(numarul) + " nu este un numar prim")
    print("Numarul de numere verificate este: " + str(numar_numere_verificate))
    print("Numarul de numere prime este: " +str(numar_numere_prime))

def patrat_perfect(numarul):
    radacina_patrata=math.sqrt(numarul)
    if int(radacina_patrata + 0.5)**2==numarul:
        print(str(numarul)+" este un patrat perfect")
    else:
        print(str(numarul)+" nu este un patrat perfect")


        
choice =  ''
while choice != 'q':
    print("[1] Doriti sa introduceti un numar pe care vreti sa il verificati ")
    print("[q] Apasati q pentru a iesi ")
    
    choice = input("Alegeti o optiune din cele 2 ")
    
    if choice == '1':
        numarul=int(input("Introduceti de la tastatura un numar natural:"))
        print("Sa testam numarul introdus")
        numar_prim(numarul)
        patrat_perfect(numarul)
    elif choice == 'q':
        break
    else:
        print("Nu ati ales o optiune valida")
