textul=input("Introduceti textul dorit:")
def litera_mare(textul):
    propozitii=textul.split('.')
    for i in propozitii:
        print(i.capitalize())

litera_mare(textul)

textul2=input("Introduceti textul dorit:")
def dictionar_count(textul):
    numaraparitii = {}
    for n in textul:
        keys = numaraparitii.keys()
        if n  in keys:
            numaraparitii[n] += 1 
        else:
            numaraparitii[n] = 1
    print(numaraparitii)
    print(numaraparitii.keys())
    print(numaraparitii.values())
    print(numaraparitii.items())
    
dictionar_count(textul2)