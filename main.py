'''
functia patratperfect verifica daca numarul primit este sau nu un patrat perfect
'''
def patratperfect(n):
    for i in range(n//2):
        if i*i==n:
            return True
    return False
'''
functia get_longest_all_perfect_squares cauta cea mai lunga secventa de numere care sunt patrate perfecte
'''
def get_longest_all_perfect_squares(v:list[int]):
    final=0
    lungimemax=0
    lungime=0
    for i in range(len(v)):
        if patratperfect(v[i])==True:
            lungime=lungime+1
            if lungime>lungimemax:
                lungimemax=lungime
                final=i
        else:
            lungime=0
    return v[final-lungimemax+1:final+1]
'''
functia get_longest_arithmetic_progression cauta cea mai lunga secventa de numere care formeaza o progresie aritmetica
'''
def get_longest_arithmetic_progression(v:list[int]):
    final=0
    lungime=0
    lungimemax=0
    for i in range(len(v)-1):
        if v[i]*2==v[i-1]+v[i+1]:
            lungime=lungime+1
            if lungime>lungimemax:
                lungimemax=lungime
                final=i
        else:
            lungime=0
    lungimemax=lungimemax+2
    final=final+1
    return v[final-lungimemax+1:final+1]

def test_get_longest_arithmetic_progression():
    assert get_longest_arithmetic_progression([1, 2, 3, 7, 9, 11, 13]) == [7, 9, 11, 13]
    assert get_longest_arithmetic_progression([54, 30, 6, 1, 5]) == [54, 30, 6]
    assert get_longest_arithmetic_progression([90, 100, 36, 50, 64, 78]) == [36, 50, 64, 78]

def test_get_longest_all_perfect_squares():
    assert get_longest_all_perfect_squares([1, 4, 5, 16, 36, 49]) == [16, 36, 49]
    assert get_longest_all_perfect_squares([2, 9, 3]) == [9]
    assert get_longest_all_perfect_squares([7, 40, 36, 100, 10]) == [36, 100]

def main():
    test_get_longest_arithmetic_progression()

    vector=[]
    while True:
        print("1.Cea mai lunga secventa de numere patrate perfecte")
        print("2.Cea mai lunga secventa de numere in progresie aritmetica")
        print("3.Iesire")
        optiune=int(input("Alegeti comanda: "))
        if optiune==1:
            nrdenumere=int(input("Introduceti numarul de elemente din vector: "))
            for i in range (nrdenumere):
             vector.append(int(input("Introduceti elementele vectorului: ")))
            vectorfinal=get_longest_all_perfect_squares(vector)
            print(vectorfinal)
        elif optiune==2:
            nrdenumere=int(input("Introduceti numarul de elemente din vector: "))
            for i in range (nrdenumere):
             vector.append(int(input("Introduceti elementele vectorului: ")))
            vectorfinal=get_longest_arithmetic_progression(vector)
            print(vectorfinal)
        elif optiune==3:
            break

main()