voto = float(input("inserire voto "))
if voto < 6 and voto >= 3:
    print("Il voto è insufficiente, devi impegnarti di più.")
elif voto == 6:
    print("Il voto è sufficiente, ma puoi fare di meglio.")
elif voto > 6 and voto <= 9:
    print("Il voto è buono, ottimo.")
elif voto == 10 and voto <= 10:
    print("Il voto è eccellente, bravissimo.")
else:
    print("Il voto inserito non è valido.")